USE ecommerce_ai;


-- Data Validation

SELECT 'customers' AS table_name, COUNT(*) AS row_count
FROM customers

UNION ALL

SELECT 'orders', COUNT(*)
FROM orders

UNION ALL

SELECT 'products', COUNT(*)
FROM products

UNION ALL

SELECT 'support_tickets', COUNT(*)
FROM support_tickets

UNION ALL

SELECT 'payments', COUNT(*)
FROM payments;


-- Overall Sales Analysis

SELECT
    COUNT(DISTINCT customer_id) AS unique_customers,
    COUNT(*) AS total_orders,
    SUM(quantity) AS units_sold,
    ROUND(SUM(sales), 2) AS total_sales
FROM orders;


-- Top Customers

SELECT
    o.customer_id,
    c.customer_name,
    c.city,
    c.segment,
    COUNT(o.order_id) AS total_orders,
    ROUND(SUM(o.sales), 2) AS total_sales
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
GROUP BY
    o.customer_id,
    c.customer_name,
    c.city,
    c.segment
ORDER BY total_sales DESC
LIMIT 10;


-- Sales by City

SELECT
    c.city,
    COUNT(DISTINCT o.customer_id) AS customers,
    COUNT(o.order_id) AS total_orders,
    ROUND(SUM(o.sales), 2) AS total_sales
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
GROUP BY c.city
ORDER BY total_sales DESC;


-- Sales by Category

SELECT
    p.category,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(o.quantity) AS units_sold,
    ROUND(SUM(o.sales), 2) AS total_sales
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY total_sales DESC;


-- Monthly Sales Trend

SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS sales_month,
    COUNT(order_id) AS total_orders,
    SUM(quantity) AS units_sold,
    ROUND(SUM(sales), 2) AS total_sales
FROM orders
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY sales_month;


-- Product Performance

SELECT
    p.product_id,
    p.product_name,
    p.category,
    SUM(o.quantity) AS units_sold,
    ROUND(SUM(o.sales), 2) AS total_sales
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
GROUP BY
    p.product_id,
    p.product_name,
    p.category
ORDER BY total_sales DESC;


-- Order Status Analysis

SELECT
    status,
    COUNT(*) AS total_orders,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(AVG(sales), 2) AS average_order_value
FROM orders
GROUP BY status
ORDER BY total_orders DESC;


-- Failed Payment Analysis

SELECT
    payment_method,
    COUNT(*) AS failed_transactions,
    ROUND(SUM(amount), 2) AS failed_amount
FROM payments
WHERE payment_status = 'Failed'
GROUP BY payment_method
ORDER BY failed_transactions DESC;


-- Support Issue Analysis

SELECT
    issue_type,
    COUNT(*) AS total_tickets,
    ROUND(AVG(resolution_hours), 2) AS avg_resolution_hours
FROM support_tickets
GROUP BY issue_type
ORDER BY total_tickets DESC;


-- High Value Customers

SELECT
    c.customer_id,
    c.customer_name,
    c.city,
    ROUND(s.total_sales, 2) AS total_sales,
    COALESCE(st.support_tickets, 0) AS support_tickets,
    ROUND(st.avg_resolution_hours, 2) AS avg_resolution_hours
FROM customers c

JOIN (
    SELECT
        customer_id,
        SUM(sales) AS total_sales
    FROM orders
    GROUP BY customer_id
    HAVING SUM(sales) > 90000
) s
    ON c.customer_id = s.customer_id

LEFT JOIN (
    SELECT
        customer_id,
        COUNT(ticket_id) AS support_tickets,
        AVG(resolution_hours) AS avg_resolution_hours
    FROM support_tickets
    GROUP BY customer_id
) st
    ON c.customer_id = st.customer_id

ORDER BY total_sales DESC;