#!/usr/bin/env node

import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import path from "node:path";
import process from "node:process";

// Volume is a review dimension (review-change, code-shape reference, "Volume"): a narrow request with a
// wide diff needs an ownership reason. This prints the numbers so the handover
// can report them; it never blocks.
const GENERATED_PATH =
  /(^|\/)(node_modules|dist|build|coverage|\.next|drizzle\/meta|generated)(\/|$)|pnpm-lock\.yaml$|_snapshot\.json$/;
const TEST_PATH = /\.(test|spec)\.[^/]+$|(^|\/)(e2e|__tests__|fixtures)\//;

export function summarizeVolume(numstat) {
  const totals = {
    files: 0,
    implementationAdded: 0,
    implementationRemoved: 0,
    testAdded: 0,
    testRemoved: 0,
  };

  for (const line of numstat.split(/\r?\n/)) {
    const [added, removed, file] = line.split("\t");
    if (!file || GENERATED_PATH.test(file) || added === "-") continue;
    totals.files += 1;
    const bucket = TEST_PATH.test(file) ? "test" : "implementation";
    totals[`${bucket}Added`] += Number(added);
    totals[`${bucket}Removed`] += Number(removed);
  }

  return totals;
}

function formatVolume(totals) {
  const lines = [
    `  - files: ${totals.files}`,
    `  - implementation: +${totals.implementationAdded} -${totals.implementationRemoved}`,
    `  - tests: +${totals.testAdded} -${totals.testRemoved}`,
  ];

  if (
    totals.testAdded > totals.implementationAdded &&
    totals.implementationAdded > 0
  ) {
    lines.push(
      "  - test lines exceed implementation lines: justify or trim (review-change, Volume)",
    );
  }

  return lines.join("\n");
}

const isDirectExecution =
  process.argv[1] &&
  fileURLToPath(import.meta.url) === path.resolve(process.argv[1]);

if (isDirectExecution) {
  const base = spawnSync("git", ["merge-base", "origin/main", "HEAD"], {
    encoding: "utf8",
  }).stdout.trim();
  const result = spawnSync("git", ["diff", "--numstat", base], {
    encoding: "utf8",
  });
  console.log(formatVolume(summarizeVolume(result.stdout ?? "")));
}
