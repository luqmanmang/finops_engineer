from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MARKET = REPO_ROOT / "market"
LEARNING = REPO_ROOT / "learning"
DOCS = REPO_ROOT / "docs"

MATRIX = MARKET / "vacancy_skill_matrix.csv"
COVERAGE = LEARNING / "JD_COVERAGE_MATRIX.csv"
SUPPLEMENTAL = LEARNING / "JD_SUPPLEMENTAL_TERMS.json"

META_COLUMNS = {"vacancy_id", "company", "job_title"}


class JDLearningCoverageTests(unittest.TestCase):
    def vacancy_rows(self) -> list[dict[str, str]]:
        with MATRIX.open(encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))

    def coverage_rows(self) -> list[dict[str, str]]:
        with COVERAGE.open(encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))

    def test_every_observed_taxonomy_requirement_has_learning_coverage(self) -> None:
        vacancy_rows = self.vacancy_rows()
        fieldnames = list(vacancy_rows[0].keys())
        observed_counts = {}
        for key in fieldnames:
            if key in META_COLUMNS:
                continue
            count = sum((row.get(key) or "").strip().lower() == "true" for row in vacancy_rows)
            if count:
                observed_counts[key] = count

        coverage = {row["requirement_key"]: row for row in self.coverage_rows()}

        self.assertTrue(observed_counts, "No positive JD requirements were derived")
        self.assertEqual(
            set(),
            set(observed_counts) - set(coverage),
            "Every positive vacancy_skill_matrix field must have a coverage row",
        )

        for key, count in observed_counts.items():
            row = coverage[key]
            self.assertEqual(
                count,
                int(row["observed_count"]),
                f"{key}: observed_count drifted from canonical vacancy matrix",
            )
            self.assertNotEqual("GAP", row["learning_status"], f"{key} is still a learning GAP")
            for required in ("theory", "explanation", "example", "step_by_step", "interview"):
                self.assertEqual(
                    "yes",
                    row[required],
                    f"{key}: {required} must be explicitly represented",
                )
            for artifact in [p.strip() for p in row["artifact"].split(";") if p.strip()]:
                self.assertTrue(
                    (REPO_ROOT / artifact).exists(),
                    f"{key}: coverage artifact does not exist: {artifact}",
                )

    def test_coverage_matrix_contains_no_unexplained_gap(self) -> None:
        for row in self.coverage_rows():
            self.assertIn(row["learning_status"], {"COMPLETE", "PARTIAL", "REFERENCE_ONLY"})
            self.assertTrue(row["requirement_key"].strip())
            self.assertTrue(row["category"].strip())
            self.assertTrue(row["learning_depth"].strip())

    def test_supplemental_named_terms_are_traceable_to_source_and_handbook(self) -> None:
        payload = json.loads(SUPPLEMENTAL.read_text(encoding="utf-8"))
        handbook = (DOCS / "VOLUME_2_JD_COVERAGE_HANDBOOK.md").read_text(encoding="utf-8").lower()

        self.assertEqual("2026-09-30", payload["snapshot_date"])
        self.assertGreaterEqual(len(payload["terms"]), 20)

        for item in payload["terms"]:
            term = item["term"]
            self.assertIn(
                item["learning_status"],
                {"COMPLETE", "PARTIAL", "REFERENCE_ONLY"},
                f"{term}: invalid learning status",
            )
            self.assertIn(term.lower(), handbook, f"{term}: missing from Volume 2 handbook")
            self.assertTrue(item["source_vacancies"], f"{term}: source_vacancies must not be empty")
            for vacancy_id in item["source_vacancies"]:
                source_path = MARKET / "raw" / f"{vacancy_id}.json"
                self.assertTrue(source_path.exists(), f"{term}: missing raw source {vacancy_id}")
                raw_text = source_path.read_text(encoding="utf-8").lower()
                self.assertIn(
                    term.lower(),
                    raw_text,
                    f"{term}: not found in declared source {vacancy_id}",
                )

    def test_certification_rows_point_to_volume_3(self) -> None:
        certification_rows = [
            row for row in self.coverage_rows() if row["category"] == "certification"
        ]
        self.assertTrue(certification_rows)
        for row in certification_rows:
            self.assertIn(
                "docs/VOLUME_3_CERTIFICATION_INTERVIEW_TRANSFER.md",
                row["artifact"],
            )


if __name__ == "__main__":
    unittest.main()
