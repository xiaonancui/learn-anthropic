#!/usr/bin/env python3
"""
Generate markdown tutorial files from claude.com/resources/tutorials.

Usage:
    python3 scripts/generate_tutorials.py
"""

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
TUTORIALS_DIR = os.path.join(PROJECT_DIR, "tutorials")

BASE_URL = "https://claude.com/resources/tutorials"

TUTORIALS = [
    # Professional - Claude Cowork
    {
        "slug": "set-up-claude-cowork",
        "title": "Set up Claude Cowork to work the way you do",
        "category": "Professional",
        "product": "Claude Cowork",
    },
    {
        "slug": "customize-plugins-cowork",
        "title": "How to customize plugins in Claude Cowork",
        "category": "Professional",
        "product": "Claude Cowork",
    },
    {
        "slug": "build-plugin-scratch",
        "title": "How to build a plugin from scratch in Claude Cowork",
        "category": "Professional",
        "product": "Claude Cowork",
    },
    {
        "slug": "claude-cowork-preview",
        "title": "Claude Cowork, a research preview",
        "category": "Professional",
        "product": "Claude Cowork",
    },
    {
        "slug": "cowork-enterprise-admin",
        "title": "Claude Cowork Enterprise Admin Guide",
        "category": "Professional",
        "product": "Claude Cowork",
    },
    {
        "slug": "scaling-workflows-cowork",
        "title": "Scaling workflows with Claude Cowork",
        "category": "Professional",
        "product": "Claude Cowork",
    },
    # Professional - Claude.ai
    {
        "slug": "navigating-desktop-app",
        "title": "Navigating the Claude desktop app: Chat, Claude Cowork, Claude Code",
        "category": "Professional",
        "product": "Claude.ai",
    },
    {
        "slug": "getting-good-at-claude",
        "title": "Getting good at Claude: A research-backed curriculum",
        "category": "Professional",
        "product": "AI Fluency",
    },
    {
        "slug": "choosing-claude-model",
        "title": "Choosing the right Claude model: Haiku, Sonnet, and Opus",
        "category": "Professional",
        "product": "Claude.ai",
    },
    {
        "slug": "get-most-from-opus-4-6",
        "title": "Get the most from Claude Opus 4.6",
        "category": "Professional",
        "product": "Claude.ai",
    },
    {
        "slug": "claude-in-chrome",
        "title": "Simplify your browsing experience with Claude in Chrome",
        "category": "Professional",
        "product": "Claude in Chrome",
    },
    {
        "slug": "getting-started-claude-ai",
        "title": "Getting started with Claude.ai",
        "category": "Professional",
        "product": "Claude.ai",
    },
    {
        "slug": "applying-opus-4-5",
        "title": "Applying Claude Opus 4.5's strengths to your everyday work",
        "category": "Professional",
        "product": "Claude.ai",
    },
    {
        "slug": "use-artifacts-create-apps",
        "title": "Use artifacts to visualize and create AI apps",
        "category": "Professional",
        "product": "Claude.ai",
    },
    {
        "slug": "teach-claude-skills",
        "title": "Teach Claude your way of working using skills",
        "category": "Professional",
        "product": "Claude.ai",
    },
    {
        "slug": "getting-started-excel",
        "title": "Getting started with Claude in Excel",
        "category": "Professional",
        "product": "Claude in Excel",
    },
    {
        "slug": "professional-results-sonnet-4-5",
        "title": "Create professional results with Claude Sonnet 4.5",
        "category": "Professional",
        "product": "Claude.ai",
    },
    {
        "slug": "create-edit-files",
        "title": "Create and edit files with Claude",
        "category": "Professional",
        "product": "Claude.ai",
    },
    {
        "slug": "most-out-of-sonnet-4-5",
        "title": "Getting the most out of Sonnet 4.5 in Claude.ai",
        "category": "Professional",
        "product": "Claude.ai",
    },
    {
        "slug": "intro-to-artifacts",
        "title": "Intro to Artifacts",
        "category": "Professional",
        "product": "Claude.ai",
    },
    {
        "slug": "intro-to-projects",
        "title": "Intro to Projects",
        "category": "Professional",
        "product": "Claude.ai",
    },
    {
        "slug": "getting-started-connectors",
        "title": "Getting started with connectors",
        "category": "Professional",
        "product": "Claude.ai",
    },
    {
        "slug": "using-research",
        "title": "Using Research",
        "category": "Professional",
        "product": "Claude.ai",
    },
    {
        "slug": "prototype-apps-artifacts",
        "title": "Prototype AI-Powered Apps with Claude artifacts",
        "category": "Professional",
        "product": "Claude.ai",
    },
    {
        "slug": "connect-tools",
        "title": "Connect your tools for a smarter AI companion",
        "category": "Professional",
        "product": "Claude.ai",
    },
    {
        "slug": "create-skill-conversation",
        "title": "How to create a skill through conversation",
        "category": "Professional",
        "product": "Claude.ai",
    },
    {
        "slug": "enterprise-admin-guide",
        "title": "Claude Enterprise Administrator Guide",
        "category": "Professional",
        "product": "Claude.ai",
    },
    {
        "slug": "enable-claude-code-enterprise",
        "title": "How to enable Claude Code for Enterprise",
        "category": "Professional",
        "product": "Claude Code",
    },
    {
        "slug": "claude-product-management",
        "title": "Claude for Product Management",
        "category": "Professional",
        "product": "Claude.ai",
    },
    {
        "slug": "google-docs-integration",
        "title": "Using the Google Docs integration",
        "category": "Professional",
        "product": "Claude.ai",
    },
    {
        "slug": "research-google-workspace",
        "title": "Using Research and Google Workspace",
        "category": "Professional",
        "product": "Claude.ai",
    },
    # Engineering
    {
        "slug": "what-is-managed-agents",
        "title": "What is Claude Managed Agents?",
        "category": "Engineering",
        "product": "Claude Platform",
    },
    {
        "slug": "claude-code-remote-control",
        "title": "Using Claude Code Remote Control",
        "category": "Engineering",
        "product": "Claude Code",
    },
    {
        "slug": "skills-vs-features",
        "title": "How skills compare to other Claude Code features",
        "category": "Engineering",
        "product": "Claude Code",
    },
    {
        "slug": "what-are-skills",
        "title": "What are skills?",
        "category": "Engineering",
        "product": "Claude Code",
    },
    {
        "slug": "github-integration",
        "title": "Using the GitHub integration",
        "category": "Engineering",
        "product": "Claude.ai",
    },
    {
        "slug": "troubleshooting-skills",
        "title": "Troubleshooting skills",
        "category": "Engineering",
        "product": "Claude Code",
    },
    {
        "slug": "sharing-skills",
        "title": "Sharing skills",
        "category": "Engineering",
        "product": "Claude Code",
    },
    {
        "slug": "configuration-multi-file-skills",
        "title": "Configuration and multi-file skills",
        "category": "Engineering",
        "product": "Claude Code",
    },
    {
        "slug": "creating-first-skill",
        "title": "Creating your first skill",
        "category": "Engineering",
        "product": "Claude Code",
    },
    {
        "slug": "claude-for-engineering",
        "title": "Claude for Engineering",
        "category": "Engineering",
        "product": "Claude.ai",
    },
    # Finance
    {
        "slug": "claude-financial-services",
        "title": "Getting Started with Claude for Financial Services",
        "category": "Finance",
        "product": "Claude.ai",
    },
    {
        "slug": "claude-excel-accounting",
        "title": "How to use Claude in Excel for accounting",
        "category": "Finance",
        "product": "Claude.ai",
    },
    {
        "slug": "claude-excel-hr",
        "title": "How to use Claude in Excel for HR: Headcount planning",
        "category": "Finance",
        "product": "Claude.ai",
    },
    {
        "slug": "financial-plugins-cowork",
        "title": "Install financial services plugins for Claude Cowork",
        "category": "Finance",
        "product": "Claude Cowork",
    },
    {
        "slug": "databricks-data-analysis",
        "title": "Using Databricks for Data Analysis",
        "category": "Finance",
        "product": "Claude.ai",
    },
    {
        "slug": "factset-financial-research",
        "title": "Using FactSet for financial research",
        "category": "Finance",
        "product": "Claude.ai",
    },
    {
        "slug": "daloopa-financial-analysis",
        "title": "Using Daloopa for financial analysis",
        "category": "Finance",
        "product": "Claude.ai",
    },
    {
        "slug": "egnyte-data-room",
        "title": "Using Egnyte for data room management",
        "category": "Finance",
        "product": "Claude.ai",
    },
    {
        "slug": "six-financial-skills",
        "title": "Six skills for financial service professionals",
        "category": "Finance",
        "product": "Claude.ai",
    },
    {
        "slug": "financial-services-overview",
        "title": "Claude for financial services overview",
        "category": "Finance",
        "product": "Claude.ai",
    },
    {
        "slug": "financial-analysis-workflows",
        "title": "Financial analysis workflows with Claude",
        "category": "Finance",
        "product": "Claude.ai",
    },
    {
        "slug": "morningstar-investment-research",
        "title": "Using Morningstar for investment research",
        "category": "Finance",
        "product": "Claude.ai",
    },
    {
        "slug": "aiera-earnings-intelligence",
        "title": "Using Aiera for earnings intelligence",
        "category": "Finance",
        "product": "Claude.ai",
    },
    {
        "slug": "lseg-market-analysis",
        "title": "Using LSEG for financial market data analysis",
        "category": "Finance",
        "product": "Claude.ai",
    },
    {
        "slug": "financial-prompting-strategies",
        "title": "Prompting strategies for financial analysis",
        "category": "Finance",
        "product": "Claude.ai",
    },
    {
        "slug": "chronograph-portfolio-monitoring",
        "title": "Using Chronograph for portfolio monitoring",
        "category": "Finance",
        "product": "Claude.ai",
    },
    {
        "slug": "mt-newswires-news",
        "title": "Using MT Newswires for real-time news",
        "category": "Finance",
        "product": "Claude.ai",
    },
    {
        "slug": "moodys-financial-analysis",
        "title": "Using Moody's for financial analysis",
        "category": "Finance",
        "product": "Claude.ai",
    },
    {
        "slug": "pitchbook-investment-research",
        "title": "Using PitchBook for investment research",
        "category": "Finance",
        "product": "Claude.ai",
    },
    {
        "slug": "sp-global-analysis",
        "title": "Using S&P global data for financial analysis",
        "category": "Finance",
        "product": "Claude.ai",
    },
    # Life Sciences
    {
        "slug": "claude-life-sciences",
        "title": "Getting Started with Claude for Life Sciences",
        "category": "Life Sciences",
        "product": "Claude.ai",
    },
    {
        "slug": "tooluniverse-extension",
        "title": "Using the ToolUniverse Extension in Claude",
        "category": "Life Sciences",
        "product": "Claude.ai",
    },
    {
        "slug": "biorender-connector",
        "title": "Using the BioRender Connector in Claude",
        "category": "Life Sciences",
        "product": "Claude.ai",
    },
    {
        "slug": "10x-genomics-extension",
        "title": "Using the 10x Genomics Extension in Claude",
        "category": "Life Sciences",
        "product": "Claude.ai",
    },
    {
        "slug": "nextflow-deployment-skill",
        "title": "Nextflow Deployment agent skill with Claude Code",
        "category": "Life Sciences",
        "product": "Claude Code",
    },
    {
        "slug": "instrument-data-allotrope",
        "title": "Instrument Data to Allotrope Skill with Claude",
        "category": "Life Sciences",
        "product": "Claude.ai",
    },
    {
        "slug": "clinicaltrials-gov-connector",
        "title": "Using the ClinicalTrials.gov Connector",
        "category": "Life Sciences",
        "product": "Claude.ai",
    },
    {
        "slug": "pubmed-connector",
        "title": "Using the PubMed Connector in Claude",
        "category": "Life Sciences",
        "product": "Claude.ai",
    },
    {
        "slug": "biorxiv-medrxiv-connector",
        "title": "Using bioRxiv and medRxiv Connectors",
        "category": "Life Sciences",
        "product": "Claude.ai",
    },
    {
        "slug": "clinical-trial-protocol-skill",
        "title": "Clinical Trial Protocol Draft Generation skill",
        "category": "Life Sciences",
        "product": "Claude.ai",
    },
    {
        "slug": "single-cell-rna-qc-skill",
        "title": "How to use the single-cell-rna-qc skill",
        "category": "Life Sciences",
        "product": "Claude.ai",
    },
    {
        "slug": "benchling-connector",
        "title": "Using the Benchling connector in Claude",
        "category": "Life Sciences",
        "product": "Claude.ai",
    },
    {
        "slug": "scientific-problem-selection",
        "title": "Scientific Problem Selection Skill with Claude",
        "category": "Life Sciences",
        "product": "Claude.ai",
    },
    {
        "slug": "scvi-tools-bioinformatics",
        "title": "scVI-Tools bioinformatics skill bundle",
        "category": "Life Sciences",
        "product": "Claude.ai",
    },
    {
        "slug": "chembl-connector",
        "title": "Using the ChEMBL Connector in Claude",
        "category": "Life Sciences",
        "product": "Claude.ai",
    },
    {
        "slug": "owkin-connector",
        "title": "Using the Owkin Connector in Claude",
        "category": "Life Sciences",
        "product": "Claude.ai",
    },
    {
        "slug": "open-targets-connector",
        "title": "Using the Open Targets Connector in Claude",
        "category": "Life Sciences",
        "product": "Claude.ai",
    },
    {
        "slug": "medidata-connector",
        "title": "Using the Medidata Connector in Claude",
        "category": "Life Sciences",
        "product": "Claude.ai",
    },
    {
        "slug": "synapse-org-connector",
        "title": "Using the Synapse.org Connector in Claude",
        "category": "Life Sciences",
        "product": "Claude.ai",
    },
    {
        "slug": "scholar-gateway-connector",
        "title": "Using the Scholar Gateway Connector in Claude",
        "category": "Life Sciences",
        "product": "Claude.ai",
    },
    # Healthcare
    {
        "slug": "function-connector",
        "title": "Using the Function Connector in Claude",
        "category": "Healthcare",
        "product": "Claude.ai",
    },
    {
        "slug": "healthex-connector",
        "title": "Using the HealthEx Connector in Claude",
        "category": "Healthcare",
        "product": "Claude.ai",
    },
    {
        "slug": "icd-10-connector",
        "title": "Using the ICD-10 Connector in Claude",
        "category": "Healthcare",
        "product": "Claude.ai",
    },
    {
        "slug": "prior-auth-review-skill",
        "title": "Prior Auth Review sample skill with Claude",
        "category": "Healthcare",
        "product": "Claude.ai",
    },
    {
        "slug": "cms-coverage-connector",
        "title": "Using the CMS Coverage Connector in Claude",
        "category": "Healthcare",
        "product": "Claude.ai",
    },
    {
        "slug": "fhir-developer-skill",
        "title": "FHIR Developer agent skill with Claude Code",
        "category": "Healthcare",
        "product": "Claude Code",
    },
    {
        "slug": "npi-registry-connector",
        "title": "Using the NPI Registry Connector in Claude",
        "category": "Healthcare",
        "product": "Claude.ai",
    },
    # AI Fluency
    {
        "slug": "ai-diligence-statement",
        "title": "Writing an AI diligence statement",
        "category": "AI Fluency",
        "product": "Professional",
    },
    {
        "slug": "ai-fluency-index-guide",
        "title": "A discussion guide for the AI Fluency Index",
        "category": "AI Fluency",
        "product": "AI Fluency",
    },
    # Nonprofits
    {
        "slug": "claude-nonprofits",
        "title": "Getting started with Claude for nonprofits",
        "category": "Nonprofits",
        "product": "Claude.ai",
    },
    {
        "slug": "candid-connector",
        "title": "Using the Candid connector in Claude",
        "category": "Nonprofits",
        "product": "Claude.ai",
    },
    {
        "slug": "blackbaud-connector",
        "title": "Using the Blackbaud connector in Claude",
        "category": "Nonprofits",
        "product": "Claude.ai",
    },
    {
        "slug": "benevity-connector",
        "title": "Using the Benevity connector in Claude",
        "category": "Nonprofits",
        "product": "Claude.ai",
    },
    {
        "slug": "nonprofits-partnership-guide",
        "title": "Claude for nonprofits partnership guide",
        "category": "Nonprofits",
        "product": "Claude.ai",
    },
    {
        "slug": "nonprofits-admin-success",
        "title": "Claude for nonprofits success guide for admins",
        "category": "Nonprofits",
        "product": "Claude.ai",
    },
    # Education
    {
        "slug": "visuals-study-claude",
        "title": "Visuals that appear as you study with Claude",
        "category": "Education",
        "product": "Claude.ai",
    },
    # Marketing
    {
        "slug": "claude-for-marketing",
        "title": "Claude for Marketing",
        "category": "Marketing",
        "product": "Claude.ai",
    },
    # HR
    {
        "slug": "claude-for-hr",
        "title": "Claude for Human Resources",
        "category": "HR",
        "product": "Claude.ai",
    },
    # Sales
    {
        "slug": "claude-for-sales",
        "title": "Claude for Sales",
        "category": "Sales",
        "product": "Claude.ai",
    },
]


def create_markdown(filepath, title, url, category, product):
    """Create markdown file with frontmatter and placeholder sections."""
    content = f"""---
title: "{title}"
url: {url}
date:
tags: ["tutorials", "{category.lower().replace(" ", "-")}"]
category: {category}
product: {product}
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
    os.makedirs(TUTORIALS_DIR, exist_ok=True)

    created = 0
    skipped = 0

    for tutorial in TUTORIALS:
        slug = tutorial["slug"]
        title = tutorial["title"]
        category = tutorial["category"]
        product = tutorial["product"]
        url = f"{BASE_URL}/{slug}"

        filepath = os.path.join(TUTORIALS_DIR, f"{slug}.md")

        if os.path.exists(filepath):
            skipped += 1
            continue

        create_markdown(filepath, title, url, category, product)
        created += 1
        print(f"  Created: tutorials/{slug}.md")

    print(f"\nDone!")
    print(f"  Created: {created}")
    print(f"  Skipped: {skipped}")
    print(f"  Total: {len(TUTORIALS)}")


if __name__ == "__main__":
    main()
