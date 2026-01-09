import pandas as pd
from pathlib import Path


BASE = Path(__file__).resolve().parent
RAW = BASE / "data_raw"
OUT = BASE / "data_output"

OUT.mkdir(exist_ok=True)

customers = pd.read_csv(RAW / "olist_customers_dataset.csv")
orders    = pd.read_csv(RAW / "olist_orders_dataset.csv")
items     = pd.read_csv(RAW / "olist_order_items_dataset.csv")
products  = pd.read_csv(RAW / "olist_products_dataset.csv")
cat       = pd.read_csv(RAW / "product_category_name_translation.csv")
reviews   = pd.read_csv(RAW / "olist_order_reviews_dataset.csv")
payments  = pd.read_csv(RAW / "olist_order_payments_dataset.csv")

dt_cols = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]
for c in dt_cols:
    if c in orders.columns:
        orders[c] = pd.to_datetime(orders[c], errors="coerce")

for c in ["review_creation_date", "review_answer_timestamp"]:
    if c in reviews.columns:
        reviews[c] = pd.to_datetime(reviews[c], errors="coerce")


products2 = products.merge(cat, how="left", on="product_category_name")
products2["product_category_name_english"] = products2["product_category_name_english"].fillna("unknown")


cust2 = customers[
    ["customer_id", "customer_unique_id", "customer_zip_code_prefix", "customer_city", "customer_state"]
].copy()


reviews_sorted = reviews.sort_values(["order_id", "review_creation_date", "review_answer_timestamp"])
reviews_one = reviews_sorted.groupby("order_id", as_index=False).tail(1)[["order_id", "review_score"]]


pay_agg = payments.groupby("order_id", as_index=False).agg(
    payment_value=("payment_value", "sum"),
    payment_installments=("payment_installments", "max"),
)


pay_mode = (
    payments.groupby("order_id")["payment_type"]
    .agg(lambda s: s.mode().iat[0] if len(s.mode()) else s.iloc[0])
    .reset_index()
)
pay_agg = pay_agg.merge(pay_mode, on="order_id", how="left")


df = (
    items.merge(
        orders[[
            "order_id",
            "customer_id",
            "order_status",
            "order_purchase_timestamp",
            "order_delivered_customer_date",
            "order_estimated_delivery_date",
        ]],
        on="order_id",
        how="left",
    )
    .merge(cust2, on="customer_id", how="left")
    .merge(
        products2[["product_id", "product_category_name", "product_category_name_english"]],
        on="product_id",
        how="left",
    )
    .merge(reviews_one, on="order_id", how="left")
    .merge(pay_agg, on="order_id", how="left")
)


df["gmv"] = df["price"].fillna(0) + df["freight_value"].fillna(0)

df["delivery_days"] = (
    (df["order_delivered_customer_date"] - df["order_purchase_timestamp"])
    .dt.total_seconds()
    / 86400.0
)

df["is_delivered"] = df["order_status"].eq("delivered")

df["is_late"] = (
    (df["order_delivered_customer_date"] > df["order_estimated_delivery_date"])
    & df["is_delivered"]
)

df["order_year"] = df["order_purchase_timestamp"].dt.year
df["order_month"] = df["order_purchase_timestamp"].dt.to_period("M").astype(str)


order_totals = df.groupby("order_id", as_index=False).agg(
    order_gmv=("gmv", "sum"),
    order_item_revenue=("price", "sum"),
    order_freight=("freight_value", "sum"),
)
df = df.merge(order_totals, on="order_id", how="left")


keep_cols = [
    "order_id", "order_item_id", "product_id", "seller_id",
    "customer_id", "customer_unique_id", "customer_city", "customer_state", "customer_zip_code_prefix",
    "order_status", "order_purchase_timestamp", "order_year", "order_month",
    "order_delivered_customer_date", "order_estimated_delivery_date",
    "price", "freight_value", "gmv",
    "order_item_revenue", "order_freight", "order_gmv",
    "delivery_days", "is_delivered", "is_late",
    "product_category_name", "product_category_name_english",
    "review_score",
    "payment_type", "payment_value", "payment_installments",
]
keep_cols = [c for c in keep_cols if c in df.columns]  # safe
df_out = df[keep_cols].copy()

out_path = OUT / "olist_ecommerce_analytics.csv"
df_out.to_csv(out_path, index=False)

