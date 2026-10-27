
from pathlib import Path
import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data" / "synthetic"

load_dotenv(ROOT_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL is not configured. "
        "Create a .env file in the project root."
    )

engine = create_engine(DATABASE_URL)

TABLES = [
    ("customers", "customers.csv"),
    ("products", "products.csv"),
    ("orders", "orders.csv"),
    ("order_items", "order_items.csv"),
]



def load_table(table_name, filename, connection):
    path = DATA_DIR / filename

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    dataframe = pd.read_csv(path)

    # Convert date columns from text to actual dates
    date_columns = {
        "customers": ["signup_date"],
        "orders": ["order_date"],
    }

    for column in date_columns.get(table_name, []):
        dataframe[column] = pd.to_datetime(
            dataframe[column], errors="raise"
        ).dt.date

    dataframe.to_sql(
        name=table_name,
        con=connection,
        if_exists="append",
        index=False,
        chunksize=1000,
        method="multi",
    )

    print(f"[OK] {table_name}: {len(dataframe):,} rows loaded")


def main():
    # A single transaction prevents a partially loaded dataset
    # if one of the inserts fails.
    with engine.begin() as connection:
        for table_name, filename in TABLES:
            count = connection.execute(
                text(f'SELECT COUNT(*) FROM "{table_name}"')
            ).scalar_one()

            if count > 0:
                raise RuntimeError(
                    f"Table {table_name} is not empty "
                    f"({count} rows). Aborting to avoid duplicates."
                )

        for table_name, filename in TABLES:
            load_table(table_name, filename, connection)

    print("\nAll datasets loaded successfully.")


if __name__ == "__main__":
    try:
        main()
    finally:
        engine.dispose()
