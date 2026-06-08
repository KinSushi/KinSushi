CREATE TABLE IF NOT EXISTS customers (
    customer_id TEXT PRIMARY KEY,
    customer_segment TEXT NOT NULL,
    country TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS accounts (
    account_id TEXT PRIMARY KEY,
    customer_id TEXT NOT NULL REFERENCES customers(customer_id),
    account_type TEXT NOT NULL,
    currency TEXT NOT NULL,
    opened_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id TEXT PRIMARY KEY,
    account_id TEXT NOT NULL REFERENCES accounts(account_id),
    source_system TEXT NOT NULL,
    event_timestamp TIMESTAMP NOT NULL,
    booking_date DATE NOT NULL,
    amount_chf NUMERIC(18, 2) NOT NULL,
    currency TEXT NOT NULL,
    channel TEXT NOT NULL,
    merchant_category TEXT NOT NULL,
    country TEXT NOT NULL,
    risk_score NUMERIC(5, 4) NOT NULL,
    status TEXT NOT NULL,
    is_suspicious BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS quality_check_results (
    check_id TEXT PRIMARY KEY,
    check_name TEXT NOT NULL,
    status TEXT NOT NULL,
    failed_rows INTEGER NOT NULL,
    executed_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
