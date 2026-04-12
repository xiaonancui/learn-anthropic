#!/usr/bin/env python3
"""
Update categories.json to include full URLs from sitemap.json.

Usage:
    python3 scripts/update_categories.py
"""

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(PROJECT_DIR, "data")

SITEMAP_PATH = os.path.join(PROJECT_DIR, "sitemap.json")
CATEGORIES_PATH = os.path.join(DATA_DIR, "categories.json")


def load_json(path):
    with open(path, "r") as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def build_slug_url_map(sitemap):
    """Build a mapping from slug to full URL."""
    slug_to_url = {}
    for page in sitemap["pages"]:
        path = page["path"]
        url = page["url"]
        if not path:
            continue
        # Extract slug (last part of path)
        slug = path.rstrip("/").split("/")[-1]
        if slug:
            slug_to_url[slug] = url
    return slug_to_url


def update_categories(categories, slug_to_url):
    """Update categories to include URLs."""
    updated = {}
    stats = {"matched": 0, "missing": 0}

    for section, subcategories in categories.items():
        updated[section] = {}
        for subcat, items in subcategories.items():
            updated_items = []
            for slug in items:
                url = slug_to_url.get(slug)
                if url:
                    updated_items.append({"slug": slug, "url": url})
                    stats["matched"] += 1
                else:
                    updated_items.append({"slug": slug, "url": None})
                    stats["missing"] += 1
                    print(f"  Missing URL: {section}/{subcat}/{slug}")
            updated[section][subcat] = updated_items

    return updated, stats


def main():
    print("Loading sitemap...")
    sitemap = load_json(SITEMAP_PATH)
    print(f"  {len(sitemap['pages'])} pages found")

    print("Loading categories...")
    categories = load_json(CATEGORIES_PATH)

    print("Building slug-to-URL map...")
    slug_to_url = build_slug_url_map(sitemap)
    print(f"  {len(slug_to_url)} slugs mapped")

    print("Updating categories...")
    updated_categories, stats = update_categories(categories["categories"], slug_to_url)

    categories["categories"] = updated_categories
    categories["last_updated"] = "2026-04-11"

    print("Saving categories.json...")
    save_json(CATEGORIES_PATH, categories)

    print(f"\nDone!")
    print(f"  Matched: {stats['matched']}")
    print(f"  Missing: {stats['missing']}")


if __name__ == "__main__":
    main()
