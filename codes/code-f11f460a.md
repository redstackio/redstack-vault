---
id: f11f460a-ab58-430f-aaf7-264619b3df2a
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:55:54.548805+00:00'
updated_at: '2023-04-06T03:55:54.554614+00:00'
---

# Code Snippet f11f460a

**Language**: Powershell

```powershell
GET /endpoint HTTP/1.1
Host: victim.example.com
Origin: https://evil.com
Cookie: sessionid=... 

HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://evil.com
Access-Control-Allow-Credentials: true 

{"[private API key]"}
```
