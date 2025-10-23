---
id: 16a6468d-fb87-44cd-b4a3-75a50ebf50c5
name: Check Kubernetes API Health
type: command
executor: bash
data: curl -k https://<IP Address>:6443/healthz
output: null
created_at: '2023-04-06T03:56:01.450991+00:00'
updated_at: '2023-04-10T20:34:06.193303+00:00'
---

# Check Kubernetes API Health

```bash
curl -k https://<IP Address>:6443/healthz
```


