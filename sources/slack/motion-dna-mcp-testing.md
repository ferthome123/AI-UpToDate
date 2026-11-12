# #motion_dna_mcp_testing — digest

- **Channel:** #motion_dna_mcp_testing (`C0CAJ42DDS8`) — https://konsus.slack.com/archives/C0CAJ42DDS8
- **Date range read:** 2026-10-19 to 2026-11-12 (entire history; 2 pages, all threads read)
- **Newest message ts read:** `1794472551.027969` (2026-11-12 05:35 -03)
- **About:** beta-testing channel for Motion DNA, an After Effects plugin + MCP by Gian Orsi and Aaron Amortegui (personal R&D outside project hours, no product-team support). Presented at AI Briefly 2026-10-28.

## Items (newest first)

### Motion Maxxing (Solar team) — 2026-11-03
Andres Mariño and Igor Nascimento's AE add-on (Claude API keys) with the same goal as Motion DNA, but plans the video and builds a Figma storyboard first, understands editing (SFX, pacing), connects to 3D and does 2D character lip-sync. Aaron says Motion DNA's agent has since absorbed its logic "to complement". Margot set up a cross-studio call (became #make-it-awesome).
- https://konsus.slack.com/archives/C0CAJ42DDS8/p1793716742997749 · https://konsus.slack.com/archives/C0CAJ42DDS8/p1793722106980209

### Claude motion bypassing After Effects (Axel Torres) — 2026-11-03
Mentioned only: Axel Torres doing motion with Claude without AE (Gen AI tribe channel).
- https://konsus.slack.com/archives/C0CAJ42DDS8/p1793718981348349

### Motion DNA with ChatGPT Codex (Reddit account) — 2026-10-30
Fariel Minozzo connected Codex to AE via Motion DNA so he can work on Reddit, which disallows Claude. Gian was adding a Codex-only mode with a client brand profile; suggested animating master ads with the brand profile then resizes.
- https://konsus.slack.com/archives/C0CAJ42DDS8/p1793384581064889

### Fix: Figma MCP disconnects due to Avast HTTPS scanning — 2026-10-29
Cristina Corat's workaround for `Failed to connect: InvalidHTTPResponse fetching mcp.figma.com` (see Known issues).
- https://konsus.slack.com/archives/C0CAJ42DDS8/p1793307033755239

### Motion DNA Library guide (HTML) — 2026-10-28
Preliminary ~49 MB HTML guide to everything inside the plugin; start with pixel-art character creation + lip sync.
- https://konsus.slack.com/archives/C0CAJ42DDS8/p1793203652981329

### Motion DNA video tutorials T02–T10 — 2026-10-20 to 2026-10-22
Panel tour, connecting apps, behaviours & curves, brands (vision: link to Brand Brain), the Agent (same Claude as the app, with prompt library in-panel), Figma/Flora→AE example, more Agent examples, prompt library. UI has since changed (2026-10-28 note).
- https://konsus.slack.com/archives/C0CAJ42DDS8/p1792517942975409 (first) · https://konsus.slack.com/archives/C0CAJ42DDS8/p1792719392122739 (last)

### Higgsfield AE MCP — 2026-10-20
Gian uses both Higgsfield's AE MCP and Motion DNA; they coexist.
- https://konsus.slack.com/archives/C0CAJ42DDS8/p1792513533163999

### Motion DNA Quick Install guide (PDF + video) — 2026-10-19 (re-shared 10-28, 11-10)
7 steps / ~5 min; Claude Code installs it from the repo.
- Repo: https://github.com/aaronamortegui-glitch/Motion_library
- https://konsus.slack.com/archives/C0CAJ42DDS8/p1792430635040219

### Motion DNA (AE plugin + MCP) — 2026-10-19, updated through 2026-11-04
Lets Claude/Codex animate in AE with editable layers from Figma storyboards, video references and brand profiles; built-in Agent chat; style map from 20+ analysed motion videos ("animate in elegant/editorial/modern style"); customizable curves and brand guidelines for refinement. Connects Figma, Krea, Flora, Blender 3D; pixel-art characters with lip-sync; SFX. Library (10-22): 71 presets + 9 recipes, 113 kit pieces, 46 transitions, 12 techniques, 9 styles, 14 easing curves, 14 code video templates, 41 AE tools, 166 licensed outside resources. Updates: library-suggestion skill + pixel-art characters (10-22); image then video references in Agent chat (10-23); absorbed Stageshow (benjitaylor/skills) and claude-animation-skills (artemnovitckii) repos incl. motion_qa and Web Motion tab (11-04).
- https://konsus.slack.com/archives/C0CAJ42DDS8/p1792430099332629 · https://konsus.slack.com/archives/C0CAJ42DDS8/p1792681078539359 · https://konsus.slack.com/archives/C0CAJ42DDS8/p1793810534389019

## Install / setup notes
1. Claude desktop › Code › + New session in any projects folder (not the After Effects folder — needs admin rights).
2. Send: `Install Motion DNA from https://github.com/aaronamortegui-glitch/Motion_library` — Claude clones, runs setup (signed panel, fonts, Claude link), checks it.
3. AE › Preferences › Scripting & Expressions › tick *Allow Scripts to Write Files and Access Network*.
4. Restart AE › Window › Extensions › Motion DNA (also File › Scripts); dock it. MCP link starts automatically with AE.
5. Agent › Connect: Claude (sign in), Figma (optional); Flora/Krea via claude.ai › Settings › Connectors (optional). Gian polled for Krea/Flora/Weavy access.
6. Manual install: `git clone` + `python tools/setup.py` (docs/quick-install/MANUAL.md). Uninstall: `python tools/setup.py --uninstall`.
7. **Update often** (refined daily): Agent › Setup › Update (or Project › Connect › Update) then *Reload panel*/restart AE; or ask Claude in the Motion DNA folder: "Update Motion DNA from the repo. Keep any local changes of mine (stash them, don't delete them), then tell me the version."
8. **Mac video references:** install Homebrew, `brew install ffmpeg`, update plugin, restart AE; then Agent › Chat › + Image / video.
9. Existing AE MCP: Motion DNA installs side-by-side; say "use Motion DNA" to choose it; don't run both on the same comp.

## Known issues & feedback
- **Mac bug: Figma storyboard link not animating** (Leonardo Rica, 10-19) — untested on Mac (devs on PC); fixed: update, then switch Agent to *Full* mode and repaste link. Install also needed "a few terminal fixes" on Mac. https://konsus.slack.com/archives/C0CAJ42DDS8/p1792435658803289
- **Curve editor:** request to snap points to 45° with Shift (Fariel, 10-19). Generated Intuit ProPartner cut from storyboard + reference + guidelines in ~6k tokens. https://konsus.slack.com/archives/C0CAJ42DDS8/p1792445019307549
- **Video references** work "pretty decently" in Claude (storyboard + style video → editable AE layers). https://konsus.slack.com/archives/C0CAJ42DDS8/p1792784088997749
- **Panel window stuck / can't dock or resize** (Gabriel Perdomo, Mac, and Gian on PC, 10-28) — fix pushed; update plugin. https://konsus.slack.com/archives/C0CAJ42DDS8/p1793223001364949
- **Figma MCP `InvalidHTTPResponse` on Windows with Avast** (Cristina Corat, 10-29) — Avast Web Shield HTTPS scanning; temporarily disable, run `claude mcp login "plugin:figma:figma"`, re-enable, add exception for mcp.figma.com or claude.exe. Axel Torres raised a security-compliance concern about disabling HTTPS scanning; recommended fix is an IT-set targeted exception. Aaron plans an in-app warning when a third-party security tool blocks connections. https://konsus.slack.com/archives/C0CAJ42DDS8/p1793307033755239
- **"Motion DNA down / can't connect to Claude or Codex"** (Fariel, 11-03) — cause: installation folder had been moved; don't move the repo folder (panel reads the library from it). https://konsus.slack.com/archives/C0CAJ42DDS8/p1793716734302629
- **Tutorial UI drift:** UI differs from first-release tutorials. https://konsus.slack.com/archives/C0CAJ42DDS8/p1793202767722679
- **Open questions:** how brand info/motion guidelines (potentially sensitive) are stored/shared; no company guidance on centralising similar efforts (Motion Maxxing etc.). https://konsus.slack.com/archives/C0CAJ42DDS8/p1793717289778209
