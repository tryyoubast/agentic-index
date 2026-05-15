# Agentic Index Design

## Goal

Build a repository with real 10k-star potential by serving as the fastest practical entry point into the AI coding-agent ecosystem: skills, subagents, MCP servers, memory layers, HUDs, session tools, orchestration, and safety tools.

## Market Read

The strongest star signals are ecosystem entry points and workflow accelerators:

- `punkpeye/awesome-mcp-servers`: 86k+ stars
- `thedotmack/claude-mem`: 75k+ stars
- `gsd-build/get-shit-done`: 62k+ stars
- `upstash/context7`: 55k+ stars
- `hesreallyhim/awesome-claude-code`: 43k+ stars
- `jarrodwatts/claude-hud`: 22k+ stars
- `ComposioHQ/awesome-codex-skills`: 9.7k+ stars

Single-purpose privacy, scanner, and viewer tools show weaker demand. The project should therefore be an ecosystem map with executable utility, not another narrow agent tool.

## Positioning

**Agentic Index** is a structured, installable index of the AI coding-agent stack.

Tagline: **Stop hunting through awesome lists. Pick your agent stack in seconds.**

It is not an agent framework, not an MCP marketplace clone, and not a generic awesome list. It ships:

- A curated machine-readable dataset.
- A CLI that recommends stack combinations by workflow.
- A generated static site.
- Markdown guides generated from the same dataset.
- CI that validates link shape, schema, duplicate slugs, and generated output drift.

## MVP

The first release should be small but polished:

- `data/projects.json`: curated seed index with categories, clients, install hints, use cases, star counts, URLs, and risk notes.
- `agentic-index` CLI:
  - `list`
  - `search <query>`
  - `recommend --client codex --goal memory`
  - `show <slug>`
  - `export --format markdown|json`
- Static site generator that creates `public/index.html`.
- Strong README with star-proven market context and practical workflows.
- GitHub Action for tests and generated site drift checks.

## Data Model

Each project entry has:

- `slug`
- `name`
- `url`
- `summary`
- `category`
- `clients`
- `use_cases`
- `stars`
- `install`
- `why_it_matters`
- `caveats`
- `tags`

Categories:

- `context`
- `memory`
- `skills`
- `subagents`
- `mcp`
- `hud`
- `session`
- `orchestration`
- `security`
- `workflow`
- `learning`

## Differentiation

Existing awesome lists are useful but mostly static prose. Agentic Index adds:

- Task-oriented recommendation.
- Structured JSON that other tools can consume.
- Generated outputs so the repo stays consistent.
- Cross-client tagging for Codex, Claude Code, Cursor, OpenCode, Gemini, and MCP-compatible tools.
- A clear "starter stack" narrative for developers who are new to agentic coding.

## Constraints

- No scraping in the MVP; seed data is manually curated from public GitHub metadata gathered during research.
- No inflated claims about guaranteeing stars.
- No copying README content from competitors.
- No paid API required.
- All generated artifacts must be reproducible locally.

## Success Criteria

- A developer can understand the repo in under 30 seconds.
- A developer can run a useful command in under 2 minutes.
- The README makes the star-proven demand obvious.
- The project looks alive and maintainable from day one.
- It can be pushed to GitHub under the user's account as an original MIT-licensed project.
