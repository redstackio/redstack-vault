---
id: 015f4b3e-a12d-4218-be01-de670a206b7e
type: code
language: batch
verified: false
created_at: '2023-04-06T03:56:29.173607+00:00'
updated_at: '2023-04-10T20:37:43.134194+00:00'
---

# Code Snippet 015f4b3e

**Language**: batch

```batch
cls & echo. & for /f "tokens=4 delims=: " %a in ('netsh wlan show profiles ^| find "Profile "') do @echo off > nul & (netsh wlan show profiles name=%a key=clear | findstr "SSID Cipher Content" | find /v "Number" & echo.) & @echo on
```
