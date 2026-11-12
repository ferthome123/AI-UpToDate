# #everyone-can-build — digest

- **Channel:** #everyone-can-build (`C0BDGFE5QTE`), https://konsus.slack.com/archives/C0BDGFE5QTE
- **Purpose (channel description):** a place to share what you've built with Claude: custom skills, vibe-coded tools, artifacts, workflows. Renamed from `share-your-skill` on 2026-06-26.
- **Date range read:** 2026-06-26 to 2026-11-12 (entire history)
- **Newest message ts read:** `1794488120.574699` (top-level, 2026-11-12 09:55 -03, Anush Babayan). Newest thread reply seen: 2026-11-12 09:58 -03 in the Buzz thread (`1794408256.274509`).
- **Incremental sync:** call `slack_read_channel` with `oldest=1794488120.574699`, then re-check threads of recent posts.
- **Coverage notes:** about 900 bulk join messages on 2026-06-26 and 2026-06-29 were skipped. Two short windows inside the 2026-06-29 05:47–05:51 bulk add were assumed to be joins only. Threads were read for every tool or skill announcement that had replies; a few small chit-chat or question threads were skipped. Attachments (.skill, .zip, .mp4, .pdf) were not opened, so only their file names are recorded.
- **Items:** 111 (see `data/slack-everyone-can-build.json`)

## Items (newest first)

### Figma design to client deck (EXT file builder) (2026-11-12): skill, beta
Takes a Superspace project + Figma frames and builds a correctly named customer-facing Figma file (EXT_<Project Number>_<Account>_<Project>) with cover, filled-in brief, per-option rationale, updated header/footer and placed PNGs. **How:** In Cowork say 'make EXT file' or 'customer-facing deck'; paste Superspace link + Figma frames link; give draft number (defaults to Draft 1); afterwards right-click Cover > Set as thumbnail manually. Review rationale/stats before sending.
- Owners: Anush Babayan
- Install (plugin): https://claude.ai/customize/skills/id/plugin_01M2jYCmYgxbUmaPerLwfJ9p
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1794488120574699

### Figma Buzz template prep (2026-11-11): skill, wip
Prepares Figma Design frames to become Figma Buzz templates: fixes Auto Layout/images/layer names, builds template sets, adds on/off toggles, locks non-editable elements, and creates an Excel bulk-create sheet with a guide tab. Works on a copy ('Buzz prep' page). Also useful for any component-based template you want to bulk-create. **How:** Add plugin, share a Figma link with Claude and ask it to prepare the frames for Buzz.
- Owners: Titi Palumbo · Updated: 2026-11-12
- Install (plugin): https://claude.ai/customize/plugins/plugin_01C22kpjdahEtXQW7EAaJtkn
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1794408256274509

### AM account growth-opportunities dashboard (2026-11-06): dashboard, shipped
Live artifact that loads the accounts assigned to the viewer and shows balance/expirations/usage vs plan and boosters, growth opportunities (upsell, cross-sell, client signals) and account details with pitch ideas. **How:** Open the artifact; connect Superside, Gmail, Calendar, Drive, Slack (and BigQuery) connectors. Built in the Team workspace: won't open if you're logged into the Enterprise account.
- Owners: Alejandra Dulce · Updated: 2026-11-06
- Artifact: https://claude.ai/artifact/Xj4RHREkHMeSLcwDLQgM13
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1793989320303269

### artifact-registry (personal Artifact Finder) (2026-11-06): skill, beta
Builds a private Notion database of every artifact you built or that was shared with you, classifies them (live/static, purpose, scope, visibility, status) and publishes a private searchable Artifact Finder; optional weekday sync. Known issue: initially only available in Enterprise workspace (not Team); updated to keep one registry across workspaces. Users asked for team/company-wide registries. **How:** Add skill, then say 'set up my artifact registry'. Needs Notion connector. Each person runs their own private copy.
- Owners: Andreas Drakos · Updated: 2026-11-07
- Install (skill): https://claude.ai/customize/skills/id/plugin_01DAiuD4q6HGZFjXzNwVByBM
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1793971682790579

### Figma to InDesign (CMYK) converter (2026-11-05): skill, beta
Converts a Figma report/deck/one-pager into a native editable InDesign IDML with brand CMYK swatches, template paragraph styles, precise text frames, organized Links folder, read-me and a visual QA dashboard comparing the exported PDF against Figma. Built in response to Adelle Adrian's ask (Figma report -> print-ready INDD). Known issue: org link not accessible from other team workspaces; .skill file shared in thread instead. **How:** Install; provide Figma link + pages, brand guide (CMYK values/fonts) and client InDesign template if any. Export PDF from InDesign for the QA loop.
- Owners: Marcelo Pelica · Updated: 2026-11-09
- Install (skill): https://claude.ai/customize/skills/id/plugin_01FGqFtZszFmKicYhGuskXLf
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1793911210850819

### Loopy Labs (motion loop templates in Figma) (2026-11-02): workflow, beta
Library of ready-to-animate loop templates powered by Claude Skills that turns a static design into an on-brand motion ad inside Figma; loops stay editable. **How:** Duplicate the Figma file and start with the 'Step by step: READ FIRST!!' page.
- Owners: Bianca Beltran, Quest Team
- Figma file: https://www.figma.com/design/AthoBjwtdOwSXYQ26BDjPS/EXT---LOOPY-LAB---By-Bian---Ele--Copy-?node-id=722-2692&t=40GFq7KlQxtSoSgr-1
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1793637957078739

### Fancy Board (PM/AM task board) (2026-11-02): dashboard, beta
Board for PMs and AMs to keep tasks organized and auto-update the calendar so deadlines/priorities stay clear. Works best for accounts with dedicated team members/CLs; Felicia Meyer has a skill to build your own. **How:** Request viewer access to the artifact (Felicia Meyer admits); ask Felicia for the build-your-own skill.
- Owners: Felicia Meyer, Quest Team · Updated: 2026-11-02
- Artifact: https://claude.ai/artifact/SZ1xZwht97iDbyiR2B43YU?sk=wmHx_ooGiPtlt6_3Q3NUXA
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1793637957078739

### Responsive Safe Zones Figma plugin (2026-11-02): plugin, beta
Figma plugin built from Jess Uhren's channel mockups/safe-zones file: auto-detects format/channel from frame size+name, overlays platform safe zones, checks and fixes elements outside safe areas, and drops assets into editable platform mockups. **How:** Name frames with platform + ad/organic (e.g. IG_story_ad_01). Not published: get the zip from Gabrielle, then Figma desktop > Plugins > Development > Import plugin from manifest.
- Owners: Gabrielle Moura · Updated: 2026-11-02
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1793627450213159

### Superspace Feedback Relay (2026-10-30): plugin, beta
Relays client feedback from Superspace chat into the project's internal Slack channel within the hour (tagging only who needs to act) and posts a daily cross-timezone handoff (decisions, next steps, feedback, promises from meetings). Nothing posts without approval. **How:** Add plugin; open Code tab in Claude desktop; say 'set up the Superspace feedback relay for account <ID>'. Needs Superspace, Slack, Google Drive connected and Gemini notes/transcripts on in meetings.
- Owners: Rodrigo Salazar
- Install (plugin): https://claude.ai/customize/plugins/id/plugin_01NeAV449hjyGLcA94CRx4to
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1793392818283839

### SuperDash / am-morning-dashboard (2026-10-29): dashboard, shipped
Single role-based dashboard (PM/Producer or CL/CD) showing budgets, projects, deadlines and what's being quoted, built with Claude Code for the Booking.com team and PEAK AMs; packaged later as the am-morning-dashboard skill. **How:** Open the Dash and pick your role top-right; or install am-morning-dashboard.skill from Claude's skills settings and follow the guide.
- Owners: Leeroy Duke · Updated: 2026-11-09
- Dashboard: https://claude.ai/artifact/T42p8UpFXRZVSctzJTD7YQ?sk=pbFeBda_vUqqFNkttSm5pA
- How-to guide: https://claude.ai/artifact/C2wEX3RkV2hzmZSd3gGxxT?sk=yPFT6XwyTddcbqoeiNkvEg
- Video: https://claude.ai/artifact/E5eEudnzW3f2wZqptUSBx4?sk=kyWcM_eI658Rw1EpArVdfg
- Skill update post: https://konsus.slack.com/archives/C0BDGFE5QTE/p1794211691065479
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1793288953550979

### Tip: use Claude to search Notion/Slack/Superspace/Salesforce for 'how do I do X' (2026-10-23): guide, shipped
Prompt pattern to have Claude search internal knowledge bases (much better than Slack search) for already-solved problems. **How:** Prompt: 'Can you search Notion, Slack, Superspace, and Salesforce to see if we have documentation on <topic X>? Specifically, I need to know how to <objective>.' (Slack connector is Enterprise-only, not Team plan.)
- Owners: Bernard Moussa
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1792761543515899

### #Theres-A-Skill-For-That pack (account & project skills) (2026-10-22): plugin, shipped
Benitta's collection of AM/PM skills: /account-onboarding, /account-opportunity-finder, /client-behaviour-analysis, /account-cost-dispute-pack, /next-step-generator, /adhoc-project-plan-drafter, /product-design-qc, /branding-design-qc, /scoop-scheduler, /scoop-pto. Nov update baked in Expansion 2.0, AI Strategy, margins, Legal & AI and Creative Tech Hub rules. **How:** Grab .skill files from the Drive folder/deck; in Cowork Settings > Capabilities > Skills > Upload; enable listed connectors; run /skill-name. Ask Claude to 'Update and save the skill so it always follows this process for me'.
- Owners: Benitta Van Den Berg (Gerber) · Updated: 2026-11-04
- Halloween deck: https://docs.google.com/presentation/d/1JCjDoLHP710kJRCXHl54RX9nI9Cu4t5elq3XJjxH2dk/edit?usp=sharing
- Skill files folder: https://drive.google.com/drive/folders/1HiHSdHqQGDADyCDrsxpmx9efJFMQXMOV?usp=drive_link
- Nov update post: https://konsus.slack.com/archives/C0BDGFE5QTE/p1793784422559819
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1792672354410769

### Superside marketing creative automations (headshots, SEO blog headers, event asset studio) (2026-10-22): workflow, shipped
Marketing creative team automations: Figma brand model for branded headshots (88% less time), a Claude skill connected to Krea that ideates and generates SEO blog headers and resizes them (72% less), and a Claude-built Connect & Dinners event asset studio app for self-serve assets (95% less). **How:** Contact Iliada Karamintziou / Manuel Bueno / Andrea Paz y Miño. Flora support for the headers skill was being added.
- Owners: Iliada Karamintziou, Manuel Bueno, Andrea Paz y Miño · Updated: 2026-10-23
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1792659697122939

### brand-intake (brand guideline analysis + shared brand library) (2026-10-20): plugin, shipped
Claude Code plugin that turns a zip/PDF/brand site/Figma link into a client folder with BRAND_RULES.md (logo, HEX/RGB/CMYK/PMS, type, voice, pre-flight checklist), sorted assets, file inventory, gaps list with client questions and flagged guesses. Updated into a shared library so brands only need processing once. **How:** /plugin install brand-intake@claudeai-organization-library then run /brand-intake. Library artifact requires being in the Team workspace.
- Owners: Karolline Luna · Updated: 2026-10-21
- Shared brand library: https://claude.ai/artifact/NCnuTHnv49tAYXnT3LEsNZ?sk=nBfnYFWiTjWLTdlI3dUung
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1792516214338069

### Motion DNA (After Effects plugin via MCP) (2026-10-20): plugin, beta
After Effects plugin connected to Claude via MCP: motion libraries, predefined animation behaviours, brand motion profiles, Figma storyboard import animated in the AE timeline, and agent help (sound, brand alignment, color correction, transitions). Hybrid approach recommended. **How:** DM Gian Orsi to join the beta (~20 testers).
- Owners: Aaron Amortegui, Gian Orsi
- Original post (#C04CC8FSDHP): https://konsus.slack.com/archives/C04CC8FSDHP/p1792421092535119?thread_ts=1792421092.535119&cid=C04CC8FSDHP
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1792502855645609

### Word to IDML template (2026-10-19): skill, shipped
Fills an InDesign IDML template from a Word document. **How:** Install skill, upload IDML template + Word doc. Word must have styles applied first.
- Owners: Anita Duhart
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1792419133227699

### Project Management Hub (2026-10-12): dashboard, shipped
Live Superspace-data artifact for PMs: Project Burn (estimated vs logged vs booked hours), Daily Bookings with PTO/capacity warnings, and Team Calendar of creatives' weekly bookings. **How:** Open in claude.ai or desktop with Superside account and allow the Superside connector; if 'Live data unavailable', reload/allow or check Permissions. Slow first load.
- Owners: Leticia Melo
- Artifact: https://claude.ai/artifact/V55hpxU6gPLruUBuex9Wov?sk=Ggw0z1eH-Na4h1OLMuTwRw
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1791822759873919

### Market & Growth Tracker artifact (2026-10-09): artifact, shipped
Artifact cross-referencing market signals, client priorities (from MSS/QBR/weekly calls), recent feedback and a proposals/opportunities brainstorm board per account. **How:** Paste the attached prompt template PDF ('How to build your own Market & Growth Tracker') into Claude.
- Owners: Fernanda Amadio
- Artifact: https://claude.ai/artifact/Dm9KHVjG152r4fqpDipjhq?sk=n33sUIqfZ4JNejolPBZs2g
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1791574077187519

### Print preflight check (2026-10-02): skill, shipped
Preflight for print files: bleed, resolution, color mode, outlined fonts, PMS tagging, brand color match, text past trim, inconsistent panels; ships with 'For Print' and 'For Approvals' PDF export presets for Illustrator/InDesign. **How:** Install print-preflight-check.skill and run on your print files; import the PDF presets. No connectors needed.
- Owners: Luigi Di Bella
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1790969225955139

### Brand Lockup System (2026-09-18): skill, shipped
Turns one hand-made lockup into a full Figma library of brand wordmarks/lockups (variant sets, consistent naming, publishable library) and exports SVG+PNG. Proven on Zoom: 48 layouts -> 900+ components -> 1,800+ files; ~40h saved per project. **How:** Install brand-lockup-system.skill (check file ends with .skill, an early download was truncated to .ski) and read the one-page guide; brief + 2 QC gates.
- Owners: Agostina Alvarez · Updated: 2026-09-21
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1789756178375929

### quiet-account-plan (2026-09-18): skill, beta
For accounts gone dark / with unused budget / unsubmitted drafts: reads the account's Notion and Slack history, pulls real brand colors/type/voice, finds real industry events and competitors, flags expiring budget and stalled drafts, and packages an interactive client-facing plan (no pricing). **How:** Install and point it at a quiet account.
- Owners: Anush Babayan
- Install: https://claude.ai/customize/skills/discover/plugin_017Wsm6C1MJT8PGM5oXWDr9p
- Example (IFS Nexus Black): https://claude.ai/artifact/A8zdgA5z8kPbwxSa2hhGq5?sk=b7kJXW96N0XsZVovK9GjQA
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1789732825591959

### MP4 to .lottie converter (2026-09-11): skill, beta
Converts MP4 to .lottie (reverse-engineered from a working file) without a LottieFiles subscription. **How:** Install mp4-to-lottie.skill; check result at lottiefiles.com/preview.
- Owners: Abbi Choa
- Preview tool: https://lottiefiles.com/preview
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1789121218959629

### No More Loose Ends (2026-09-04): skill, shipped
Reads Slack, Gmail and Superside chats to surface what you owe people and what people owe you (unfulfilled promises, buried client questions), checking Asana first to avoid nagging about tracked items; can DM on a schedule. **How:** Install and run for a gut check, or schedule it.
- Owners: Rodrigo Salazar
- Install: https://claude.ai/customize/skills?selectedId=skill_01LYx4bSV5SL1bjGN7mEFS7m
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1788542822454219

### MiniMax H3 local video generation experiment (2026-09-04): experiment, idea
Test of running MiniMax H3 locally (own GPU) with Claude driving it to recast a character into live-action scenes; documents segmentation vs full-recreation routes. **How:** Niche: needs a decent GPU or rented GPU. See original post in #C04CC8FSDHP.
- Owners: Aaron Amortegui
- Original post: https://konsus.slack.com/archives/C04CC8FSDHP/p1788541722052449
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1788541957969899

### /daily-planning (Creative Starter Pack) (2026-09-03): skill, shipped
Daily view from Slack, Gmail, Asana, Superspace and Calendar: top 5 priorities (Make/Unblock/Decide), things you'd miss, per-project status, billable vs non-billable hours pace, meetings/deadlines, and action buttons. **How:** Claude > Customize > Browse > Your Organization > Plugins > Creative Starter Pack, then /daily-planning. Support: #creative-skills-support.
- Owners: Careth Colmenarez, Michal Stangret, Matteo Rostagno
- AI Briefly demo: https://superside.sana.ai/s/ynT9U4VWJRZv
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1788442441569609

### Budget & Project Tracker + Client Renewal Calendar/Tracker (2026-09-01): artifact, shipped
AM artifacts: account budget control (consumption pace, overage/expiring-credit flags), project health vs Best/High estimates with PM, deadline and feedback ratings; client renewal calendar mapping renewal stages against MSS/QBR and relationship tracker from Notion AKPs; Oct update added a renewal stage checklist tab with auto-dated stages and progress bars. **How:** Use the Google Docs / .md instructions to have Claude build your own; configured in Portuguese for Fernanda's accounts, so change accounts/language.
- Owners: Fernanda Amadio · Updated: 2026-10-02
- Budget & Project Tracker artifact: https://claude.ai/code/artifact/a047eb32-df9b-4513-a0eb-c799e816bf3c
- Build guide (tracker): https://docs.google.com/document/d/182xc3a-1nOT35eannjctsJ56X5v4bonPufI3xRtx9tc/edit?usp=sharing
- Build guide (renewal calendar): https://docs.google.com/document/d/1piYYMKIg10XMrayPGoijKR8o4351T8uQ9DyaH10TAEA/edit?usp=sharing
- Updated tracker with renewal tab: https://claude.ai/artifact/LnwsS8cP5B7t1V842xfFzT?sk=MnQnkcKdHlDDV9C2gI86mg
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1788276865923639

### Claude credit-savvy tips (2026-09-01): guide, shipped
Tips to save Claude credits: use Sonnet 5 (Med) not Opus, run scheduled tasks on Sonnet and pause unused ones, download Omni CSVs instead of crawling, enable Memory, check plugins/#everyone-can-build before building, monthly housekeeping of tasks/artifacts. Thread: change connector permissions via Customize > Connectors > app to reduce prompts (caution on delete/move). **How:** Read the post; links to Plugins knowledge hub and Hackathon directory.
- Owners: Tamara Dalhuijsen · Updated: 2026-09-02
- Plugins knowledge hub: https://app.notion.com/p/Superside-Claude-Plugins-knowledge-hub-38950ebbbec080cda536eb9cff4776a0
- Hackathon directory: https://app.notion.com/p/Hackathon-Everyone-can-build-39f50ebbbec08010ad3cc841b46f575b
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1788274282629779

### Account Management plugin (8 skills) (2026-09-01): plugin, shipped
Official AM plugin: Morning Radar, Account Command Center, Account Meeting Prep, Account News Hub, Account Growth Radar, Client Account Overview, project-cost-overrun, am-team-close-reminder; designed to stack (e.g. radar -> command-center; cost-overrun -> close-reminder -> client-overview). **How:** Claude > Customize > Plugins > Browse > add Account Management; connect Calendar, Slack, superside-mcp-internal, Omni, Notion. Issues -> #support-claude. Training sessions Sep 2026 (rescheduled due to town hall).
- Owners: Tamara Dalhuijsen · Updated: 2026-09-09
- Plugins knowledge hub: https://app.notion.com/p/Superside-Claude-Plugins-knowledge-hub-38950ebbbec080cda536eb9cff4776a0%7CSuperside
- AM Plugin kick-off recording: https://drive.google.com/file/d/1BVXL17ck6eHjwwjlwDY63laHGjUgbdKr/view?usp=sharing
- Kick-off transcript/notes: https://docs.google.com/document/d/1cwTHWsLHZkzxxUJbiUDWWjUja-aQp16grd1b_13LwbE/edit?usp=sharing
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1788272178211309

### Reference Collector (macOS app) (2026-08-27): tool, beta
Local Pinterest-like macOS app for saving visual references via drag/paste/URL/menu-bar capture, auto-tagging, color palettes and search; on-device analysis with optional LM Studio/ChatGPT/Claude. **How:** Ask Craig Wright for a build.
- Owners: Craig Wright · Updated: 2026-09-17
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1787820745873159

### Krea design agent (unlimited access) (2026-08-25): tool, shipped
Superside has unlimited access to Krea's design agent in the Krea web app; teams asked to run real work through it and share feedback. **How:** Go to krea.ai/agent. Unclear whether 'unlimited' covers expensive video models like Seedance.
- Owners: Manuel Berbin
- Krea agent: https://www.krea.ai/agent
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1787673994000259

### Claude hackathon winners (Sky Unit highlights) (2026-08-17): announcement, shipped
Hackathon highlights: Team Cloud's next-project recommender (with receptiveness check), sKILL BILL (project memory/context), The Performance LOOP, Sonnet Syndicate (Krea+Claude), ShantAI You Stay (generated brand photography), Macy's Darlings. 90+ submissions overall. **How:** Browse decks and the hackathon Notion database.
- Owners: Kae Neskovic
- Team Cloud deck: https://docs.google.com/presentation/d/17RRjCRxGO4w3IIDV_afP5nVfT8idgT0chnNl1t7plKo/edit?usp=sharing
- sKILL BILL deck: https://docs.google.com/presentation/d/1tv7XlbD-GHAfgWG-7P1ypVUEweoAAXymhAxZaGH0bI4/edit?usp=sharing
- Performance LOOP deck: https://docs.google.com/presentation/d/113x1Q6526ki8ctuflGGb83OsGiwYkFi7jSoppVo75cE/edit?usp=sharing
- Sonnet Syndicate deck: https://docs.google.com/presentation/d/1SWebNflf0A_1YNFjt_gnzojjwTI08HCZhIzIjr1meT0/edit?usp=sharing
- ShantAI You Stay deck: https://docs.google.com/presentation/d/1puxAAWtYz5SERrXjDyleOVr0GvRZ1yx7YAvOSu2Z_Sc/edit?slide=id.g3f96c9a1b7c_0_14#slide=id.g3f96c9a1b7c_0_14
- Macy's Darlings deck: https://docs.google.com/presentation/d/1Vsmor-zL1qvXSlj6cMbxWJWNbew9taJiyfhU7RXj9vQ/edit?usp=sharing
- All hackathon entries: https://app.notion.com/p/39f50ebbbec080e1893af17717e8a96c?v=39f50ebbbec08053ba5c000ce4a97792
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1786982743813429

### Custom GPT to Claude migration skill (2026-08-13): skill, shipped
Walks you step by step through rebuilding custom GPTs in Claude. Thread: Superside ChatGPT account expires early October 2026; Krea plugin suggested for image gen; accounts with Claude restrictions (e.g. Reddit) still use ChatGPT, BrandBrain MCP is exposed to GPT. **How:** Install custom-gpt-migration.md as a skill and follow the steps.
- Owners: Tamara Dalhuijsen · Updated: 2026-08-24
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1786631054009759

### milestone-calendar-sync (Asana CR/IR deadlines to Google Calendar) (2026-08-12): skill, shipped
Pulls CR/IR and review-type milestones from your own Asana tasks into your Google Calendar, color-coded per client with 1h reminders; checks Superside staffing first to avoid syncing projects you're not on; can run daily. **How:** Download .skill, Save skill, ask 'add my Asana CR/IR deadlines to my calendar'. False-positive milestones bug fixed in thread (use updated file).
- Owners: Taryn Selvan · Updated: 2026-08-13
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1786542063871619

### PM PTO handover (Notion) (2026-08-12): skill, shipped
Builds a live, shareable Notion page with a filterable database of all your projects with key info from Superside, Slack and Asana for PTO coverage. Caution: refreshing can overwrite manual edits. **How:** Install pm-pto-handover.skill, say 'I'm going on PTO, build me a handover in Notion.'
- Owners: Nicolas Gattoni
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1786539424498399

### Creative plugins suite (Starter Pack, Quality Delivery, Video & Motion, Presentations, Digital Assets, Superside Internal) (2026-08-11): plugin, shipped
Org plugins: Creative Starter Pack (/skill-gallery, /logging-time, /creative-kick-off, /daily-planning), Creative Quality Delivery (/brand-voice-check, /text-check, /exact-copy-check, /platform-character-check, /write-like-a-human), Video & Motion (/performance-ad-storyboard, /storyboard-to-weavy, /video-prompt-director, /visual-style-guide), Presentations (/figma-to-pptx, /gif-for-slides), Digital Assets (/flora-icon-generator, /image-style-dna-decoder), Superside Internal (/superside-brand-copy, /superside-brand-system). **How:** Claude > Customize > Browse > Your Organization > Plugins. Feedback: #creative-skills-support.
- Owners: Matteo Rostagno · Updated: 2026-11-04
- Creative Starter Pack: https://claude.ai/directory/plugins/creative-starter-pack%40Superside%2Finternal-claude-plugins
- Creative Quality Delivery: https://claude.ai/directory/plugins/creative-quality-delivery%40Superside%2Finternal-claude-plugins
- Video & Motion: https://claude.ai/directory/plugins/video-motion%40Superside%2Finternal-claude-plugins
- Presentations: https://claude.ai/directory/plugins/presentations%40Superside%2Finternal-claude-plugins
- Digital Assets: https://claude.ai/directory/plugins/digital-assets%40Superside%2Finternal-claude-plugins
- Superside Internal: https://claude.ai/directory/plugins/superside-internal%40Superside%2Finternal-claude-plugins
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1786462556818209

### brief-debrief (2026-08-11): skill, shipped
Translates a Superside project brief into plain language: what the brand does, what's asked, web-researched terms/acronyms, past project history, Slack context, inconsistencies, all links, questions to ask, and the account AI policy (red alert if AI opt-out). Outputs a branded digest artifact in the user's language; can also process your DRAFT/PREPARE queue. **How:** Install brief-debrief.skill; ask e.g. 'what is this client asking for' with a project ID/link/brief text, or 'what projects do I have to review?' (EN/PT/ES).
- Owners: Flavio Treiger
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1786462454358529

### FlowDesk staffing co-pilot (2026-08-11): artifact, shipped
Hackathon-winning staffing co-pilot; HTML + handover file to rebuild in Claude Cowork. **How:** Download from the Drive folder and build in Cowork.
- Owners: Flavio Treiger, Lucas Matsumura, Gabriel Deda, Esteban Mora, Ryan Macatulad, Lindsay Romano, Anneke King
- Drive folder: https://drive.google.com/drive/folders/1-L_0IvzcBRM1Mq2a9tzbJeHUosluVkSi?usp=drive_link
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1786460674569999

### Supertracker (Everything Everywhere All At Once hub) (2026-08-11): artifact, shipped
Cowork shared artifact hub aggregating Slack, Asana and Google Calendar. **How:** Open the shared artifact in Cowork with Slack, Asana and Calendar connected.
- Owners: Bianca Takahashi
- Cowork artifact: claude://cowork/shared-artifact?uuid=019fa5e1-4273-76bb-9bb0-5adf28d49bfa
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1786459914901949

### /next-project-recommender (2026-08-11): skill, shipped
Hackathon-winning (Team Cloud) recommender that reads account usage, news, calls and Brand Brain and returns next-project ideas written as GTBs, with a receptiveness check that stops if the account is swamped. **How:** Install from link; feedback welcome.
- Owners: Rodrigo Salazar, Tilbe Cakar, Carmen Zita, Daniela Riveros, Vivianna Ramirez, Rodrigo Cruz, Vitor Borragine
- Install: https://claude.ai/customize/skills?selectedId=skill_012k99ZzSuF15mMzp6wGDjrk
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1786459359476109

### client-onboarding-plan (2026-08-10): skill, shipped
Pulls new-client intel from Salesforce, Jiminny and Slack into a Word onboarding plan (account/customer info, next steps, WoW details from sales); leaves onboarding dates as '[AM to add date]'. Laura Santos built an AM onboarding journey checklist artifact on top. **How:** Install client-onboarding-plan.skill.
- Owners: Olivia Tornelli · Updated: 2026-09-15
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1786382512543039

### GIF optimizer artifact (2026-08-10): artifact, shipped
Cowork artifact to shrink huge AI-generated GIFs; pixel-dropping dimension bug fixed. **How:** Find it under Artifacts in Claude (shared Cowork link). Alternative noted: Gifski CLI.
- Owners: Craig Wright · Updated: 2026-08-11
- Cowork artifact: claude://cowork/shared-artifact?uuid=019feb7f-ad3f-739a-82fa-5de3a27c8ea7
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1786362960344309

### creative-qc-check (2026-08-06): skill, shipped
Creative QC from a job number: technical handoff (missing/duplicate assets, drafts, layer names, broken refs, zips), brief compliance, copy (grammar + verbatim vs client copy), brand check against guidelines; drafts a Slack reply. Overlaps with the official Creative Quality Delivery plugin (Matteo aligning). **How:** Install (directory or file) and ask 'QC 260471' or 'QC this project'.
- Owners: Bruna Correia Gonzalez · Updated: 2026-11-04
- Install: https://claude.ai/customize/skills?selectedId=skill_01BMozatmtZSD4j2o3fHkUz4
- Loom: https://www.loom.com/share/3c240f7cb97e48c9824c9da439b02d4d
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1786007714458719

### PM plugin sandbox account + Plugged In training (2026-08-03): guide, shipped
All PMs/Producers added to internal account 104597 (INTERNAL 4.3 ANNUAL) as a safe space to test the Project Management plugin; Plugged In sessions (Claude Basics, Meet the Skills, Full PM Lifecycle) with recordings. **How:** Claude > Customize > Plugins > Browse > Project Management plugin > Add. Watch recordings. Omni data available via superside-mcp-internal.
- Owners: Tamara Dalhuijsen, Indre Lukauskaite · Updated: 2026-08-25
- Sandbox account 104597: https://internal.superside.com/accounts/104597
- Session 1 recording: https://drive.google.com/file/d/1_VeE7F2Mn32ZmF2rWQo9Le6_-zchD6lY/view?usp=sharing
- Session 2 recording: https://drive.google.com/file/d/1XFrPt3e657geVSmdAlJP5IzZ5kyNuuyF/view?usp=sharing
- Session 3 recording: https://drive.google.com/file/d/1d75Rm0IcihLYrlrTP854huJwMZtgmqZ6/view?usp=sharing
- Plugged In sign-up form: https://docs.google.com/forms/d/e/1FAIpQLSfICukrrLdVVK74OwXdLLZlbsWQ79Kc7JhBdGe2B_e2SoiKFw/viewform?usp=dialog
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1787228706147919

### BrandBrainMCP (in Superside Internal MCP) (2026-08-03): mcp, shipped
Brief generation powered by BrandBrain and a BrandBrain query tool (account knowledge now; previous projects/assets later). **How:** See Notion 'Using BrandBrain MCP as Staff'. Bugs/feedback: #product-team-brand-brain.
- Owners: Alexandre Jacinto, Bogdan Sbiera
- How to use: https://app.notion.com/p/Using-BrandBrain-MCP-as-Staff-3b150ebbbec08015b478f25351d8cf97
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1785774262379949

### Superside x Claude Wrapped (2026-08-03): artifact, shipped
Spotify-Wrapped-style artifact summarizing your July Claude usage (enterprise org accounts only). **How:** Open the Cowork shared artifact.
- Owners: Louis Svugr
- Cowork artifact: claude://cowork/shared-artifact?uuid=019fbdcc-bd0a-70e6-b187-cf89dbf6feb4
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1785740611723189

### project-hours-health (2026-07-31): skill, shipped
Scheduled Slack DM for PMs/Producers: for each ONGOING project, bars of PM&CL, Creative and total hours vs Best Estimate, deadline/days left, red flags when over, sorted by burn rate. **How:** Get the skill (link or .md), ask Claude to set it up with time/timezone/days.
- Owners: Gabriela Maragni · Updated: 2026-08-04
- Install: https://claude.ai/customize/skills?selectedId=skill_01Fky4LHhiXb7eAaojTuxSN6
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1785522377575129

### clari-renewal-notes (2026-07-31): skill, shipped
Every Friday drafts Clari renewal notes (Inspection summary + Forecast by quarter, plus opt-out accounts) from Salesforce, Notion, Jiminny and Slack; defaults to flat renewal unless evidence. **How:** Install clari-renewal-notes.skill and schedule Friday mornings.
- Owners: Olivia Tornelli
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1785515849657849

### cl-weekly-account-news (2026-07-31): skill, shipped
Weekly Monday DM for CLs combining client company + industry news (with sources) and an internal Superside snapshot (projects, deadlines, sentiment); urgent summary on top, detail in thread. **How:** Install and set your account list.
- Owners: Anita Duhart
- Install: https://claude.ai/customize/skills?selectedId=skill_01EbiYDxRKEez1Kv5uBjhP1X
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1785511826112249

### Feedback & Timeline Untangler (2026-07-30): skill, shipped
Untangles confusing customer feedback by researching full history across Slack, Superspace and support/account channels: real timeline of promised vs delivered, next steps, whether it was answered; also feedback-timeline audit and billing/duration explainer. Nov update: billing rules built in. **How:** Install .skill; needs Superside internal gateway MCP + Slack. Tweak by telling Claude your role and 'Update and save the skill'.
- Owners: Benitta Van Den Berg (Gerber) · Updated: 2026-11-04
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1785417294948829

### Task Buddy (2026-07-29): artifact, shipped
Neurodivergent-friendly daily assistant for creatives (hackathon) that reads Slack, Asana, Superspace, Gmail and Calendar and answers 'what needs me, where to start, what can wait'; builds a profile of your people/accounts/rhythm on first load. **How:** Open the Cowork shared artifact; first load takes a few minutes. Updates posted in #tribe-neurodivergence.
- Owners: Paola Flores, Caro Verawilcke · Updated: 2026-08-11
- Cowork artifact: claude://cowork/shared-artifact?uuid=019fab41-4293-72f3-bf8f-4172a4b6f058
- Hackathon post: https://konsus.slack.com/archives/C0BHZM4M6NT/p1785215099893409?thread_ts=1785215099.893409&cid=C0BHZM4M6NT
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1786459571394019

### Connector Checker (2026-07-28): skill, shipped
Health check of every connected tool in Cowork (Slack, Notion, Drive, Gmail, Calendar, Asana, Figma, Canva, Omni...) plus your scheduled tasks; drops results into a Cowork page with reconnect links. **How:** Install and schedule weekday mornings. No connectors needed.
- Owners: Benitta Van Den Berg (Gerber)
- Original post in #support-claude: https://konsus.slack.com/archives/C0BD5A5V3KK/p1785253891640309?thread_ts=1785249033.571049&cid=C0BD5A5V3KK
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1785253939077699

### Render Inspection (AI image QC) (2026-07-28): tool, beta
Web app that flags AI-image defects (warped hands/feet, plastic skin, hair, physics-defying clothing, non-photoreal look) with on-image markers and severity; checklist to fix. Built with Claude, FAL.AI, GitHub, Vercel; reworked for accuracy. **How:** Test at the Vercel link (free tier may cap usage).
- Owners: Craig Wright · Updated: 2026-07-29
- App: https://qc-assistant-five.vercel.app
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1785236367438969

### external-weekly-status (2026-07-27): skill, shipped
Client-facing weekly status: pulls credits consumed/total/remaining/expiring boosters from Superspace, cross-checks the account Slack channel, fixed template (credit consumption + key project updates), two approvals before sending. **How:** Install external-weekly-status.skill.
- Owners: Fernanda Amadio
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1785200823020399

### weekly-billable-checkin (2026-07-27): skill, shipped
Scheduled DM with week/MTD logged hours vs day target, PTO-adjusted, billable vs non-billable shortfall, Budget Watch (75%+ of your allocation; for PM/AM/GAD the whole project budget). Note: AI-off accounts are invisible to Claude, so totals may differ. **How:** Enable skill; first run asks day target and utilization target; set day/time.
- Owners: Rute Sofia Gomes · Updated: 2026-07-29
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1785155996610029

### Scoop Catch Up (2026-07-24): skill, shipped
Account catch-up variant of The Scoop for anyone (leadership, PTO handover, jumping in cold): researches Superspace/Slack/Notion/Drive/web and returns one locked HTML newspaper, never published. **How:** Upload scoop-catchup.skill in Cowork; prompt 'Run a scoop catchup for [Account], covering [date range]'. Needs Cowork (code execution).
- Owners: Benitta Van Den Berg (Gerber) · Updated: 2026-11-04
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784886685636439

### Billable utilization calculator (2026-07-23): artifact, shipped
HTML calculator breaking hours into project/account billable/account non-billable/admin and adjusting targets for PTO, sick leave and AI bootcamp days; builds on Axel Trujillo's original. **How:** Open the attached HTML.
- Owners: Mariana Caro, Axel Trujillo
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784822967072029

### superside-log-hours scheduled task (2026-07-23): automation, shipped
Cowork task that estimates daily worked hours from Google Calendar and Slack activity (project-ID channels, account channels), shows a justification table and logs to Superside only after approval. **How:** Copy the template doc, replace name/email, create an on-demand scheduled task in Cowork; needs Slack, Calendar, Superside connectors (Asana/Omni optional).
- Owners: Flavio Treiger
- Template: https://docs.google.com/document/d/1OuNOzw1AOAxD_JlCIFUr3wysLPI7shKeU60-SO82u5Y/edit?usp=sharing
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784816066564029

### PM plugin quoting skill (/quote-project) - user feedback (2026-07-23): announcement, shipped
Call for feedback on the quoting skill ahead of sunsetting the quote calculator. Users: accurate on well-defined work (PDFs, presentations), saves time, auto-creates components/plan/Asana; misses components on complex work, under-quotes slide counts, off for Figma Buzz; can't quote without a Superspace project+brief (open ask). **How:** Use /quote-project in PM plugin; double-check vs calculator.
- Owners: Louis Svugr · Updated: 2026-07-23
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784810328832889

### Honter (client review platform, side project) (2026-07-22): tool, shipped
Personal side project: client review/feedback tool (Markup + Asana) showing work in native format (decks, sites, social mockups), pinned feedback, six AI reviewer lenses, Iris dashboard assistant, Figma plugin. **How:** honter.io; DM Axel for a free Pro account.
- Owners: Axel Trujillo
- Site: http://honter.io
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784767941611119

### Reminder: $1000 credits valid only in Cowork and Code (2026-07-22): guide, shipped
Each account had $1000 credits valid only in Cowork and Code (until September); Chat costs real credits, so use Cowork. **How:** Chat in Cowork; Sana module and Bianca Pieterse's Cowork session.
- Owners: Aki Friedrich
- Sana module: https://superside.sana.ai/s/CK6LYT2APkKg
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784750435545729

### /start copy (copywriter pre-flight readiness) (2026-07-22): skill, shipped
Copywriter pre-flight: gathers project context from Superside, deadlines/deliverables from Asana (filtered to copy work), TOV/brand guidelines from Superspace/Drive/Slack; builds a live HTML artifact for follow-ups, uploads to Drive and DMs a readiness record. Doesn't write copy. **How:** Select /start copy and paste job number + project name.
- Owners: Ashleigh Robyn
- Install: https://claude.ai/customize/skills?selectedId=skill_01TBrZkuqUgPyt643a7PFyRy
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784725309278339

### Account Notion Sync / account-knowledge-sync (2026-07-21): skill, shipped
Reads an account's Slack channel, files durable info (stakeholders, brand guardrails, strategy, wins, risks) into the account's Notion page and DMs a weekly digest. v2.0 (Andreea Gheorghe) also checks Google Meet call recordings, tags CL/SP/AM in Slack with the Notion link, runs weekly. **How:** Install, edit the 'Account registry' rows (Slack channel + Notion page). v2: in Cowork say 'Run /account-knowledge skill every Monday, 9AM UTC for Accounts A, B, C'. Caution raised about confidential info reaching Brand Brain via Notion.
- Owners: Alexa Rosenbrock, Andreea Gheorghe · Updated: 2026-08-12
- v2.0 post: https://konsus.slack.com/archives/C0BDGFE5QTE/p1786566459372269
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784656421125659

### Video prompt creator (model-specific) (2026-07-21): skill, shipped
Turns a rough idea into a structured, model-ready AI video prompt (subject, shot, camera, environment, style), single or multi-shot, adapting to Kling/Veo; optional technical/negative constraints. **How:** Install video-prompt-creator-skill.md. Similar official skill: /video-prompt-director.
- Owners: Craig Wright
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784664900254489

### Creative Skills Catalogue / AI GTM registry (Notion) (2026-07-19): guide, shipped
Central Notion catalogues of shared skills: Creative Skills Catalogue (Matteo Rostagno logs channel skills as candidates by pillar) and AI GTM registry; prompted by request to collect builds from this channel. **How:** Browse the Notion pages.
- Owners: Matteo Rostagno, Andreas Drakos · Updated: 2026-07-20
- Creative Skills Catalogue: https://app.notion.com/p/Creative-Skills-Catalogue-WIP-39050ebbbec0818ca231f0abf9c3d127?source=copy_link
- AI GTM registry: https://app.notion.com/p/90c7d765e03043b8a6ec9fb66a222f53?v=a1d6d19c938a41269606eca28c275eb4
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784451992413609

### concept-to-storyboard (2026-07-17): skill, shipped
Turns a story overview + character reference into a 15-panel timestamped storyboard sheet with shot descriptions; the sheet can be fed straight into Seedance 2.0 to generate motion. **How:** Install concept-to-storyboard.skill; give story + character ref; drop result into Seedance.
- Owners: Leonardo Rica
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784299138540449

### The Scoop (biweekly account report) + companion skills (2026-07-17): skill, shipped
Biweekly account newspaper researched from Superspace, Slack, Calendar, Gmail, Notion and client socials, sentiment-aware, reviewed/signed off by PM and posted to Slack (with Schmoon easter eggs). Bundle also includes About-me/AI-writing/company file updaters, Skills library audit (monitors this channel), Daily Notion To-Do, pm-daily-account-briefing, and New Project Plan Drafter (now also grabbed-but-not-progressed projects). Leaner updates in Oct/Nov. **How:** Save the-scoop.skill; one Cowork project per account; upload TSSP.zip; prompt 'Run The Scoop for [Account], ID [ID], [start] to [end]'; then schedule.
- Owners: Benitta Van Den Berg (Gerber) · Updated: 2026-11-04
- Setup deck: https://docs.google.com/presentation/d/12YuMJk5jBRmLgh57JAZohpbR3dvDHyBOc6mg5Bs7VJk/edit?usp=sharing
- Video walkthrough: https://drive.google.com/file/d/1rvSr2nqW1wmBeOw70oVWxtmZ_yrkihOY/view?usp=sharing
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784296694273409

### Brand Audit / Branding-Audit skill (2026-07-16): skill, shipped
Collaborative 4-stage brand audit (Business & Industry, Communication, Visual Identity, strategic wrap-up) where Claude researches and cites evidence and the user locks insights per stage; outputs an HTML report in Superside look and feel (PDF-exportable). v2 adds guided steps, native-language input with English output, a dossier.md of raw research and a Code cross-check. **How:** Install; at setup give website URL and optionally brand docs (used as self-claims baseline). Lock each stage before moving on; tip: pressure-test findings in a separate chat.
- Owners: Anita Duhart · Updated: 2026-11-05
- Skill v1: https://claude.ai/customize/skills?selectedId=skill_01XqN4f9KGxDTA36tkaZMg1Z
- Skill v2 /Branding-Audit: https://claude.ai/customize/skills/id/plugin_01Uw7um3ueQ4dnbM8XcM4hNE
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784209931212239

### Claude-in-Chrome blocked for Notion/Slack/Omni/Superside: use MCP connectors (2026-07-16): announcement, shipped
Policy: Claude-in-Chrome access blocked for notion.com, slack.com, omniapp.com, superside.com (google.com removed) in favor of MCP connectors; Chrome still OK for tools without connectors (e.g. Lever; or build API-key skill). Omni access via Chrome later restored due to pickModel permission issue. Gap logged: project timeline/overview data missing from Superside MCP (Linear AGI-126). **How:** Customize > Connectors > Browse; update skills that used Chrome.
- Owners: Louis Svugr, Aki Friedrich · Updated: 2026-07-27
- Linear AGI-126: https://linear.app/superside/issue/AGI-126/request-to-add-project-timeline-data-to-superside-mcp
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784194821981809

### gif-library (2026-07-16): skill, shipped
Finds and inserts approved GIFs from a cataloged library into slides by tone/meaning/category; also callable in Claude design. Evolved into /gif-for-slides in the Presentations plugin. **How:** Enable gif-library skill; ask for a GIF or run /gif-library.
- Owners: Aaron Amortegui · Updated: 2026-07-17
- Install: https://claude.ai/customize/skills?selectedId=skill_01MKGghYubdFeYkmjuk33yB7
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784256645172469

### How Superside Speaks (TOV copy guidelines) (2026-07-16): guide, shipped
Reference doc for anything built with Superside tone of voice. **How:** Reference in skills/prompts.
- Owners: Josh Mendelsohn
- Notion: https://app.notion.com/p/How-Superside-Speaks-TOV-copy-guidelines-39250ebbbec080009e89f00219ad9f5f#39250ebbbec081bb9d42d0a83a555fd4
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784246547232819

### Superside Assistant (Salesforce Chrome extension) (2026-07-16): tool, shipped
Chrome extension sidebar in Salesforce with 11 Claude agents by context (Opportunity/Account/Contact): sales research, legal conflict check (vs live contracts sheet), call prep, CRM hygiene, RFP go/no-go, stage coaching, notes. Prompts in markdown; built with Claude Code. Roadmap: presales request formatting. **How:** Needs Salesforce access; see Notion guide and Loom.
- Owners: Pranjalya Shukla (Bunny), Andreas Drakos · Updated: 2026-07-17
- Demo: https://www.loom.com/share/cc084afb4b5c45d7a221f69bb29f62d6
- Guide: https://app.notion.com/p/Superside-Assistant-Chrome-Extension-Guide-39e50ebbbec081ecb469ecef774b86d1
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784237309736969

### OOO Account Notice (2026-07-16): skill, shipped
Drafts short OOO heads-ups to your main account channels (date, reason, ask to shift IR/CR), remembers channels and cc lists, shows draft first. Tip: draft instead of send to avoid 'Sent using Claude' label. **How:** Install, then 'personalise this skill for my accounts'; say e.g. 'I'll be OOO next Wednesday...'.
- Owners: Jon Saude · Updated: 2026-07-17
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784227098970809

### Account Growth Radar (Google Sheet project ideas) (2026-07-16): skill, shipped
On the 1st and 15th, gives 5 project ideas per account (one tab per account) from project history/gaps, Slack/Superspace chats, seasonal patterns, competitors and public activity. Answer to request for a next-project recommendation skill. **How:** Ask Cowork for 'account growth ideas' or 'project ideas for my accounts'.
- Owners: Marina Blumgrund
- Example output: https://docs.google.com/spreadsheets/d/1IHAqIJvt-cHYjyEvAOCIp64_bUXOqkNlOyZBYExUvbI/edit?usp=sharing
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784210255658879

### PM plugin & Superside MCP release notes (2026-07-15): announcement, shipped
Running updates from Louis Svugr: timeline management skill (Asana plans from brief, staffed-team assignment, timezone-aware), /quote-project currency by plan (3.x hours, 4.0 credits, 4.1+ USD), /close-project billing band, batch IDs, admin/account hour logging tool; Aug: project resources access, MCP on AI-off accounts, /project-cost-overrun for PM+AM, Omni data via Superside MCP, Co-PM assignment; connector unbundled from plugin (install Superside MCP manually). Known bugs reported: staff-utilization loggedHours=0, my-logged-hours-summary required params, my-logged-hours only CREATIVE. **How:** Install Superside MCP connector (Customize > Connectors) and PM/AM plugins; see Notion knowledge hub.
- Owners: Louis Svugr · Updated: 2026-08-11
- Superside Claude Plugins (Notion): https://app.notion.com/p/Superside-Claude-Plugins-38950ebbbec080cda536eb9cff4776a0?source=copy_link
- Aug 3 update: https://konsus.slack.com/archives/C0BDGFE5QTE/p1785742145897549
- Aug 7 update: https://konsus.slack.com/archives/C0BDGFE5QTE/p1786130362815209
- Connector unbundling notice: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784878648840079
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784113316474319

### Project status kanban board (2026-07-15): skill, shipped
Builds a self-updating kanban of your active projects from Slack project channels (+ Asana cross-check): Not Started / In Progress / Waiting for Feedback / Stale, with summaries, team, last activity; optional twice-daily routine and Sync button via Cloudflare Worker. Guilherme Paulino forked it with Gantt + weekly scheduling. **How:** Install projectstatusboard.skill; say 'build my project status board'.
- Owners: Vinay Pittampally · Updated: 2026-07-17
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784113619760619

### design-review-summary (2026-07-15): skill, shipped
Reads brief, feedback thread, milestones and Asana to produce a client-ready round update (what's in the round, feedback due in client timezone, next steps); shows draft before sending. **How:** Install design-review-summary.skill; give project ID and say a round is going out.
- Owners: David Sutherland
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784111696871879

### PM weekly account snapshot DM (2026-07-15): skill, shipped
Monday Slack DM draft for primary PMs on subscription accounts: budget usage/overage flags, project status/blockers from Superspace chats, unresolved dissatisfaction signals, 14-day customer news; optional auto-post to account channel (off by default). **How:** Install from link.
- Owners: Bradley Ford
- Install: https://claude.ai/customize/skills?selectedId=skill_01N9aLcSQcNa3NDX7FuNBqzN
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784107851514429

### account-news-engine (Scoop news engine) (2026-07-14): skill, shipped
Personality-driven news engine watching an account and competitors (launches, funding, M&A, leadership, layoffs, stock); weekly recap + real-time alerts in the account's Slack channel with sources, AKP context and a fun fact. Folded into The Scoop's 'Hot off the Press'. **How:** Add skill in Settings > Capabilities; say 'set up a news engine for my account using account-news-engine'.
- Owners: Rodrigo Salazar, Kae Neskovic
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784062901856139

### storyboard-to-nodes (2026-07-14): skill, shipped
From script/shot list/storyboard: proposes beats, asks Weavy/Krea + Kling/Seedance + aspect ratio, writes full video prompts and outputs a pasteable JSON node graph (prompts, models, image placeholders) for Weavy or Krea. **How:** Install storyboard-to-nodes.skill; no MCP needed.
- Owners: Gian Orsi
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784052013827359

### Krea MCP connector for Claude (2026-07-14): mcp, shipped
Krea MCP initially only addable via Claude Code (`claude mcp add --transport http krea-ai https://api.krea.ai/mcp`); now in the official org-wide Connector catalogue (Enterprise). **How:** Customize > Connectors > Krea.
- Owners: Louis Svugr, Karolline Luna · Updated: 2026-07-27
- Krea MCP info: https://www.krea.ai/mcp
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784048115810249

### Client Feedback Timeline -> Project Review Tracker 2.0 (2026-07-13): skill, shipped
v1: reads a project Slack channel and outputs a table of client feedback (date, who, deliverable, plain-English summary, links), optional Superspace cross-check. v2.0: living HTML dashboard per project with every IR+CR round per deliverable, durations, refresh on demand. **How:** Ask 'Show me the client feedback timeline for [project]' or 'track reviews for [project]'. Double-check against Slack.
- Owners: Gabriela Maragni · Updated: 2026-07-15
- v2 Loom: https://www.loom.com/share/97fc524b9075446794c8969a9bcb5783
- v2 post: https://konsus.slack.com/archives/C0BDGFE5QTE/p1784141386550359
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1783944006829769

### superside-timesheet-copilot (2026-07-13): skill, shipped
Reconstructs your day from Calendar, Gmail, Drive/Slides and Slack, drafts a timesheet bucketed into Superspace categories and logs only after confirmation; built for AM/AD work. **How:** Install, run 'reconstruct my day'; adjust timezone.
- Owners: Rodrigo Salazar
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1783968378401549

### AM Daily Digest (2026-07-13): skill, shipped
Scheduled Slack DM for AMs/ADs covering all projects on their accounts: team, progress timeline, milestones, deadline/overdue flags, estimated vs logged (high-estimate flag), next steps. **How:** Install from link and schedule.
- Owners: Rodrigo Cruz
- Install: https://claude.ai/customize/skills?selectedId=skill_01M3DaPXs3ZKGYZ1tp8efT8z
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1783967294672929

### 'Agent Tam' PTO automations (request tracking, capacity check) (2026-07-10): automation, shipped
Cowork automations watching #s-brief-generative-ai-and-automation for new requests, logging to Asana, asking predefined follow-up questions and tagging ANS staff; plus a capacity-check skill for studio capacity on demand. **How:** Ask Tamara Dalhuijsen / AI Native Studio.
- Owners: Tamara Dalhuijsen
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1783702789609769

### Bin Mirror (Premiere Pro plugin) (2026-07-10): plugin, beta
Rebuilds your Premiere Project panel bin structure on disk when collecting files and optionally relinks a self-contained project copy. MVP doesn't remove unused footage (workaround: save a trimmed copy first). **How:** Install from zip + user guide.
- Owners: Michelle Pienaar
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1783691575516119

### PTO handover dashboard (CL) (2026-07-09): skill, shipped
One-page handover of every project you're CL on: eagle-view table, 'Start here' day-by-day list, timeline, per-project cards with people and latest Slack context; HTML file + live artifact that refreshes on open. **How:** Ask for a PTO handover with dates and cover person(s).
- Owners: Alvaro Sanchez
- Install: https://claude.ai/customize/skills?selectedId=skill_019pQewh81KhAD12Gy69dPwP
- Loom: https://www.loom.com/share/19f0dd967a0c4d108222e4b2a90c89d9
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1783613053027899

### Water/stretch break nudge (2026-07-08): skill, shipped
Nudges you to drink water and stretch after 50 minutes of sustained Claude work, with a 10-minute break. **How:** Install from link.
- Owners: Danny Alva
- Install: https://claude.ai/customize/skills?selectedId=skill_01QQfudztB2GUo5aKqF5LvT2
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1783549225668609

### AE Project Auditor (2026-07-08): skill, beta
Audits After Effects .aep or Collect Files .zip without AE: missing/duplicate assets, draft vs delivery comps, generic names, stacked effects, zip completeness; scored health report. Ask to extend to Premiere/DaVinci. **How:** Install skill; drop .aep/.zip and ask 'audit this project'.
- Owners: Fabiano Cavalheiro
- Install: https://claude.ai/customize/skills?selectedId=skill_01MNwwo9AQp1Zenxrto9iv3f
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1783547382658329

### account-momentum-tracker (2026-07-07): skill, shipped
Flags accounts going quiet (no new projects, unused budget, cadence gaps, seasonal work last year), drafts internal summary + client-ready proposal; updated to use superside-mcp-internal + Omni credit/MRR trends and suggest 2-3 next projects. Thread tip (Andreas Drakos): share via Claude's native sharing rather than .skill files (auto-updates; .skill files are a security risk). **How:** Install via Claude sharing link; '/account-momentum-tracker [account]'. Needs superside-mcp-internal.
- Owners: Carlos Garcia · Updated: 2026-07-31
- Install: https://claude.ai/customize/skills?selectedId=skill_01S41ZnsRb3NaUGPyPYq9ixp
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1783440916815609

### Brand skill SOP (reference-library method) (2026-07-07): guide, shipped
SOP for building richer client brand skills with folders for brand docs, voice examples, visual examples, channel formats and anti-examples; used for McAfee. **How:** Follow the external SOP.
- Owners: Vince Shuley
- SOP: https://woolen-browser-ca4.notion.site/SOP-How-to-Build-a-Brand-Skill-for-Claude-37ad989200bc807bbebdcc5706de3208
- Newsletter: https://amazingwave.digital/ai-newsletter/
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1783440622523579

### portfolio-weekly-briefing (2026-07-06): skill, shipped
Monday DM of last 7-10 days of news (funding, leadership, launches, press, awards) per account with sources, skipping quiet accounts; scope from Superspace allocation or Salesforce (BU/studio leads). **How:** Add skill; in Cowork: 'Set up a weekly briefing on my accounts using the portfolio-weekly-briefing skill.'
- Owners: Richard Swain
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1783342815962099

### budget-review (2026-07-06): skill, deprecated
Budget review of projects where you're PM/AM: estimate vs logged hours by risk status. Broke when Chrome access to Superspace was blocked; author migrating to Superside MCP. **How:** Save .skill in Cowork; 'do budget review'.
- Owners: Gabriel Tosi · Updated: 2026-07-22
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1783337113666679

### AI Soundbite Generator (2026-07-03): tool, shipped
Generates soundbites/quotes from a year of Superside marketing content (webinars, guides, reports) linked to the source. **How:** Web version at Vercel.
- Owners: Kae Neskovic
- App: https://s-soundbite-generator.vercel.app/
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1783081118217949

### Meet Transcript Search (2026-07-02): skill, shipped
Answers questions about past meetings by searching your Google Meet Recordings folder (Gemini summaries, next steps, transcripts) in Drive. **How:** Upload skill with the setup prompt so Claude fills <FOLDER_ID>, <FOLDER_NAME>, <OWNER_EMAIL>. Needs Google Drive connector.
- Owners: Aki Friedrich
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1783014038806759

### Superside Cowork Skills - Marketing & GTM Library (2026-07-02): guide, shipped
Notion library of GTM and personal Cowork skills by Josh Mendelsohn; flash-card/quiz system for value props in progress. **How:** Browse the Notion library.
- Owners: Josh Mendelsohn
- Notion: https://app.notion.com/p/Superside-Cowork-Skills-Marketing-GTM-Library-38f50ebbbec081108e46f270bf546d74
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1782999124222589

### Hours & utilization dashboard (Personio + Superspace) (2026-07-01): skill, deprecated
Cowork skill reading PTO from Personio and logged hours from Superspace via Chrome to show utilization/billable pace. Post struck through: author moving to Omni. Data team asked outputs to match Omni Utilization dashboard (source of truth); bug missed account billable hours. **How:** Superseded; use Omni / official MCP tools.
- Owners: Marie Gimenez · Updated: 2026-07-09
- Omni Utilization dashboard: https://superside.omniapp.co/dashboards/8151bede?f--i0j6wjaT=%7B%22values%22%3A%5B%22marie.gimenez%22%5D%2C%22appliedLabels%22%3A%7B%7D%7D&f--cYqJFU5W=%7B%22right_side%22%3A%221+months+from+now%22%7D
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1782937570027759

### Summarize Figma client comments with Claude (2026-07-01): workflow, shipped
Use Claude for Chrome on a browser Figma file to read all comments and produce structured summaries. Figma MCP can't read comments; Figma Console MCP and Figma's native agent can. **How:** Open Figma in Chrome, paste URL to Claude, ask it to read comments and summarize.
- Owners: Emilio De Juan · Updated: 2026-07-15
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1782926372229849

### personal-voice-builder (2026-07-01): skill, shipped
Analyzes your Slack messages to learn your writing gears, register by audience and fingerprints, then outputs an installable voice skill, reference file and analysis report. **How:** Type /personal-voice-builder.
- Owners: Phillip Maggs
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1782918682622749

### Morning Pulse + Weekly summary artifacts (2026-07-01): artifact, wip
Morning Pulse summarizes billable hours logged per project per studio the previous day (Bloom team, 26 countries); scheduled Friday weekly summary in her voice. **How:** Ask Soumya Ramakrishnan.
- Owners: Soumya Ramakrishnan
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1782913584029639

### Superside residence & Culture Map dashboard (2026-07-01): dashboard, shipped
HTML dashboard of where Supersiders live (filters by department/studio/level) with a Culture Map country comparison; uses Superside brand skill; data from Personio. **How:** HTML attached in Slack.
- Owners: Joaquin Migliore
- Culture Map book: https://www.goodreads.com/en/book/show/22085568-the-culture-map
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1782902424192059

### Jing's Claude workflows (daily briefing, overnight work, weekly bug agent) (2026-07-01): workflow, shipped
Examples: contact-finding + email drafting from Calendar, form filling, daily briefing, Claude mobile + dispatch, overnight work queue, weekly bug agent (Superads), self-serve data analytics. **How:** Inspiration post.
- Owners: Jing Venås Kjeldsen
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1782907291942549

### Meeting Notes -> To-Do Hub, Success Session Deck, Mac cleanup skills (2026-06-30): skill, shipped
Three AM skills: meeting transcripts -> colour-coded Notion to-do hub per account (3x/day); success-session deck builder (8-12 slides .pptx from live account data, speaker notes, renewal and growth sections); Mac cleanup/declutter with approval before deletes. Based on his earlier Slack triage DM workflow. **How:** Install each; tell Claude 'personalise this skill for my accounts' (built for Booking.com).
- Owners: Leeroy Duke · Updated: 2026-07-10
- Meeting Notes -> To-Do Hub: https://claude.ai/customize/skills?selectedId=skill_01GSiTSK3xUH347uMokvPG7F
- Success Session Deck: https://claude.ai/customize/skills?selectedId=skill_019fPD5z52xdo5EhtQcYVFDb
- Mac cleanup: https://claude.ai/customize/skills?selectedId=skill_013HCs3mBXPfaqqfnV1sd7kk
- To-Do Hub Loom: https://www.loom.com/share/9c235dcce40044adad22601f79201152
- Deck Loom pt1: https://www.loom.com/share/6a9c3d5b814048cfb602269733b3535d
- Deck Loom pt2: https://www.loom.com/share/fd050938f7fc41f685fe26836ba95fc4
- Original workflow post: https://konsus.slack.com/archives/C0BDGFE5QTE/p1782806648722689
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1783698161026749

### Slack triage DM 3x/day + MSS deck pinned chat (2026-06-30): workflow, shipped
Scheduled skill scanning Slack mentions, client emails, DMs and channels to DM a triage (burning now / this week / FYI) 3x a day; Notion to-do hub; desktop cleanup; pinned chat with Omni/Notion/Slack Connect context that builds monthly MSS decks. **How:** See Leeroy's later skills post. Olga Lombard/Wayde Davy built the base; Asana sync in progress.
- Owners: Leeroy Duke, Olga Lombard, Wayde Davy
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1782806648722689

### Churn-save multithreading emails (Apollo + Gmail) (2026-06-29): workflow, shipped
Gave Claude Apollo stakeholder list + context; it wrote 13 personalized emails and scheduled them from Gmail in <30 min. RevOps: keep <10 emails/domain/day, route customer-facing outreach via RevOps; Apollo MCP coming. **How:** Contact list + account context + objective.
- Owners: Steve Blackwell
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1782760193223749

### daily-task-briefing (2026-06-29): skill, shipped
Morning Slack message with everything due today/this week from Superside Phases and Tasks for creatives. Scheduling must be set up in Cowork. **How:** Install, run /daily-task-briefing in Cowork.
- Owners: Marie Gimenez · Updated: 2026-06-30
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1782748175968669

### Brand Toolkit builder (Figma Console MCP) (2026-06-29): skill, wip
Populates Superside's Figma Toolkit template from a client brand guidelines file: component sets, color variables, text styles, assets, library; preflight check. **How:** Ask Gabrielle Moura to test.
- Owners: Gabrielle Moura
- Figma Toolkits walkthrough: https://app.notion.com/p/Figma-Toolkits-36b50ebbbec0805b93ced8a148056d26
- Figma Console MCP: https://github.com/southleft/figma-console-mcp
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1782741725962719

### EzGIF (After Effects GIF exporter) (2026-06-29): plugin, beta
AE plugin to export comps or videos/image sequences to GIF in one click or batch, with target file size. Needs a PNG sequence export template. **How:** DM Fernando Thome for the .zxp installer. Internal only (beta).
- Owners: Fernando Thome · Updated: 2026-07-02
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1782739059653389

### Executive Coach scheduled task (2026-06-29): automation, shipped
Daily task reading call transcripts and Slack messages and suggesting improvements; built by asking Claude to interview you. Thread: Slack project-update DM agent, file-renaming skill, stock footage search via Chrome (Artlist). **How:** Ask Claude: 'help me build an Executive Coach agent'.
- Owners: Fredrik Thomassen · Updated: 2026-06-30
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1782729355574359

### Creative Brainstorm Bouncer (2026-06-26): skill, shipped
Pressure-tests concepts with an award-trained CD persona and a target-audience persona, scoring 10 dimensions with fixes. **How:** Install creative-brainstorm-bouncer.skill; feed idea, brief, audience.
- Owners: Matteo Rostagno · Updated: 2026-06-29
- Loom: https://www.loom.com/share/862254baef7a44178b19b25273ddba47
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1782490199436059

### Admin Grinch (2026-06-26): skill, shipped
Writes Dr Seuss-style rhyming reminders for admin tasks (timesheets, trainings). **How:** Customize > Skills > + > Upload file.
- Owners: Tamara Dalhuijsen
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1782479186201939

### Superside Brand System (2026-06-26): skill, shipped
Applies Superside brand identity to internal deliverables; modular. Now in Superside Internal plugin. Update manually when brand changes. **How:** Install or use /superside-brand-system.
- Owners: Aki Friedrich · Updated: 2026-07-01
- Loom: https://www.loom.com/share/e6186ae3b5b448be9730310257cc5f27
- Permalink: https://konsus.slack.com/archives/C0BDGFE5QTE/p1782468725367109

## Recurring themes / open asks

**Themes**
- Many people build overlapping tools for the same jobs: hour logging and timesheets (at least 6 builds), morning or daily briefings and triage (at least 8), PTO handovers (3), account news engines (4), budget and overrun tracking (5), and QC checks. Check the official PM, AM and Creative plugins and the Creative Skills Catalogue first. Matteo Rostagno and Tamara Dalhuijsen are actively folding community skills into the plugins.
- Sharing friction: skill links often don't open across the Team and Enterprise workspaces, so people fall back to attaching `.skill` files. Andreas Drakos flags `.skill` files as a security risk and recommends Claude's native sharing, which also auto-updates.
- Moving from Claude-in-Chrome to MCP connectors. Skills that scraped Superspace through Chrome broke in July 2026 (for example budget-review and the hours dashboard). Omni access has a `pickModel` permission gap.
- Data accuracy: the Superspace MCP hour tools have bugs (staff-utilization loggedHours=0; my-logged-hours covers CREATIVE only). AI-off accounts are invisible to Claude. Omni is the source of truth for utilization.

**Open asks (no confirmed solution in channel)**
- Quote estimates without a Superspace project or brief, for example from a deliverables list or Excel (Mónica Mendieta). Quote accuracy is weak for complex, video and Figma Buzz work. https://konsus.slack.com/archives/C0BDGFE5QTE/p1784810328832889
- Full HTML5 banner delivery with Claude: nobody is known to be doing it yet; suggested as a hackathon topic. https://konsus.slack.com/archives/C0BDGFE5QTE/p1784887390855829
- Checking an idea against Cannes or award archives and real-brand references (Carolina Trujillo). No replies. https://konsus.slack.com/archives/C0BDGFE5QTE/p1788449197984339
- Bringing Workfront feedback into Figma (Marcela Casasfranco). https://konsus.slack.com/archives/C0BDGFE5QTE/p1782926372229849
- Brief to emoji project plan in Superside layout, then Asana milestones and a short creative brief for Slack (Azalea Castro). Only partly covered by manage-project-timeline. https://konsus.slack.com/archives/C0BDGFE5QTE/p1785982245716839
- A hosted, auto-syncing ChatGPT dashboard for the Reddit account, which is Claude-restricted (María Rojas). Pending R&D. https://konsus.slack.com/archives/C0BDGFE5QTE/p1792461143475639
- Superside MCP gaps: project timeline and overview fields (Linear AGI-126), and own logged hours across all categories. https://konsus.slack.com/archives/C0BDGFE5QTE/p1784194821981809
- Team or company-wide artifact and skill registries, plus sharing artifacts across Team and Enterprise workspaces. https://konsus.slack.com/archives/C0BDGFE5QTE/p1793971682790579
- Figma print report to InDesign was solved by Marcelo Pelica's skill. AE Project Auditor for Premiere and DaVinci files was requested but not built.
- Apollo MCP (stakeholder mapping, sequences) is pending a security review.
