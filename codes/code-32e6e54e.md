---
id: 32e6e54e-0cad-4d7c-8148-e3fa7805eb6b
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:55:54.980792+00:00'
updated_at: '2023-04-06T03:55:54.986545+00:00'
---

# Code Snippet 32e6e54e

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


