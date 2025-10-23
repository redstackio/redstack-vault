---
id: 16bf0fb3-71d5-4537-aa74-2b8b8d4ec91d
name: Metadata Service URL
type: command
executor: bash
data: 'curl "http://metadata.google.internal/computeMetadata/v1/?recursive=true&alt=text"
  -H "Metadata-Flavor: Google"

  '
output: null
created_at: '2020-07-14T19:08:34.244216+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Metadata Service URL

```bash
curl "http://metadata.google.internal/computeMetadata/v1/?recursive=true&alt=text" -H "Metadata-Flavor: Google"

```


