

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(255),
    country VARCHAR(100)
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(300),
    price NUMERIC(10,2)
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    product_id INTEGER REFERENCES products(product_id),
    order_date DATE,
    quantity INTEGER
);

INSERT INTO customers
    (customer_id, customer_name, email, country)
VALUES
    (101, 'John', 'john@example.com', 'Portugal'),
    (102, 'Sam', 'sam@example.com', 'Spain'),
    (103, 'Raj', 'raj@example.com', 'Nepal');

CREATE INDEX idx_customers_customer_id
ON customers(customer_id);

EXPLAIN
SELECT *
FROM customers;

EXPLAIN ANALYZE
SELECT *
FROM customers
WHERE customer_id = 101;


SELECT indexname, indexdef
FROM pg_indexes
WHERE tablename = 'customers';

DROP INDEX idx_customers_customer_id;

SET enable_seqscan = OFF;

EXPLAIN ANALYZE
SELECT *
FROM customers
WHERE customer_id = 101;

SET enable_seqscan = ON;

CREATE TABLE etl_orders(
	order_id INTEGER PRIMARY KEY,
	customer_name VARCHAR(100),
	customer_email VARCHAR(255),
	product_id INTEGER,
	price NUMERIC(10,2),
	quantity INTEGER,
	order_value NUMERIC(10,2)
);

SELECT * FROM etl_orders;

DELETE FROM etl_orders
WHERE order_id = 999;

SELECT COUNT(*) AS total_orders
FROM etl_orders;

SELECT 
    order_id,
	price,
	quantity,
	order_value,
	price * quantity AS calculated_value
FROM etl_orders
LIMIT 10;


SELECT 
	COUNT(*) AS total_rows,
	COUNT(DISTINCT order_id) AS unique_orders
FROM etl_orders;