---
id: 9384fdd8-0c69-4560-8744-c6968354db1e
name: Set pass as self
type: command
executor: bash
data: "ldappasswd -H ldaps://ldap.domain.com:6361 -D 'cn=John Doe (jdoe),ou=hr,ou=users,o=domain.com'\
  \ -S -W -A  \n"
output: null
created_at: '2020-07-14T18:21:09.676024+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Set pass as self

```bash
ldappasswd -H ldaps://ldap.domain.com:6361 -D 'cn=John Doe (jdoe),ou=hr,ou=users,o=domain.com' -S -W -A  

```


