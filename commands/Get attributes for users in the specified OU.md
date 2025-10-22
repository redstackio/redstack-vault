---
id: ecab26e8-443a-403f-9e7b-d267768470ef
name: Get attributes for users in the specified OU
type: command
executor: bash
data: 'dsquery user <OU=PUT OU HERE> -limit 0 |dsget user -dn -samid -display -desc
  -office -tel -email -title -hmdir -profile -loscr -mustchpwd -canchpwd -pwdneverexpires
  -disabled

  '
output: null
created_at: '2020-07-14T18:21:11.826525+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Get attributes for users in the specified OU

```bash
dsquery user <OU=PUT OU HERE> -limit 0 |dsget user -dn -samid -display -desc -office -tel -email -title -hmdir -profile -loscr -mustchpwd -canchpwd -pwdneverexpires -disabled

```
