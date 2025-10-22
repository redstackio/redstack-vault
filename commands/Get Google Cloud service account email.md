---
id: 2b6b8e3e-b7d4-4244-8329-834c5929864e
name: Get Google Cloud service account email
type: command
executor: bash
data: curl http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/email
output: null
created_at: '2023-04-06T03:56:17.031672+00:00'
updated_at: '2023-04-10T20:33:50.751327+00:00'
---

# Get Google Cloud service account email

```bash
curl http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/email
```
