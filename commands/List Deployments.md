---
id: b40beea3-5d7a-415a-bc5d-0c98509b4b2e
name: List Deployments
type: command
executor: bash
data: 'curl -v -H "Authorization: Bearer <jwt_token>" https://<master_ip>:<port>/apis/extensions/v1beta1/namespaces/default/deployments

  '
output: null
created_at: '2023-04-06T03:56:01.386182+00:00'
updated_at: '2023-04-10T20:34:01.659280+00:00'
---

# List Deployments

```bash
curl -v -H "Authorization: Bearer <jwt_token>" https://<master_ip>:<port>/apis/extensions/v1beta1/namespaces/default/deployments

```


