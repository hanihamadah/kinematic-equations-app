# Session Log — Work Done by Weight Slide Deck

## What Was Built
A 10-slide HTML presentation explaining W_fg = ±mgh.
- Moving UP → W = +F·d = +mgh (positive, energy stored)
- Moving DOWN → W = −F·d = −mgh (negative, energy released)
- Includes derivation, diagrams, and 3 worked examples

## Live URL
```
https://work-done-by-weight.pages.dev
```
Hosted on Cloudflare Pages. Deployed manually from Mac using wrangler CLI.

## How to Redeploy After Changes
1. Edit `index.html` in this repo
2. Push to `main` branch (Claude can do this)
3. In Terminal on your Mac:
```bash
cd ~/Downloads/work-slides
curl -O https://raw.githubusercontent.com/hanihamadah/kinematic-equations-app/main/index.html
wrangler pages deploy . --project-name work-done-by-weight
```

## Mistakes Made This Session (and why)

| # | Mistake | What Happened | Fix |
|---|---------|---------------|-----|
| 1 | Gave GitHub Pages URL before enabling it | Link showed 404 — not suitable for students | GitHub Pages needs manual activation in repo Settings |
| 2 | Repo name is "kinematic-equations-app" | Content is about Work/Energy, not kinematics — confusing name | Name was pre-existing; content is correct |
| 3 | Gave htmlpreview link without mobile testing | Navigation buttons were hidden on iPhone (iOS Safari viewport bug) | Fixed with `position: fixed` on nav bar |
| 4 | Tried two `dvh` viewport fixes before finding root cause | Both failed on iOS | `position: fixed` was the correct solution |
| 5 | Tried to deploy to Cloudflare from cloud environment | Cloudflare blocks API calls from this server's IP range — "Host not in allowlist" | Must deploy from local Mac using wrangler |
| 6 | Asked user to create API tokens twice | Both tokens rejected — problem was never the token, it was the IP block | Should have diagnosed IP block first and directed to local deploy immediately |

## Cloudflare Notes
- This was the first time creating a Cloudflare API token
- Tokens are at: dash.cloudflare.com → person icon (top right) → My Profile → API Tokens
- The tokens shared in chat should be deleted and rotated: dash.cloudflare.com → My Profile → API Tokens → delete the two `cfut_` tokens created today
- Future Cloudflare deployments must be run from your Mac, not from Claude Code cloud sessions

## Files in This Repo
- `index.html` — the slide deck (single self-contained file)
- `.github/workflows/pages.yml` — GitHub Actions workflow (set up for GitHub Pages if ever needed)
