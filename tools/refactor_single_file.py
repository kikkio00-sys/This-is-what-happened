#!/usr/bin/env python3
"""Split the oversized self-contained homepage into maintainable source files.

The script is intentionally conservative:
- it only rewrites the root index.html;
- it extracts embedded CSS and inline JavaScript into styles.css and app.js;
- it decodes embedded image data URIs into assets/embedded-* files;
- it applies the approved visitor-facing labels and homepage family selector;
- it leaves internal room keys, routes, biography pages, and other files untouched.
"""

from __future__ import annotations

import base64
import hashlib
import re
from pathlib import Path
from urllib.parse import unquote_to_bytes

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
CSS = ROOT / "styles.css"
JS = ROOT / "app.js"
ASSETS = ROOT / "assets"

STYLE_RE = re.compile(r"<style(?:\s[^>]*)?>(.*?)</style>", re.IGNORECASE | re.DOTALL)
SCRIPT_RE = re.compile(r"<script(?![^>]*\bsrc=)(?:\s[^>]*)?>(.*?)</script>", re.IGNORECASE | re.DOTALL)
DATA_URI_RE = re.compile(
    r"data:image/(?P<kind>png|jpe?g|gif|webp|svg\+xml)"
    r"(?P<meta>(?:;[^,\"')>]*)?),(?P<data>[^\"')>]+)",
    re.IGNORECASE,
)

FAMILY_MAP_MARKUP = """
<section class="family-map" aria-labelledby="family-map-title">
  <p id="family-map-title" class="family-map-title">Choose a family line</p>
  <div class="family-map-stage" role="group" aria-label="Four family lines">
    <button type="button" class="family-map-branch" data-map-family="Zahner">Zahner</button>
    <button type="button" class="family-map-branch" data-map-family="Downing">Downing</button>
    <button type="button" class="family-map-branch" data-map-family="Blackwell">Blackwell</button>
    <button type="button" class="family-map-branch" data-map-family="Barrett">Barrett</button>
    <p class="family-map-root">One archive · four family lines.</p>
  </div>
</section>
""".strip()

FAMILY_MAP_CSS = r"""

/* Homepage family-map invitation */
.family-map{width:min(100%,620px);margin:0 auto 10px}
.family-map-title{margin:0 0 7px;text-align:center;color:var(--gold2);font:700 9px/1.2 system-ui;letter-spacing:.16em;text-transform:uppercase}
.family-map-stage{position:relative;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:7px;padding:24px 9px 38px;border:1px solid var(--line);border-radius:16px;background:radial-gradient(circle at 50% 115%,rgba(195,152,80,.2),transparent 45%),linear-gradient(180deg,#1a120d,#0c0907);overflow:hidden}
.family-map-stage:before{content:"";position:absolute;left:12.5%;right:12.5%;bottom:28px;height:1px;background:var(--gold)}
.family-map-stage:after{content:"";position:absolute;left:50%;bottom:10px;width:1px;height:19px;background:var(--gold)}
.family-map-branch{position:relative;z-index:1;min-height:42px;border:1px solid currentColor;border-radius:999px;background:#17110d;padding:8px 4px;color:var(--cream);font-size:clamp(9px,2.5vw,12px);cursor:pointer}
.family-map-branch:after{content:"";position:absolute;left:50%;top:100%;width:1px;height:18px;background:var(--gold)}
.family-map-branch:nth-of-type(1){color:var(--blue)}
.family-map-branch:nth-of-type(2){color:var(--green)}
.family-map-branch:nth-of-type(3){color:var(--red)}
.family-map-branch:nth-of-type(4){color:var(--amber)}
.family-map-branch:hover,.family-map-branch:focus-visible{background:#2a1c13;transform:translateY(-1px);outline:2px solid var(--gold2);outline-offset:2px}
.family-map-root{position:absolute;left:0;right:0;bottom:5px;margin:0;text-align:center;color:var(--gold2);font:italic 10px/1.2 Georgia,serif}
@media(max-width:430px){.family-map-stage{gap:4px;padding-left:5px;padding-right:5px}.family-map-branch{font-size:8px;padding:7px 2px}}
"""

FAMILY_MAP_JS = r"""

// Homepage family-map invitation: reuse the existing family navigation behavior.
document.querySelectorAll("[data-map-family]").forEach((button) => {
  button.addEventListener("click", () => {
    const family = button.dataset.mapFamily;
    const target = [...document.querySelectorAll(".family-line [data-family]")]
      .find((candidate) => candidate.dataset.family === family);
    if (target) target.click();
  });
});
"""


def decode_data_uri(match: re.Match[str]) -> str:
    kind = match.group("kind").lower()
    meta = (match.group("meta") or "").lower()
    encoded = match.group("data").strip()

    try:
        if ";base64" in meta:
            raw = re.sub(r"\s+", "", encoded)
            raw += "=" * (-len(raw) % 4)
            payload = base64.b64decode(raw, validate=False)
        else:
            payload = unquote_to_bytes(encoded)
    except Exception as exc:
        preview = encoded[:80].replace("\n", " ")
        raise RuntimeError(
            f"Could not decode embedded image ({kind}{meta}); payload begins {preview!r}"
        ) from exc

    if not payload:
        raise RuntimeError(f"Embedded {kind} image near character {match.start()} decoded to zero bytes.")

    digest = hashlib.sha256(payload).hexdigest()[:12]
    extension = {"jpeg": "jpg", "jpg": "jpg", "svg+xml": "svg"}.get(kind, kind)
    ASSETS.mkdir(parents=True, exist_ok=True)
    relative = Path("assets") / f"embedded-{digest}.{extension}"
    destination = ROOT / relative
    if not destination.exists():
        destination.write_bytes(payload)
    return relative.as_posix()


def insert_family_map(html: str) -> str:
    if 'class="family-map"' in html:
        return html
    nav = re.search(r"(<nav\b[^>]*class=[\"'][^\"']*\bfamily-line\b[^\"']*[\"'][^>]*>.*?</nav>)", html, re.IGNORECASE | re.DOTALL)
    if not nav:
        raise RuntimeError("Could not locate the existing family-line navigation.")
    return html[: nav.end()] + "\n" + FAMILY_MAP_MARKUP + html[nav.end() :]


def main() -> None:
    original = INDEX.read_text(encoding="utf-8")
    html = original.replace("\r\n", "\n")

    styles = STYLE_RE.findall(html)
    scripts = SCRIPT_RE.findall(html)
    if not styles:
        raise RuntimeError("No embedded <style> block found; refusing to rewrite.")
    if not scripts:
        raise RuntimeError("No inline <script> block found; refusing to rewrite.")

    css = "\n\n".join(part.strip() for part in styles if part.strip())
    js = "\n\n".join(part.strip() for part in scripts if part.strip())

    html = DATA_URI_RE.sub(decode_data_uri, html)
    css = DATA_URI_RE.sub(decode_data_uri, css)
    js = DATA_URI_RE.sub(decode_data_uri, js)

    html = STYLE_RE.sub("", html)
    html = SCRIPT_RE.sub("", html)
    if 'href="styles.css"' not in html:
        html = html.replace("</head>", '  <link rel="stylesheet" href="styles.css">\n</head>', 1)
    if 'src="app.js"' not in html:
        html = html.replace("</body>", '  <script src="app.js"></script>\n</body>', 1)

    html = html.replace("Family Assembly", "Meet the Family").replace("Album", "Photographs")
    js = js.replace("Family Assembly", "Meet the Family").replace("Album", "Photographs")

    html = insert_family_map(html)
    if "Homepage family-map invitation" not in css:
        css = css.rstrip() + FAMILY_MAP_CSS
    if "data-map-family" not in js:
        js = js.rstrip() + FAMILY_MAP_JS

    html = re.sub(r"\n{3,}", "\n\n", html).strip() + "\n"
    css = css.strip() + "\n"
    js = js.strip() + "\n"

    INDEX.write_text(html, encoding="utf-8", newline="\n")
    CSS.write_text(css, encoding="utf-8", newline="\n")
    JS.write_text(js, encoding="utf-8", newline="\n")

    remaining = []
    for path in (INDEX, CSS, JS):
        if "data:image/" in path.read_text(encoding="utf-8"):
            remaining.append(path.name)
    if remaining:
        raise RuntimeError(f"Embedded image data remains in: {', '.join(remaining)}")
    if INDEX.stat().st_size > 1_000_000:
        raise RuntimeError(f"index.html is still unexpectedly large: {INDEX.stat().st_size} bytes")

    print(f"index.html: {INDEX.stat().st_size:,} bytes")
    print(f"styles.css: {CSS.stat().st_size:,} bytes")
    print(f"app.js: {JS.stat().st_size:,} bytes")
    print(f"extracted assets: {len(list(ASSETS.glob('embedded-*')))}")


if __name__ == "__main__":
    main()
