CREATE TABLE IF NOT EXISTS customers (
    customer_id TEXT PRIMARY KEY,
    customer_segment TEXT NOT NULL,
    country TEXT NOT NULL,
    created_at DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS accounts (
    account_id TEXT PRIMARY KEY,
    customer_id TEXT NOT NULL REFERENCES customers(customer_id),
    account_type TEXT NOT NULL,
    currency TEXT NOT NULL,
    opened_at DATE NOT NULL,
    balance_chf NUMERIC(18, 2) NOT NULL
);
