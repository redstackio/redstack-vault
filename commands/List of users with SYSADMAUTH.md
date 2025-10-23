---
id: a63d2ca4-ab5f-4690-9133-f3ab66ccd754
name: List of users with SYSADMAUTH
type: command
executor: bash
data: select name from SYSIBM.SYSUSERAUTH where SYSADMAUTH = ‘Y’ or SYSADMAUTH = ‘G’
output: null
created_at: '2023-04-06T03:56:32.690174+00:00'
updated_at: '2023-04-10T20:22:02.658518+00:00'
---

# List of users with SYSADMAUTH

```bash
select name from SYSIBM.SYSUSERAUTH where SYSADMAUTH = ‘Y’ or SYSADMAUTH = ‘G’
```


