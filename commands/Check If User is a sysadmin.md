---
id: 3c98c47e-dfb6-4362-ae52-591d32a338a4
name: Check If User is a sysadmin
type: command
executor: bash
data: '-- possible roles: sysadmin, serveradmin, dbcreator, setupadmin, bulkadmin,
  securityadmin, diskadmin, public, processadmin

  SELECT is_srvrolemember(''sysadmin'');'
output: null
created_at: '2023-04-06T03:56:34.157965+00:00'
updated_at: '2023-04-10T20:22:47.331484+00:00'
---

# Check If User is a sysadmin

```bash
-- possible roles: sysadmin, serveradmin, dbcreator, setupadmin, bulkadmin, securityadmin, diskadmin, public, processadmin
SELECT is_srvrolemember('sysadmin');
```


