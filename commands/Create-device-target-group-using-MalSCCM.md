---
id: 914a295e-a552-4e98-8e07-dd1fda2d96de
type: command
executor: powershell
data: 'MalSCCM.exe group /create /groupname:$_GROUP_NAME /grouptype:device'
output: null
created_at: '2023-04-06T03:56:08.126061+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - sccm
  - persistence
verified: true
validated: true
---

# Create-device-target-group-using-MalSCCM

## Command

```powershell
MalSCCM.exe group /create /groupname:$_GROUP_NAME /grouptype:device
```

## Description

Creates a new static device collection in SCCM for targeted deployments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /groupname:$_GROUP_NAME | Name of the new group (e.g., TargetGroup) | Yes |
| /grouptype:device | Specifies device type collection | Yes |

## Examples

### Basic Usage

```powershell
MalSCCM.exe group /create /groupname:TargetGroup /grouptype:device
```

## Expected Output

Group 'TargetGroup' created successfully.
Collection ID: SMS00001

Confirmation of creation.

## Related

- [[procedures/Create-and-Deploy-Malicious-Application-via-SCCM]]
