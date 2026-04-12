#!/usr/bin/env python3
"""
Generate markdown use case files from claude.com/resources/use-cases.

Usage:
    python3 scripts/generate_use_cases.py
"""

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
USE_CASES_DIR = os.path.join(PROJECT_DIR, "use-cases")

BASE_URL = "https://claude.com/resources/use-cases"

USE_CASES = [
    # Personal (16)
    {
        "slug": "custom-webpage",
        "title": "Create a custom webpage",
        "category": "Personal",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking",
    },
    {
        "slug": "design-skills",
        "title": "Elevate Claude's design using skills",
        "category": "Personal",
        "model": "Sonnet 4.5",
        "features": "Skills",
    },
    {
        "slug": "interactive-diagrams",
        "title": "Build interactive diagram tools",
        "category": "Personal",
        "model": "Opus 4.5",
        "features": "Extended Thinking",
    },
    {
        "slug": "organize-desktop",
        "title": "Organize files across your desktop",
        "category": "Personal",
        "model": "Opus 4.5",
        "features": "Cowork",
    },
    {
        "slug": "map-understanding",
        "title": "Map understanding and build lessons",
        "category": "Personal",
        "model": "Opus 4.6",
        "features": "Extended Thinking",
    },
    {
        "slug": "stress-test-finance",
        "title": "Stress-test financial plans",
        "category": "Personal",
        "model": "Opus 4.6",
        "features": "Extended Thinking",
    },
    {
        "slug": "gift-giving",
        "title": "Thoughtful gift giving with Claude",
        "category": "Personal",
        "model": "Opus 4.5",
        "features": "Web Search, Connectors",
    },
    {
        "slug": "bucket-list",
        "title": "Build a custom bucket list",
        "category": "Personal",
        "model": "Opus 4.5",
        "features": "Extended Thinking",
    },
    {
        "slug": "foraging-guide",
        "title": "Design a local foraging guide",
        "category": "Personal",
        "model": "Opus 4.5",
        "features": "Extended Thinking",
    },
    {
        "slug": "text-to-notes",
        "title": "Turn text threads to researched notes",
        "category": "Personal",
        "model": "Sonnet 4.5",
        "features": "Connectors, Web Search",
    },
    {
        "slug": "design-plans",
        "title": "Turn inspiration into design plans",
        "category": "Personal",
        "model": "Sonnet 4.5",
        "features": "Web Search",
    },
    {
        "slug": "health-notes",
        "title": "Create health and exercise notes",
        "category": "Personal",
        "model": "Sonnet 4.5",
        "features": "Web Search, Connectors",
    },
    {
        "slug": "digital-recipes",
        "title": "Create digital recipe cards",
        "category": "Personal",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking",
    },
    {
        "slug": "travel-itinerary",
        "title": "Create a daily travel itinerary",
        "category": "Personal",
        "model": "Sonnet 4.5",
        "features": "Web Search, Extended Thinking",
    },
    {
        "slug": "debate-practice",
        "title": "Debate practice with feedback",
        "category": "Personal",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking",
    },
    {
        "slug": "compare-destinations",
        "title": "Research and compare travel destinations",
        "category": "Personal",
        "model": "Sonnet 4.5",
        "features": "Web Search, Extended Thinking",
    },
    # Professional (18)
    {
        "slug": "create-brand-assets",
        "title": "Create brand assets",
        "category": "Professional",
        "model": "Sonnet 4.5",
        "features": "Web Search",
    },
    {
        "slug": "brand-guidelines-skill",
        "title": "Package brand guidelines in a skill",
        "category": "Professional",
        "model": "Sonnet 4.5",
        "features": "Skills",
    },
    {
        "slug": "explore-claude",
        "title": "Explore what Claude can do for you",
        "category": "Professional",
        "model": "Opus 4.5",
        "features": "Connectors",
    },
    {
        "slug": "build-analysis",
        "title": "Build analysis from scattered data",
        "category": "Professional",
        "model": "Sonnet 4.5",
        "features": "Cowork",
    },
    {
        "slug": "daily-briefing",
        "title": "Build a daily briefing across tools",
        "category": "Professional",
        "model": "Sonnet 4.5",
        "features": "Cowork",
    },
    {
        "slug": "process-vendors",
        "title": "Process batches of vendors",
        "category": "Professional",
        "model": "Sonnet 4.5",
        "features": "Cowork",
    },
    {
        "slug": "size-market",
        "title": "Size a market using research",
        "category": "Professional",
        "model": "Sonnet 4.5",
        "features": "Cowork",
    },
    {
        "slug": "source-insights-deck",
        "title": "Source insights to build a deck",
        "category": "Professional",
        "model": "Opus 4.6",
        "features": "Extended Thinking, Browser Use",
    },
    {
        "slug": "evaluate-company",
        "title": "Evaluate company (science to balance sheet)",
        "category": "Professional",
        "model": "Opus 4.6",
        "features": "Extended Thinking",
    },
    {
        "slug": "status-reports",
        "title": "Generate project status reports",
        "category": "Professional",
        "model": "Sonnet 4.5",
        "features": "Connectors",
    },
    {
        "slug": "user-feedback-patterns",
        "title": "Analyze patterns in user feedback",
        "category": "Professional",
        "model": "Sonnet 4.5",
        "features": "Connectors",
    },
    {
        "slug": "week-prep",
        "title": "Quickly prep for your week",
        "category": "Professional",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking, Connectors",
    },
    {
        "slug": "compare-options",
        "title": "Compare and analyze competing options",
        "category": "Professional",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking",
    },
    {
        "slug": "interactive-pdf",
        "title": "Create interactive PDF forms",
        "category": "Professional",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking",
    },
    {
        "slug": "process-flowchart",
        "title": "Create a process flowchart",
        "category": "Professional",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking",
    },
    {
        "slug": "email-event-tracker",
        "title": "Turn emails into an event tracker",
        "category": "Professional",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking, Connectors",
    },
    {
        "slug": "company-newsletter",
        "title": "Create a company newsletter",
        "category": "Professional",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking",
    },
    # Education (11)
    {
        "slug": "plan-syllabus",
        "title": "Plan your syllabus",
        "category": "Education",
        "model": "Sonnet 4.6",
        "features": "Custom visuals",
    },
    {
        "slug": "grant-options",
        "title": "Work through grant options in chat",
        "category": "Education",
        "model": "Sonnet 4.6",
        "features": "Custom visuals",
    },
    {
        "slug": "apply-formula",
        "title": "Apply a formula as you learn it",
        "category": "Education",
        "model": "Sonnet 4.6",
        "features": "Custom visuals",
    },
    {
        "slug": "whiteboard-lesson",
        "title": "Bring your whiteboard lesson to life",
        "category": "Education",
        "model": "Sonnet 4.6",
        "features": "Custom visuals",
    },
    {
        "slug": "visualize-mechanism",
        "title": "Visualize mechanism behind explanation",
        "category": "Education",
        "model": "Sonnet 4.6",
        "features": "Custom visuals",
    },
    {
        "slug": "map-lit-review",
        "title": "Map your lit review mid-conversation",
        "category": "Education",
        "model": "Sonnet 4.6",
        "features": "Custom visuals",
    },
    {
        "slug": "chart-data",
        "title": "Chart data in conversation",
        "category": "Education",
        "model": "Sonnet 4.6",
        "features": "Custom visuals",
    },
    {
        "slug": "research-to-presentations",
        "title": "Turn research into presentations",
        "category": "Education",
        "model": "Sonnet 4.5",
        "features": "Connectors",
    },
    {
        "slug": "course-materials",
        "title": "Create custom course materials",
        "category": "Education",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking",
    },
    {
        "slug": "case-interviews",
        "title": "Practice case interviews",
        "category": "Education",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking",
    },
    {
        "slug": "career-path",
        "title": "Plan your career path",
        "category": "Education",
        "model": "Sonnet 4.5",
        "features": "Connectors, Research",
    },
    # Nonprofits (12)
    {
        "slug": "theory-of-change",
        "title": "See your theory of change in chat",
        "category": "Nonprofits",
        "model": "Sonnet 4.6",
        "features": "Custom visuals",
    },
    {
        "slug": "campaign-goal",
        "title": "See campaign goal requirements",
        "category": "Nonprofits",
        "model": "Sonnet 4.6",
        "features": "Custom visuals",
    },
    {
        "slug": "budget-scenarios",
        "title": "See budget futures side by side",
        "category": "Nonprofits",
        "model": "Sonnet 4.6",
        "features": "Custom visuals",
    },
    {
        "slug": "donor-retention",
        "title": "See donor retention vs acquisition",
        "category": "Nonprofits",
        "model": "Sonnet 4.6",
        "features": "Custom visuals",
    },
    {
        "slug": "workflow-planner",
        "title": "Workflow improvement planner",
        "category": "Nonprofits",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking",
    },
    {
        "slug": "grant-proposal-line",
        "title": "Grant proposal assembly line",
        "category": "Nonprofits",
        "model": "Sonnet 4.5",
        "features": "Connectors",
    },
    {
        "slug": "program-toolkit",
        "title": "Develop a program toolkit",
        "category": "Nonprofits",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking",
    },
    {
        "slug": "visualize-program-data",
        "title": "Visualize program data",
        "category": "Nonprofits",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking",
    },
    {
        "slug": "volunteer-management",
        "title": "Create volunteer management system",
        "category": "Nonprofits",
        "model": "Sonnet 4.5",
        "features": "N/A",
    },
    {
        "slug": "fundraising-performance",
        "title": "Analyze fundraising performance",
        "category": "Nonprofits",
        "model": "Sonnet 4.5",
        "features": "Connectors",
    },
    {
        "slug": "ai-policy",
        "title": "Generate an AI policy",
        "category": "Nonprofits",
        "model": "Sonnet 4.5",
        "features": "Web Search",
    },
    {
        "slug": "impact-report",
        "title": "Write an impact report",
        "category": "Nonprofits",
        "model": "Sonnet 4.5",
        "features": "N/A",
    },
    # Finance (6)
    {
        "slug": "update-financial-model",
        "title": "Update financial model after earnings",
        "category": "Finance",
        "model": "Opus 4.6",
        "features": "Connectors, Skills",
    },
    {
        "slug": "understand-spreadsheet",
        "title": "Understand inherited spreadsheet",
        "category": "Finance",
        "model": "Opus 4.5",
        "features": "Extended Thinking",
    },
    {
        "slug": "reconcile-transactions",
        "title": "Reconcile transactions across accounts",
        "category": "Finance",
        "model": "Sonnet 4.5",
        "features": "Cowork",
    },
    {
        "slug": "build-financial-models",
        "title": "Build financial models",
        "category": "Finance",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking, Web Search",
    },
    {
        "slug": "investment-memos",
        "title": "Draft investment memos",
        "category": "Finance",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking, Web Search",
    },
    {
        "slug": "business-finances",
        "title": "Organize business finances",
        "category": "Finance",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking",
    },
    # Legal (4)
    {
        "slug": "contract-negotiation",
        "title": "Contract redlining and negotiation",
        "category": "Legal",
        "model": "Opus 4.5",
        "features": "Extended Thinking",
    },
    {
        "slug": "compliance-audit",
        "title": "Prep documents for compliance audit",
        "category": "Legal",
        "model": "Sonnet 4.5",
        "features": "Cowork",
    },
    {
        "slug": "legal-projects",
        "title": "Organize legal workflows using Projects",
        "category": "Legal",
        "model": "Opus 4.5",
        "features": "Projects",
    },
    {
        "slug": "discovery-timelines",
        "title": "Track discovery timelines",
        "category": "Legal",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking, Connectors",
    },
    # Research (4)
    {
        "slug": "feedback-themes",
        "title": "Surface themes from feedback channels",
        "category": "Research",
        "model": "Sonnet 4.5",
        "features": "Cowork",
    },
    {
        "slug": "transit-research",
        "title": "Turn transit time into research time",
        "category": "Research",
        "model": "Opus 4.5",
        "features": "Research, Web Search",
    },
    {
        "slug": "verify-statistics",
        "title": "Verify statistics from raw data",
        "category": "Research",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking",
    },
    {
        "slug": "plan-lit-review",
        "title": "Plan your literature review",
        "category": "Research",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking",
    },
    # Claude in Chrome (6)
    {
        "slug": "log-sales-calls",
        "title": "Log sales calls to your CRM",
        "category": "Claude in Chrome",
        "model": "Haiku 4.5",
        "features": "Browser Use",
    },
    {
        "slug": "compare-products",
        "title": "Compare products across sites",
        "category": "Claude in Chrome",
        "model": "Haiku 4.5",
        "features": "Browser Use",
    },
    {
        "slug": "plan-calendar",
        "title": "Prepare and plan from your calendar",
        "category": "Claude in Chrome",
        "model": "Haiku 4.5",
        "features": "Browser Use",
    },
    {
        "slug": "clean-inbox",
        "title": "Clean up promotional emails",
        "category": "Claude in Chrome",
        "model": "Haiku 4.5",
        "features": "Browser Use",
    },
    {
        "slug": "pull-metrics",
        "title": "Pull metrics from dashboards",
        "category": "Claude in Chrome",
        "model": "Haiku 4.5",
        "features": "Browser Use",
    },
    {
        "slug": "organize-drive",
        "title": "Organize files in Google Drive",
        "category": "Claude in Chrome",
        "model": "Haiku 4.5",
        "features": "Browser Use",
    },
    # Marketing (3)
    {
        "slug": "adapt-content",
        "title": "Adapt content across platforms",
        "category": "Marketing",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking, Connectors",
    },
    {
        "slug": "campaign-performance",
        "title": "Analyze campaign performance",
        "category": "Marketing",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking",
    },
    {
        "slug": "customer-personas",
        "title": "Build customer personas",
        "category": "Marketing",
        "model": "Sonnet 4.5",
        "features": "Connectors, Extended Thinking",
    },
    # Sales (4)
    {
        "slug": "sales-proposal",
        "title": "Create sales proposal presentation",
        "category": "Sales",
        "model": "Opus 4.5",
        "features": "Extended Thinking, Connectors",
    },
    {
        "slug": "prep-sales-deals",
        "title": "Prepare for sales deals",
        "category": "Sales",
        "model": "Sonnet 4.5",
        "features": "Connectors, Extended Thinking",
    },
    {
        "slug": "sales-reports",
        "title": "Create sales reports",
        "category": "Sales",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking, Connectors",
    },
    {
        "slug": "battle-cards",
        "title": "Build a battle card library",
        "category": "Sales",
        "model": "Sonnet 4.5",
        "features": "Web Search, Connectors",
    },
    # Life Sciences (2)
    {
        "slug": "preclinical-analysis",
        "title": "Preclinical study analysis",
        "category": "Life Sciences",
        "model": "Sonnet 4.5",
        "features": "Connectors",
    },
    {
        "slug": "genomic-analysis",
        "title": "Genomic data analysis",
        "category": "Life Sciences",
        "model": "Sonnet 4.5",
        "features": "Connectors, Extended Thinking",
    },
    # HR (1)
    {
        "slug": "onboarding-guides",
        "title": "Create new hire onboarding guides",
        "category": "HR",
        "model": "Sonnet 4.5",
        "features": "Extended Thinking",
    },
]


def create_markdown(filepath, title, url, category, model, features):
    """Create markdown file with frontmatter and placeholder sections."""
    content = f"""---
title: "{title}"
url: {url}
date:
tags: ["use-cases", "{category.lower().replace(" ", "-")}"]
category: {category}
model: {model}
features: {features}
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
    os.makedirs(USE_CASES_DIR, exist_ok=True)

    created = 0
    skipped = 0

    for use_case in USE_CASES:
        slug = use_case["slug"]
        title = use_case["title"]
        category = use_case["category"]
        model = use_case["model"]
        features = use_case["features"]
        url = f"{BASE_URL}/{slug}"

        category_dir = os.path.join(USE_CASES_DIR, category.lower().replace(" ", "-"))
        os.makedirs(category_dir, exist_ok=True)
        filepath = os.path.join(category_dir, f"{slug}.md")

        if os.path.exists(filepath):
            skipped += 1
            continue

        create_markdown(filepath, title, url, category, model, features)
        created += 1
        print(f"  Created: use-cases/{category.lower().replace(' ', '-')}/{slug}.md")

    print(f"\nDone!")
    print(f"  Created: {created}")
    print(f"  Skipped: {skipped}")
    print(f"  Total: {len(USE_CASES)}")


if __name__ == "__main__":
    main()
