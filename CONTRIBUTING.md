# Contributing to learn-anthropic

Thank you for your interest in contributing!

## How to Contribute

### The Simplest Way: Add One-Line Summaries

Each paper or article should have a one-line summary explaining what it covers. If you've read one, simply edit the corresponding file and add your summary.

### Find Missing Pages

Run `scripts/fetch-sitemap.sh` to compare against the current dataset. If you discover new pages, submit a PR updating `data/sitemap.json`.

### Write In-Depth Analysis

If you have deep understanding of a paper or series, we welcome your analysis. See the templates in `research/interpretability/` for formatting guidance.

### Improve the Learning Path

Think the learning sequence needs adjustment? A concept should be introduced earlier? Open an issue to discuss.

## Directory Conventions

- `research/` — Organized by topic; filenames use page slugs
- `engineering/` — Organized by series; multiple pages may be combined in a single file
- `news/` — Only include entries with educational value; pure commercial announcements are omitted
- Each file begins with YAML frontmatter containing metadata

## File Template

```markdown
---
title: Paper or Article Title
url: https://www.anthropic.com/research/xxx
date: YYYY-MM-DD
tags: [tag1, tag2]
---

## One-Liner

What this covers — the one-line version.

## Key Points

- Point 1
- Point 2

## Related

- Links to related papers or articles
```

## What We Don't Do

- ❌ We do not reproduce Anthropic's original content
- ❌ We do not translate papers (summaries and analysis only)
- ❌ We do not include non-public content

## License

Contributions are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).