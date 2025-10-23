---
id: 25e6a25f-de8a-423f-a7c8-b0754fffc5db
name: Retrieve Default Namespace Secrets
type: command
executor: bash
data: '$ curl -k -v -H "Authorization: Bearer <jwt_token>" https://<master_ip>:<port>/api/v1/namespaces/default/secrets/'
output: null
created_at: '2023-04-06T03:56:01.357661+00:00'
updated_at: '2023-04-10T20:33:59.621982+00:00'
---

# Retrieve Default Namespace Secrets

```bash
$ curl -k -v -H "Authorization: Bearer <jwt_token>" https://<master_ip>:<port>/api/v1/namespaces/default/secrets/
```


