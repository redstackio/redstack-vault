---
id: afcd05c0-1f68-48c8-97e9-b50855a789bc
name: System Lookup
type: command
executor: bash
data: 'ldapsearch -x -h ldap.domain.com -L -s sub -b ou=ITsystems,ou=computers,o=domain.com
  "(cn=itwks-001.it.domain.com)" <filteroptional>

  '
output: null
created_at: '2020-07-14T18:21:09.675246+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# System Lookup

```bash
ldapsearch -x -h ldap.domain.com -L -s sub -b ou=ITsystems,ou=computers,o=domain.com "(cn=itwks-001.it.domain.com)" <filteroptional>

```


