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
        ]
        joined = "\n".join(titles)
        for phrase in required:
            self.assertIn(phrase, joined)

    def test_generated_markdown_contract(self) -> None:
        chapter_files = sorted((BOOK_DIR / "chapters").glob("*.md"))
        self.assertEqual(27, len(chapter_files))
        required_sections = [
            "## 1. Chapter Brief",
            "## 6. Examples",
            "## 7. Justification / Why the Approach Works",
            "## 8. Senior FinOps Approach",
            "## 9. Step-by-Step Execution",
            "## 11. Trade-offs",
            "## 12. Failure Modes / Edge Cases",
            "## 21. FinOps Framework 2026 Reconciliation",
            "## 22. Malaysia N=7 Market Relevance",
            "## 25. Interview Mapping",
        ]
        for path in chapter_files:
            text = path.read_text(encoding="utf-8")
            for section in required_sections:
                self.assertIn(section, text, f"{path.name} missing {section}")

    def test_chapter_index_matches_generated_files(self) -> None:
        with (BOOK_DIR / "chapter_index.csv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(27, len(rows))
        for row in rows:
            self.assertTrue((BOOK_DIR / row["markdown_file"]).exists())


if __name__ == "__main__":
    unittest.main()
