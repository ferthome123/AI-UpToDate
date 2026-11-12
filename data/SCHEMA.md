# Item schema (data/*.json)

Each source writes `data/<source-slug>.json`: a JSON array of items, one per distinct AI-made thing
(skill, plugin, MCP, agent, dashboard/artifact, workflow, prompt pack, tool adoption, guide, experiment).

```json
{
  "id": "kebab-case-unique-name",
  "name": "Human name of the thing",
  "type": "skill | plugin | mcp | agent | dashboard | artifact | workflow | automation | guide | tool | experiment | announcement",
  "summary": "1-2 sentences: what it does / what problem it solves",
  "how_to_use": "Short steps or trigger phrase, if given",
  "owners": ["Full Name"],
  "teams": ["e.g. Creative, AM, PM, Motion, Ops, People"],
  "tools": ["Claude", "Figma", "Cowork", "Superspace MCP", "..."],
  "tags": ["problem keywords someone would search for: decks, resizing, buzz, hours, briefs, ..."],
  "status": "shipped | beta | wip | idea | deprecated | unknown",
  "date": "YYYY-MM-DD (first posted)",
  "updated": "YYYY-MM-DD (latest update seen) or null",
  "links": [{"label": "Install / artifact / doc / demo", "url": "https://..."}],
  "source": {"kind": "slack|meeting|sana", "channel": "#name", "permalink": "https://konsus.slack.com/archives/<C>/p<ts-without-dot>"}
}
```

Rules: no secrets/tokens; keep links exactly as posted; one item per distinct tool (merge
updates/versions into the same item, bump `updated`); skip join messages and pure chit-chat.
Slack permalink format: `https://konsus.slack.com/archives/<CHANNEL_ID>/p<ts with the dot removed>`.
