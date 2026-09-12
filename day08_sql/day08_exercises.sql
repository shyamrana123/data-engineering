CREATE INDEX idx_orders_customer_id
ON orders(customer_id);

CREATE INDEX idx_orders_product_id
ON orders(product_id);

BEGIN;

UPDATE orders
SET quantity = quantity + 2
WHERE order_id = 1002;

COMMIT;

BEGIN;

UPDATE orders
SET quantity = quantity + 2
WHERE order_id = 1003;

ROLLBACK;