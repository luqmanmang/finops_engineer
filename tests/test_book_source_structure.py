from __future__ import annotations

import base64
import csv
import gzip
import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
BOOK_DIR = REPO_ROOT / "research" / "books" / "cloud_finops_2e"
SOURCE = BOOK_DIR / "source" / "book_structure.json.gz.b64"


class BookSourceStructureTests(unittest.TestCase):
    def load_manifest(self) -> dict:
        raw = base64.b64decode(SOURCE.read_text(encoding="ascii"))
        return json.loads(gzip.decompress(raw).decode("utf-8"))

    def chapter_files(self) -> list[Path]:
        return sorted((BOOK_DIR / "chapters").glob("*.md"))

    def test_owned_book_structure_has_27_chapters(self) -> None:
        manifest = self.load_manifest()
        self.assertEqual(27, manifest["chapter_count"])
        self.assertEqual(27, len(manifest["chapters"]))

    def test_expected_key_chapters_are_present(self) -> None:
        titles = [c["title"] for c in self.load_manifest()["chapters"]]
        required = [
            "What Is FinOps?",
            "Anatomy of the Cloud Bill",
            "Accurate Forecasting",
            "Using Less",
            "Paying Less",
            "Commitment-Based Discount",
            "Automating Cost Management",
            "Metric-Driven Cost Optimization",
            "FinOps for the Container World",
            "Partnering with Engineers",
            "Data-Driven Decision Making",
            "Secret Ingredient",
        ]
        joined = "\n".join(titles)
        for phrase in required:
            self.assertIn(phrase, joined)

    def test_all_27_chapter_notes_are_completed(self) -> None:
        chapter_files = self.chapter_files()
        self.assertEqual(27, len(chapter_files))

        semantic_anchors = [
            "Chapter Brief",
            "Why This Chapter Matters",
            "Source Section Map",
            "Core Concepts",
            "Detailed Explanation",
            "Examples",
            "Justification",
            "Senior FinOps Approach",
            "Step-by-Step Execution",
            "Decision Rules",
            "Trade-offs",
            "Failure Modes",
            "Data Required",
            "SQL / Python / IaC",
            "Provider Implementation",
            "Stakeholder Perspective",
            "Validation",
            "KPIs",
            "Guardrails",
            "Real-World Implications",
            "FinOps Framework 2026 Reconciliation",
            "Malaysia N=7 Market Relevance",
            "Lab Mapping",
            "Power BI Mapping",
            "Interview Mapping",
            "Key Takeaways",
            "Source Locator",
        ]

        forbidden_markers = ["_TODO", "TODO —", "TODO_"]

        for path in chapter_files:
            text = path.read_text(encoding="utf-8")
            self.assertGreater(
                len(text),
                5000,
                f"{path.name} is too small to satisfy the detailed chapter-note contract",
            )

            # Enforce all 27 numbered learning-contract sections while allowing
            # minor title wording differences such as 'Justification' vs
            # 'Justification / Why the Approach Works'.
            for section_number in range(1, 28):
                self.assertIn(
                    f"## {section_number}.",
                    text,
                    f"{path.name} missing numbered section {section_number}",
                )

            for anchor in semantic_anchors:
                self.assertIn(anchor, text, f"{path.name} missing semantic anchor {anchor}")

            for marker in forbidden_markers:
                self.assertNotIn(marker, text, f"{path.name} still contains placeholder {marker}")

            self.assertIn("OEBPS/ch", text, f"{path.name} missing EPUB source locator")
            self.assertIn(
                "Source",
                text,
                f"{path.name} missing an explicit source/source-boundary marker",
            )

    def test_chapter_index_matches_generated_files(self) -> None:
        with (BOOK_DIR / "chapter_index.csv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(27, len(rows))
        for row in rows:
            self.assertTrue((BOOK_DIR / row["markdown_file"]).exists())


if __name__ == "__main__":
    unittest.main()
