---
id: 4b4e1f59-1102-42e0-af6a-3e08fb16cde4
name: Set pass as admin
type: command
executor: bash
data: "ldappasswd -H ldaps://ldap.domain.com:6361 -x -D 'cn=admin,ou=hr,ou=users,o=domain.com'\
  \ -S -W 'uid=jdoe,ou=hr users,o=domain.com '   \n"
output: null
created_at: '2020-07-14T18:21:09.675821+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Set pass as admin

```bash
ldappasswd -H ldaps://ldap.domain.com:6361 -x -D 'cn=admin,ou=hr,ou=users,o=domain.com' -S -W 'uid=jdoe,ou=hr users,o=domain.com '   

```


