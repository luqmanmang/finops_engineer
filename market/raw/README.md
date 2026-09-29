# Raw Vacancy Records

Store exactly one JSON record per candidate vacancy using the stable vacancy ID as the filename.

```text
MY-FE-0001.json
MY-FE-0002.json
```

Use `../templates/vacancy_record.template.json` as the starting contract.

## Rules

1. Preserve source facts, terminology, named technologies and short evidence phrases. For public-repository safety, paraphrase long job-description prose instead of copying full vacancy text.
2. `date_checked` is the date the source was reviewed.
3. `job_url` must point to the source actually reviewed.
4. Do not manually set derived taxonomy columns in this file. Use `manual_overrides` only when the deterministic classifier needs correction.
5. An input record is not automatically part of the canonical census. Eligibility is decided with the matching record under `../evidence/`.
6. Prefer one canonical record per underlying vacancy. Do not multiply-count obvious syndications of the same employer, role, location and materially identical description.

Optional research notes may be kept beside the JSON using the same vacancy ID. The build only reads `*.json`.
