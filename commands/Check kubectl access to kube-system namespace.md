---
id: 4ed87fe4-7511-408c-a95e-d41f3176af53
name: Check kubectl access to kube-system namespace
type: command
executor: bash
data: kubectl auth can-i --list --namespace=kube-system
output: null
created_at: '2023-04-06T03:56:01.145417+00:00'
updated_at: '2023-04-10T20:33:58.599683+00:00'
---

# Check kubectl access to kube-system namespace

```bash
kubectl auth can-i --list --namespace=kube-system
```


