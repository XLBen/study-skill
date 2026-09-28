#!/usr/bin/env python3
"""Extract figures from a PDF into PNG files (no vision required).

Three-tier strategy per page:
  1. Embedded raster images  — extracted as-is (best quality when present).
  2. Vector figure region    — cluster vector-drawing bounding boxes, grow to
                               nearby text (axis labels) while excluding the
                               caption line, optionally anchored to a caption
                               like "Figure 3.6"; render the clipped region.
  3. Full-page render        — fallback (also used when one cluster covers
                               most of the page, e.g. one-figure slides).

Usage:
  python3 extract_figures.py file.pdf --pages 29,32 [--caption "Figure 3.6"] \
      [--out assets/my-note] [--dpi 200]

Prints one line per saved image: path, source page, strategy, crop rectangle.
Requires PyMuPDF:  pip3 install pymupdf   (or --break-system-packages).
"""
import argparse
import sys
from pathlib import Path

try:
    import pymupdf
except ImportError:
    try:
        import fitz as pymupdf
    except ImportError:
        sys.exit("error: PyMuPDF not installed. Try: pip3 install pymupdf")

PAD = 4          # padding around a vector cluster (points)
GROW = 18        # how far text blocks may stick into the region to be absorbed
MIN_AREA = 800   # ignore clusters smaller than this (points^2)
FULL_PAGE_RATIO = 0.72  # largest cluster area / page area above which we render full page


def is_furniture(rect, page):
    """Full-width thin bands are page furniture (slide header/footer bars)."""
    return rect.height < 40 and rect.width > 0.8 * page.rect.width


def cluster_rects(rects, gap=12):
    """Union-find clustering of rects by proximity."""
    boxes = [pymupdf.Rect(r) for r in rects]
    changed = True
    while changed:
        changed = False
        out = []
        for b in boxes:
            merged = False
            for i, o in enumerate(out):
                inflated = pymupdf.Rect(o.x0 - gap, o.y0 - gap, o.x1 + gap, o.y1 + gap)
                if inflated.intersects(b):
                    out[i] = o | b
                    merged = True
                    changed = True
                    break
            if not merged:
                out.append(pymupdf.Rect(b))
        boxes = out
    return boxes


def text_blocks(page):
    blocks = []
    for b in page.get_text("blocks"):
        rect, text = pymupdf.Rect(b[:4]), (b[4] or "").strip()
        if text:
            blocks.append((rect, text))
    return blocks


def is_caption(text):
    t = text.lstrip()
    return t.startswith(("Figure", "Fig.", "图", "Table", "表"))


def grow_with_labels(cluster, blocks):
    """Absorb text blocks that overlap the cluster margin (axis labels),
    but never absorb caption-style blocks or page furniture."""
    rect = pymupdf.Rect(cluster)
    margin = pymupdf.Rect(rect.x0 - GROW, rect.y0 - GROW, rect.x1 + GROW, rect.y1 + GROW)
    for trect, text in blocks:
        if is_caption(text) or len(text) > 300:
            continue
        center = ((trect.x0 + trect.x1) / 2, (trect.y0 + trect.y1) / 2)
        if margin.contains(center):
            rect = rect | trect
    return rect


def save(pix, path):
    pix.save(path)
    return path


def extract_page(page, pno, outdir, dpi, caption):
    results = []
    mat = pymupdf.Matrix(dpi / 72, dpi / 72)

    # tier 1: embedded rasters
    for i, img in enumerate(page.get_images(full=True)):
        try:
            pix = pymupdf.Pixmap(page.parent, img[0])
            if pix.n - pix.alpha >= 4:
                pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
            path = outdir / f"p{pno}-img{i}.png"
            save(pix, path)
            results.append((path, "embedded raster", "-"))
        except Exception as exc:  # noqa: BLE001
            print(f"  p{pno}: raster {i} failed: {exc}", file=sys.stderr)
    if results:
        return results

    # tier 2: vector regions (portrait pages, i.e. book-style layouts;
    # landscape slide pages render full-page in tier 3 unless captioned)
    drawings = page.get_drawings()
    is_slide = page.rect.width > page.rect.height
    if drawings and not (is_slide and not caption):
        blocks = text_blocks(page)
        clusters = [
            c for c in cluster_rects([d["rect"] for d in drawings])
            if abs(c) >= MIN_AREA and not is_furniture(c, page)
        ]
        if clusters:
            clusters.sort(key=lambda c: abs(c), reverse=True)
            page_area = abs(page.rect)
            if abs(clusters[0]) / page_area >= FULL_PAGE_RATIO:
                pass  # fall through to full page
            else:
                if caption:
                    hits = page.search_for(caption)
                    if hits:
                        anchor = hits[0]

                        def dist(c):
                            if c.y1 <= anchor.y0:
                                dy = anchor.y0 - c.y1
                            elif c.y0 >= anchor.y1:
                                dy = c.y0 - anchor.y1
                            else:
                                dy = 0
                            dx = max(0.0, c.x0 - anchor.x1, anchor.x0 - c.x1)
                            return dy + dx

                        clusters.sort(key=dist)
                    else:
                        print(f"  p{pno}: caption {caption!r} not found; using largest cluster",
                              file=sys.stderr)
                picked = clusters[:1] if caption else clusters[:3]
                for j, cl in enumerate(picked):
                    region = grow_with_labels(cl, blocks)
                    region = pymupdf.Rect(region.x0 - PAD, region.y0 - PAD,
                                          region.x1 + PAD, region.y1 + PAD) & page.rect
                    pix = page.get_pixmap(matrix=mat, clip=region)
                    path = outdir / f"p{pno}-vec{j}.png"
                    save(pix, path)
                    results.append((path, "vector region",
                                    f"({region.x0:.0f},{region.y0:.0f})-({region.x1:.0f},{region.y1:.0f})"))
                if results:
                    return results

    # tier 3: full page
    pix = page.get_pixmap(matrix=mat)
    path = outdir / f"p{pno}.png"
    save(pix, path)
    return [(path, "full page", f"{pix.width}x{pix.height}")]


def main():
    ap = argparse.ArgumentParser(description="Extract figures from a PDF (no vision needed).")
    ap.add_argument("pdf", help="source PDF path")
    ap.add_argument("--pages", required=True, help="comma-separated 1-based page numbers")
    ap.add_argument("--caption", default=None,
                    help='caption text to anchor the figure, e.g. "Figure 3.6"')
    ap.add_argument("--out", default="figures", help="output directory (created if missing)")
    ap.add_argument("--dpi", type=int, default=200)
    args = ap.parse_args()

    src = Path(args.pdf)
    if not src.is_file():
        sys.exit(f"error: no such file: {src}")
    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)

    doc = pymupdf.open(src)
    for pno in (int(x) for x in args.pages.split(",") if x.strip()):
        if not 1 <= pno <= doc.page_count:
            print(f"p{pno}: out of range (1-{doc.page_count}), skipped", file=sys.stderr)
            continue
        for path, strategy, rect in extract_page(doc[pno - 1], pno, outdir, args.dpi, args.caption):
            print(f"saved {path}  <-  p.{pno}  [{strategy}]  rect={rect}")


if __name__ == "__main__":
    main()
