#!/usr/bin/env python3
"""Generate the ai-uptodate skill (as a plugin folder + a standalone .skill zip) from the catalog.

Run after build_index.py:
    python3 scripts/build_index.py && python3 scripts/build_skill.py

Outputs:
    plugin/ai-uptodate/                     plugin folder (publishable to the org with PublishPlugin)
      .claude-plugin/plugin.json
      skills/ai-uptodate/SKILL.md
      skills/ai-uptodate/references/...    catalog snapshot + source digests
    dist/ai-uptodate.skill                  zip of the skill folder, for Settings > Skills upload
"""
import json, os, shutil, zipfile, datetime
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGIN = os.path.join(ROOT, "plugin", "ai-uptodate")
SKILL = os.path.join(PLUGIN, "skills", "ai-uptodate")
REF = os.path.join(SKILL, "references")
DIST = os.path.join(ROOT, "dist")

items = json.load(open(os.path.join(ROOT, "data", "catalog.json")))
sources = json.load(open(os.path.join(ROOT, "sources.json")))
today = datetime.date.today().isoformat()
newest = max((i.get("updated") or i.get("date") or "") for i in items)

shutil.rmtree(PLUGIN, ignore_errors=True)
os.makedirs(REF)
os.makedirs(os.path.join(PLUGIN, ".claude-plugin"))
os.makedirs(DIST, exist_ok=True)

# 1. catalog.jsonl: one item per line, grep-friendly
KEEP = ["id", "name", "type", "summary", "how_to_use", "owners", "teams", "tools", "tags",
        "status", "date", "updated", "links"]
with open(os.path.join(REF, "catalog.jsonl"), "w") as f:
    for it in items:
        row = {k: it.get(k) for k in KEEP if it.get(k)}
        row["sources"] = [{k: v for k, v in s.items() if k in ("kind", "channel", "permalink")}
                          for s in it.get("sources", []) if s]
        f.write(json.dumps(row, ensure_ascii=False) + "\n")

# 2. index.md: compact one-liners grouped by type (fast first read)
by_type = defaultdict(list)
for it in items:
    by_type[it.get("type", "tool")].append(it)
lines = [f"# AI-UpToDate index — {len(items)} items (snapshot {today}, newest item {newest})", "",
         "One line per item: `id` — name — summary [tags]. Full record: grep the id in catalog.jsonl.", ""]
for t in sorted(by_type, key=lambda t: -len(by_type[t])):
    lines += [f"## {t} ({len(by_type[t])})", ""]
    for it in by_type[t]:
        tags = ", ".join(it.get("tags", [])[:8])
        lines.append(f"- `{it['id']}` — **{it['name']}** — {it.get('summary', '')} [{tags}]")
    lines.append("")
open(os.path.join(REF, "index.md"), "w").write("\n".join(lines))

# 3. source digests
digests = [c["digest"] for c in sources["slack_channels"]] + [m["digest"] for m in sources["meetings"]]
if "sana" in sources:
    digests.append(sources["sana"]["digest"])
os.makedirs(os.path.join(REF, "sources"))
digest_list = []
for d in digests:
    src = os.path.join(ROOT, d)
    if os.path.exists(src):
        name = d.replace("sources/", "").replace("/", "__")
        shutil.copy(src, os.path.join(REF, "sources", name))
        digest_list.append(f"- `references/sources/{name}`")

channels = ", ".join(f"{c['name']} (`{c['id']}`)" for c in sources["slack_channels"])

SKILL_MD = f"""---
name: ai-uptodate
description: Find out whether anyone at Superside already built, shared, tested or talked about an AI solution (Claude skill, plugin, MCP/connector, agent, dashboard, artifact, workflow, automation, course or guide) before building something new. Use whenever the user asks "is there a skill/MCP/tool for X", "has anyone done X with AI", "did someone mention X", "who built X", "how do I install X", or needs an AI solution for a work problem (decks, resizing, Figma, After Effects, Premiere, video, briefs, quoting, hours, account dashboards, brand kits, etc.). Searches a weekly-updated catalog of Superside's AI channels, the AI, Briefly meeting recordings and Sana Learn AI courses, then checks live Slack and Sana for anything newer.
---

# AI-UpToDate: find existing AI solutions at Superside

Snapshot: **{len(items)} items**, built {today} (newest item {newest}). Covers Slack {channels};
the weekly **AI, Briefly** meeting (Sana recordings #3 onward); and AI courses in **Sana Learn**.
The snapshot is refreshed weekly from the `ferthome123/AI-UpToDate` repo.

## How to answer

1. **Expand the query.** List the problem's keywords plus synonyms and tool names
   (e.g. "Premiere" → premiere, video edit, timeline, Adobe, MCP, DaVinci, After Effects, editing).
2. **Search the snapshot** (use grep/search over files, case-insensitive; don't read everything):
   - `references/index.md`: one line per item, best first pass.
   - `references/catalog.jsonl`: full records (how_to_use, owners, links, Slack permalinks). Grep the item id.
   - `references/sources/*.md`: per-source digests with context, install steps, known issues,
     "open asks" (requests nobody solved yet) and "tools the team has been watching".
     Grep these too: they mention things that aren't catalog items.
3. **Check live sources** whenever the snapshot has no strong match, the topic is fast-moving, or the
   user asks about anything recent (after {newest}):
   - Slack: `slack_search_public_and_private` with the keywords (all channels, not only the tracked ones).
   - Sana: `search_courses` (read-only: never create, edit or delete).
   - Also consider connectors already enabled in the session that cover the need directly.
   Skip a source if its connector isn't available, and say so.
4. **Answer** in this shape:
   - **Direct hits**: name, what it does, who built it, status, how to install/use, link + Slack permalink or Sana link.
   - **Near misses**: related tools that partially solve it, and what's missing.
   - **Mentions/leads**: people who talked about it, open asks, external tools the team watched.
   - **Verdict**: "exists / partially exists / nobody has built this yet", and who to ask (owners of near misses).
   Say plainly when nothing matches. Mark which findings came from the snapshot and which from live search.

## Notes
- Builders often share `.skill` files in Slack threads because org install links fail across
  Team/Enterprise workspaces; point to the thread if the install link is reported broken.
- Treat statuses (beta/wip) and known issues as real caveats; repeat them.
- This skill only reads. Never post to Slack or change Sana content on its behalf.

## Files
- `references/index.md`
- `references/catalog.jsonl`
{chr(10).join(digest_list)}
"""
open(os.path.join(SKILL, "SKILL.md"), "w").write(SKILL_MD)

json.dump({
    "name": "ai-uptodate",
    "version": "1." + today.replace("-", ""),
    "description": "Find existing AI solutions at Superside: weekly catalog of AI channels, AI, Briefly and Sana AI courses, plus live Slack/Sana search.",
}, open(os.path.join(PLUGIN, ".claude-plugin", "plugin.json"), "w"), indent=2)

# 4. standalone .skill zip (folder ai-uptodate/ at zip root)
zpath = os.path.join(DIST, "ai-uptodate.skill")
with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
    for base, _, files in os.walk(SKILL):
        for fn in sorted(files):
            full = os.path.join(base, fn)
            z.write(full, os.path.join("ai-uptodate", os.path.relpath(full, SKILL)))
print(f"skill: {len(items)} items -> {os.path.relpath(SKILL, ROOT)}, {os.path.relpath(zpath, ROOT)} "
      f"({os.path.getsize(zpath)//1024} KB)")
