---
id: eec4b56f-e7a2-472b-a84f-6692eec2c101
type: command
executor: powershell
data: 'MalSCCM.exe app /cleanup /name:$_APP_NAME'
output: null
created_at: '2023-04-06T03:56:08.127014+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - sccm
  - defense-evasion
verified: true
validated: true
---

# Cleanup-application-using-MalSCCM

## Command

```powershell
MalSCCM.exe app /cleanup /name:$_APP_NAME
```

## Description

Removes an application and its deployments from SCCM to cover tracks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /name:$_APP_NAME | Application to clean up | Yes |

## Examples

### Basic Usage

```powershell
MalSCCM.exe app /cleanup /name:demoapp
```

## Expected Output

Application 'demoapp' cleaned up successfully.

Removal confirmation.

## Related

- [[procedures/Create-and-Deploy-Malicious-Application-via-SCCM]]
