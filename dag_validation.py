from airflow.models import DagBag
import pytest

def test_dag_validation():
    dag_bag = DagBag(dag_folder='./dags/', include_examples=False)
    
    # print(dag_bag.dagbag_report())
    #for dag in dag_bag.bags:
        #assert dags.keys() != ''
    #    print(dag.keys())

test_dag_validation()

#for dag in dag_bag.dags:
#    dag.size() 
