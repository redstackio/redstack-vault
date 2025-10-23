---
id: 896c6ce3-5e2d-445a-9a62-c5817fce78c9
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:55:54.324142+00:00'
updated_at: '2023-04-06T03:55:54.329455+00:00'
---

# Code Snippet 896c6ce3

**Language**: Powershell

```powershell
GET /endpoint HTTP/1.1
Host: api.internal.example.com
Origin: https://evil.com

HTTP/1.1 200 OK
Access-Control-Allow-Origin: *

{"[private API key]"}
```


