---
name: ai-uptodate
description: Find out whether anyone at Superside already built, shared, tested or talked about an AI solution (Claude skill, plugin, MCP/connector, agent, dashboard, artifact, workflow, automation, course or guide) before building something new. Use whenever the user asks "is there a skill/MCP/tool for X", "has anyone done X with AI", "did someone mention X", "who built X", "how do I install X", or needs an AI solution for a work problem (decks, resizing, Figma, After Effects, Premiere, video, briefs, quoting, hours, account dashboards, brand kits, etc.). Searches a weekly-updated catalog of Superside's AI channels, the AI, Briefly meeting recordings and Sana Learn AI courses, then checks live Slack and Sana for anything newer.
---

# AI-UpToDate: find existing AI solutions at Superside

Snapshot: **302 items**, built 2026-11-12 (newest item 2026-11-12). Covers Slack #everyone-can-build (`C0BDGFE5QTE`), #tribe-generative-ai (`C04CC8FSDHP`), #motion_dna_mcp_testing (`C0CAJ42DDS8`), #make-it-awesome (`C0CGDPJA0S3`);
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
   user asks about anything recent (after 2026-11-12):
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
- `references/sources/slack__everyone-can-build.md`
- `references/sources/slack__tribe-generative-ai.md`
- `references/sources/slack__motion-dna-mcp-testing.md`
- `references/sources/slack__make-it-awesome.md`
- `references/sources/meetings__ai-briefly.md`
- `references/sources/sana__courses.md`
