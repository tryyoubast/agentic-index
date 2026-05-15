# Starter Stacks

These are deliberately small. The fastest way to ruin an agent setup is to
install everything at once.

## Codex: Skills First

Use when you want Codex to get better at repeatable workflows.

```bash
PYTHONPATH=src python3 -m agentic_index.cli recommend --client codex --goal skills
```

Start with:

- `awesome-codex-skills`
- `codex-skill-manager`
- `keep-codex-fast`

Add MCP and memory only after you know which workflows repeat.

## Claude Code: Visibility First

Use when Claude Code is doing real work and you need to see what is happening.

```bash
PYTHONPATH=src python3 -m agentic_index.cli recommend --client claude-code --goal hud
```

Start with:

- `claude-hud`
- `claude-code-tools`
- `context-engineering-intro`

Add memory after your project instructions are clean.

## MCP: Tool Discovery

Use when you are ready to connect agents to external tools.

```bash
PYTHONPATH=src python3 -m agentic_index.cli recommend --client mcp --goal mcp
```

Start with:

- `awesome-mcp-servers`
- `context7`
- `claude-context`

Install MCP servers slowly. Treat every new tool as a capability and a risk.

## Long Projects: Memory And Handoffs

Use when agent work spans multiple sessions or branches.

```bash
PYTHONPATH=src python3 -m agentic_index.cli recommend --client claude-code --goal memory
```

Start with:

- `claude-mem`
- `claude-memory-compiler`
- `continuous-claude-v3`

Memory is useful only when curated. Bad memory is just stale context with a
better name.

## Parallel Work: Isolation

Use when multiple agents or branches work at the same time.

```bash
PYTHONPATH=src python3 -m agentic_index.cli recommend --client codex --goal orchestration
```

Start with:

- `container-use`
- `continuous-claude-v3`

Isolation matters before orchestration. Make agents safe before making them
numerous.
