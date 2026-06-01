# CLAUDE.md — kinematic-equations-app

## What This Repo Is
Physics slide decks for a teacher (Hani Hamadeh). Each `index.html` is a self-contained slide presentation for students.

## Live Deployment
- **URL**: https://work-done-by-weight.pages.dev
- **Host**: Cloudflare Pages (project name: `work-done-by-weight`)
- **Source file**: `index.html` in this repo (main branch)

## How to Redeploy to Cloudflare
Cloudflare API calls are BLOCKED from Claude Code cloud sessions (IP not in allowlist).
Deployment MUST be done from the user's local Mac. Tell the user to run in Terminal:
```bash
cd ~/Downloads/work-slides
curl -O https://raw.githubusercontent.com/hanihamadah/kinematic-equations-app/main/index.html
wrangler pages deploy . --project-name work-done-by-weight
```

## User Preferences
- Prefers short, direct answers — no prolonged back-and-forth
- Do NOT give links until they are verified to work
- Do NOT suggest GitHub Pages or htmlpreview as alternatives to Cloudflare — user wants Cloudflare
- When Cloudflare deployment is needed: immediately tell user to run wrangler locally on their Mac
- User is a physics teacher, not a developer — explain technical steps in plain language

## Known Issues / Lessons from Session 2026-06-01
- GitHub Pages was never enabled (Branch: None) — caused 404 links to be shared with students
- iOS Safari hides bottom nav when using `100vh` — fix is `position: fixed` on `#nav`
- Cloudflare API tokens with IP restrictions fail with "Host not in allowlist" — do not ask user to create tokens for use from this cloud environment
- The repo name "kinematic-equations-app" is misleading — content is about Work & Energy

## Cloudflare Token Security
- User created API tokens on 2026-06-01 that were shared in chat — they should be deleted
- Location: dash.cloudflare.com → person icon → My Profile → API Tokens
