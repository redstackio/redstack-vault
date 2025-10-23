---
id: b1d5cc4d-2b71-4998-8b11-6983f21d77ed
name: Enable SeBackupPrivilege
type: command
executor: bash
data: 'Import-Module .\SeBackupPrivilegeUtils.dll

  Import-Module .\SeBackupPrivilegeCmdLets.dll


  Set-SeBackupPrivilege'
output: null
created_at: '2023-04-06T03:56:06.525831+00:00'
updated_at: '2023-04-10T20:26:17.815665+00:00'
---

# Enable SeBackupPrivilege

```bash
Import-Module .\SeBackupPrivilegeUtils.dll
Import-Module .\SeBackupPrivilegeCmdLets.dll

Set-SeBackupPrivilege
```


