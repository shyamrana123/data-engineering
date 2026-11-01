-- ==========================================
-- DAY 27: E-COMMERCE DATA WAREHOUSE
-- Star Schema
-- Grain: One row per order item
-- ==========================================


-- 1. CUSTOMER DIMENSION
CREATE TABLE dim_customers (
    customer_key INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    customer_name VARCHAR(100) NOT NULL,
    country VARCHAR(100),
    city VARCHAR(100)
);


-- 2. PRODUCT DIMENSION
CREATE TABLE dim_products (
    product_key INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_id INTEGER NOT NULL,
    product_name VARCHAR(150) NOT NULL,
    category VARCHAR(100)
);


-- 3. DATE DIMENSION
CREATE TABLE dim_date (
    date_key INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_date DATE NOT NULL UNIQUE,
    day INTEGER NOT NULL,
    month INTEGER NOT NULL,
    year INTEGER NOT NULL
);


-- 4. SALES FACT TABLE
CREATE TABLE fact_sales (
    sales_key BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    order_id INTEGER NOT NULL,
    order_item_number INTEGER NOT NULL,

    customer_key INTEGER NOT NULL,
    product_key INTEGER NOT NULL,
    date_key INTEGER NOT NULL,

    quantity INTEGER NOT NULL CHECK (quantity > 0),
    sales_amount NUMERIC(12,2) NOT NULL CHECK (sales_amount >= 0),

    CONSTRAINT fk_sales_customer
        FOREIGN KEY (customer_key)
        REFERENCES dim_customers(customer_key),

    CONSTRAINT fk_sales_product
        FOREIGN KEY (product_key)
        REFERENCES dim_products(product_key),

    CONSTRAINT fk_sales_date
        FOREIGN KEY (date_key)
        REFERENCES dim_date(date_key),

    CONSTRAINT unique_order_item
        UNIQUE (order_id, order_item_number)
);


-- Indexes to support common joins
CREATE INDEX idx_sales_customer
    ON fact_sales(customer_key);

CREATE INDEX idx_sales_product
    ON fact_sales(product_key);

CREATE INDEX idx_sales_date
    ON fact_sales(date_key);



SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
  AND table_name IN (
      'dim_customers',
      'dim_products',
      'dim_date',
      'fact_sales'
  )
ORDER BY table_name;


SELECT
    tc.table_name,
    tc.constraint_name,
    tc.constraint_type,
    kcu.column_name
FROM information_schema.table_constraints AS tc
LEFT JOIN information_schema.key_column_usage AS kcu
    ON tc.constraint_name = kcu.constraint_name
    AND tc.table_schema = kcu.table_schema
WHERE tc.table_schema = 'public'
  AND tc.table_name IN (
      'dim_customers',
      'dim_products',
      'dim_date',
      'fact_sales'
  )
ORDER BY tc.table_name, tc.constraint_type;


-- Customers
INSERT INTO dim_customers
    (customer_id, customer_name, country, city)
VALUES
    (101, 'John', 'Portugal', 'Lisbon'),
    (102, 'Sam', 'Spain', 'Madrid'),
    (103, 'Raj', 'Nepal', 'Kathmandu'),
    (104, 'Alex', 'Portugal', 'Porto');


-- Products
INSERT INTO dim_products
    (product_id, product_name, category)
VALUES
    (501, 'Laptop', 'Electronics'),
    (502, 'Mouse', 'Electronics'),
    (503, 'Office Chair', 'Furniture'),
    (504, 'Keyboard', 'Electronics');


-- Dates
INSERT INTO dim_date
    (full_date, day, month, year)
VALUES
    ('2026-10-28', 28, 10, 2026),
    ('2026-10-29', 29, 10, 2026),
    ('2026-10-30', 30, 10, 2026);


SELECT * FROM dim_customers;
SELECT * FROM dim_products;
SELECT * FROM dim_date;


INSERT INTO fact_sales
    (
        order_id,
        order_item_number,
        customer_key,
        product_key,
        date_key,
        quantity,
        sales_amount
    )
VALUES
    (5001, 1, 1, 1, 1, 1, 1200.00),
    (5001, 2, 1, 2, 1, 2, 50.00),
    (5002, 1, 2, 3, 2, 1, 180.00),
    (5003, 1, 3, 4, 2, 2, 150.00),
    (5004, 1, 4, 1, 3, 1, 1200.00);

SELECT * FROM fact_sales
ORDER BY order_id, order_item_number;



SELECT
    c.country,
    SUM(f.sales_amount) AS total_revenue
FROM fact_sales AS f
JOIN dim_customers AS c
    ON f.customer_key = c.customer_key
GROUP BY c.country
ORDER BY total_revenue DESC;

SELECT
    p.category,
    SUM(f.sales_amount) AS total_revenue,
    SUM(f.quantity) AS total_quantity_sold
FROM fact_sales AS f
JOIN dim_products AS p
    ON f.product_key = p.product_key
GROUP BY p.category
ORDER BY total_revenue DESC;


SELECT
    d.full_date,
    d.month,
    d.year,
    SUM(f.sales_amount) AS total_revenue
FROM fact_sales AS f
JOIN dim_date AS d
    ON f.date_key = d.date_key
GROUP BY
    d.full_date,
    d.month,
    d.year
ORDER BY d.full_date;


SELECT
    f.order_id,
    c.customer_name,
    c.country,
    p.product_name,
    p.category,
    d.full_date,
    f.quantity,
    f.sales_amount
FROM fact_sales AS f
JOIN dim_customers AS c
    ON f.customer_key = c.customer_key
JOIN dim_products AS p
    ON f.product_key = p.product_key
JOIN dim_date AS d
    ON f.date_key = d.date_key
ORDER BY f.order_id, f.order_item_number;
