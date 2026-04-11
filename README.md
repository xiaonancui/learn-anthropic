# learn-anthropic 📚

> A structured, community-driven guide to everything Anthropic publishes.

From research papers to engineering practices, model releases to safety policies — 390+ pages of Anthropic's public content, organized into a learnable knowledge system.

## Why This Exists

Anthropic publishes high-quality content, but it's scattered across their website. Research papers, engineering blogs, and news announcements are mixed together with no learning path, no prioritization, and no connections between them. You might read a paper without knowing how it applies in practice.

This project solves that problem.

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
├── data/                          # Raw data
│   ├── sitemap.json               # Full sitemap (with lastmod)
│   └── categories.json            # Category mappings
└── scripts/                       # Utility scripts
    └── fetch-sitemap.sh           # Update sitemap
```

## Learning Path

### Getting Started (1–2 days)
1. [The Claude Constitution](https://www.anthropic.com/constitution) — Understand Anthropic's core philosophy
2. [Core Views on AI Safety](https://www.anthropic.com/news/core-views-on-ai-safety) — How they think about AI risk
3. [Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy) — Quantified safety commitments

### Intermediate (1–2 weeks)
4. [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) — Agent design patterns
5. [Constitutional AI](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback) — Alignment methodology
6. [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices) — Engineering in practice

### Deep Dive (ongoing)
7. [Interpretability Series](research/interpretability/) — From Transformer circuits to monosemanticity
8. [Agent Engineering Series](engineering/agents.md) — From tool design to long-running architectures
9. [Safety & Red-Teaming Series](news/safety/) — From detection to defense

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

## Quick Stats

| Section | Count | Last Updated |
|---------|-------|--------------|
| Research Papers | 111 | 2026-04-08 |
| Engineering Blogs | 23 | 2026-04-10 |
| News Announcements | 198 | 2026-04-10 |
| Legal Terms | 16 | 2026-04-10 |
| Events | 9 | 2026-04-11 |
| **Total** | **390** | |

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

**Where we need the most help right now:**
- Adding one-line summaries to research papers
- Adding technical keyword tags to engineering posts
- Finding pages missing from the sitemap

## Updating

Run `scripts/fetch-sitemap.sh` to fetch the latest page list:

```bash
bash scripts/fetch-sitemap.sh
```

## License

Content in this project is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Original content is copyrighted by Anthropic. This project only organizes links and metadata; it does not reproduce original content.