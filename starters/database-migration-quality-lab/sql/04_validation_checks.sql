-- Row-count validation
SELECT 'customers_row_count' AS check_name, COUNT(*) AS target_count
FROM customers;

SELECT 'accounts_row_count' AS check_name, COUNT(*) AS target_count
FROM accounts;

-- Orphan account validation
SELECT 'orphan_accounts' AS check_name, COUNT(*) AS failed_rows
FROM accounts a
LEFT JOIN customers c ON a.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

-- Balance validity validation
SELECT 'negative_balances' AS check_name, COUNT(*) AS failed_rows
FROM accounts
WHERE balance_chf < 0;

-- Unknown segment validation
SELECT 'unknown_segments' AS check_name, COUNT(*) AS failed_rows
FROM customers
WHERE customer_segment = 'unknown';
