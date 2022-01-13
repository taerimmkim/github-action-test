from airflow.models import DagBag
import pytest

def test_dag_validation():
    dag_bag = DagBag(dag_folder='./dags/', include_examples=False)
    assert dag_bag

#for dag in dag_bag.dags:
#    dag.size() 
