# k8s-dynamic-workers-monorepo
Monolithic repository approach to project regarding dynamic workers in K8s 

## Project structure
```text
├── .github
|     └── workflows
|           └── build-and-push.yml
├── Containerfile
├── Helm-Chart
|     ├── Chart.yaml
|     ├── templates
|     |     ├── configmap.yaml
|     |     └── deployment.yaml
|     └── values.yaml
├── README.md
├── src
|     ├── main.py
|     └── queries
|           ├── __init__.py
|           ├── mysql.py
|           ├── oracle.py
|           └── postgres.py
```
