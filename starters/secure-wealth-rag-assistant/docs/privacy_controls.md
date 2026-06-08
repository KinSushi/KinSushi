# Privacy Controls

## Purpose

This document defines privacy controls for the secure RAG starter.

The project uses synthetic documents only and must not ingest real client, banking, insurance, health, employer or private documents.

---

## Controls

| Control | Purpose | Evidence |
|---|---|---|
| Synthetic corpus only | Prevent private data exposure | `docs_sample/` review |
| PII scan before ingestion | Detect accidental personal data | planned `src/guardrails.py` |
| Redaction before indexing | Prevent private text from entering vector store | planned preprocessing step |
| Citation-grounded outputs | Reduce unsupported answers | retrieval evaluation |
| Human review policy | Avoid sensitive automated decisions | `docs/human_review_policy.md` |

---

## Forbidden data

- real client names;
- real account numbers;
- real insurance policies;
- real health records;
- real employer documents;
- private PDFs;
- contracts;
- identity documents.

---

## Public-safety note

This is public technical evidence. It is not a production privacy program.
