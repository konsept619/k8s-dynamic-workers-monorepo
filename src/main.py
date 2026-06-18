import os
import time
from datetime import datetime
import importlib

VARIABLES_TO_CHECK = [
    "DBUSER", "DB_TYPE",
    "BKTNAME", "LOGLEVEL", "HTTP_PROXY_MOCK", "HTTPS_PROXY_MOCK"
]

def print_status():
    print(f"\n--- Forcing change in global scope 13:21 ---")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n--- ETL Status Check: {now} ---")

    print("[Env Vars]:")
    for var in VARIABLES_TO_CHECK:
        value = os.getenv(var, "NOT SET")
        print(f"  {var}: {value}")

def print_query():
    etl_db_type = os.environ.get("DB_TYPE", "mysql").lower()

    try:
        query_module = importlib.import_module(f"queries.{etl_db_type}")
        query_module.run_query()
    except ModuleNotFoundError:
        print(f"Error: No module named 'queries.{etl_db_type}' found.")
    except Exception as e:
        print(f"Error during query execution: {e}")

if __name__ == "__main__":
    print("ETL Application Container Started.")
    try:
        while True:
            print_status()
            print_query()
            time.sleep(120)
    except KeyboardInterrupt:
        print("\nETL Application Container Stopped gracefully.")
