from __future__ import annotations

import datetime
import os

from airflow import DAG
from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook


ENV_ID = os.environ.get("SYSTEM_TESTS_ENV_ID")
DAG_ID = "daily_report_of_tracks"

with DAG(
        dag_id=DAG_ID,
        start_date=datetime.datetime(2023, 5, 2),
        schedule="@daily",
        catchup=False,
) as dag:
    @task()
    def get_daily_with_hook():
        hook = PostgresHook(postgres_conn_id="postgres_local")
        df = hook.get_pandas_df(sql="SELECT DISTINCT on (plane_id) * FROM track "
                                    "WHERE created_date > current_date - interval '1' day "
                                    "and ground_speed > 0 "
                                    "and track.altitude > 0")
        print(df)
        return df

    get_daily = get_daily_with_hook()

    @task.virtualenv(
        task_id="daily_sql_to_report", requirements=["ydata_profiling"], system_site_packages=False
    )
    def transform_sql_to_report(df: dict):
        import pathlib
        from ydata_profiling import ProfileReport

        profile = ProfileReport(df, title="Flights In Moment Report")
        # profile.to_file(pathlib.Path(__file__).parent.parent / 'app' / 'templates' / "daily_tracks.html") # write to file is not recommended
        print("Finished")

    create_report = transform_sql_to_report(get_daily)

    get_daily >> create_report