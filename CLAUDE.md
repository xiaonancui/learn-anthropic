# CLAUDE.md - Working Notes

## Project Overview
**learn-anthropic** - A structured, community-driven guide to everything Anthropic publishes. Organizes 490+ pages from anthropic.com and claude.com into a learnable knowledge system.

## Working Style
**Option B: Concise and efficient**
- Provide fewer explanations, more direct actions
- Batch tool calls when possible
- Use `start_line`/`end_line` for targeted file reads
- Skip redundant verification steps

## Project Structure
```
research/         - Papers & reports (interpretability, alignment, evals, economics, agents, circuits)
engineering/      - Engineering blogs (agents, claude-code, tools, infrastructure)
news/             - News (model-releases, partnerships, safety, policy, education, enterprise, funding)
tutorials/        - Claude tutorials from claude.com (professional, finance, life-sciences, engineering, healthcare, nonprofits, ai-fluency, education, marketing, hr, sales)
data/             - default-sitemap.json (raw anthropic.com sitemap), categories.json
scripts/          - fetch-sitemap.sh, generate_content.py, generate_tutorials.py, generate_local_sitemap.py, update_categories.py
sitemap.json      - Combined local sitemap (primary reference file)
```

## Sitemap Structure
- `sitemap.json` (root) — Primary reference file, combines all sources (490 pages)
- `data/default-sitemap.json` — Raw anthropic.com sitemap (390 pages)
- Always regenerate `sitemap.json` after updating default or adding new content

## Key Commands
```bash
# Update anthropic.com default sitemap
bash scripts/fetch-sitemap.sh

# Regenerate combined local sitemap (run after any content changes)
python3 scripts/generate_local_sitemap.py

# Regenerate content files
python3 scripts/generate_content.py
python3 scripts/generate_tutorials.py

# Update categories with URLs
python3 scripts/update_categories.py

# Check git status
git status
```

## File Conventions
- YAML frontmatter with title, url, date, tags
- One-line summaries for papers
- Key points and related links sections
- Page slugs for filenames in research/
- Tutorials organized by category subfolders

## Current Stats
- 111 research papers (last: 2026-04-08)
- 23 engineering blogs (last: 2026-04-10)
- 198 news announcements (last: 2026-04-10)
- 100 tutorials (claude.com)
- 16 legal documents (last: 2026-04-10)
- 9 events (last: 2026-04-11)
- **Total: 490 pages**