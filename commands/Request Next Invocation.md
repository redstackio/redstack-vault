---
id: 10e92dc7-c31f-4fa1-ae0d-3b7af885fe47
name: Request Next Invocation
type: command
executor: bash
data: curl "http://${AWS_LAMBDA_RUNTIME_API}/2018-06-01/runtime/invocation/next"
output: null
created_at: '2023-04-06T03:56:38.338342+00:00'
updated_at: '2023-04-10T20:24:06.950737+00:00'
---

# Request Next Invocation

```bash
curl "http://${AWS_LAMBDA_RUNTIME_API}/2018-06-01/runtime/invocation/next"
```


