---
id: c02a0177-8eac-45aa-aac2-3ab5d97dcbdf
name: Retrieve Secrets
type: command
executor: bash
data: 'curl -v -H "Authorization: Bearer <jwt_token>" https://<master_ip>:<port>/api/v1/namespaces/kube-system/secrets/'
output: null
created_at: '2023-04-06T03:56:01.199447+00:00'
updated_at: '2023-04-10T20:34:00.315523+00:00'
---

# Retrieve Secrets

```bash
curl -v -H "Authorization: Bearer <jwt_token>" https://<master_ip>:<port>/api/v1/namespaces/kube-system/secrets/
```
