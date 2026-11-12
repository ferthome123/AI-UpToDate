# AI-UpToDate — instructions for Claude

This repo is a living catalog of everything Superside people build or adopt with AI
(skills, plugins, MCPs, dashboards, workflows, guides). Owner uses it to answer
"do we already have a solution for X?".

## Answering a question
1. Search `CATALOG.md` (tag index at the bottom) and `data/catalog.json` for the problem keywords.
2. Open the matching digest in `sources/` for context, install steps, known issues.
3. Answer with: the item name, who built it, how to use/install it, link, Slack permalink.
   Say clearly if nothing matches, and point to near-misses and open asks.

## Syncing (incremental)
Sources and the last synced message ts per channel live in `sources.json`.
1. For each Slack channel, read messages with `oldest = last_ts` (Slack MCP `slack_read_channel`),
   plus threads with new replies on recent announcements.
2. Add/merge items in that source's `data/*.json` following `data/SCHEMA.md`
   (one item per tool; updates bump `updated`, they don't create duplicates).
3. Append new entries to the digest in `sources/` and update its "newest ts" header.
4. AI Briefly: check Calendar/Drive/Slack for the latest session's notes and add to `sources/meetings/ai-briefly.md`.
5. Update `last_ts` in `sources.json`, run `python3 scripts/build_index.py`, add a line to `CHANGELOG.md`, commit, push.

Never post to Slack or edit other people's docs from a sync. No tokens/secrets in the repo.
