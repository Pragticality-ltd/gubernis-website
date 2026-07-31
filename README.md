# gubernis-website

Source files for the **Gubernis** marketing website at [gubernis.com](https://gubernis.com).

Static HTML/CSS — no build step, no JavaScript framework, no dependencies beyond Google Fonts. Sibling to [`pragticality-website`](https://github.com/Pragticality-ltd/pragticality-website) (the holding-company site) and [`gnomon-website`](https://github.com/Pragticality-ltd/gnomon-website) (the sibling product site).

## What Gubernis is

The regulatory watch for UK, EU, and US trade compliance. Surfaces what changed in regulation; flags ambiguity where careful readings diverge. A Pragticality Ltd product alongside Gnomon (classification) — the wedge in the wedge → destination product architecture.

Brand kernel: **Surfaces change. You decide.**

Strategic context: `pragticality-docs/gubernis/` in the [`pragticality-docs`](https://github.com/Pragticality-ltd/pragticality-docs) repo, particularly:

- `00_README.md` — what Gubernis is, naming rationale, relationship to Gnomon
- `05_product_thesis.md` — Gubernis-as-product wedge → destination thesis
- `06_brand_direction.md` — kernel, voice, palette, ornament, three tones explored
- `strategic_package/website/gubernis-brand-direction.html` — the design exploration that became this site

## Read first

1. **[`SESSION_START.md`](./SESSION_START.md)** — quick orientation, deploy workflow
2. **[`CLAUDE.md`](./CLAUDE.md)** — guidance for AI assistants editing this repo (brand voice rules, the hard "do not"s)
3. The strategic docs above

## Repo structure

```
gubernis-website/
├── README.md           this file
├── SESSION_START.md    quick orientation + deploy workflow
├── CLAUDE.md           guidance for AI editing this repo
├── .gitignore
├── .htaccess           forces HTTPS, canonicalises www → apex
├── styles.css          single shared stylesheet
├── robots.txt
├── sitemap.xml
├── favicon.svg         the § mark in oxblood
├── index.html          single-page landing site
├── privacy/            privacy notice
├── terms/              subscription agreement
├── samples/            Watch Forward sample dispatches
├── scripts/            deploy-time patch + card-picker scripts
├── .well-known/        RFC 9116 security.txt
└── .github/workflows/  deploy.yml — lftp mirror to IONOS on push
```

Multi-page expansion (e.g. `/about/`, `/pricing/`, `/how-it-works/`) is deferred to a later session. The single-page V1 is enough to validate willingness-to-pay via the LinkedIn survey planned in `pragticality-docs/gubernis/05_product_thesis.md` §6.

## How it deploys

**Live on IONOS, auto-deployed.** `gubernis.com` (registered 2026-05-12) runs
on IONOS web hosting (same vendor as `pragticality.com`), with DNS managed in
the IONOS control panel. The site went live end-to-end on 2026-05-24.

Deployment is automated — no manual upload:

1. **Push to `main`** triggers the GitHub Actions workflow at
   `.github/workflows/deploy.yml`, which stages public files into `dist/` and
   `lftp`-mirrors them to IONOS over SFTP (port 22). The SFTP user is chrooted
   to `/Gubernis/`. Same pattern as `gnomon-website`. Three repo secrets:
   `IONOS_FTP_HOST`, `IONOS_FTP_USER`, `IONOS_FTP_PASS`.
2. **Two values self-patch at deploy time** from the live engine's public
   endpoints, so their values in `index.html` source are stale by design —
   what's served is always fresh:
   - the **Watch counter** (`scripts/patch_watch_counter.py`), and
   - the **"Areas of focus" cards** (`scripts/patch_featured_cards.py`).
3. An **hourly scheduled redeploy** keeps those numbers current without needing
   a push.

`.htaccess` forces HTTPS and canonicalises `www.gubernis.com` → apex (Let's
Encrypt SSL at IONOS). Google Search Console is verified and `sitemap.xml`
(covering `/privacy/`, `/terms/`, `/samples/`) is submitted; Bing Webmaster
Tools is deferred.

See `SESSION_START.md` ("What's wired up") for full hosting / DNS / SFTP
details and the deploy-adjacent backlog.

## What this isn't

- **The Gubernis engine** — that's the `gubernis/` module in [`pragticality`](https://github.com/Pragticality-ltd/pragticality) (merged to `main` 2026-05-21; daily scheduler live on the Mola IONOS VPS at `app.gnomon.info`, migrated off Railway 2026-06-03). Connectors for US Federal Register, OFAC SDN, UK gov.uk, UK HMRC Trade Tariff, EU Consolidated Sanctions, EUR-Lex, USTR Section 301, BIS Section 232, US Congress, EU Legislative Train, UK Parliament; dual-LLM cross-check tagger; semantic diff engine; automated smoke test. See `pragticality-docs/gubernis/04_poc_report.md` for the PoC verdict.
- **The Gubernis sub-brand assets** (logo SVG variants, social-share images, business cards). Those don't yet exist; only the `§` wordmark and oxblood palette are defined. Add when needed.
- **The Pragticality Ltd holding-company site** — that's [`pragticality-website`](https://github.com/Pragticality-ltd/pragticality-website).
- **The Gnomon product site** — that's [`gnomon-website`](https://github.com/Pragticality-ltd/gnomon-website).

## Conventions (inherited from sibling repos)

- **Markdown for guides, HTML for the site itself.** No SCSS, no preprocessors, no JS toolchain.
- **One stylesheet** (`styles.css`) shared across all pages. Per-page styles are forbidden.
- **Internal links use absolute paths** (`/about/`, `/pricing/`) so they work whether deployed at root or a subpath.
- **External links** open in a new tab with `rel="noopener"`.
- **Brand voice rules** are enforced in `CLAUDE.md` for AI assistants editing the repo. The hard ones: no "AI-powered" language, no mechanism description in customer copy, no unsupported competitive claims.

## Notes on brand voice

Gubernis copy is **trusted-advisor-with-skin-in-the-game**. Quiet authority, plain English, no SaaS marketing tells. Specifically:

- **Never** describe the dual-LLM cross-check mechanism in customer copy. The Ambiguity Watch is the *outcome* the customer sees; the engine architecture is invisible infrastructure. Memory rule: *"saying 'dual AI' might convince some people it can go wrong twice as fast."*
- **Never** make unsupported competitive claims like "no other regulatory monitor offers this." Either verify with research, or describe the product and let readers infer differentiation.
- **Never** use words like *empower, harness, transform, next-generation, AI-powered, intelligence platform.* These tells mark generic-SaaS-marketing voice that Gubernis explicitly opposes.

See `CLAUDE.md` for the full voice guide.
