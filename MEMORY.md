# MEMORY.md — User Preferences & Learned Behaviours

## About the User
- Name: Hani Hamadeh (hani.hamadeh@gmail.com)
- Role: Physics teacher
- GitHub: hanihamadah
- Cloudflare account: Hani.hamadeh@gmail.com
- Mac Air (local machine for deployments)

## Communication Style
- Keep responses short and direct
- No emoji
- Use plain language — user is not a developer
- When giving a link, verify it works BEFORE sharing it
- Code blocks for anything the user needs to copy/paste

## Deployment Rules
1. **Always deploy to Cloudflare Pages** — this is the user's preferred host
2. Claude Code cloud CAN deploy to Cloudflare if the token has no IP restrictions
3. If "Host not in allowlist" error appears, the token was created with IP filtering — ask user to create a new token leaving "Client IP Address Filtering" empty
4. Do not offer GitHub Pages or htmlpreview as alternatives unless Cloudflare is truly unavailable

## Cloudflare Projects (as of 2026-06-01)
- pulley-system-sim.pages.dev
- physics-learning-tools.pages.dev
- physics-final-exam-prep.pages.dev
- momentum-impulse-mast... .pages.dev
- aus-phy001-preparatory-... .pages.dev
- work-done-by-weight.pages.dev ← created this session

## What NOT to Do
- Do not give unverified links
- Do not ask user to create Cloudflare API tokens for use from Claude Code cloud — they will always fail
- Do not suggest prolonged multi-step processes when a simpler path exists
- Do not use emoji
