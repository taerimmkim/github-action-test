from airflow.models import DagBag
import pytest

def test_dag_validation():
    dag_bag = DagBag(dag_folder='./dags/', include_examples=False)
    expected_dag_size = len(dag_bag.dagbag_stats)
    assert dag_bag.size() == expected_dag_size
    
