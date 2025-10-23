---
id: 0443d3d7-e82f-44fe-9a9d-7ceb406bd5d1
name: User lookup by UID
type: command
executor: bash
data: 'ldapsearch -x -h ldap.domain.com -b o=domain.com -s sub uid=jdoe| egrep "uid:|uidnumber:|gidnumber:|cn:|gecos:|description:|loginshell:|homedirectory:"

  '
output: null
created_at: '2020-07-14T18:21:09.675384+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# User lookup by UID

```bash
ldapsearch -x -h ldap.domain.com -b o=domain.com -s sub uid=jdoe| egrep "uid:|uidnumber:|gidnumber:|cn:|gecos:|description:|loginshell:|homedirectory:"

```


