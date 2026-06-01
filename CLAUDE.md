# CLAUDE.md — kinematic-equations-app

## What This Repo Is
Physics slide decks for a teacher (Hani Hamadeh). Each `index.html` is a self-contained slide presentation for students.

## Live Deployment
- **URL**: https://work-done-by-weight.pages.dev
- **Host**: Cloudflare Pages (project name: `work-done-by-weight`)
- **Source file**: `index.html` in this repo (main branch)

## How to Redeploy to Cloudflare
Claude Code cloud CAN deploy to Cloudflare — but the API token must have NO IP restrictions.

If deployment fails with "Host not in allowlist", the token was created with IP filtering enabled.
Fix: create a new token at dash.cloudflare.com → My Profile → API Tokens → Create Token
→ use "Edit Cloudflare Workers" template → leave "Client IP Address Filtering" EMPTY → save.

Then set the token and deploy:
```bash
CLOUDFLARE_API_TOKEN=<token> wrangler pages deploy /home/user/kinematic-equations-app --project-name work-done-by-weight
```

## Google Stitch (AI UI design) — Setup on Mac
Stitch is Google's free AI UI design tool. It can connect to Claude Code via an MCP server,
so you describe a UI in plain English and the generated design + code flows into this repo.

**This only works when running Claude Code locally on the Mac** (it needs `npx`, which the
cloud session can't run). Setup steps for the Mac:

1. Get an API key: stitch.withgoogle.com/settings → "API Keys" → Create API Key
2. Add to the MCP client config (`~/.claude/settings.json` or `.mcp.json`):
   ```json
   {
     "mcpServers": {
       "stitch": { "command": "npx", "args": ["@_davideast/stitch-mcp", "proxy"] }
     }
   }
   ```
3. Set the key: `export STITCH_API_KEY=<key>` (or use the OAuth path for long-term use)

Then: describe a slide layout → Stitch designs it → Claude turns it into `index.html` to deploy to Cloudflare.

## User Preferences
- Prefers short, direct answers — no prolonged back-and-forth
- Do NOT give links until they are verified to work
- Do NOT suggest GitHub Pages or htmlpreview as alternatives to Cloudflare — user wants Cloudflare
- When Cloudflare deployment is needed: immediately tell user to run wrangler locally on their Mac
- User is a physics teacher, not a developer — explain technical steps in plain language

## Known Issues / Lessons from Session 2026-06-01
- GitHub Pages was never enabled (Branch: None) — caused 404 links to be shared with students
- iOS Safari hides bottom nav when using `100vh` — fix is `position: fixed` on `#nav`
- Cloudflare "Host not in allowlist" error means the TOKEN has IP filtering enabled, not that the cloud server is blocked. Cloudflare worked fine from cloud 30 hours prior with an unrestricted token.
- The repo name "kinematic-equations-app" is misleading — content is about Work & Energy

## Cloudflare Token Security
- User created API tokens on 2026-06-01 that were shared in chat — they should be deleted
- Location: dash.cloudflare.com → person icon → My Profile → API Tokens
