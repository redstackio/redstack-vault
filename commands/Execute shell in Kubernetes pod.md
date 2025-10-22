---
id: 4b154013-95b8-434b-a9c7-0a85ffbd4039
name: Execute shell in Kubernetes pod
type: command
executor: bash
data: kubectl exec -it <POD NAME> -n <PODS NAMESPACE> -- sh
output: null
created_at: '2023-04-06T03:56:01.280289+00:00'
updated_at: '2023-04-10T20:34:05.504277+00:00'
---

# Execute shell in Kubernetes pod

```bash
kubectl exec -it <POD NAME> -n <PODS NAMESPACE> -- sh
```
