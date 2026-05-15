# Agentic Index Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and publish Agentic Index, a structured index plus CLI and generated site for discovering practical AI coding-agent stacks.

**Architecture:** Python package with a single source of truth in `data/projects.json`. CLI, Markdown export, and static HTML are generated from validated project entries.

**Tech Stack:** Python 3.11+, standard library, pytest, GitHub Actions.

---

### Task 1: Repository Foundation

**Files:**
- Create: `pyproject.toml`
- Create: `LICENSE`
- Create: `.gitignore`
- Create: `README.md`

- [ ] Add package metadata and test tooling.
- [ ] Add MIT license.
- [ ] Add launch-focused README.

### Task 2: Data Model And Seed Index

**Files:**
- Create: `data/projects.json`
- Create: `src/agentic_index/models.py`
- Create: `src/agentic_index/catalog.py`
- Test: `tests/test_catalog.py`

- [ ] Add curated seed data.
- [ ] Validate required fields, duplicate slugs, URL shape, and category names.
- [ ] Test loading, searching, filtering, and recommendations.

### Task 3: CLI

**Files:**
- Create: `src/agentic_index/cli.py`
- Modify: `pyproject.toml`
- Test: `tests/test_cli.py`

- [ ] Implement `list`, `search`, `show`, `recommend`, and `export`.
- [ ] Keep output terminal-friendly and deterministic.
- [ ] Test CLI behavior through direct function calls.

### Task 4: Site Generator

**Files:**
- Create: `scripts/generate_site.py`
- Create: `public/index.html`
- Test: `tests/test_site_generation.py`

- [ ] Generate a static HTML site from the catalog.
- [ ] Include category filters as simple anchor sections.
- [ ] Test that generation includes all seeded projects.

### Task 5: Launch Polish

**Files:**
- Create: `.github/workflows/ci.yml`
- Create: `CONTRIBUTING.md`
- Create: `docs/launch-notes.md`

- [ ] Add CI for tests and site drift.
- [ ] Add contribution rules for adding projects.
- [ ] Add launch notes and positioning.

### Task 6: Verification And Publish

**Files:**
- Modify as needed.

- [ ] Run tests.
- [ ] Run site generation and verify no drift.
- [ ] Initialize git, commit, create GitHub repo, and push.
