# Agentic Index

Structured index of practical AI coding-agent tools.

## Context

### [Context7](https://github.com/upstash/context7)

- Slug: `context7`
- Stars: `55,349`
- Clients: `claude-code, codex, cursor, opencode, gemini, mcp`
- Use cases: `docs, context, mcp`
- Summary: Up-to-date code documentation for LLMs and AI code editors.
- Why it matters: Fresh library docs are a universal pain point for coding agents.
- Caveats: Coverage and freshness vary by library.

### [Claude Context](https://github.com/zilliztech/claude-context)

- Slug: `claude-context`
- Stars: `11,093`
- Clients: `claude-code, mcp`
- Use cases: `context, search, mcp`
- Summary: Code search MCP for Claude Code that makes entire codebases available as agent context.
- Why it matters: Codebase search remains a central bottleneck for agentic coding.
- Caveats: MCP setup and indexing costs depend on project size.

## Hud

### [Claude HUD](https://github.com/jarrodwatts/claude-hud)

- Slug: `claude-hud`
- Stars: `22,842`
- Clients: `claude-code`
- Use cases: `hud, visibility, monitoring`
- Summary: Statusline plugin showing context usage, active tools, running agents, and todo progress.
- Why it matters: Developers want live visibility into agent behavior and context usage.
- Caveats: Claude Code focused; use adjacent tools for other clients.

## Learning

### [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code)

- Slug: `awesome-claude-code`
- Stars: `43,802`
- Clients: `claude-code`
- Use cases: `discovery, skills, plugins`
- Summary: Curated skills, hooks, commands, orchestrators, applications, and plugins for Claude Code.
- Why it matters: A high-star ecosystem map proves demand for agentic coding entry points.
- Caveats: Claude-specific; not every item transfers cleanly to Codex or Cursor.

### [Context Engineering Intro](https://github.com/coleam00/context-engineering-intro)

- Slug: `context-engineering-intro`
- Stars: `13,319`
- Clients: `claude-code, codex, cursor, opencode, gemini`
- Use cases: `learning, context, workflow`
- Summary: Practical introduction to making AI coding assistants work through better context engineering.
- Why it matters: Context engineering has become a mainstream developer concern.
- Caveats: Educational material, not a drop-in runtime.

### [Awesome AI Coding Tools](https://github.com/ai-for-developers/awesome-ai-coding-tools)

- Slug: `awesome-ai-coding-tools`
- Stars: `1,716`
- Clients: `codex, claude-code, cursor, copilot, gemini`
- Use cases: `discovery, learning, tools`
- Summary: Curated list of AI-powered coding tools.
- Why it matters: Tool discovery has broad developer pull outside any single client.
- Caveats: General list; not optimized for stack recommendations.

## Mcp

### [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers)

- Slug: `awesome-mcp-servers`
- Stars: `86,915`
- Clients: `claude-code, codex, cursor, opencode, gemini, mcp`
- Use cases: `mcp, discovery, tooling`
- Summary: The largest community index of Model Context Protocol servers.
- Why it matters: MCP discovery is one of the clearest star-proven demand centers in agentic development.
- Caveats: Large lists need extra vetting before installing third-party servers.

## Memory

### [Claude Mem](https://github.com/thedotmack/claude-mem)

- Slug: `claude-mem`
- Stars: `75,869`
- Clients: `claude-code, codex, opencode, gemini, cursor`
- Use cases: `memory, continuity, context`
- Summary: Persistent context across sessions for Claude Code, Codex, Gemini, OpenCode, and more.
- Why it matters: Memory is the strongest current developer demand signal in AI coding-agent workflows.
- Caveats: Memory systems can inject stale or low-quality context if not maintained.

### [Claude Memory Compiler](https://github.com/coleam00/claude-memory-compiler)

- Slug: `claude-memory-compiler`
- Stars: `1,046`
- Clients: `claude-code`
- Use cases: `memory, knowledge-base, sessions`
- Summary: Hooks and compiler that organize Claude Code sessions into structured knowledge articles.
- Why it matters: Structured memory is emerging as the next layer after raw session capture.
- Caveats: Requires maintenance of generated knowledge quality.

## Orchestration

### [Container Use](https://github.com/dagger/container-use)

- Slug: `container-use`
- Stars: `3,778`
- Clients: `codex, claude-code, cursor, opencode`
- Use cases: `orchestration, isolation, workflow`
- Summary: Development environments for coding agents so multiple agents can work safely and independently.
- Why it matters: Safe parallel agent work is becoming a real workflow need.
- Caveats: Requires comfort with containers and local dev environment setup.

## Security

### [Agentic Radar](https://github.com/splx-ai/agentic-radar)

- Slug: `agentic-radar`
- Stars: `965`
- Clients: `claude-code, codex, cursor, mcp`
- Use cases: `security, scanner, workflow`
- Summary: Security scanner for LLM agentic workflows.
- Why it matters: Agent security is rising, even if not every developer prioritizes it yet.
- Caveats: Scanner findings need human review.

## Session

### [Coding Agent Session Search](https://github.com/Dicklesworthstone/coding_agent_session_search)

- Slug: `coding-agent-session-search`
- Stars: `759`
- Clients: `codex, claude-code, gemini, cursor, aider`
- Use cases: `sessions, search, history`
- Summary: Unified TUI and CLI to index and search local coding-agent session history across many providers.
- Why it matters: Session history becomes valuable once agents do meaningful work.
- Caveats: Read-only search is useful but not a full memory system.

## Skills

### [Awesome Codex Skills](https://github.com/ComposioHQ/awesome-codex-skills)

- Slug: `awesome-codex-skills`
- Stars: `9,728`
- Clients: `codex`
- Use cases: `skills, workflow, automation`
- Summary: Curated practical Codex skills for automating workflows across Codex CLI and API.
- Why it matters: Codex skills are near the 10k-star threshold and still early.
- Caveats: Skill quality and maintenance differ by contributor.

### [Microsoft Skills](https://github.com/microsoft/skills)

- Slug: `skills`
- Stars: `2,315`
- Clients: `codex, claude-code, copilot, mcp`
- Use cases: `skills, mcp, grounding`
- Summary: Skills, MCP servers, custom agents, and AGENTS.md for grounding coding agents.
- Why it matters: Large vendors are converging around reusable agent capabilities.
- Caveats: Broad reference repo; not all examples are plug-and-play.

### [Codex Skill Manager](https://github.com/Dimillian/CodexSkillManager)

- Slug: `codex-skill-manager`
- Stars: `1,046`
- Clients: `codex`
- Use cases: `skills, management, desktop`
- Summary: macOS app for managing Codex skills.
- Why it matters: Skill management is a real friction point as Codex skills proliferate.
- Caveats: macOS focused.

## Subagents

### [Awesome Claude Code Subagents](https://github.com/VoltAgent/awesome-claude-code-subagents)

- Slug: `awesome-claude-code-subagents`
- Stars: `19,841`
- Clients: `claude-code`
- Use cases: `subagents, skills, workflow`
- Summary: Collection of specialized Claude Code subagents across development use cases.
- Why it matters: Role-specific agent packs are a proven viral format.
- Caveats: Quality varies; install only roles you actually use.

### [Awesome Codex Subagents](https://github.com/VoltAgent/awesome-codex-subagents)

- Slug: `awesome-codex-subagents`
- Stars: `4,680`
- Clients: `codex`
- Use cases: `subagents, skills, workflow`
- Summary: Collection of specialized Codex subagents for development tasks.
- Why it matters: Codex-native role packs are gaining fast ecosystem traction.
- Caveats: Avoid installing broad role packs without clear task boundaries.

## Workflow

### [Get Shit Done](https://github.com/gsd-build/get-shit-done)

- Slug: `get-shit-done`
- Stars: `62,329`
- Clients: `claude-code, codex, cursor`
- Use cases: `workflow, context, planning`
- Summary: Meta-prompting, context engineering, and spec-driven development system for Claude Code.
- Why it matters: Spec-driven agent workflows have huge adoption momentum.
- Caveats: Opinionated workflows may need pruning for smaller projects.

### [InsForge](https://github.com/InsForge/InsForge)

- Slug: `insforge`
- Stars: `9,836`
- Clients: `codex, claude-code, cursor`
- Use cases: `backend, shipping, workflow`
- Summary: Open-source backend platform for agentic coding: database, auth, storage, compute, hosting, and AI gateway.
- Why it matters: Agentic coding increasingly needs shippable infrastructure, not just prompts.
- Caveats: Heavier than a prompt or skill; evaluate stack fit first.

### [Continuous Claude v3](https://github.com/parcadei/Continuous-Claude-v3)

- Slug: `continuous-claude-v3`
- Stars: `3,771`
- Clients: `claude-code`
- Use cases: `memory, handoff, orchestration`
- Summary: Context management for Claude Code with ledgers, handoffs, MCP execution, and isolated agent orchestration.
- Why it matters: Handoffs and isolated context are central to long-running agent work.
- Caveats: Claude Code oriented and opinionated.

### [Claude Code Tools](https://github.com/pchalasani/claude-code-tools)

- Slug: `claude-code-tools`
- Stars: `1,788`
- Clients: `claude-code, codex`
- Use cases: `workflow, productivity, tools`
- Summary: Practical productivity tools for Claude Code, Codex CLI, and similar coding agents.
- Why it matters: Cross-agent productivity tooling is more durable than one-client hacks.
- Caveats: Tool coverage varies by client.

### [Keep Codex Fast](https://github.com/vibeforge1111/keep-codex-fast)

- Slug: `keep-codex-fast`
- Stars: `1,029`
- Clients: `codex`
- Use cases: `maintenance, workflow, skills`
- Summary: Backup-first Codex skill for keeping local Codex state fast, clean, and recoverable.
- Why it matters: Local agent state management becomes painful as usage grows.
- Caveats: Run cleanup tools carefully and keep backups.
