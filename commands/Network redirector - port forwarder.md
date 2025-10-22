---
id: 3248f76a-502d-4576-b717-3fdd0f92aa61
name: Network redirector / port forwarder
type: command
executor: bash
data: socat tcp-listen:135,reuseaddr,fork tcp:10.0.0.3:9999
output: null
created_at: '2023-04-06T03:56:30.201549+00:00'
updated_at: '2023-04-10T20:37:35.154793+00:00'
---

# Network redirector / port forwarder

```bash
socat tcp-listen:135,reuseaddr,fork tcp:10.0.0.3:9999
```
