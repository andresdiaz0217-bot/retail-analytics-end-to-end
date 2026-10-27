
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    region VARCHAR(100) NOT NULL,
    signup_date DATE
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(200) NOT NULL,
    category VARCHAR(100) NOT NULL,
    unit_price NUMERIC(12, 2) NOT NULL
        CHECK (unit_price >= 0)
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL
        REFERENCES customers(customer_id),
    order_date DATE NOT NULL,
    status VARCHAR(30) NOT NULL
);

CREATE TABLE order_items (
    order_id INTEGER NOT NULL
        REFERENCES orders(order_id),
    product_id INTEGER NOT NULL
        REFERENCES products(product_id),
    quantity INTEGER NOT NULL
        CHECK (quantity > 0),
    unit_price NUMERIC(12, 2) NOT NULL
        CHECK (unit_price >= 0),
    discount_pct NUMERIC(5, 2) NOT NULL
        CHECK (discount_pct BETWEEN 0 AND 100),
    PRIMARY KEY (order_id, product_id)
);

CREATE INDEX idx_orders_customer
    ON orders(customer_id);

CREATE INDEX idx_orders_date
    ON orders(order_date);

CREATE INDEX idx_order_items_product
    ON order_items(product_id);
