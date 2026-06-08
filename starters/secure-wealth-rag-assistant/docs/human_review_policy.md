# Human Review Policy

## Purpose

This document defines when a human reviewer is required in the secure RAG starter.

---

## Human review required

Human review is required when an answer involves:

- risk classification;
- client-sensitive interpretation;
- financial, insurance, health or legal implications;
- incomplete or conflicting retrieved context;
- privacy uncertainty;
- low retrieval confidence;
- prompt-injection attempt detection.

---

## Response boundary

The assistant should provide:

- source-grounded summaries;
- clear uncertainty;
- non-advisory explanations;
- escalation recommendation when context is insufficient.

It should not provide:

- investment advice;
- medical advice;
- legal advice;
- production decisions;
- unsupported claims.

---

## Public-safety note

This policy is a portfolio artifact and not a production governance policy.
