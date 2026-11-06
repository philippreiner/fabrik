#!/usr/bin/env node

import { readFileSync } from "node:fs";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import path from "node:path";
import process from "node:process";

import ts from "typescript";

// Comments should carry the reason a line exists, not restate it. Files above
// this ratio are prose candidates. The check warns; `--strict` makes it fail.
// Repository p95 for explanatory density is 7%, so 12% marks a clear outlier
// without pulling in files that are simply well explained.
const COMMENT_DENSITY_WARN_RATIO = 0.12;
// Below this length one honest header comment crosses the ratio.
const MIN_SCANNED_LINES = 60;
// A single comment this long is prose even when the file density stays low.
// Repository p95 for a comment block is 50 words, so 70 is prose by any reading.
const LONG_COMMENT_LINES = 12;
const LONG_COMMENT_WORDS = 70;

const IGNORED_PATH =
  /(^|\/)(node_modules|dist|build|out|coverage|\.next|\.turbo|\.output|generated)(\/|$)/;
const NON_RUNTIME_FILE = /\.(test|spec)\.[^.]+$|\.d\.ts$/;
const SOURCE_FILE = /\.(m|c)?[jt]sx?$/;

// The TypeScript scanner is used instead of a regex so URLs, strings, and
// regex literals cannot look like comments.
export function scanComments(source) {
  const scanner = ts.createScanner(
    ts.ScriptTarget.Latest,
    false,
    ts.LanguageVariant.Standard,
    source,
  );
  const lineStarts = [0];
  for (let index = 0; index < source.length; index += 1) {
    if (source[index] === "\n") lineStarts.push(index + 1);
  }

  function lineOf(position) {
    let low = 0;
    let high = lineStarts.length - 1;
    while (low < high) {
      const mid = (low + high + 1) >> 1;
      if (lineStarts[mid] <= position) low = mid;
      else high = mid - 1;
    }
    return low;
  }

  const commentLines = new Set();
  // `/** */` on an exported symbol is API documentation, not accreted prose, so
  // it is excluded from density and judged only by block length.
  const docLines = new Set();
  const comments = [];
  let token = scanner.scan();
  while (token !== ts.SyntaxKind.EndOfFileToken) {
    if (
      token === ts.SyntaxKind.SingleLineCommentTrivia ||
      token === ts.SyntaxKind.MultiLineCommentTrivia
    ) {
      const first = lineOf(scanner.getTokenStart());
      const last = lineOf(Math.max(scanner.getTokenEnd() - 1, 0));
      const text = scanner.getTokenText();
      const isDoc = text.startsWith("/**");
      for (let line = first; line <= last; line += 1) {
        commentLines.add(line);
        if (isDoc) docLines.add(line);
      }
      comments.push({
        startLine: first + 1,
        endLine: last + 1,
        lines: last - first + 1,
        isDoc,
        words: (
          text
            .replace(/^\/[/*]+|\*+\/$/g, " ")
            .match(/[A-Za-z][A-Za-z0-9'_-]*/g) ?? []
        ).length,
      });
    }
    // Without the parser the scanner can stall, as on a regex literal after
    // `(`; step past one character so every file finishes.
    const end = scanner.getTokenEnd();
    token = scanner.scan();
    if (token !== ts.SyntaxKind.EndOfFileToken && scanner.getTokenEnd() <= end) {
      scanner.resetTokenState(end + 1);
      token = scanner.scan();
    }
  }

  const explanatoryLines = commentLines.size - docLines.size;

  return {
    totalLines: lineStarts.length,
    commentLines: explanatoryLines,
    ratio: explanatoryLines / lineStarts.length,
    comments,
  };
}

// Consecutive single-line comments read as one block, so they are merged before
// the length judgement.
export function longComments(source) {
  const blocks = [];

  for (const comment of scanComments(source).comments) {
    const previous = blocks.at(-1);
    if (
      previous &&
      previous.isDoc === comment.isDoc &&
      comment.startLine === previous.endLine + 1
    ) {
      previous.endLine = comment.endLine;
      previous.lines += comment.lines;
      previous.words += comment.words;
      continue;
    }
    blocks.push({ ...comment });
  }

  return blocks.filter(
    (block) =>
      block.lines >= LONG_COMMENT_LINES || block.words >= LONG_COMMENT_WORDS,
  );
}

export function isScannedFile(file) {
  return (
    SOURCE_FILE.test(file) &&
    !IGNORED_PATH.test(file) &&
    !NON_RUNTIME_FILE.test(file)
  );
}

export function commentProblems(files, { readFile = readFileSync } = {}) {
  const dense = [];
  const long = [];

  for (const file of files) {
    const source = readFile(file, "utf8");
    const density = scanComments(source);

    if (
      density.totalLines >= MIN_SCANNED_LINES &&
      density.ratio > COMMENT_DENSITY_WARN_RATIO
    ) {
      dense.push({ file, ...density });
    }

    for (const block of longComments(source)) {
      long.push({ file, ...block });
    }
  }

  return {
    dense: dense.sort((a, b) => b.ratio - a.ratio),
    long: long.sort((a, b) => b.words - a.words || b.lines - a.lines),
  };
}

function git(args) {
  const result = spawnSync("git", args, {
    encoding: "utf8",
    maxBuffer: 1024 * 1024 * 32,
  });

  return result.status === 0 ? (result.stdout ?? "") : null;
}

function listAllFiles() {
  return (git(["ls-files"]) ?? "").split("\n");
}

// Routine runs scope to the branch so the check is a ratchet on new comments
// instead of a standing backlog. `--all` restores the repository view.
function listChangedFiles(base) {
  const merged = git(["merge-base", base, "HEAD"]);
  if (merged === null) return null;

  return [
    git(["diff", "--name-only", "--diff-filter=ACMR", merged.trim()]) ?? "",
    git(["ls-files", "--others", "--exclude-standard"]) ?? "",
  ].flatMap((output) => output.split("\n"));
}

function listSourceFiles({ base }) {
  const files = base ? listChangedFiles(base) : listAllFiles();
  if (files === null) return null;

  return [...new Set(files)].filter((file) => file && isScannedFile(file));
}

// Output is read by agents as often as by people: one line per finding, path
// and metric only. Every finding prints, because a truncated list reads as a
// clean scope that was never checked.
function printSection(label, rows, format) {
  console.log(`${label}: ${rows.length}`);

  for (const row of rows) {
    console.log(`  ${format(row)}`);
  }
}

function report({ base, strict }) {
  const files = listSourceFiles({ base });

  if (files === null) {
    console.log(`comment usage: skipped, ${base} is unavailable`);
    return;
  }

  const { dense, long } = commentProblems(files);

  printSection(
    `comment-density >${Math.round(COMMENT_DENSITY_WARN_RATIO * 100)}% (warn)`,
    dense,
    (row) => `${row.file} ${Math.round(row.ratio * 100)}%`,
  );
  printSection(
    `long-comments >=${LONG_COMMENT_LINES}l or >=${LONG_COMMENT_WORDS}w (warn)`,
    long,
    (row) => `${row.file}:${row.startLine} ${row.lines}l ${row.words}w`,
  );

  if (dense.length + long.length > 0) {
    console.log(
      "  fix: rewrite a long block to its reason, invariant, exact scope, and system relation; delete restatement, history, and cross-file claims; move durable background to the owning doc.",
    );
    if (strict) process.exitCode = 1;
  }
}

const isDirectExecution =
  process.argv[1] &&
  fileURLToPath(import.meta.url) === path.resolve(process.argv[1]);

if (isDirectExecution) {
  report({
    base: process.argv.includes("--all") ? null : "origin/main",
    strict: process.argv.includes("--strict"),
  });
}
