---
id: 82e64568-e1a5-43ff-afb0-52d134c4ffe0
name: Retrieve User Object
type: command
executor: bash
data: $UserObject = ([ADSI]("LDAP://CN=User,OU=Users,DC=ad,DC=domain,DC=tld"))
output: null
created_at: '2023-04-06T03:56:06.779340+00:00'
updated_at: '2023-04-10T20:26:00.143985+00:00'
---

# Retrieve User Object

```bash
$UserObject = ([ADSI]("LDAP://CN=User,OU=Users,DC=ad,DC=domain,DC=tld"))
```


