---
id: 1b86ddb0-e8d0-4a04-915c-ea36124560c2
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:28.695981+00:00'
updated_at: '2023-04-10T20:37:53.214435+00:00'
---

# Code Snippet 1b86ddb0

**Language**: Powershell

```powershell
ipconfig /all
Get-NetIPConfiguration | ft InterfaceAlias,InterfaceDescription,IPv4Address
Get-DnsClientServerAddress -AddressFamily IPv4 | ft
```


