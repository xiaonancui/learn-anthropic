---
title: "Best Practices for Claude Code"
site: "Claude Code Docs"
source: "https://www.anthropic.com/engineering/claude-code-best-practices"
domain: "code.claude.com"
language: "en"
description: "Tips and patterns for getting the most out of Claude Code, from configuring your environment to scaling across parallel sessions."
word_count: 4113
url: https://www.anthropic.com/engineering/claude-code-best-practices
date:
tags: ["engineering", "claude_code"]
---

Claude Code is an agentic coding environment. Unlike a chatbot that answers questions and waits, Claude Code can read your files, run commands, make changes, and autonomously work through problems while you watch, redirect, or step away entirely. This changes how you work. Instead of writing code yourself and asking Claude to review it, you describe what you want and Claude figures out how to build it. Claude explores, plans, and implements. But this autonomy still comes with a learning curve. Claude works within certain constraints you need to understand. This guide covers patterns that have proven effective across Anthropic's internal teams and for engineers using Claude Code across various codebases, languages, and environments. For how the agentic loop works under the hood, see [How Claude Code works](https://www.anthropic.com/docs/en/how-claude-code-works).

---

Most best practices are based on one constraint: Claude's context window fills up fast, and performance degrades as it fills. Claude's context window holds your entire conversation, including every message, every file Claude reads, and every command output. However, this can fill up fast. A single debugging session or codebase exploration might generate and consume tens of thousands of tokens. This matters since LLM performance degrades as context fills. When the context window is getting full, Claude may start "forgetting" earlier instructions or making more mistakes. The context window is the most important resource to manage. To see how a session fills up in practice, [watch an interactive walkthrough](https://www.anthropic.com/docs/en/context-window) of what loads at startup and what each file read costs. Track context usage continuously with a [custom status line](https://www.anthropic.com/docs/en/statusline), and see [Reduce token usage](https://www.anthropic.com/docs/en/costs#reduce-token-usage) for strategies on reducing token usage.

---

## Give Claude a way to verify its work

Include tests, screenshots, or expected outputs so Claude can check itself. This is the single highest-leverage thing you can do.

Claude performs dramatically better when it can verify its own work, like run tests, compare screenshots, and validate outputs. Without clear success criteria, it might produce something that looks right but actually doesn't work. You become the only feedback loop, and every mistake requires your attention.

| Strategy | Before | After |
| --- | --- | --- |
| **Provide verification criteria** | *"implement a function that validates email addresses"* | *"write a validateEmail function. example test cases: [email protected] is true, invalid is false, [email protected] is false. run the tests after implementing"* |
| **Verify UI changes visually** | *"make the dashboard look better"* | *"[paste screenshot] implement this design. take a screenshot of the result and compare it to the original. list differences and fix them"* |
| **Address root causes, not symptoms** | *"the build is failing"* | *"the build fails with this error: [paste error]. fix it and verify the build succeeds. address the root cause, don't suppress the error"* |

UI changes can be verified using the [Claude in Chrome extension](https://www.anthropic.com/docs/en/chrome). It opens new tabs in your browser, tests the UI, and iterates until the code works. Your verification can also be a test suite, a linter, or a Bash command that checks output. Invest in making your verification rock-solid.

---

## Explore first, then plan, then code

Separate research and planning from implementation to avoid solving the wrong problem.

Letting Claude jump straight to coding can produce code that solves the wrong problem. Use [Plan Mode](https://www.anthropic.com/docs/en/common-workflows#use-plan-mode-for-safe-code-analysis) to separate exploration from execution. The recommended workflow has four phases:

Plan Mode is useful, but also adds overhead.For tasks where the scope is clear and the fix is small (like fixing a typo, adding a log line, or renaming a variable) ask Claude to do it directly.Planning is most useful when you're uncertain about the approach, when the change modifies multiple files, or when you're unfamiliar with the code being modified. If you could describe the diff in one sentence, skip the plan.

---

## Provide specific context in your prompts

The more precise your instructions, the fewer corrections you'll need.

Claude can infer intent, but it can't read your mind. Reference specific files, mention constraints, and point to example patterns.

| Strategy | Before | After |
| --- | --- | --- |
| **Scope the task.** Specify which file, what scenario, and testing preferences. | *"add tests for foo.py"* | *"write a test for foo.py covering the edge case where the user is logged out. avoid mocks."* |
| **Point to sources.** Direct Claude to the source that can answer a question. | *"why does ExecutionFactory have such a weird api?"* | *"look through ExecutionFactory's git history and summarize how its api came to be"* |
| **Reference existing patterns.** Point Claude to patterns in your codebase. | *"add a calendar widget"* | *"look at how existing widgets are implemented on the home page to understand the patterns. HotDogWidget.php is a good example. follow the pattern to implement a new calendar widget that lets the user select a month and paginate forwards/backwards to pick a year. build from scratch without libraries other than the ones already used in the codebase."* |
| **Describe the symptom.** Provide the symptom, the likely location, and what "fixed" looks like. | *"fix the login bug"* | *"users report that login fails after session timeout. check the auth flow in src/auth/, especially token refresh. write a failing test that reproduces the issue, then fix it"* |

Vague prompts can be useful when you're exploring and can afford to course-correct. A prompt like `"what would you improve in this file?"` can surface things you wouldn't have thought to ask about.

### Provide rich content

Use `@` to reference files, paste screenshots/images, or pipe data directly.

You can provide rich data to Claude in several ways:
- **Reference files with `@`** instead of describing where code lives. Claude reads the file before responding.
- **Paste images directly**. Copy/paste or drag and drop images into the prompt.
- **Give URLs** for documentation and API references. Use `/permissions` to allowlist frequently-used domains.
- **Pipe in data** by running `cat error.log | claude` to send file contents directly.
- **Let Claude fetch what it needs**. Tell Claude to pull context itself using Bash commands, MCP tools, or by reading files.

---

## Configure your environment

A few setup steps make Claude Code significantly more effective across all your sessions. For a full overview of extension features and when to use each one, see [Extend Claude Code](https://www.anthropic.com/docs/en/features-overview).

### Write an effective CLAUDE.md

Run `/init` to generate a starter CLAUDE.md file based on your current project structure, then refine over time.

CLAUDE.md is a special file that Claude reads at the start of every conversation. Include Bash commands, code style, and workflow rules. This gives Claude persistent context it can't infer from code alone. The `/init` command analyzes your codebase to detect build systems, test frameworks, and code patterns, giving you a solid foundation to refine. There's no required format for CLAUDE.md files, but keep it short and human-readable. For example:

```markdown
# Code style
- Use ES modules (import/export) syntax, not CommonJS (require)
- Destructure imports when possible (eg. import { foo } from 'bar')

# Workflow
- Be sure to typecheck when you're done making a series of code changes
- Prefer running single tests, and not the whole test suite, for performance
```

CLAUDE.md is loaded every session, so only include things that apply broadly. For domain knowledge or workflows that are only relevant sometimes, use [skills](https://www.anthropic.com/docs/en/skills) instead. Claude loads them on demand without bloating every conversation. Keep it concise. For each line, ask: *"Would removing this cause Claude to make mistakes?"* If not, cut it. Bloated CLAUDE.md files cause Claude to ignore your actual instructions!

| ✅ Include | ❌ Exclude |
| --- | --- |
| Bash commands Claude can't guess | Anything Claude can figure out by reading code |
| Code style rules that differ from defaults | Standard language conventions Claude already knows |
| Testing instructions and preferred test runners | Detailed API documentation (link to docs instead) |
| Repository etiquette (branch naming, PR conventions) | Information that changes frequently |
| Architectural decisions specific to your project | Long explanations or tutorials |
| Developer environment quirks (required env vars) | File-by-file descriptions of the codebase |
| Common gotchas or non-obvious behaviors | Self-evident practices like "write clean code" |

If Claude keeps doing something you don't want despite having a rule against it, the file is probably too long and the rule is getting lost. If Claude asks you questions that are answered in CLAUDE.md, the phrasing might be ambiguous. Treat CLAUDE.md like code: review it when things go wrong, prune it regularly, and test changes by observing whether Claude's behavior actually shifts. You can tune instructions by adding emphasis (e.g., "IMPORTANT" or "YOU MUST") to improve adherence. Check CLAUDE.md into git so your team can contribute. The file compounds in value over time. CLAUDE.md files can import additional files using `@path/to/import` syntax:

```markdown
See @README.md for project overview and @package.json for available npm commands.

# Additional Instructions
- Git workflow: @docs/git-instructions.md
- Personal overrides: @~/.claude/my-project-instructions.md
```

You can place CLAUDE.md files in several locations:
- **Home folder (`~/.claude/CLAUDE.md`)**: applies to all Claude sessions
- **Project root (`./CLAUDE.md`)**: check into git to share with your team
- **Project root (`./CLAUDE.local.md`)**: personal project-specific notes; add this file to your `.gitignore` so it isn't shared with your team
- **Parent directories**: useful for monorepos where both `root/CLAUDE.md` and `root/foo/CLAUDE.md` are pulled in automatically
- **Child directories**: Claude pulls in child CLAUDE.md files on demand when working with files in those directories

### Configure permissions

Use [auto mode](https://www.anthropic.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode) to let a classifier handle approvals, `/permissions` to allowlist specific commands, or `/sandbox` for OS-level isolation. Each reduces interruptions while keeping you in control.

By default, Claude Code requests permission for actions that might modify your system: file writes, Bash commands, MCP tools, etc. This is safe but tedious. After the tenth approval you're not really reviewing anymore, you're just clicking through. There are three ways to reduce these interruptions:
- **Auto mode**: a separate classifier model reviews commands and blocks only what looks risky: scope escalation, unknown infrastructure, or hostile-content-driven actions. Best when you trust the general direction of a task but don't want to click through every step
- **Permission allowlists**: permit specific tools you know are safe, like `npm run lint` or `git commit`
- **Sandboxing**: enable OS-level isolation that restricts filesystem and network access, allowing Claude to work more freely within defined boundaries
Read more about [permission modes](https://www.anthropic.com/docs/en/permission-modes), [permission rules](https://www.anthropic.com/docs/en/permissions), and [sandboxing](https://www.anthropic.com/docs/en/sandboxing).

### Use CLI tools

Tell Claude Code to use CLI tools like `gh`, `aws`, `gcloud`, and `sentry-cli` when interacting with external services.

CLI tools are the most context-efficient way to interact with external services. If you use GitHub, install the `gh` CLI. Claude knows how to use it for creating issues, opening pull requests, and reading comments. Without `gh`, Claude can still use the GitHub API, but unauthenticated requests often hit rate limits. Claude is also effective at learning CLI tools it doesn't already know. Try prompts like `Use 'foo-cli-tool --help' to learn about foo tool, then use it to solve A, B, C.`

### Connect MCP servers

Run `claude mcp add` to connect external tools like Notion, Figma, or your database.

With [MCP servers](https://www.anthropic.com/docs/en/mcp), you can ask Claude to implement features from issue trackers, query databases, analyze monitoring data, integrate designs from Figma, and automate workflows.

### Set up hooks

Use hooks for actions that must happen every time with zero exceptions.

[Hooks](https://www.anthropic.com/docs/en/hooks-guide) run scripts automatically at specific points in Claude's workflow. Unlike CLAUDE.md instructions which are advisory, hooks are deterministic and guarantee the action happens. Claude can write hooks for you. Try prompts like *"Write a hook that runs eslint after every file edit"* or *"Write a hook that blocks writes to the migrations folder."* Edit `.claude/settings.json` directly to configure hooks by hand, and run `/hooks` to browse what's configured.

### Create skills

Create `SKILL.md` files in `.claude/skills/` to give Claude domain knowledge and reusable workflows.

[Skills](https://www.anthropic.com/docs/en/skills) extend Claude's knowledge with information specific to your project, team, or domain. Claude applies them automatically when relevant, or you can invoke them directly with `/skill-name`. Create a skill by adding a directory with a `SKILL.md` to `.claude/skills/`:

```markdown
---
name: api-conventions
description: REST API design conventions for our services
---
# API Conventions
- Use kebab-case for URL paths
- Use camelCase for JSON properties
- Always include pagination for list endpoints
- Version APIs in the URL path (/v1/, /v2/)
```

Skills can also define repeatable workflows you invoke directly:

```markdown
---
name: fix-issue
description: Fix a GitHub issue
disable-model-invocation: true
---
Analyze and fix the GitHub issue: $ARGUMENTS.

1. Use `gh issue view` to get the issue details
2. Understand the problem described in the issue
3. Search the codebase for relevant files
4. Implement the necessary changes to fix the issue
5. Write and run tests to verify the fix
6. Ensure code passes linting and type checking
7. Create a descriptive commit message
8. Push and create a PR
```

Run `/fix-issue 1234` to invoke it. Use `disable-model-invocation: true` for workflows with side effects that you want to trigger manually.

### Create custom subagents

Define specialized assistants in `.claude/agents/` that Claude can delegate to for isolated tasks.

[Subagents](https://www.anthropic.com/docs/en/sub-agents) run in their own context with their own set of allowed tools. They're useful for tasks that read many files or need specialized focus without cluttering your main conversation.

```markdown
---
name: security-reviewer
description: Reviews code for security vulnerabilities
tools: Read, Grep, Glob, Bash
model: opus
---
You are a senior security engineer. Review code for:
- Injection vulnerabilities (SQL, XSS, command injection)
- Authentication and authorization flaws
- Secrets or credentials in code
- Insecure data handling

Provide specific line references and suggested fixes.