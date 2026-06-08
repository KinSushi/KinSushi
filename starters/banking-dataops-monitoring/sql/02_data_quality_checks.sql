-- Critical null checks
SELECT 'critical_nulls' AS check_name, COUNT(*) AS failed_rows
FROM transactions
WHERE transaction_id IS NULL
   OR account_id IS NULL
   OR event_timestamp IS NULL
   OR amount_chf IS NULL;

-- Duplicate transaction identifiers
SELECT 'duplicate_transactions' AS check_name, COUNT(*) AS failed_groups
FROM (
    SELECT transaction_id
    FROM transactions
    GROUP BY transaction_id
    HAVING COUNT(*) > 1
) duplicates;

-- Implausible amounts
SELECT 'invalid_amounts' AS check_name, COUNT(*) AS failed_rows
FROM transactions
WHERE amount_chf <= 0
   OR amount_chf > 1000000;

-- Referential integrity check
SELECT 'orphan_transactions' AS check_name, COUNT(*) AS failed_rows
FROM transactions t
LEFT JOIN accounts a ON t.account_id = a.account_id
WHERE a.account_id IS NULL;

-- Freshness check
SELECT 'latest_transaction_timestamp' AS check_name, MAX(event_timestamp) AS latest_transaction
FROM transactions;
