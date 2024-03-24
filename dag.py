from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago


default_args={
'owner':'airflow',
'start_date':datetime(2024,03,19),
'depends_on_past':False,
'email':['lakkawardhananjay@gmail.com'],
'email_on_failure':False,
'email_on_retry':False,
'retries':1,
'retry_delay':timedelta(minutes=5)






}
dag=DAG('run_external_script',
        default_args=default_args,
        description='Runs an external Python Script',
        schedule_interval='@daily' ,
        catchup=False)
with dag:
    run_script_task=BashOperator(
       task_id='run_script',
       bash_commands='python C:/Users/Payal/Desktop/loolker/main.py'

    )  
