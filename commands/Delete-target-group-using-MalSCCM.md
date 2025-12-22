---
id: 3e98470e-3a8f-41db-b260-83ebd863214d
type: command
executor: powershell
data: 'MalSCCM.exe group /delete /groupname:$_GROUP_NAME'
output: null
created_at: '2023-04-06T03:56:08.127114+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - sccm
  - defense-evasion
verified: true
validated: true
---

# Delete-target-group-using-MalSCCM

## Command

```powershell
MalSCCM.exe group /delete /groupname:$_GROUP_NAME
```

## Description

Deletes a device group from SCCM after use.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /groupname:$_GROUP_NAME | Group to delete | Yes |

## Examples

### Basic Usage

```powershell
MalSCCM.exe group /delete /groupname:TargetGroup
```

## Expected Output

Group 'TargetGroup' deleted.

Deletion confirmation.

## Related

- [[procedures/Create-and-Deploy-Malicious-Application-via-SCCM]]
