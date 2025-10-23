---
id: 82de18a3-911b-4352-96bf-e9501b922378
name: List default namespace daemonsets
type: command
executor: bash
data: 'curl -v -H "Authorization: Bearer <jwt_token>" https://<master_ip>:<port>/apis/extensions/v1beta1/namespaces/default/daemonsets

  '
output: null
created_at: '2023-04-06T03:56:01.386360+00:00'
updated_at: '2023-04-10T20:34:01.659280+00:00'
---

# List default namespace daemonsets

```bash
curl -v -H "Authorization: Bearer <jwt_token>" https://<master_ip>:<port>/apis/extensions/v1beta1/namespaces/default/daemonsets

```


