---
id: ad527cd1-fdea-4025-927a-c26d4689a4ef
name: List members of a group (Global Admins in this case)
type: command
executor: bash
data: 'Get-MsolRole -RoleName "Company Administrator"

  Get-MSolGroupMember –GroupObjectId $GUID

  '
output: null
created_at: '2020-07-14T19:07:50.920601+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# List members of a group (Global Admins in this case)

```bash
Get-MsolRole -RoleName "Company Administrator"
Get-MSolGroupMember –GroupObjectId $GUID

```
