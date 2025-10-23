---
id: a15ea0b5-5a3f-4d1f-b69f-bf4a89449406
name: HTTP GET to /endpoint
type: command
executor: bash
data: 'GET /endpoint HTTP/1.1

  Host: api.internal.example.com

  Origin: https://evil.com

  '
output: null
created_at: '2023-04-06T03:55:55.840833+00:00'
updated_at: '2023-04-10T20:21:22.641662+00:00'
---

# HTTP GET to /endpoint

```bash
GET /endpoint HTTP/1.1
Host: api.internal.example.com
Origin: https://evil.com

```


