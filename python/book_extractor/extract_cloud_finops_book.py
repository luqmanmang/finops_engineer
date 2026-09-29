#!/usr/bin/env python3
"""Build copyright-safe Markdown research scaffolds from an EPUB.

The extractor intentionally does NOT copy chapter body text. It preserves only
metadata, chapter/section titles, structural locators, and quantitative metadata
(word counts). The generated files are designed as a source-of-truth scaffold
for human/model-authored derived notes.
"""
from __future__ import annotations

import argparse
import base64
import csv
import gzip
import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def clean_text(text: str | None) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def element_text(el: ET.Element) -> str:
    return clean_text(" ".join(t for t in el.itertext()))


def slugify(text: str) -> str:
    text = text.lower().replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "chapter"


def read_xml(zf: zipfile.ZipFile, name: str) -> ET.Element:
    return ET.fromstring(zf.read(name))


def find_rootfile(zf: zipfile.ZipFile) -> str:
    root = read_xml(zf, "META-INF/container.xml")
    for el in root.iter():
        if local_name(el.tag) == "rootfile":
            path = el.attrib.get("full-path")
            if path:
                return path
    raise RuntimeError("EPUB rootfile not found")


def parse_metadata(zf: zipfile.ZipFile, opf_path: str) -> dict[str, str]:
    root = read_xml(zf, opf_path)
    values: dict[str, str] = {}
    wanted = {"title", "creator", "publisher", "date", "identifier", "language"}
    for el in root.iter():
        name = local_name(el.tag)
        if name in wanted and name not in values:
            value = element_text(el)
            if value:
                values[name] = value
    return values


def chapter_files(zf: zipfile.ZipFile) -> list[str]:
    names = [n for n in zf.namelist() if re.search(r"(?:^|/)ch\d{2}\.xhtml$", n)]
    return sorted(names, key=lambda n: int(re.search(r"ch(\d{2})\.xhtml$", n).group(1)))


def parse_chapter(zf: zipfile.ZipFile, name: str, number: int) -> dict:
    root = read_xml(zf, name)
    headings: list[dict[str, str | int]] = []
    body_words: list[str] = []
    for el in root.iter():
        lname = local_name(el.tag).lower()
        txt = element_text(el)
        if lname in {"h1", "h2", "h3", "h4", "h5", "h6"} and txt:
            headings.append({"level": int(lname[1]), "title": txt, "anchor": el.attrib.get("id", "")})
        if lname in {"p", "li", "td", "th", "blockquote"} and txt:
            body_words.extend(re.findall(r"\b\w+[\w’'/-]*\b", txt, flags=re.UNICODE))
    title = next((str(h["title"]) for h in headings if h["level"] == 1), None)
    if not title:
        title = next((str(h["title"]) for h in headings), f"Chapter {number}")
    return {
        "number": number,
        "source_file": name,
        "title": title,
        "slug": slugify(title),
        "word_count": len(body_words),
        "headings": headings,
    }


def scaffold_text(ch: dict) -> str:
    outline = []
    for h in ch["headings"]:
        indent = "  " * max(int(h["level"]) - 2, 0)
        anchor = f"#{h['anchor']}" if h["anchor"] else ""
        outline.append(f"{indent}- {h['title']}  `[{ch['source_file']}{anchor}]`")
    outline_text = "\n".join(outline) if outline else "- No heading structure detected."
    return f"""# Chapter {ch['number']:02d} — {ch['title']}

> **Role:** Derived textbook source-of-truth note.  
> **Book source locator:** `{ch['source_file']}`  
> **Source word count:** {ch['word_count']:,}  
> **Copyright boundary:** This note records structure and derived analysis; it does not reproduce the chapter body.

## 1. Chapter Brief

_TODO — explain the chapter's purpose, scope, and why it matters to a FinOps Engineer._

## 2. Why This Chapter Matters

_TODO — connect the chapter to operational/business decisions._

## 3. Source Section Map

{outline_text}

## 4. Core Concepts

_TODO — derived concept definitions, relationships, terminology, and mental models._

## 5. Detailed Explanation

_TODO — explain each major section in your own words, preserving the source's organization and intent._

## 6. Examples

_TODO — paraphrase source examples where useful, then add clearly labelled project examples._

## 7. Justification / Why the Approach Works

_TODO — why the book recommends or motivates the approach; separate source-derived rationale from project analysis._

## 8. Senior FinOps Approach

_TODO — how a senior IC should frame the decision before acting._

## 9. Step-by-Step Execution

```text
CONTEXT
→ BUSINESS QUESTION
→ DATA REQUIRED
→ HYPOTHESIS
→ ANALYSIS
→ OPTIONS
→ DECISION
→ IMPLEMENTATION
→ TECHNICAL VALIDATION
→ FINANCIAL VALIDATION
→ BUSINESS / SLA VALIDATION
→ GUARDRAIL
```

_TODO — specialize this sequence for the chapter._

## 10. Decision Rules

_TODO — when to use approach A/B, thresholds, escalation criteria, and decision ownership._

## 11. Trade-offs

_TODO — cost, performance, reliability, SLA, speed, lock-in, and organizational trade-offs._

## 12. Failure Modes / Edge Cases

_TODO — common mistakes, ambiguous cases, and conditions where the chapter's default approach may fail._

## 13. Data Required

_TODO — cost, usage, pricing, ownership, utilization, business-driver, contract, and operational data._

## 14. SQL / Python / IaC Application

_TODO — analyses and automation that belong in SQL, Python, Terraform/CI/CD, or are not applicable._

## 15. Provider Implementation

### AWS
_TODO_

### Azure
_TODO_

### Microsoft Fabric
_TODO where relevant_

### Snowflake
_TODO where relevant_

### Databricks
_TODO where relevant_

## 16. Stakeholder Perspective

- Engineering — _TODO_
- Finance — _TODO_
- Procurement — _TODO_
- Leadership / Business — _TODO_
- FinOps — _TODO_

## 17. Validation

- Technical validation — _TODO_
- Financial validation — _TODO_
- Business / SLA validation — _TODO_

## 18. KPIs

_TODO — metrics that prove progress/outcome, including denominator and grain._

## 19. Guardrails

- Preventive — _TODO_
- Detective — _TODO_
- Corrective — _TODO_

## 20. Real-World Implications

_TODO — connect to Grade A/B cases without inventing undisclosed company behavior._

## 21. FinOps Framework 2026 Reconciliation

_TODO — mark concepts as CURRENT / EVOLVED / SUPERSEDED / NEEDS RECONCILIATION._

## 22. Malaysia N=7 Market Relevance

_TODO — map only to verified vacancy signals; retain N=7 limitation._

## 23. Lab Mapping

_TODO — lab(s), synthetic fault(s), expected evidence, teardown/cost controls._

## 24. Power BI Mapping

_TODO — Diagnose → Hypothesis → Finding → Solution → Validation → Insight views/measures._

## 25. Interview Mapping

### 30-second answer
_TODO_

### 2-minute answer
_TODO_

### Senior follow-up
_TODO — WHAT / WHY / WHEN / HOW / TRADEOFF / VALIDATION / BUSINESS IMPACT._

## 26. Key Takeaways

_TODO — concise derived takeaways._

## 27. Source Locator

- EPUB file: `{ch['source_file']}`
- Section headings and anchors are preserved above for traceability.
- Body text is intentionally not copied into this repository artifact.
"""


def write_outputs_from_manifest(manifest: dict, out: Path) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    chapters_dir = out / "chapters"
    chapters_dir.mkdir(exist_ok=True)
    for stale in chapters_dir.glob("*.md"):
        stale.unlink()
    chapters = manifest["chapters"]
    meta = manifest.get("metadata", {})
    (out / "book_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    with (out / "chapter_index.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["chapter", "title", "source_file", "word_count", "section_count", "markdown_file"])
        for ch in chapters:
            md_name = f"{ch['number']:02d}_{ch['slug']}.md"
            w.writerow([ch["number"], ch["title"], ch["source_file"], ch["word_count"], len(ch["headings"]), f"chapters/{md_name}"])
            (chapters_dir / md_name).write_text(scaffold_text(ch), encoding="utf-8")
    title = meta.get("title", "Cloud FinOps")
    inventory = [f"# {title} — Book Source of Truth", "", "> Canonical textbook-layer inventory generated from the owned EPUB structure. Chapter body text is not reproduced.", "", "## Metadata", ""]
    for key in ["title", "creator", "publisher", "date", "identifier", "language"]:
        inventory.append(f"- **{key.title()}:** {meta.get(key, 'Not detected')}")
    inventory += ["", "## Coverage", "", f"- Chapters detected: **{len(chapters)}**", f"- Approximate chapter-body words indexed: **{manifest.get('total_words', 0):,}**", "", "## Chapters", "", "| # | Chapter | Words | Sections | Note |", "|---:|---|---:|---:|---|"]
    for ch in chapters:
        md_name = f"{ch['number']:02d}_{ch['slug']}.md"
        inventory.append(f"| {ch['number']} | {ch['title']} | {ch['word_count']:,} | {len(ch['headings'])} | [`{md_name}`](chapters/{md_name}) |")
    inventory += ["", "## Source-of-truth hierarchy", "", "```text", "FINOPS_ENGINEERING_FIELD_LAB_SOURCE_OF_TRUTH", "  └─ textbook layer", "      └─ BOOK_SOURCE_OF_TRUTH / chapter notes", "          └─ source locator → owned EPUB", "```", "", "The project master source of truth controls scope, evidence rules, completion gates and market constraints. These files are canonical only for the textbook layer."]
    (out / "BOOK_SOURCE_OF_TRUTH.md").write_text("\n".join(inventory) + "\n", encoding="utf-8")
    return manifest


def write_outputs(epub: Path, out: Path) -> dict:
    with zipfile.ZipFile(epub) as zf:
        opf = find_rootfile(zf)
        meta = parse_metadata(zf, opf)
        chapters = [parse_chapter(zf, name, i + 1) for i, name in enumerate(chapter_files(zf))]
    manifest = {"metadata": meta, "chapter_count": len(chapters), "total_words": sum(ch["word_count"] for ch in chapters), "chapters": chapters}
    return write_outputs_from_manifest(manifest, out)


def load_manifest_b64_gzip(path: Path) -> dict:
    raw = base64.b64decode(path.read_text(encoding="ascii"))
    return json.loads(gzip.decompress(raw).decode("utf-8"))


def main() -> None:
    p = argparse.ArgumentParser()
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--epub", type=Path)
    src.add_argument("--manifest-b64-gzip", type=Path)
    p.add_argument("--out", type=Path, default=Path("research/books/cloud_finops_2e"))
    p.add_argument("--expect-chapters", type=int, default=27)
    args = p.parse_args()
    manifest = write_outputs(args.epub, args.out) if args.epub else write_outputs_from_manifest(load_manifest_b64_gzip(args.manifest_b64_gzip), args.out)
    if len(manifest["chapters"]) != args.expect_chapters:
        raise SystemExit(f"Expected {args.expect_chapters} chapters, found {len(manifest['chapters'])}")
    print(f"Generated {len(manifest['chapters'])} chapter scaffolds in {args.out}")


if __name__ == "__main__":
    main()
