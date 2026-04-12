#!/usr/bin/env python3
"""
Generate a combined local sitemap that includes:
- All anthropic.com pages from the default sitemap
- All claude.com tutorials from the tutorials/ folder
- Any additional content added to the project

Usage:
    python3 scripts/generate_local_sitemap.py
"""

import json
import os
import re
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(PROJECT_DIR, "data")
TUTORIALS_DIR = os.path.join(PROJECT_DIR, "tutorials")
COURSES_DIR = os.path.join(PROJECT_DIR, "courses")

DEFAULT_SITEMAP = os.path.join(DATA_DIR, "default-sitemap.json")
LOCAL_SITEMAP = os.path.join(PROJECT_DIR, "sitemap.json")


def load_json(path):
    """Load JSON file."""
    with open(path, "r") as f:
        return json.load(f)


def save_json(path, data):
    """Save JSON file with proper formatting."""
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def get_anthropic_pages():
    """Load pages from the default anthropic.com sitemap."""
    if not os.path.exists(DEFAULT_SITEMAP):
        print(f"  Warning: {DEFAULT_SITEMAP} not found")
        return []

    sitemap = load_json(DEFAULT_SITEMAP)
    pages = []

    for page in sitemap.get("pages", []):
        pages.append(
            {
                "url": page["url"],
                "path": page["path"],
                "section": page.get("section", "anthropic"),
                "source": "anthropic.com",
            }
        )

    return pages


def get_tutorial_pages():
    """Extract tutorial pages from the tutorials/ folder."""
    pages = []

    if not os.path.exists(TUTORIALS_DIR):
        print(f"  Warning: {TUTORIALS_DIR} not found")
        return pages

    for category in os.listdir(TUTORIALS_DIR):
        category_dir = os.path.join(TUTORIALS_DIR, category)
        if not os.path.isdir(category_dir):
            continue

        for filename in os.listdir(category_dir):
            if not filename.endswith(".md"):
                continue

            filepath = os.path.join(category_dir, filename)
            slug = filename[:-3]  # Remove .md extension

            # Try to extract URL from frontmatter
            url = extract_url_from_file(filepath)
            if not url:
                # Construct URL from slug
                url = f"https://claude.com/resources/tutorials/{slug}"

            pages.append(
                {
                    "url": url,
                    "path": f"tutorials/{category}/{slug}",
                    "section": "tutorials",
                    "category": category,
                    "source": "claude.com",
                }
            )

    return pages


def get_course_pages():
    """Extract course pages from the courses/ folder."""
    pages = []

    if not os.path.exists(COURSES_DIR):
        print(f"  Warning: {COURSES_DIR} not found")
        return pages

    for category in os.listdir(COURSES_DIR):
        category_dir = os.path.join(COURSES_DIR, category)
        if not os.path.isdir(category_dir):
            continue

        for filename in os.listdir(category_dir):
            if not filename.endswith(".md"):
                continue

            filepath = os.path.join(category_dir, filename)
            slug = filename[:-3]  # Remove .md extension

            # Try to extract URL from frontmatter
            url = extract_url_from_file(filepath)
            if not url:
                # Construct URL from slug
                url = f"https://claude.com/resources/courses/{slug}"

            pages.append(
                {
                    "url": url,
                    "path": f"courses/{category}/{slug}",
                    "section": "courses",
                    "category": category,
                    "source": "claude.com",
                }
            )

    return pages


def extract_url_from_file(filepath):
    """Extract URL from YAML frontmatter."""
    try:
        with open(filepath, "r") as f:
            content = f.read()

        # Match url in frontmatter
        match = re.search(r"^url:\s*(.+)$", content, re.MULTILINE)
        if match:
            return match.group(1).strip()
    except Exception:
        pass
    return None


def build_sections(pages):
    """Build section statistics from pages."""
    sections = {}
    for page in pages:
        section = page.get("section", "unknown")
        source = page.get("source", "unknown")
        key = f"{source}/{section}" if source != section else section
        sections[key] = sections.get(key, 0) + 1
    return dict(sorted(sections.items()))


def main():
    print("Generating local sitemap...")

    # Collect all pages
    all_pages = []

    print("  Loading anthropic.com pages...")
    anthropic_pages = get_anthropic_pages()
    print(f"    Found {len(anthropic_pages)} anthropic.com pages")
    all_pages.extend(anthropic_pages)

    print("  Loading claude.com tutorial pages...")
    tutorial_pages = get_tutorial_pages()
    print(f"    Found {len(tutorial_pages)} tutorial pages")
    all_pages.extend(tutorial_pages)

    print("  Loading claude.com course pages...")
    course_pages = get_course_pages()
    print(f"    Found {len(course_pages)} course pages")
    all_pages.extend(course_pages)

    # Build section statistics
    sections = build_sections(all_pages)

    # Create local sitemap
    local_sitemap = {
        "version": "1.0",
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "total": len(all_pages),
        "sources": {
            "anthropic.com": len(anthropic_pages),
            "claude.com": len(tutorial_pages) + len(course_pages),
        },
        "sections": sections,
        "pages": all_pages,
    }

    print(f"  Saving local sitemap ({len(all_pages)} total pages)...")
    save_json(LOCAL_SITEMAP, local_sitemap)

    print(f"\nDone! Local sitemap saved to {LOCAL_SITEMAP}")
    print(f"  Total pages: {len(all_pages)}")
    print(f"  Anthropic.com: {len(anthropic_pages)}")
    print(f"  Claude.com tutorials: {len(tutorial_pages)}")
    print(f"  Claude.com courses: {len(course_pages)}")
    print(f"\nSections:")
    for section, count in sections.items():
        print(f"    {section}: {count}")


if __name__ == "__main__":
    main()
