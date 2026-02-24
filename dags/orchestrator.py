from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def example_task():
    print("This is an example task.")

default_args = {
    'owner': 'samrat',
}

with DAG(
    dag_id="weather_api_orchestrator",
    default_args=default_args,
    description="A DAG to orchestrate weather data pipeline",
    schedule=timedelta(minutes=1),
    start_date=datetime(2026, 2, 28),
    catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id='example_task',
        python_callable=example_task
    )