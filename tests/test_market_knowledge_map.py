from __future__ import annotations

import csv
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
FREQUENCY_PATH = REPO_ROOT / "market" / "finops_capability_frequency.csv"
MAPPING_PATH = REPO_ROOT / "market" / "market_to_knowledge_mapping.csv"
KNOWLEDGE_MAP_PATH = REPO_ROOT / "docs" / "KNOWLEDGE_MAP.md"
SOURCE_REGISTER_PATH = REPO_ROOT / "docs" / "SOURCE_REGISTER.md"


class MarketKnowledgeMapTests(unittest.TestCase):
    def load_csv(self, path: Path) -> list[dict[str, str]]:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return list(csv.DictReader(handle))

    def test_all_recurring_capabilities_are_mapped(self) -> None:
        frequencies = self.load_csv(FREQUENCY_PATH)
        mappings = self.load_csv(MAPPING_PATH)

        recurring = {
            row["capability"]
            for row in frequencies
            if int(row["count"]) >= 2
        }
        mapped = {row["requirement"] for row in mappings}

        self.assertEqual(recurring, mapped)
        self.assertEqual(16, len(recurring))

    def test_mapping_preserves_market_counts_and_percentages(self) -> None:
        frequency_by_capability = {
            row["capability"]: row
            for row in self.load_csv(FREQUENCY_PATH)
            if int(row["count"]) >= 2
        }

        for row in self.load_csv(MAPPING_PATH):
            source = frequency_by_capability[row["requirement"]]
            self.assertEqual(int(source["count"]), int(row["count"]))
            self.assertAlmostEqual(float(source["percentage"]), float(row["percentage"]), places=2)

    def test_priority_is_deterministic_from_frequency(self) -> None:
        for row in self.load_csv(MAPPING_PATH):
            count = int(row["count"])
            expected = "P0" if count >= 5 else "P1" if count >= 3 else "P2"
            self.assertEqual(expected, row["priority"], row["requirement"])

    def test_mapping_has_required_lineage_and_gap_fields(self) -> None:
        required = [
            "framework_domain",
            "framework_capability",
            "book_mapping",
            "official_provider_mapping",
            "resume_status",
            "gap",
            "target_depth",
            "lab_mapping",
            "interview_risk",
        ]
        allowed_resume_status = {"strong", "partial", "gap"}

        for row in self.load_csv(MAPPING_PATH):
            for field in required:
                self.assertTrue(row[field].strip(), f"{row['requirement']} missing {field}")
            self.assertIn(row["resume_status"], allowed_resume_status)

    def test_knowledge_map_declares_mapping_not_mastery(self) -> None:
        text = KNOWLEDGE_MAP_PATH.read_text(encoding="utf-8")
        self.assertIn("Checkpoint 2 mapping coverage: 16 / 16 = 100%", text)
        self.assertIn("does **not** mean the later hands-on", text)
        self.assertIn("N = 7", text)

    def test_source_register_contains_core_evidence_grades(self) -> None:
        text = SOURCE_REGISTER_PATH.read_text(encoding="utf-8")
        self.assertIn("A-CASE-001", text)
        self.assertIn("B-AWS-001", text)
        self.assertIn("C-FWK-001", text)
        self.assertIn("Grade A/B", text)


if __name__ == "__main__":
    unittest.main()
