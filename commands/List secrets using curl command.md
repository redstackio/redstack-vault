---
id: a145947a-3e57-4644-a6c5-4c4566de62a6
name: List secrets using curl command
type: command
executor: bash
data: 'curl -v -H "Authorization: Bearer <jwt_token>" https://<master_ip>:<port>/api/v1/namespaces/default/secrets/'
output: null
created_at: '2023-04-06T03:56:01.386048+00:00'
updated_at: '2023-04-10T20:34:01.659280+00:00'
---

# List secrets using curl command

```bash
curl -v -H "Authorization: Bearer <jwt_token>" https://<master_ip>:<port>/api/v1/namespaces/default/secrets/
```
