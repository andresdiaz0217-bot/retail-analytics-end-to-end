
-- 1. Overall order performance
SELECT
    COUNT(*) AS total_orders,
    COUNT(*) FILTER (WHERE status = 'Completed') AS completed_orders,
    COUNT(*) FILTER (WHERE status = 'Cancelled') AS cancelled_orders,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE status = 'Cancelled')
        / NULLIF(COUNT(*), 0),
        2
    ) AS cancellation_rate_pct
FROM orders;


-- 2. Monthly sales performance
-- Revenue is calculated from completed orders only.
SELECT
    DATE_TRUNC('month', o.order_date)::DATE AS sales_month,
    COUNT(DISTINCT o.order_id) AS completed_orders,
    SUM(oi.quantity) AS units_sold,
    ROUND(
        SUM(
            oi.quantity * oi.unit_price
            * (1 - oi.discount_pct / 100.0)
        ),
        2
    ) AS net_revenue
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
WHERE o.status = 'Completed'
GROUP BY DATE_TRUNC('month', o.order_date)::DATE
ORDER BY sales_month;


-- 3. Revenue by product category
SELECT
    p.category,
    SUM(oi.quantity) AS units_sold,
    ROUND(
        SUM(
            oi.quantity * oi.unit_price
            * (1 - oi.discount_pct / 100.0)
        ),
        2
    ) AS net_revenue
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON oi.product_id = p.product_id
WHERE o.status = 'Completed'
GROUP BY p.category
ORDER BY net_revenue DESC;


-- 4. Revenue by customer region
SELECT
    c.region,
    COUNT(DISTINCT o.order_id) AS completed_orders,
    ROUND(
        SUM(
            oi.quantity * oi.unit_price
            * (1 - oi.discount_pct / 100.0)
        ),
        2
    ) AS net_revenue
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
WHERE o.status = 'Completed'
GROUP BY c.region
ORDER BY net_revenue DESC;


-- 5. Top 10 products by net revenue
SELECT
    p.product_id,
    p.product_name,
    p.category,
    SUM(oi.quantity) AS units_sold,
    ROUND(
        SUM(
            oi.quantity * oi.unit_price
            * (1 - oi.discount_pct / 100.0)
        ),
        2
    ) AS net_revenue
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
JOIN orders o
    ON oi.order_id = o.order_id
WHERE o.status = 'Completed'
GROUP BY p.product_id, p.product_name, p.category
ORDER BY net_revenue DESC
LIMIT 10;
