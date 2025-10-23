---
id: 0a38f52e-cebf-4724-9c29-fd19748b22d9
name: API Endpoint Request
type: command
executor: bash
data: 'GET /endpoint HTTP/1.1

  Host: api.internal.example.com

  Origin: https://evil.com


  '
output: null
created_at: '2023-04-06T03:55:54.678340+00:00'
updated_at: '2023-04-06T03:55:54.684690+00:00'
---

# API Endpoint Request

```bash
GET /endpoint HTTP/1.1
Host: api.internal.example.com
Origin: https://evil.com


```


