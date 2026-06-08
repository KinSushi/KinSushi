-- Row counts by table
SELECT 'customers' AS table_name, COUNT(*) AS row_count FROM customers
UNION ALL
SELECT 'accounts', COUNT(*) FROM accounts
UNION ALL
SELECT 'transactions', COUNT(*) FROM transactions;

-- Latest event timestamp
SELECT MAX(event_timestamp) AS latest_event_timestamp
FROM transactions;

-- Query plan example: booking-date operational query
EXPLAIN SELECT booking_date, COUNT(*) AS transaction_count
FROM transactions
GROUP BY booking_date
ORDER BY booking_date;

-- Query plan example: high-risk sample query
EXPLAIN SELECT transaction_id, account_id, event_timestamp, risk_score
FROM transactions
WHERE is_suspicious = TRUE
ORDER BY event_timestamp DESC
LIMIT 50;
