# olist-ecommerce-customer-insights
This project analyzes customer behavior, revenue performance, and operational efficiency using transactional e-commerce data from the Olist marketplace. The objective was to move beyond static reporting and develop an interactive Tableau dashboard that supports business decision-making across growth, retention, and operations.

Interactive Dashboard (Tableau Public):
  https://public.tableau.com/views/OlistEcommerce_17664395225210/ProductOperationsPerformance?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

**Business Questions Addressed**
How is overall revenue and order volume trending over time?
Which customer segments contribute the most to total revenue?
How concentrated is revenue across the customer base?
How do product categories scale in terms of orders and revenue?
Are operational issues (late deliveries) impacting core revenue drivers?

**Dashboard Structure**
Page A — Executive Overview

Provides a high-level snapshot of business performance, including:
  -Total revenue, orders, customers, and average order value
  -Monthly revenue trends
  -Repeat customer rate and delivery performance

Insight: Revenue grows steadily over time, but repeat customer rate remains relatively low, suggesting growth is primarily acquisition-driven.

Page B — Customer Segmentation (RFM Analysis)

Customers are segmented using purchase frequency and total spend into High-, Mid-, and Low-Value groups.

Insight: High-value customers represent roughly one-third of the customer base but generate approximately 74% of total revenue, indicating strong revenue concentration and highlighting retention as a high-ROI strategy.

Page C — Orders vs. Revenue (Category Efficiency)

Analyzes product categories by:
  -Order volume
  -Total revenue
  -Delivery performance (on-time vs late)

Insight: Revenue scales proportionally with order volume across top categories. Late deliveries are largely concentrated among lower-volume, lower-revenue categories, suggesting operational challenges are not currently constraining core revenue drivers.

**Dataset**
Source: Public Olist Brazilian E-commerce dataset from Kaggle (https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
Size: ~100,000 orders over two years from 2016-2018
