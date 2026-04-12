#!/usr/bin/env python3
"""
Generate markdown content files from categories.json.

Usage:
    python3 scripts/generate_content.py
"""

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(PROJECT_DIR, "data")
CATEGORIES_PATH = os.path.join(DATA_DIR, "categories.json")


def load_json(path):
    with open(path, "r") as f:
        return json.load(f)


def slug_to_title(slug):
    """Convert slug to readable title."""
    return slug.replace("-", " ").replace("_", " ").title()


def create_markdown(filepath, title, url, tags):
    """Create markdown file with frontmatter and placeholder sections."""
    content = f"""---
title: {title}
url: {url}
date:
tags: {json.dumps(tags)}
---

## One-Liner

TODO: Add one-line summary.

## Key Points

- TODO: Add key points

## Related

- [{title}]({url})
"""
    with open(filepath, "w") as f:
        f.write(content)


def main():
    print("Loading categories...")
    categories = load_json(CATEGORIES_PATH)

    created = 0
    skipped = 0

    for section, subcategories in categories["categories"].items():
        for subcat, items in subcategories.items():
            # Create directory
            dir_path = os.path.join(PROJECT_DIR, section, subcat)
            os.makedirs(dir_path, exist_ok=True)

            for item in items:
                slug = item["slug"]
                url = item["url"]
                title = slug_to_title(slug)
                tags = [section, subcat]

                filepath = os.path.join(dir_path, f"{slug}.md")

                if os.path.exists(filepath):
                    skipped += 1
                    continue

                create_markdown(filepath, title, url, tags)
                created += 1
                print(f"  Created: {section}/{subcat}/{slug}.md")

    print(f"\nDone!")
    print(f"  Created: {created}")
    print(f"  Skipped: {skipped}")


if __name__ == "__main__":
    main()
