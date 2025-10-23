---
id: 4627e20e-1704-46d2-9994-1755adb85875
name: List Pods
type: command
executor: bash
data: 'curl -v -H "Authorization: Bearer <jwt_token>" https://<master_ip>:<port>/api/v1/namespaces/default/pods/'
output: null
created_at: '2023-04-06T03:56:01.385942+00:00'
updated_at: '2023-04-10T20:34:01.659280+00:00'
---

# List Pods

```bash
curl -v -H "Authorization: Bearer <jwt_token>" https://<master_ip>:<port>/api/v1/namespaces/default/pods/
```


