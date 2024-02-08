"""
PL_snowflake_connection_test
DAG auto-generated by Astro Cloud IDE.
"""

from airflow.decorators import dag
from astro import sql as aql
from astro.table import Table, Metadata
import pandas as pd
import pendulum




@aql.run_raw_sql(conn_id="snowflake_sql_conn", task_id="sql_snowflake_sql_conn", results_format="pandas_dataframe")
def sql_snowflake_sql_conn_func():
    return """
    select * from ACADIA_EDW_STG.TEST_DATA_1
    """

@aql.run_raw_sql(conn_id="snowflake_sql_conn", task_id="sql_1", results_format="pandas_dataframe")
def sql_1_func():
    return """
    select * from ACADIA_EDW_STG.TEST_DATA_1
    """

default_args={
    "email": [
        "siddhardha.madda@acadiahealthcare.com",
    ],
    "email_on_retry": True,
    "email_on_failure": True,
    "retries": 2,
    "owner": "Siddhardha Madda,Open in Cloud IDE",
}

@dag(
    default_args=default_args,
    schedule="0-2 * * * *",
    start_date=pendulum.from_format("2024-01-28", "YYYY-MM-DD").in_tz("UTC"),
    catchup=False,
    owner_links={
        "Siddhardha Madda": "mailto:siddhardha.madda@acadiahealthcare.com",
        "Open in Cloud IDE": "https://cloud.astronomer.io/clrpl8m6r01hx01mp5w9ydyy9/cloud-ide/clrxr6ls1002u01kuqliasul6/clrxr74bp007j01ij2im5epoe",
    },
)
def PL_snowflake_connection_test():
    sql_snowflake_sql_conn = sql_snowflake_sql_conn_func()

    sql_1 = sql_1_func()

    sql_1 << sql_snowflake_sql_conn

dag_obj = PL_snowflake_connection_test()
