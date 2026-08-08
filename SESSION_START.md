# SESSION_START — gubernis-website

## ⚠️ Workspace & Git rules — READ FIRST (all machines)

**Where repos live — local, never cloud-synced:**
- **Mac:** `~/Developer/…` — **NEVER** `~/Documents` or `~/Desktop` (iCloud-synced — corrupts `.git`).
- **Windows:** a local path like `C:\dev\…` — **NEVER** under OneDrive (Documents/Desktop break Git the same way).
- Tell-tale damage: empty "husk" folders, or ` 2` conflict-copy junk in `.git/objects`. If you see either, you're in a synced copy — stop and switch to the `~/Developer` clone.

**Three devices:** travel MacBook · old Mac (desktop) · Windows PC. They share code **only through GitHub** — never a synced folder. **`origin/main` is the single source of truth.**

**Every session:**
- **Start:** `git pull` before touching anything — another machine may be ahead.
- **After each chunk / before walking away:** commit + `git push`. Keep `origin/main` == local.
- Stay on `main` unless there's a real reason to branch.

**If a repo looks broken** (wrong location, ` 2` junk, empty folders): don't work in it. Everything's on GitHub — re-clone fresh and copy over local-only files like `.env.local`.

---

Quick orientation for picking up work on this repo. Read `README.md` and `CLAUDE.md` for the substance; this file is just for the *what now* question.

## Working across machines — pull first, push last (read before touching anything)

This repo is edited from more than one machine (Mac, mobile, web sessions). The
**remote is the single source of truth**; a local checkout is only as fresh as
its last pull. To avoid clobbering work done elsewhere:

1. **Start of session — pull before you do anything.** Fast-forward both `main`
   and the branch you'll work on, so you're building on the latest:
   ```
   git pull origin main
   git pull origin <your-working-branch>
   ```
   A fresh web/cloud session clones the repo current — but `main` can still move
   *underneath* a long session, so pull again if you've been idle.

2. **While working — never `--force`.** A normal push is fast-forward-only: git
   rejects it if another machine pushed in the meantime. A rejected push is the
   safety net working — **fetch and reconcile, never force over it.** A
   force-push is the only way to actually lose another machine's work.

3. **End of session — push, then update this file.** Two non-negotiable closing
   steps, in order:
   - `git push` your branch so the next machine can pull it.
   - **Update this `SESSION_START.md`** — what changed, what's now live, what's
     left. This has long been the practice; it is now the rule. The session doc
     is only trustworthy if every session leaves it current, so append to the
     relevant section and never let it drift behind the code.

## Recent changes

- **2026-07-31 → 2026-08-02** — Docs + homepage-copy pass (site side of a larger cross-repo session; the bulk of that session was engine work in the `mola` repo — see its `BACKLOG.md`). **(1) README refreshed** — the "How it deploys" section described the site as pre-deploy ("host pending", manual upload); rewritten to the live reality (IONOS + GitHub Actions auto-deploy, the two self-patching values — Watch counter + Areas-of-focus cards, hourly redeploy). **(2) Stale Railway references purged** — the engine moved off Railway to the Mola IONOS VPS at `app.gnomon.info` (2026-06-03); README/SESSION_START/script docstrings still said Railway and could send a future session debugging a dead host. All corrected; Doc-25 Workstream A follow-up flipped to DONE. **(3) Areas-of-Focus section reframed** — heading `Areas of focus this period` → **`What a Gubernis read looks like`** with a new sample/agency dek (*"A sample. Yours would be focused on your area — every claim cited, the decision left to you."*), section label → **`From the Weekly Watch`**, both CTAs → *"See how we read a change"*, and the stale `WHAT CHANGED THIS WEEK` comment fixed. The cards are a *teaser of the read-quality* a subscriber gets on their own area, not a live watchlist; the "decision left to you" closer doubles as the liability posture (kernel: Surfaces change. You decide.). New `.section-dek` CSS mirroring `.pricing-section .subhead`. **(4) Follow-up #5 logged** — the real-time premium alert-tier pivot (canonical backlog entry lives in `mola/BACKLOG.md`). Touches: `index.html`, `styles.css`, `README.md`, this file. Deploy: push → auto-deploy to IONOS; verified live (cards re-patched from the approved cardset each deploy).

- **2026-06-09** — Three discrete pieces shipped. **(1) `#this-week` cards refreshed** — three new substantive flagged changes folded into the homepage: UK Steel Industry (Nationalisation) Bill at v11, EU Decision 2014/145 corrigendum on the Russia / Ukraine territorial-integrity restrictive-measures regime, and the modernised EU-Mexico Global Agreement at its eighth Legislative-Train iteration. Each card carries a full plain-English summary (10–25 words description, 3-sentence body) rather than `[WRITE SUMMARY]`. **(2) Public CTAs rewired now Stripe is in prod.** Every `Start free` / `Subscribe` / `Subscribe to Pro` CTA on the page now routes to `https://app.gubernis.com/gubernis/app` (Clerk magic-link → config → Stripe Checkout); **Watch Forward CTA routed to mailto** per the integration spec §2 (Watch Forward / Enterprise are "contact us" until the role-targeted dispatch feature exists on the engine — don't sell what doesn't ship). **(3) `#sign-up` section reframed** — Formspree early-access form retired, "Gubernis is currently in pre-launch" copy removed; section becomes a `Create your account →` doorway pointing at `app.gubernis.com/gubernis/app`. Section `id="sign-up"` preserved so existing anchors don't 404. **(4) Liquet teaser headline sharpened** — the "regulatory weather" metaphor on the closing-table sister-offering section replaced with `For M&A diligence: Gubernis surfaces change. Liquet grades a target's exposure to it — current and future.` Names the audience explicitly, picks up `grades` from the body copy so the register stays tight. Touches: `index.html` only. Deploy: push to `main` → auto-deploys to IONOS (verified live by Steve).

- **2026-06-05** — Messaging + samples refresh. **Hero** now carries the
  hours-back/exposure promise as a kicker under the H1 ("The hours back. The
  risk in front of you."); **pricing** leads with "Your inbox, triaged by
  exposure." and folds the "stop reading everything" line + the payback framing
  ("one avoided misclassification or missed control change pays for the year")
  into the subhead. New CSS `.hero-kicker` / `.pricing-kicker` (Source Serif /
  ink / oxblood, mobile-scaled). "Surfaces change. You decide." kept as the H1.
  The **`/samples/`** page is reframed as a deliberately-lagged **archive
  sample** — "Week ending 23 May / Dispatch No. 23" → "From a recent week /
  archive sample", plus a lag note ("subscribers receive the current week's
  watch — not this one") — so current-week intelligence stays behind the
  paywall. Touches: `index.html`, `styles.css`, `samples/index.html`. Deploy:
  push to `main` → auto-deploys to IONOS. (Companion: conservative ROI/payback
  models for Gubernis + Gnomon live in the `Pragticality` working folder for sales.)

- **2026-06-02** — Gubernis MVP-scope specs landed in the Mola engine
  repo at `hs-mvp/docs/gubernis/` (seven docs + index README). Spine
  doc is `gubernis-clerk-stripe-integration.md` (data model, Clerk auth,
  Stripe webhooks); read order and Phase 2 carve-outs in `00_README.md`.
  `gubernis-tier-transition-clarification.md` governs precedence where
  the others disagree (key rule: free-tier preferences are stored but
  ignored at dispatch time). The `/files/{engine_id}` architecture
  question is now resolved — dynamic Gubernis surfaces live at
  `app.gubernis.com`; apex stays static. Captured as `ADR 003` in
  `hs-mvp/docs/architecture_decisions/003_app_subdomain_for_dynamic_surfaces.md`
  with the Gubernis-wide consequences (config page, archive, Watchlist,
  Ask Gubernis all on `app.`). Cross-references added to this repo's
  `CLAUDE.md` under "Auth, payments, privacy — coordination with the
  Mola engine repo": pricing-page CTAs → Stripe Checkout via `app.`,
  `#sign-up` → Clerk magic link, `/privacy/` revision against the
  substantive data policy, and the `/files/{engine_id}` route resolution.
  No code on this site changes yet — all the above is deferred until
  the engine work lands.
- **2026-06-02** — Editorial discipline note from today's session: the
  steel-card refresh demonstrated that engine-surfaced regulatory items
  need a sense-check against current state-of-play before publishing as
  lighthouse content. The first pass framed *"is 1 July application
  confirmed?"* as an open ambiguity, sourced from a Legislative-Train /
  Council press-release divergence; Parliament had already adopted in
  plenary on 19 May (606–16–39), closing the ambiguity. The fix is
  editorial (sense-check), not architectural — but every dispatch and
  lighthouse piece going forward inherits this discipline. Worth
  watching for in dispatch review window (Friday 06:00–08:00 UK, per
  `dispatch-template-v1.md` §9).
- **2026-06-02** — Cards refreshed and then Card 3 swapped mid-session:
  - First pass: HMRC-NEWS-6565 (UK China quota 058949 critical, welded
    pipes Ch. 73), FR-2026-10873 (FDA draft guidance on streamlined
    nonclinical safety for oncology biologics/conjugates, docket
    FDA-2026-D-2839, comments to 31 Jul), and the EU LegTrain pipeline
    file on steel overcapacity. Long-form briefing pack written to
    `~/Downloads/gubernis-areas-of-focus-2026-06-02.md` for the
    copywriter.
  - Same-day swap of Card 3: replaced the LegTrain pipeline framing with
    a fresh card on the **EU steel safeguard replacement** —
    `EU-STEEL-SAFEGUARD-REPLACEMENT-2026`. Parliament adopted the
    regulation in plenary on 19 May 2026 (606–16–39), so the earlier
    *"is 1 July application confirmed?"* ambiguity is closed. The new
    card surfaces the three substantive questions that remain open in
    the 28-day window to entry into force: country quota allocations
    (still being negotiated for WTO compatibility), the Commission's
    implementing rules on *melt and pour country* traceability evidence
    (due 31 August — 62-day gap between substantive rule and evidence
    framework), and product-scope drift from 28 to 30 categories.
- **2026-05-31** — Renamed the homepage `#this-week` section heading from
  *"What changed this week"* to *"Areas of focus this period"* (commit
  `2d8d070`). The weekly framing was an implicit cadence promise the
  editorial refresh doesn't actually keep. The two CTAs that point at the
  section now read *"See what we're configured to watch at this moment"*.
  Docs (CLAUDE.md, this file, script docstring) updated in lockstep.
  Anchor `id="this-week"` left as internal plumbing; `samples/` page kept
  its weekly wording because those dispatches genuinely are weekly.
- **2026-05-31** — Cards refreshed (commit `1913648`): HMRC-NEWS-6533
  (UK commodity code dynamic-alignment with EU), OFAC-DELTA-2026-05-29
  (standard SDN delta), EURLEX-32026R1144 (EU cultural-goods export
  e-licences). All three ambiguity-flagged in the engine; picked for
  jurisdiction balance (UK/US/EU) and topic spread (tariff /
  sanctions / export control). Pulled from the live engine's last
  14-day window via the picker script.

## ✅ Live — as of 2026-05-24

**gubernis.com is live.** Engine running daily on the Mola IONOS VPS
(`app.gnomon.info`, migrated off Railway 2026-06-03), marketing site
deployed to IONOS, legal floor in place, search engines verified.

**What's wired up:**

- DNS: gubernis.com nameservers at IONOS (`ns1045.ui-dns.*`); A record
  auto-set to `217.160.0.23` by IONOS once domain was connected to
  webspace under `/Gubernis/`
- Hosting: IONOS web space, contract 107127470, host
  `access-5018101164.webspace-host.com`
- SFTP user: `a2016447` (chrooted to `/Gubernis/`) — created via the
  IONOS panel
- Auto-deploy: GitHub Actions workflow at `.github/workflows/deploy.yml`
  uses `lftp` over SFTP port 22. Mirror of the gnomon-website pattern.
  Three secrets in the repo: `IONOS_FTP_HOST`, `IONOS_FTP_USER`,
  `IONOS_FTP_PASS`. lftp uploads to `/` (chroot root IS `/Gubernis/`).
  Every push to `main` redeploys; a daily `0 5 * * *` UTC schedule also
  redeploys, so the Watch counter + "site snapshot" timestamp stay current
  without a push (landed 2026-05-26 via PR #1, commit `7882693`).
- Form: Formspree endpoint `https://formspree.io/f/xwvzopqy` wired into
  `#sign-up`. Submissions land in the Formspree dashboard and forward
  to Stephen's email. End-to-end tested 2026-05-21.
- Watch counter: **auto-patched at deploy time** from the live engine's
  public `/gubernis/watch-counter` endpoint (`scripts/patch_watch_counter.py`
  runs in the deploy workflow). Fail-soft — if the endpoint is
  unreachable, deploy proceeds with whatever numbers are baked into the
  repo. The numbers in `index.html` source are therefore stale by
  design; what's served is always fresh.
- HTTPS canonicalisation: `.htaccess` forces HTTPS + apex (strips
  `www.`). SSL cert provisioned via Let's Encrypt at IONOS.
- Samples: five Watch Forward sample dispatches live at `/samples/`.
  Marked explicitly as illustrative (commit `eae22ed` rewrote the
  earlier fabricated ambiguity flags after a traceability review —
  every claim now ties to a real ingest or primary source, or is
  labelled illustrative).
- Search engines: Google Search Console verified; sitemap
  (`/privacy/`, `/terms/`, `/samples/` included) submitted.
- Security disclosure: RFC 9116 `security.txt` published at
  `/.well-known/security.txt`.
- Legal floor: privacy notice at `/privacy/` (commit `903a11b`),
  subscription agreement at `/terms/` (commit `7ed2e81`). Footer
  carries Companies House No. 17207406 + ICO ZC134066 + Privacy +
  Terms links. Named contacts: `privacy@gubernis.com` (UK GDPR
  data-subject requests), `legal@gubernis.com` (legal notices,
  complaints). Watch Forward IP-protection clauses in §8 of the
  terms — named-seat enforcement, no verbatim client retransmission,
  no syndication, no derivative database, 1-yr confidentiality
  survival.

**Follow-ups worth doing when you pick this up:**

1. **Automate "Areas of focus this period" cards — LIVE end-to-end 2026-06-13.**
   Watch-counter numbers AND cards are now both auto-patched at
   deploy. The full loop is closed: Areas of Focus page in `/app` at
   `https://app.gnomon.info/app` (fifth tab, Basic auth interim) →
   operator picks 3 from engine candidates (or clicks *⚡ Propose three
   for me* for engine picks + brand-voice drafter summaries with
   identifier-grounding checks) → edits inline (autosave) → submits →
   `POST /gubernis/operator/cardsets/approve` writes a new approved
   cardset → `GET /gubernis/featured-cards` serves it → next push to
   `main` triggers `patch_featured_cards.py` in the deploy workflow
   (restored 2026-06-13 by `0eba0ab` — revert of yesterday's revert,
   safe now that the page produces fresh cardsets) → cards live on
   gubernis.com homepage. First end-to-end run verified 2026-06-13:
   `cardset-aof-2026-06-13-operator-a8bbb4` (3 cards, Steve-edited)
   landed on the live homepage. **Spec:**
   `hs-mvp/docs/gubernis/gubernis-areas-of-focus-page-spec.md`.

   **Wed 07:00 UTC approval email keeps the mobile path** —
   `[✓ Approve as-is]` still publishes via the signed-URL flow for
   travel/quick approves; the page owns the *refine before publish*
   path. Same publish target, two front doors.

   **Picker script** (`scripts/refresh_this_week_cards.py`) stays in
   the repo as a fallback for when the engine is unreachable, but the
   page is the primary workflow now. Worth retiring after a few weeks
   of clean Areas of Focus runs.

2. **Manual cards refresh in the meantime.** Until item 1 lands, run
   the picker weekly during the marketing push:

   ```
   cd gubernis-website
   python3 scripts/refresh_this_week_cards.py
   # — pick 3, write a sentence each, review with `git diff`
   git commit -am "this-week: refresh cards"
   git push    # → auto-deploys, picks up live Watch-counter too
   ```

   The script needs no env vars; the endpoint is public read-only.
   Defaults to 10 candidates from the last 7 days. Override with
   `--limit 20 --days 14` if the week was quiet.

3. **Legal stack — future work** (low urgency, the floor is laid):
   - **Informal lawyer-friend review.** Worth getting a sanity-check
     read-through from a UK B2B-SaaS lawyer-friend (NOT a billable
     engagement, per Stephen's in-house drafting discipline). Look
     specifically at the liability cap, governing law, and §8
     enforcement clauses.
   - **Data Processing Addendum (DPA).** Stub-referenced in §15 of
     the terms but not actually written. Only needed when a customer
     puts us in a processor relationship — i.e. they provide us
     personal data to process on their behalf. Today none of the
     tiers contemplate that.
   - **Acceptable Use Policy.** Currently the prohibitions live in
     §7 of terms. If the misuse landscape gets richer (e.g. specific
     scraping patterns emerge), break out into a separate AUP linked
     from §7.
   - ~~`security.txt`~~ — **DONE** (commit `9d272f8`). Published at
     `/.well-known/security.txt` per RFC 9116. The
     `security@gubernis.com` mailbox itself is still TBC.

4. **Doc-25 Workstream A — Tier 2 wave — DONE 2026-06-03.** The engine
   migrated off Railway (`pragticality-production.up.railway.app`) to the
   Mola IONOS VPS at the custom domain `app.gnomon.info`. All of this
   repo's engine callers were cut over together and now point at
   `app.gnomon.info`: `.github/workflows/deploy.yml` (`/gubernis/watch-counter`
   and `/gubernis/featured-cards` at every deploy), `scripts/patch_watch_counter.py`
   (endpoint passed by the workflow), `scripts/patch_featured_cards.py`
   (same), and `scripts/refresh_this_week_cards.py` (`DEFAULT_ENDPOINT` →
   `/gubernis/recent-changes`). No Railway hostnames remain in this repo.
   Background on the coordinated sequence: `pragticality/docs/state_of_codebase.md`
   Section 13 "Doc-25 Workstream A — Tier 2 wave".

5. **Pivot idea logged — real-time premium alert tier (2026-08-02).** Today
   the product is a *batch* cadence (weekly Friday dispatch + the homepage
   Areas-of-Focus sample). The idea: a **pay-extra tier that fires an
   immediate, retrieval-grounded (RAG) warning** when a change matching a
   paying customer's watch profile lands — the value bought is *time-to-know*,
   sharpening the kernel's "we're already telling you" from up-to-a-week to
   immediate. Engine-side is the primary work; the **canonical backlog entry
   lives in the Mola repo — `BACKLOG.md` → "◻ LATER — Real-time premium alert"**
   (trigger via the existing `matching.py`, grounding ladder gates it, never
   fire a fabricated alert). **Site-side consequences when it ships:** a new
   pay-extra tier row in `#pricing` and CTA/copy that names immediacy — but
   hold the credibility gate: don't sell it on the site until it demonstrably
   ships. Positioning/pricing detail → `pragticality-docs`.

---

## Where this repo sits

| | Location |
|---|---|
| This repo (the marketing site) | `gubernis-website/` |
| The engine | `pragticality/gubernis/` (on `main` as of 2026-05-21, commit `f73bf05`) |
| The strategic docs | `pragticality-docs/gubernis/` |
| The holding-co site (sibling) | `pragticality-website/` |
| The other product site (sibling) | `gnomon-website/` |

## How the site works

- Single-page HTML at `index.html`
- One stylesheet at `styles.css`
- Section anchors handle all in-page navigation
- No build step, no JavaScript framework
- Hostable anywhere static files run

## Deploying

Deploy is live and automated. Push to `main` → GitHub Actions
(`.github/workflows/deploy.yml`) runs lftp over SFTP to IONOS. See the
"What's wired up" section at the top for hosting / DNS / SFTP details.

What happens on each push:

1. Stage public files (`index.html`, `styles.css`, legal pages,
   `samples/`, `.well-known/`, sitemap, etc.) into `dist/`.
2. Patch the Watch counter in `dist/index.html` from the live engine's
   `/gubernis/watch-counter` endpoint (`scripts/patch_watch_counter.py`,
   fail-soft).
3. lftp mirror `dist/` to the IONOS chroot root (no `--delete` — manually
   placed files like Google verification HTML and Let's Encrypt
   challenges are left alone).

Search-engine and canonicalisation setup are already done:
- Google Search Console — verified (HTML file at repo root).
- Sitemap — `sitemap.xml` includes `/privacy/`, `/terms/`, `/samples/`.
- `.htaccess` — forces HTTPS, canonicalises `www.gubernis.com` → apex.

Outstanding deploy-adjacent items:
- Bing Webmaster Tools — set up via "Import from Google" (deferred).
- `Organization` JSON-LD in `<head>` — optional SEO refinement (deferred).

## What to do first when picking this up

1. **Read `README.md`** for the broader context — Gubernis as a product, the wedge → destination architecture, what this site is and isn't.
2. **Read `CLAUDE.md`** for the brand voice rules — what language is allowed, what's forbidden, what register to write in.
3. **Open `index.html` in a browser** to see the current state. Three things to check first:
   - The Watch counter — is it showing reasonable numbers or are they obviously stale?
   - The "Areas of focus this period" cards — are the dates current?
   - The Ambiguity Watch section copy — does it still read as sharp, or has it drifted toward generic SaaS?
4. **Check open decisions** at the bottom of `CLAUDE.md` — most are still unresolved as of the initial commit.

## Common edits and how to make them safely

### Refreshing the Watch counter

Don't. It's auto-patched at deploy time from the live engine's public
`/gubernis/watch-counter` endpoint (`scripts/patch_watch_counter.py`,
called from the deploy workflow). The numbers in `index.html` source
are intentionally stale; what's served is fresh on every push.

If the deployed numbers look wrong, debug the endpoint, not the HTML:
```
curl -s https://app.gnomon.info/gubernis/watch-counter | python3 -m json.tool
```

### Refreshing the "Areas of focus this period" cards

Currently manual / editorial. Use the picker:

```
cd gubernis-website
python3 scripts/refresh_this_week_cards.py
# — pick 3, write a sentence each, review with `git diff`
git commit -am "this-week: refresh cards"
git push    # → auto-deploys, picks up live Watch-counter too
```

The script fetches from `/gubernis/recent-changes` (public, no auth).
Defaults to 10 candidates from the last 7 days; override with
`--limit 20 --days 14` if the week was quiet.

Per `feedback_dispatch_traceability.md`, summary copy must tie to the
real ingest — no fabricated specifics. The script's interactive prompt
makes this explicit ("editorial pick step" is the whole point of
keeping it human).

Automation of this step is a stated goal — see follow-up #1 at the
top of this file.

### Adding a new section

1. Sketch in `pragticality-docs/strategic_package/website/gubernis-brand-direction.html` first
2. Port to `index.html` once the design is stable
3. Add styles to `styles.css` (single shared stylesheet, no per-page styles)
4. Add anchor link to the `site-nav` if it's a major section

### Adjusting pricing tiers

Pricing is in the `.pricing-grid` section. **Five tiers** (as of
2026-05-24): Free Watch (£0) / Starter (£200) / Pro (£800) /
**Watch Forward (£1,800)** / Enterprise (£30k+/yr). The Ambiguity
Watch sits in Pro as the upgrade gate; Watch Forward adds
pipeline-tracking on top. Watch Forward at £21,600/yr sits ~£3.4k
under the £25k procurement-threshold from
`feedback_procurement_threshold_pricing.md` — adding features that
push the price up risks crossing into procurement-friction land.

## What this session is NOT for

- Implementing the engine — that's the `pragticality` repo, on `main`
  branch (in `gubernis/`).
- Strategic direction — that's `pragticality-docs/gubernis/`.
- Building a blog / multi-page expansion — deferred until V1 is validated.
- Adding tracking / analytics without explicit privacy review.
- Anything that adds JavaScript frameworks or a build step.

## Auto-memory rules that apply here

If you're Claude Code, the following auto-memory entries are load-bearing for this repo:

- `feedback_gubernis_customer_copy.md` — never describe mechanism in customer copy
- `feedback_marketing_claim_defensibility.md` — no unsupported competitive claims
- `feedback_dispatch_traceability.md` — no fabricated specifics in cards / Watch Forward dispatches; every claim cites engine ingest or primary source
- `feedback_procurement_threshold_pricing.md` — keep wedge-tier annual spend below £25k
- `feedback_gubernis_scope_discipline.md` — goods-affecting regulation only; not insurance, sales tax, freight
- `feedback_drive_terminal_ops.md` — drive multi-step terminal work via Bash tool, don't paste copy-paste lists
- `feedback_ground_rules.md` — ask before push / deploy / delete

## Pairs with

- `README.md` (this repo)
- `CLAUDE.md` (this repo)
- `pragticality-docs/gubernis/06_brand_direction.md` (the brand spec)
- `pragticality-docs/gubernis/05_product_thesis.md` (the product thesis)
- `pragticality-website/SESSION_START.md` (the sibling site's session-start; similar structure)
