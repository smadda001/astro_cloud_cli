FROM quay.io/astronomer/astro-runtime:10.0.3

ENV AIRFLOW__CORE__ENABLE_XCOM_PICKLING=True
ENV AIRFLOW__ASTRO_SDK__DATAFRAME_ALLOW_UNSAFE_STORAGE=True
ENV AIRFLOW__SCHEDULER__DAG_DIR_LIST_INTERVAL=30
