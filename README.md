# AI-UpToDate

A searchable catalog of what the whole company has made with AI — so when you need a
solution, you check here first.

- **[CATALOG.md](CATALOG.md)** — every item by type, newest first, plus a "find by problem" tag index
- **[sources/](sources/)** — per-channel / per-meeting digests with context, install notes, known issues, open asks
- **[data/](data/)** — structured JSON (one file per source; `catalog.json` is the merged view)
- **[sources.json](sources.json)** — tracked sources and sync checkpoints
- **[CHANGELOG.md](CHANGELOG.md)** — what each sync added

## Tracked sources
| Source | Where |
|---|---|
| #everyone-can-build | Slack `C0BDGFE5QTE` |
| #tribe-generative-ai | Slack `C04CC8FSDHP` |
| #motion_dna_mcp_testing | Slack `C0CAJ42DDS8` |
| #make-it-awesome | Slack `C0CGDPJA0S3` |
| AI Briefly (weekly meeting) | Calendar / Drive / Slack announcements |
| Sana Learn | _pending — no connector yet_ |

## Rebuild the catalog
```bash
python3 scripts/build_index.py
```
