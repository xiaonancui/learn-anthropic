#!/usr/bin/env python3
"""
Find 'Learn' section URLs from sitemap.json.

Searches for URLs related to:
- Anthropic Academy
- Tutorials
- Use cases
- Engineering at Anthropic
- Developer docs

Usage:
    python3 scripts/find_learn_section.py
"""

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
SITEMAP_PATH = os.path.join(PROJECT_DIR, "data", "sitemap.json")

LEARN_KEYWORDS = [
    "learn",
    "academy",
    "tutorial",
    "use-case",
    "usecase",
    "developer",
    "docs",
]


def main():
    with open(SITEMAP_PATH, "r") as f:
        sitemap = json.load(f)

    matches = []
    for page in sitemap["pages"]:
        path = page["path"].lower()
        for kw in LEARN_KEYWORDS:
            if kw in path:
                matches.append(page)
                break

    print(f"Found {len(matches)} URLs matching 'Learn' section keywords:\n")
    for m in matches:
        print(f"  {m['url']}")

    if not matches:
        print("  (none found)")


if __name__ == "__main__":
    main()
