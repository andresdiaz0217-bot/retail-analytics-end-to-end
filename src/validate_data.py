
from pathlib import Path

import pandas as pd

DATA_DIR = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "synthetic"
)

FILES = {
    "customers": "customers.csv",
    "products": "products.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
}


def load_data():
    """Load the synthetic retail CSV files."""
    data = {}

    for name, filename in FILES.items():
        path = DATA_DIR / filename

        if not path.exists():
            raise FileNotFoundError(f"Missing file: {path}")

        data[name] = pd.read_csv(path)

    return data


def validate_data(data):
    """Run structural and relational data quality checks."""
    customers = data["customers"]
    products = data["products"]
    orders = data["orders"]
    items = data["order_items"]

    checks = {
        "customers_have_unique_ids":
            customers["customer_id"].is_unique,

        "products_have_unique_ids":
            products["product_id"].is_unique,

        "orders_have_unique_ids":
            orders["order_id"].is_unique,

        "order_items_have_unique_order_product_pairs":
            not items.duplicated(
                subset=["order_id", "product_id"]
            ).any(),

        "customers_have_no_null_ids":
            customers["customer_id"].notna().all(),

        "products_have_no_null_ids":
            products["product_id"].notna().all(),

        "orders_have_no_null_ids":
            orders["order_id"].notna().all(),

        "order_items_have_no_null_foreign_keys":
            items[["order_id", "product_id"]]
            .notna().all().all(),

        "orders_reference_existing_customers":
            orders["customer_id"].isin(
                customers["customer_id"]
            ).all(),

        "items_reference_existing_orders":
            items["order_id"].isin(
                orders["order_id"]
            ).all(),

        "items_reference_existing_products":
            items["product_id"].isin(
                products["product_id"]
            ).all(),

        "item_quantities_are_positive":
            items["quantity"].gt(0).all(),

        "item_prices_are_non_negative":
            items["unit_price"].ge(0).all(),

        "discounts_are_between_zero_and_one_hundred":
            items["discount_pct"].between(0, 100).all(),
    }

    print("\nDATASET SUMMARY")
    print("-" * 45)

    for name, dataframe in data.items():
        print(f"{name}: {len(dataframe):,} rows")

    print("\nQUALITY CHECKS")
    print("-" * 45)

    for name, passed in checks.items():
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] {name}")

    failed = [
        name for name, passed in checks.items()
        if not passed
    ]

    passed_count = len(checks) - len(failed)
    print(
        f"\nResult: {passed_count}/{len(checks)} "
        "checks passed"
    )

    if failed:
        raise ValueError(
            f"Data quality checks failed: {failed}"
        )


if __name__ == "__main__":
    datasets = load_data()
    validate_data(datasets)
