import csv
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKET = ROOT / "market"
DOCS = ROOT / "docs"


class KnowledgeMappingTests(unittest.TestCase):
    def read_csv(self, path: Path):
        with path.open(encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))

    def test_mapping_covers_every_recurring_market_capability(self):
        frequency = self.read_csv(MARKET / "finops_capability_frequency.csv")
        mapping = self.read_csv(MARKET / "market_to_knowledge_mapping.csv")

        recurring = {
            row["capability"]
            for row in frequency
            if int(row["count"]) >= 2
        }
        mapped = [row["requirement"] for row in mapping]

        self.assertEqual(len(mapped), len(set(mapped)), "mapping contains duplicate requirements")
        self.assertEqual(set(mapped), recurring)
        self.assertEqual(len(recurring), 16)

    def test_every_mapping_row_has_required_lineage(self):
        mapping = self.read_csv(MARKET / "market_to_knowledge_mapping.csv")
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
        for row in mapping:
            with self.subTest(requirement=row["requirement"]):
                for field in required:
                    self.assertTrue(row[field].strip(), f"{row['requirement']} missing {field}")
                self.assertIn(row["resume_status"], {"strong", "partial", "gap"})
                self.assertIn(row["target_depth"], {"deep", "strong", "working", "light", "defer"})

    def test_priority_is_deterministic_from_market_count(self):
        mapping = self.read_csv(MARKET / "market_to_knowledge_mapping.csv")
        for row in mapping:
            count = int(row["count"])
            expected = "P0" if count >= 5 else "P1" if count >= 3 else "P2"
            self.assertEqual(row["priority"], expected, row["requirement"])

    def test_knowledge_map_records_coverage_and_sample_guardrail(self):
        text = (DOCS / "KNOWLEDGE_MAP.md").read_text(encoding="utf-8")
        self.assertIn("16 / 16 = 100%", text)
        self.assertIn("N = 7", text)
        self.assertIn("14.29 percentage points", text)

    def test_source_register_has_required_contract_and_evidence_grades(self):
        text = (DOCS / "SOURCE_REGISTER.md").read_text(encoding="utf-8")
        required_headers = [
            "source_id", "topic", "title", "publisher", "date", "url",
            "evidence_grade", "company", "industry", "key_claim",
            "limitations", "used_in",
        ]
        for header in required_headers:
            self.assertIn(header, text)
        for grade in ["A", "B", "C", "D"]:
            self.assertIn(f"**{grade}", text)


if __name__ == "__main__":
    unittest.main()
