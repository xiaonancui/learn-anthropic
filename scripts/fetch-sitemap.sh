#!/bin/bash
# Fetch the latest sitemap from anthropic.com and update data/sitemap.json
# Usage: bash scripts/fetch-sitemap.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
DATA_DIR="$PROJECT_DIR/data"

echo "Fetching sitemap from anthropic.com..."
URLS=$(curl -s https://www.anthropic.com/sitemap.xml | grep -oP '(?<=<loc>)[^<]+' | sort -u)
TOTAL=$(echo "$URLS" | wc -l)

echo "Found $TOTAL unique pages."

# Build JSON
python3 -c "
import json, sys, datetime

urls = '''$URLS'''.strip().split('\n')
entries = []
sections = {}
for u in urls:
    u = u.strip()
    if not u:
        continue
    path = u.replace('https://www.anthropic.com/', '')
    parts = path.split('/') if path else []
    section = parts[0] if parts else 'root'
    sections[section] = sections.get(section, 0) + 1
    entries.append({'url': u, 'path': path, 'section': section})

result = {
    'total': len(entries),
    'fetched_at': datetime.datetime.utcnow().isoformat() + 'Z',
    'sections': dict(sorted(sections.items(), key=lambda x: -x[1])),
    'pages': entries
}

with open('$DATA_DIR/sitemap.json', 'w') as f:
    json.dump(result, f, indent=2)

print(f'Updated {len(entries)} pages across {len(sections)} sections.')
print('Sections:', ', '.join(f'{k}({v})' for k, v in sorted(sections.items(), key=lambda x: -x[1])))
"

echo "Done. data/sitemap.json updated."
