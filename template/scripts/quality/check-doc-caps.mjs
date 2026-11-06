#!/usr/bin/env node

import { existsSync, readdirSync, readFileSync } from "node:fs";
import path from "node:path";
import process from "node:process";

// Shared context docs grew with every feature until they anchored agents to
// past shapes. Line caps were met with longer lines, so caps count characters:
// a pull request retires text before it adds text. Raise a cap only with the
// user's agreement.
const CAPS = {
  "AGENTS.md": 8_000,
  "DESIGN.md": 4_500,
  "PRODUCT.md": 8_000,
  "docs/architecture.md": 36_000,
};
const SKILL_DIR = ".agents/skills";
const SKILL_CAP = 12_000;
// Skills installed from upstream (`skills-lock.json`) follow their source.
const UPSTREAM_SKILLS = new Set(
  existsSync("skills-lock.json")
    ? Object.keys(JSON.parse(readFileSync("skills-lock.json", "utf8")).skills)
    : [],
);

function characters(file) {
  return readFileSync(file, "utf8").trimEnd().length;
}

const limits = Object.entries(CAPS)
  .concat(
    (existsSync(SKILL_DIR) ? readdirSync(SKILL_DIR) : [])
      .filter((name) => !UPSTREAM_SKILLS.has(name))
      .map((name) => path.join(SKILL_DIR, name, "SKILL.md"))
      .filter((file) => existsSync(file))
      .map((file) => [file, SKILL_CAP]),
  )
  .map(([file, cap]) => ({ file, cap, size: characters(file) }));

const failures = limits.filter(({ size, cap }) => size > cap);

for (const { file, cap, size } of failures) {
  console.error(
    `${file}: ${size} characters, cap ${cap}. Retire text before adding.`,
  );
}

process.exit(failures.length > 0 ? 1 : 0);
