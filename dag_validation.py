from airflow.models import DagBag

dag_bag = DagBag(dag_folder='./dags/', include_examples=False)

for dag in dag_bag.dags:
     print(f'"{dag}" DAG is correct!!!')
