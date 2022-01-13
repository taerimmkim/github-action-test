from airflow.models import DagBag

dag_bag = DagBag(dag_folder='./dags/', include_examples=False)

try:
  for dag in dag_bag.dags:
    print(f'"{dag}" DAG is correct!!!')
except Exceptione as e:
  print(f'"{dag}" DAG raises "{e}" errors!!!')


