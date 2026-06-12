"""Patch the homepage featured-cards block with the latest APPROVED cardset.

Runs in the gubernis-website deploy after index.html is staged into dist/.
Fetches the Mola engine's /gubernis/featured-cards endpoint — the cards from
the most recent cardset the reviewer approved via the weekly email — and
substitutes them into the featured-cards block. This is the publish step of
publish-on-approval: approve in the email -> cards go live on next deploy.

Fail-soft (same posture as patch_watch_counter.py): if the endpoint is
unreachable, returns no approved cards, or the markers are missing, print a
warning and exit 0 so the deploy proceeds with whatever cards are already in
the file. A stale-but-deployed homepage beats a failed deploy.

Usage:
    python3 scripts/patch_featured_cards.py \\
        --endpoint https://app.gnomon.info/gubernis/featured-cards \\
        --html dist/index.html
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request

START = "<!-- featured-cards: start (managed by scripts/refresh_this_week_cards.py) -->"
END = "<!-- featured-cards: end -->"


def fetch(endpoint: str, timeout: float = 15.0):
    try:
        req = urllib.request.Request(endpoint, headers={"User-Agent": "gubernis-website-deploy"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError) as e:
        print(f"[featured-cards] endpoint unreachable/invalid ({e}); leaving existing cards.",
              file=sys.stderr)
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Patch homepage cards from the approved cardset.")
    parser.add_argument("--endpoint", required=True,
                        help="URL of /gubernis/featured-cards on the Mola engine")
    parser.add_argument("--html", default="index.html")
    parser.add_argument("--timeout", type=float, default=15.0)
    args = parser.parse_args()

    data = fetch(args.endpoint, timeout=args.timeout)
    if not data:
        return 0
    cards_html = (data.get("cards_html") or "").strip()
    if not cards_html:
        print(f"[featured-cards] no approved cards to publish (status: {data.get('status')}); "
              "leaving existing cards.", file=sys.stderr)
        return 0

    try:
        with open(args.html, encoding="utf-8") as fh:
            html = fh.read()
    except FileNotFoundError:
        print(f"[featured-cards] {args.html} not found; nothing to patch.", file=sys.stderr)
        return 0

    start_idx = html.find(START)
    end_idx = html.find(END, start_idx + 1 if start_idx >= 0 else 0)
    if start_idx < 0 or end_idx < 0:
        print("[featured-cards] start/end markers not found in HTML; leaving file unchanged.",
              file=sys.stderr)
        return 0

    new_html = (
        html[: start_idx + len(START)]
        + "\n\n" + cards_html + "\n\n      "
        + html[end_idx:]
    )
    with open(args.html, "w", encoding="utf-8") as fh:
        fh.write(new_html)
    print(f"[featured-cards] published {data.get('count')} cards from "
          f"{data.get('cardset_id')} (approved {data.get('approved_at')}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
