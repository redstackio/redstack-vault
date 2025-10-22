---
id: 38610624-0e9f-4a42-b6c4-44950eca6426
name: Check if SMB signing is enabled
type: command
executor: bash
data: Get-SmbServerConfiguration | Select-Object -ExpandProperty 'EnableSMBSigning'
output: null
created_at: '2023-04-06T03:56:05.363134+00:00'
updated_at: '2023-04-10T20:26:21.879066+00:00'
---

# Check if SMB signing is enabled

```bash
Get-SmbServerConfiguration | Select-Object -ExpandProperty 'EnableSMBSigning'
```
