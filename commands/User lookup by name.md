---
id: 363c5ac4-587c-4294-b2fe-c2b7d4894c6d
name: User lookup by name
type: command
executor: bash
data: 'ldapsearch -x -h ldap.domain.com -b o=domain.com -s sub ''(&(sn=Tubberville)(givenname=James))''

  '
output: null
created_at: '2020-07-14T18:21:09.675597+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# User lookup by name

```bash
ldapsearch -x -h ldap.domain.com -b o=domain.com -s sub '(&(sn=Tubberville)(givenname=James))'

```


