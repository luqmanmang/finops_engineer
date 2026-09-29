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

        required_sections = [
            "## 1. Chapter Brief",
            "## 2. Why This Chapter Matters",
            "## 3. Source Section Map",
            "## 4. Core Concepts",
            "## 5. Detailed Explanation",
            "## 6. Examples",
            "## 7. Justification / Why the Approach Works",
            "## 8. Senior FinOps Approach",
            "## 9. Step-by-Step Execution",
            "## 10. Decision Rules",
            "## 11. Trade-offs",
            "## 12. Failure Modes / Edge Cases",
            "## 13. Data Required",
            "## 14. SQL / Python / IaC Application",
            "## 15. Provider Implementation",
            "## 16. Stakeholder Perspective",
            "## 17. Validation",
            "## 18. KPIs",
            "## 19. Guardrails",
            "## 20. Real-World Implications",
            "## 21. FinOps Framework 2026 Reconciliation",
            "## 22. Malaysia N=7 Market Relevance",
            "## 23. Lab Mapping",
            "## 24. Power BI Mapping",
            "## 25. Interview Mapping",
            "## 26. Key Takeaways",
            "## 27. Source Locator",
        ]

        forbidden_markers = [
            "_TODO",
            "TODO —",
            "TODO_",
        ]

        for path in chapter_files:
            text = path.read_text(encoding="utf-8")
            self.assertGreater(
                len(text),
                5000,
                f"{path.name} is too small to satisfy the detailed chapter-note contract",
            )
            for section in required_sections:
                self.assertIn(section, text, f"{path.name} missing {section}")
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
