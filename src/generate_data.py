
from pathlib import Path

import numpy as np
import pandas as pd


SEED = 42
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "data" / "synthetic"


def generate_data() -> None:
    """Generate reproducible synthetic retail data and save it as CSV files."""
    rng = np.random.default_rng(SEED)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Customers
    n_customers = 500
    customer_ids = np.arange(1, n_customers + 1)

    customers = pd.DataFrame(
        {
            "customer_id": customer_ids,
            "region": rng.choice(
                ["Andina", "Caribe", "Pacifica", "Amazonia", "Orinoquia"],
                size=n_customers,
                p=[0.40, 0.22, 0.20, 0.08, 0.10],
            ),
            "signup_date": pd.to_datetime(
                rng.integers(
                    pd.Timestamp("2022-01-01").value // 10**9,
                    pd.Timestamp("2025-01-01").value // 10**9,
                    size=n_customers,
                ),
                unit="s",
            ).normalize(),
        }
    )

    # 2. Products
    n_products = 80
    categories = {
        "Technology": ["Headphones", "Keyboard", "Mouse", "Monitor", "Webcam"],
        "Home": ["Lamp", "Chair", "Storage Box", "Desk", "Cookware"],
        "Sports": ["Water Bottle", "Yoga Mat", "Backpack", "Ball", "Dumbbells"],
        "Stationery": ["Notebook", "Pen Set", "Planner", "Folder", "Markers"],
    }

    product_categories = rng.choice(list(categories), size=n_products)
    product_names = [
        f"{category} {rng.choice(categories[category])} {i:03d}"
        for i, category in enumerate(product_categories, start=1)
    ]

    products = pd.DataFrame(
        {
            "product_id": np.arange(1, n_products + 1),
            "product_name": product_names,
            "category": product_categories,
            "unit_price": np.round(rng.uniform(8, 500, size=n_products), 2),
        }
    )

    # 3. Orders
    n_orders = 2500
    order_dates = pd.to_datetime(
        rng.integers(
            pd.Timestamp("2025-01-01").value // 10**9,
            pd.Timestamp("2026-10-01").value // 10**9,
            size=n_orders,
        ),
        unit="s",
    ).normalize()

    orders = pd.DataFrame(
        {
            "order_id": np.arange(1, n_orders + 1),
            "customer_id": rng.choice(customer_ids, size=n_orders),
            "order_date": order_dates,
            "status": rng.choice(
                ["Completed", "Processing", "Cancelled", "Returned"],
                size=n_orders,
                p=[0.78, 0.10, 0.08, 0.04],
            ),
        }
    )

    # 4. Order items: each order contains between 1 and 5 distinct products.
    item_counts = rng.integers(1, 6, size=n_orders)
    order_item_records = []

    for order_id, item_count in zip(orders["order_id"], item_counts):
        selected_products = rng.choice(
            products["product_id"],
            size=item_count,
            replace=False,
        )

        for product_id in selected_products:
            product_price = products.loc[
                products["product_id"] == product_id, "unit_price"
            ].iloc[0]

            order_item_records.append(
                {
                    "order_id": order_id,
                    "product_id": product_id,
                    "quantity": int(rng.integers(1, 6)),
                    "unit_price": float(product_price),
                    "discount_pct": float(rng.choice([0, 0.05, 0.10, 0.15])),
                }
            )

    order_items = pd.DataFrame(order_item_records)

    datasets = {
        "customers.csv": customers,
        "products.csv": products,
        "orders.csv": orders,
        "order_items.csv": order_items,
    }

    for filename, dataframe in datasets.items():
        dataframe.to_csv(OUTPUT_DIR / filename, index=False, encoding="utf-8")

    print("Synthetic retail data generated successfully.")
    print(f"Output directory: {OUTPUT_DIR}")
    for filename, dataframe in datasets.items():
        print(f"{filename}: {len(dataframe):,} rows")


if __name__ == "__main__":
    generate_data()
