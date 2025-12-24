# olist-ecommerce-customer-insights
This project analyzes customer behavior, revenue performance, and operational efficiency using transactional e-commerce data from the Olist marketplace. The objective was to move beyond static reporting and develop an interactive Tableau dashboard that supports business decision-making across growth, retention, and operations.

To interact with the dashboard (Tableau Public), visit the link and click 'View on Tableau Public' at the bottom left of the page:
  https://public.tableau.com/views/OlistEcommerce_17664395225210/ProductOperationsPerformance?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link


**Business Questions Addressed**
How is overall revenue and order volume trending over time?
Which customer segments contribute the most to total revenue?
How concentrated is revenue across the customer base?
How do product categories scale in terms of orders and revenue?
Are operational issues (late deliveries) impacting core revenue drivers?


**Data Preparation**
Data was cleaned, joined, and transformed using Python (pandas) prior to visualization.
An analytics-ready fact table was created at the order-item level, with engineered features to simplify KPI computation in Tableau.



**Dashboard Structure**

**Page A — Executive Overview**

Provides a high-level snapshot of business performance, including:
  -Total revenue, orders, customers, and average order value
  -Monthly revenue trends
  -Repeat customer rate and delivery performance

Insight: Revenue grows steadily over time, but repeat customer rate remains relatively low, suggesting growth is primarily acquisition-driven.

<img width="1197" height="698" alt="Screenshot 2025-12-24 at 5 17 37 PM" src="https://github.com/user-attachments/assets/ed514fcb-c183-4b25-8f0d-279bd412835c" />


**Page B — Customer Segmentation (RFM Analysis)**

Customers are segmented using purchase frequency and total spend into High-, Mid-, and Low-Value groups.

Insight: High-value customers represent roughly one-third of the customer base but generate approximately 74% of total revenue, indicating strong revenue concentration and highlighting retention as a high-ROI strategy.

<img width="1200" height="702" alt="Screenshot 2025-12-24 at 5 18 28 PM" src="https://github.com/user-attachments/assets/d56a33c1-ad08-4d29-bc98-8fa89a191745" />

**Page C — Orders vs. Revenue (Category Efficiency)**

Analyzes product categories by:
  -Order volume
  -Total revenue
  -Delivery performance (on-time vs late)

Insight: Revenue scales proportionally with order volume across top categories. Late deliveries are largely concentrated among lower-volume, lower-revenue categories, suggesting operational challenges are not currently constraining core revenue drivers.


<img width="1195" height="698" alt="Screenshot 2025-12-24 at 5 18 40 PM" src="https://github.com/user-attachments/assets/b1ae5cc9-2310-4ec0-bb60-5e1c8ef5fddf" />


**Dataset**
Source: Public Olist Brazilian E-commerce dataset from Kaggle (https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
Size: ~100,000 orders over two years from 2016-2018
