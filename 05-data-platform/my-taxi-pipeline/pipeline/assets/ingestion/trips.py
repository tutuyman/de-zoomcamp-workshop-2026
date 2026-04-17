"""@bruin

name: ingestion.trips

type: python

image: python:3.11

# TODO: Set the connection.
connection: duckdb-default

# TODO: Choose materialization (optional, but recommended).
# Bruin feature: Python materialization lets you return a DataFrame (or list[dict]) and Bruin loads it into your destination.
# This is usually the easiest way to build ingestion assets in Bruin.
# Alternative (advanced): you can skip Bruin Python materialization and write a "plain" Python asset that manually writes
# into DuckDB (or another destination) using your own client library and SQL. In that case:
# - you typically omit the `materialization:` block
# - you do NOT need a `materialize()` function; you just run Python code
# Docs: https://getbruin.com/docs/bruin/assets/python#materialization
materialization:
  # TODO: choose `table` or `view` (ingestion generally should be a table)
  type: table
  # TODO: pick a strategy.
  # suggested strategy: append
  strategy: append

# TODO: Define output columns (names + types) for metadata, lineage, and quality checks.
# Tip: mark stable identifiers as `primary_key: true` if you plan to use `merge` later.
# Docs: https://getbruin.com/docs/bruin/assets/columns
columns:
  - name: pickup_datetime
    type: timestamp
    description: "When the meter was engaged"
  - name: dropoff_datetime
    type: timestamp
    description: "When the meter was disengaged"

@bruin"""

import os
import json
import pandas as pd

def materialize():
    start_date = os.environ["BRUIN_START_DATE"]
    end_date = os.environ["BRUIN_END_DATE"]
    taxi_types = json.loads(os.environ["BRUIN_VARS"]).get("taxi_types", ["yellow"])

    # Generate list of months between start and end dates
    start_dt = pd.to_datetime(start_date)
    end_dt = pd.to_datetime(end_date)
    
    # 'MS' frequency ensures we get the start of each month in the range
    months_to_fetch = pd.date_range(start=start_dt.replace(day=1), end=end_dt, freq='MS')

    all_dataframes = []

    # Fetch parquet files from:
    # https://d37ci6vzurychx.cloudfront.net/trip-data/{taxi_type}_tripdata_{year}-{month}.parquet
    for taxi_type in taxi_types:
        for dt in months_to_fetch:
            year = dt.strftime("%Y")
            month = dt.strftime("%m") # ensures 2-digit month (01, 02, etc.)
            
            url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{taxi_type}_tripdata_{year}-{month}.parquet"
            print(f"Attempting to fetch: {url}")
            
            try:
                # read_parquet handles downloading directly from the URL
                df = pd.read_parquet(url)
                print("COLUMNS:", df.columns)
                df = df.rename(columns={
                    "tpep_pickup_datetime": "pickup_datetime",
                    "tpep_dropoff_datetime": "dropoff_datetime",
                    "PULocationID": "pickup_location_id",
                    "DOLocationID": "dropoff_location_id"
                })
                df["taxi_type"] = taxi_type
                all_dataframes.append(df)
                print(f"Success: Fetched {len(df)} rows.")
            except Exception as e:
                print(f"Failed to fetch {url}: {e}")

    # Combine all individual month dataframes into one large dataframe
    if all_dataframes:
        final_dataframe = pd.concat(all_dataframes, ignore_index=True)
    else:
        # Fallback to an empty dataframe if all downloads failed
        final_dataframe = pd.DataFrame()

    return final_dataframe


