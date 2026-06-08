# Rollback Plan

## Purpose

This rollback plan documents how to safely return from the target schema to the pre-migration state in a synthetic migration lab.

It is public technical evidence only. It must not be used as a production migration plan.

---

## Rollback principles

1. Validate before rollback.
2. Preserve source tables.
3. Never overwrite legacy data.
4. Keep migration scripts idempotent where possible.
5. Document every failed validation and rollback action.

---

## Minimum rollback steps

```sql
-- Remove target data only, preserving legacy source tables.
TRUNCATE TABLE accounts RESTART IDENTITY CASCADE;
TRUNCATE TABLE customers RESTART IDENTITY CASCADE;
```

---

## Pre-rollback checklist

- [ ] migration validation failed;
- [ ] issue was documented;
- [ ] source row counts are still available;
- [ ] rollback scope is target-only;
- [ ] no private or real data is involved.

---

## Post-rollback validation

Run:

```sql
SELECT COUNT(*) FROM legacy_clients;
SELECT COUNT(*) FROM legacy_accounts;
SELECT COUNT(*) FROM customers;
SELECT COUNT(*) FROM accounts;
```

Expected:

- legacy tables preserved;
- target tables cleared or restored to previous known state.
