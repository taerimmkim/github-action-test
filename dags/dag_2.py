from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.python_operator import PythonOperator

from datetime import datetime
import random
import aa

default_args = {
  'owner': 'taerim',
  'start_date': datetime(2022,1,13)
}

value = random.randint(0,9)

def hello2():
  print("hello2")

def bye():
  print("Goodbye world!")

def hello():
  if value > 5:
    hello2()
  else:
    bye()

with DAG('user_branch', default_args=default_args, catchup=False) as dag:
  hello = BranchPythonOperator(task_id='hello', python_callable=hello)
  hello2 = PythonOperator(task_id='hello2', python_callable=hello2)
  bye = PythonOperator(task_id='bye', python_callable=bye)


  hello >> [hello2, bye]
