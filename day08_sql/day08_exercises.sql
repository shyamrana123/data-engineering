CREATE INDEX idx_orders_customer_id
ON orders(customer_id);

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