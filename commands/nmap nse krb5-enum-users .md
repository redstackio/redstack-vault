---
id: 5d394b6f-5f89-44f1-bc8b-9ab3b8dc03cc
name: 'nmap nse krb5-enum-users '
type: command
executor: ''
data: nmap -p 88 --script=krb5-enum-users --script-args="krb5-enum-users.realm='$DOMAIN',userdb=$USER_LIST_FILE"
  $IP
output: null
created_at: '2023-01-11T20:26:14.115746+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# nmap nse krb5-enum-users 

```bash
nmap -p 88 --script=krb5-enum-users --script-args="krb5-enum-users.realm='$DOMAIN',userdb=$USER_LIST_FILE" $IP
```
