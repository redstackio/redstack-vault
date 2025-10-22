---
id: 7897d902-d5fc-496e-b430-90f140008de0
name: Get access scopes if on an instance
type: command
executor: bash
data: 'curl http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/scopes
  -H &#39;Metadata-Flavor:Google’

  '
output: null
created_at: '2020-07-14T19:08:34.230388+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Get access scopes if on an instance

```bash
curl http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/scopes -H &#39;Metadata-Flavor:Google’

```
