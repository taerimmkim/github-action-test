from airflow.models import DagBag
#import pytest

dag_bag = DagBag(dag_folder='./dags/', include_examples=False)

for dag in dag_bag.dags:
    dag.size() 
