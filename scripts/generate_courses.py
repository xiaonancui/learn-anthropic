#!/usr/bin/env python3
"""
Generate markdown course files from claude.com/resources/courses.

Usage:
    python3 scripts/generate_courses.py
"""

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
COURSES_DIR = os.path.join(PROJECT_DIR, "courses")

BASE_URL = "https://claude.com/resources/courses"

COURSES = [
    # Engineering
    {
        "slug": "claude-code-101",
        "title": "Claude Code 101",
        "category": "Engineering",
        "product": "Claude Code",
        "details": "12 lessons / 1 hour / Includes quiz",
    },
    {
        "slug": "introduction-to-subagents",
        "title": "Introduction to subagents",
        "category": "Engineering",
        "product": "Claude Code",
        "details": "4 lessons / 20 minutes / Includes quiz",
    },
    {
        "slug": "introduction-to-agent-skills",
        "title": "Introduction to agent skills",
        "category": "Engineering",
        "product": "Claude Code",
        "details": "6 lessons / 30 minutes / Includes quiz",
    },
    {
        "slug": "building-with-claude-api",
        "title": "Building with the Claude API",
        "category": "Engineering",
        "product": "Claude Platform",
        "details": "84 lessons / 8.1 hours / 10 quizzes",
    },
    {
        "slug": "claude-code-in-action",
        "title": "Claude Code in Action",
        "category": "Engineering",
        "product": "Claude Code",
        "details": "15 lessons / 1 hour / 1 quiz",
    },
    {
        "slug": "intro-to-mcp",
        "title": "Introduction to Model Context Protocol",
        "category": "Engineering",
        "product": "MCP",
        "details": "16 lessons / 1 hour / 1 quiz",
    },
    {
        "slug": "mcp-advanced-topics",
        "title": "Model Context Protocol: Advanced Topics",
        "category": "Engineering",
        "product": "MCP",
        "details": "15 lessons / 1.1 hours / 2 quizzes",
    },
    {
        "slug": "claude-amazon-bedrock",
        "title": "Claude with Amazon Bedrock",
        "category": "Engineering",
        "product": "Claude Platform",
        "details": "85 lessons / 8 hours / 10 quizzes",
    },
    {
        "slug": "claude-google-vertex-ai",
        "title": "Claude with Google Cloud's Vertex AI",
        "category": "Engineering",
        "product": "Claude Platform",
        "details": "85 lessons / 8 hours / 10 quizzes",
    },
    # Professional
    {
        "slug": "introduction-to-claude-cowork",
        "title": "Introduction to Claude Cowork",
        "category": "Professional",
        "product": "Claude Cowork",
        "details": "Course details TBD",
    },
    {
        "slug": "ai-fluency-framework-foundations",
        "title": "AI Fluency: Framework & Foundations",
        "category": "Professional",
        "product": "AI Fluency",
        "details": "14 lessons / 1.1 hours / 1 quiz",
    },
    {
        "slug": "claude-101",
        "title": "Claude 101",
        "category": "Professional",
        "product": "Claude.ai",
        "details": "12 lessons / 1 hour / Includes quiz",
    },
    # Education
    {
        "slug": "ai-fluency-for-educators",
        "title": "AI Fluency for Educators",
        "category": "Education",
        "product": "AI Fluency",
        "details": "4 lessons / 24 minutes / Includes quiz",
    },
    {
        "slug": "ai-fluency-for-students",
        "title": "AI Fluency for Students",
        "category": "Education",
        "product": "AI Fluency",
        "details": "5 lessons / 30 minutes / Includes quiz",
    },
    {
        "slug": "teaching-ai-fluency",
        "title": "Teaching AI Fluency",
        "category": "Education",
        "product": "AI Fluency",
        "details": "7 lessons / 36 minutes / 1 quiz",
    },
    # Nonprofits
    {
        "slug": "ai-fluency-nonprofits",
        "title": "AI Fluency for nonprofits",
        "category": "Nonprofits",
        "product": "AI Fluency",
        "details": "9 lessons / 54 minutes / 1 quiz",
    },
]


def create_markdown(filepath, title, url, category, product, details):
    """Create markdown file with frontmatter and placeholder sections."""
    content = f"""---
title: "{title}"
url: {url}
date:
tags: ["courses", "{category.lower().replace(" ", "-")}"]
category: {category}
product: {product}
---

## Course Details

{details}

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
    os.makedirs(COURSES_DIR, exist_ok=True)

    created = 0
    skipped = 0

    for course in COURSES:
        slug = course["slug"]
        title = course["title"]
        category = course["category"]
        product = course["product"]
        details = course["details"]
        url = f"{BASE_URL}/{slug}"

        category_dir = os.path.join(COURSES_DIR, category.lower().replace(" ", "-"))
        os.makedirs(category_dir, exist_ok=True)
        filepath = os.path.join(category_dir, f"{slug}.md")

        if os.path.exists(filepath):
            skipped += 1
            continue

        create_markdown(filepath, title, url, category, product, details)
        created += 1
        print(f"  Created: courses/{category.lower().replace(' ', '-')}/{slug}.md")

    print(f"\nDone!")
    print(f"  Created: {created}")
    print(f"  Skipped: {skipped}")
    print(f"  Total: {len(COURSES)}")


if __name__ == "__main__":
    main()
