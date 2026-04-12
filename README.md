# Learn Anthropic

> A structured, community-driven guide to everything Anthropic publishes.

**Current content:** 111 research papers · 23 engineering blogs · 198 news announcements · 100 tutorials · 16 courses · 86 use cases · 16 legal documents · 9 events — **592 pages** total.

## Why This Exists

Anthropic publishes high-quality content, but it's scattered across their websites (anthropic.com and claude.com). Research papers, engineering blogs, news announcements, tutorials, courses, and use cases are mixed together with no learning path, no prioritization, and no connections between them. You might read a paper without knowing how it applies in practice.

This project organizes their content into a more accessible, navigable structure.

## Content Structure

```
learn-anthropic/
├── research/                      # Research papers & technical reports (111)
│   ├── interpretability/          # Interpretability — Transformer circuits, monosemanticity, feature analysis
│   ├── alignment/                 # Alignment — Constitutional AI, sleeper agents, red-teaming
│   ├── evals/                     # Evaluations — Systematic evals, statistical methods, SWE-bench
│   ├── economics/                 # Economic research — Economic index, labor impact
│   ├── agents/                    # Agents — Building, evaluating, long-running
│   └── circuits/                  # Circuits update series
├── engineering/                   # Engineering blogs (23)
│   ├── agents.md                  # Agent building series
│   ├── claude-code.md             # Claude Code series
│   ├── tools.md                   # Tools & MCP
│   └── infrastructure.md          # Infrastructure
├── news/                          # News announcements (198)
│   ├── model-releases/            # Model releases
│   ├── partnerships/              # Partnerships
│   ├── safety/                    # Safety & red-teaming
│   ├── policy/                    # Policy & regulation
│   ├── education/                 # Education
│   ├── enterprise/                # Enterprise & industry
│   └── funding/                   # Funding & expansion
├── tutorials/                     # Claude tutorials from claude.com (100)
│   ├── professional/              # General professional use (31)
│   ├── finance/                   # Financial services workflows (20)
│   ├── life-sciences/             # Life sciences & biotech (20)
│   ├── engineering/               # Engineering & development (10)
│   ├── healthcare/                # Healthcare workflows (7)
│   ├── nonprofits/                # Nonprofit organizations (6)
│   ├── ai-fluency/                # AI Fluency guides (2)
│   ├── education/                 # Education workflows (1)
│   ├── marketing/                 # Marketing workflows (1)
│   ├── hr/                        # Human resources (1)
│   └── sales/                     # Sales workflows (1)
├── courses/                       # Claude courses from claude.com (16)
│   ├── engineering/               # API, Claude Code, MCP (9)
│   ├── professional/              # AI Fluency, Claude Cowork (3)
│   ├── education/                 # AI Fluency for educators & students (3)
│   └── nonprofits/                # AI Fluency for nonprofits (1)
├── use-cases/                     # Claude use cases from claude.com (86)
│   ├── professional/              # Business workflows (17)
│   ├── personal/                  # Personal productivity (16)
│   ├── nonprofits/                # Nonprofit workflows (12)
│   ├── education/                 # Education scenarios (11)
│   ├── finance/                   # Financial workflows (6)
│   ├── claude-in-chrome/          # Browser-based workflows (6)
│   ├── sales/                     # Sales workflows (4)
│   ├── legal/                     # Legal workflows (4)
│   ├── research/                  # Research workflows (4)
│   ├── marketing/                 # Marketing workflows (3)
│   ├── life-sciences/             # Life sciences workflows (2)
│   └── hr/                        # Human resources (1)
└── sitemap.json                   # Combined local sitemap (primary reference)
```

## Sources

| Source | Pages | Description |
|--------|-------|-------------|
| anthropic.com | 390 | Research, engineering, news, legal, events |
| claude.com — Tutorials | 100 | How-to guides and workflows |
| claude.com — Courses | 16 | Structured learning paths |
| claude.com — Use Cases | 86 | Practical application examples |
| **Total** | **592** | |

## Learning Path

### Getting Started (1–2 days)
1. [The Claude Constitution](https://www.anthropic.com/constitution) — Understand Anthropic's core philosophy
2. [Core Views on AI Safety](https://www.anthropic.com/news/core-views-on-ai-safety) — How they think about AI risk
3. [Claude 101](courses/professional/claude-101.md) — Get started with Claude

### Intermediate (1–2 weeks)
4. [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) — Agent design patterns
5. [Constitutional AI](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback) — Alignment methodology
6. [Claude Code 101](courses/engineering/claude-code-101.md) — Learn Claude Code
7. [Getting Started with Claude.ai](tutorials/professional/getting-started-claude-ai.md) — Hands-on tutorial

### Deep Dive (ongoing)
8. [Interpretability Series](research/interpretability/) — From Transformer circuits to monosemanticity
9. [Agent Engineering Series](engineering/agents.md) — From tool design to long-running architectures
10. [Safety & Red-Teaming Series](news/safety/) — From detection to defense
11. [Building with the Claude API](courses/engineering/building-with-claude-api.md) — 84-lesson deep dive

## Core Concepts Index

| Concept | Key Page | In One Line |
|---------|----------|-------------|
| Constitutional AI | [Paper](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback) | Uses AI feedback instead of human feedback to train harmlessness |
| MCP | [Announcement](https://www.anthropic.com/news/model-context-protocol) | Open protocol for connecting AI to external tools and data |
| Responsible Scaling | [Policy](https://www.anthropic.com/responsible-scaling-policy) | Progressively stronger safety measures as capabilities increase |
| Sleeper Agents | [Paper](https://www.anthropic.com/research/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training) | Deceptive behaviors that safety training may fail to remove |
| Interpretability | [Series](research/interpretability/) | Understanding what's happening inside the model |
| Computer Use | [Announcement](https://www.anthropic.com/news/developing-computer-use) | Letting Claude operate a computer |
| Many-shot Jailbreaking | [Paper](https://www.anthropic.com/research/many-shot-jailbreaking) | Long-context jailbreak attacks |

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

**Where we need the most help right now:**
- Adding one-line summaries to research papers
- Adding key points to tutorials, courses, and use cases
- Adding technical keyword tags to engineering posts
- Finding pages missing from the sitemap

## License

Content in this project is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Original content is copyrighted by Anthropic. This project only organizes links and metadata; it does not reproduce original content.