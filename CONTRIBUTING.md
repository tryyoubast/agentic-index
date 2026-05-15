# Contributing

Agentic Index is intentionally selective. The goal is not to include every AI
agent repository; the goal is to help developers choose useful stack components.

## Add Or Update A Project

Edit `data/projects.json` and keep entries sorted by rough ecosystem importance.

Required fields:

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

Run verification before opening a PR:

```bash
PYTHONPATH=src:. python3 -m unittest discover -s tests -v
PYTHONPATH=src:. python3 scripts/generate_site.py
```

## Inclusion Bar

Good candidates:

- Help real AI coding-agent workflows.
- Have public source and clear setup instructions.
- Are actively maintained or historically important.
- Fit one of the catalog categories.

Weak candidates:

- Thin wrappers with unclear value.
- Private products without useful open-source artifacts.
- Demos that cannot be run or learned from.
- Repositories with misleading claims.

## Categories

Use the closest category:

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
