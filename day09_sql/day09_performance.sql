-- Day 9 - SQL Performance & Query Analysis

-- EXPLAIN
EXPLAIN
SELECT *
FROM customers
WHERE customer_id = 101;


-- EXPLAIN ANALYZE
EXPLAIN ANALYZE
SELECT *
FROM customers
WHERE customer_id = 101;


-- Composite index
CREATE INDEX idx_orders_customer_date
ON orders(customer_id, order_date);


-- Example query using the composite index
SELECT *
FROM orders
WHERE customer_id = 101
  AND order_date >= '2026-08-01';


-- Indexing principle:
-- (customer_id, order_date) is particularly useful when queries filter by customer_id and then by order_date.