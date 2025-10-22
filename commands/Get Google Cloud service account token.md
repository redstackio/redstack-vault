---
id: 6d506d49-ae20-4674-b686-19ad6bb34c84
name: Get Google Cloud service account token
type: command
executor: bash
data: curl -s http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token
output: null
created_at: '2023-04-06T03:56:17.031725+00:00'
updated_at: '2023-04-10T20:33:50.751327+00:00'
---

# Get Google Cloud service account token

```bash
curl -s http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token
```
