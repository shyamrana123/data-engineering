CREATE TABLE IF NOT EXISTS stg_customers(
    customer_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(150),
    country VARCHAR(100),
    city VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS stg_products(
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    category VARCHAR(100),
    unit_price NUMERIC(12,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS stg_orders(
    order_id INTEGER NOT NULL,
    order_item_number INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    order_date DATE NOT NULL,
    quantity INTEGER NOT NULL CHECK(quantity > 0),
    unit_price NUMERIC(12,2) NOT NULL,
    sales_amount NUMERIC(12,2) NOT NULL,
    customer_name VARCHAR(100),
    country VARCHAR(100),
    city VARCHAR(100),
    product_name VARCHAR(150),
    category VARCHAR(100),
    PRIMARY KEY(order_id, order_item_number)
);