#!/usr/bin/env python3
"""Fast integrity checks for the static Gruvspår website."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import subprocess
import tempfile
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ("href", "src"):
            value = attrs.get(key)
            if value:
                self.targets.append(value)

# Every committed JSON file must parse.
for path in ROOT.rglob("*.json"):
    if ".git" in path.parts:
        continue
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"Invalid JSON: {path.relative_to(ROOT)} ({exc})")

# All local links and assets referenced directly by HTML must exist.
for html in ROOT.rglob("*.html"):
    parser = Links()
    try:
        parser.feed(html.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"HTML parse failure: {html.relative_to(ROOT)} ({exc})")
        continue
    for target in parser.targets:
        parts = urlsplit(target)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        rel = unquote(parts.path)
        candidate = (html.parent / rel).resolve()
        if rel.endswith("/"):
            candidate = candidate / "index.html"
        if not candidate.exists():
            errors.append(f"Broken local link in {html.relative_to(ROOT)}: {target}")

# Every profile ID in gruva.html must have a matching data file.
profile_page = ROOT / "gruva.html"
if profile_page.exists():
    source = profile_page.read_text(encoding="utf-8")
    match = re.search(r"const sites=(\[.*?\]);\s*const params=", source, re.S)
    if not match:
        errors.append("Could not read the profile registry in gruva.html")
    else:
        try:
            sites = json.loads(match.group(1))
            for site in sites:
                site_id = site[0]
                data_id = "garpenberg" if site_id == "garpenberg-nya" else site_id
                target = ROOT / "data" / "sites" / f"{data_id}.json"
                if not target.is_file():
                    errors.append(f"Missing profile data: {target.relative_to(ROOT)}")
        except Exception as exc:
            errors.append(f"Invalid profile registry in gruva.html ({exc})")

# Data files required by the pages' dynamic fetch() calls.
for rel in (
    "data/remediation-projects.json",
    "data/sources/remediation.json",
    "data/sources/nationellt.json",
):
    if not (ROOT / rel).is_file():
        errors.append(f"Missing required data file: {rel}")

# Parse every inline script with Node without executing browser code.
for html in ROOT.rglob("*.html"):
    content = html.read_text(encoding="utf-8")
    for index, match in enumerate(re.finditer(r"<script\b[^>]*>([\s\S]*?)</script>", content, re.I), 1):
        code = match.group(1).strip()
        if not code:
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8") as tmp:
            tmp.write(code)
            tmp.flush()
            result = subprocess.run(
                ["node", "--check", tmp.name],
                capture_output=True, text=True
            )
        if result.returncode:
            errors.append(
                f"JavaScript syntax error in {html.relative_to(ROOT)} "
                f"(script {index}): {result.stderr.strip()}"
            )

if errors:
    print("\n".join(f"ERROR: {item}" for item in errors))
    sys.exit(1)

print("Gruvspår smoke tests passed: JSON, local links, profile data and inline JavaScript.")
