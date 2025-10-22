---
id: 07d72816-7ce6-465b-a8ae-7c3167f2a106
name: Basic User info
type: command
executor: bash
data: 'Get-NetUser -UACFilter NOT_ACCOUNTDISABLE | select samaccountname, description,
  pwdlastset, logoncount, badpwdcount

  '
output: null
created_at: '2020-07-15T19:06:26.862365+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Basic User info

```bash
Get-NetUser -UACFilter NOT_ACCOUNTDISABLE | select samaccountname, description, pwdlastset, logoncount, badpwdcount

```
