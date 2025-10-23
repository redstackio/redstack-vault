---
id: 1edbfc09-6f55-485f-b0da-cb906684770c
name: Retrieve authorized users in DB2 instance
type: command
executor: bash
data: select distinct(authid) from sysibmadm.privileges
output: null
created_at: '2023-04-06T03:56:32.615891+00:00'
updated_at: '2023-04-10T20:22:05.508378+00:00'
---

# Retrieve authorized users in DB2 instance

```bash
select distinct(authid) from sysibmadm.privileges
```


