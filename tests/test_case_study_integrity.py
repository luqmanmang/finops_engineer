from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CASE_ROOT = REPO_ROOT / "case_studies"
CASE_FILES = [
    CASE_ROOT / "01_financial_services" / "CASE.md",
    CASE_ROOT / "02_oil_gas_energy" / "CASE.md",
    CASE_ROOT / "03_semiconductor" / "CASE.md",
    CASE_ROOT / "04_market_selected" / "CASE.md",
    CASE_ROOT / "05_market_selected" / "CASE.md",
]


class CaseStudyIntegrityTests(unittest.TestCase):
    def test_all_five_case_files_exist(self) -> None:
        self.assertEqual(5, len(CASE_FILES))
        for path in CASE_FILES:
            self.assertTrue(path.exists(), str(path))

    def test_required_case_dissection_sections_exist(self) -> None:
        required = [
            "SOURCE FACT",
            "OUR ANALYSIS",
            "OUR REPRODUCTION",
            "Diagnose",
            "Hypothesis",
            "Finding",
            "Solution",
            "Validation",
            "Insight",
            "Interview transfer",
        ]
        for path in CASE_FILES:
            text = path.read_text(encoding="utf-8")
            for marker in required:
                self.assertIn(marker, text, f"{path} missing {marker}")

    def test_every_case_has_primary_http_source(self) -> None:
        for path in CASE_FILES:
            text = path.read_text(encoding="utf-8")
            self.assertIn("https://", text, f"{path} missing source URL")

    def test_case_files_protect_realized_savings_boundary(self) -> None:
        combined = "\n".join(path.read_text(encoding="utf-8") for path in CASE_FILES)
        self.assertIn("realized", combined.lower())
        self.assertIn("projected", combined.lower())
        self.assertIn("source", combined.lower())


if __name__ == "__main__":
    unittest.main()
