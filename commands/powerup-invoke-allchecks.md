---
id: b11d3fca-73ae-42e7-be63-79a2ca582b38
name: powerup-invoke-allchecks
type: command
executor: powershell
data: Import-Module PowerUp.ps1; Invoke-AllChecks
output: null
created_at: '2023-01-12T04:55:30.127797+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - enumeration
verified: true
validated: true
---

# powerup-invoke-allchecks

## Command

```powershell
Import-Module PowerUp.ps1; Invoke-AllChecks
```

## Description

This command imports the PowerUp module from PowerSploit and runs Invoke-AllChecks, which performs a comprehensive enumeration of the local Windows system for privilege escalation opportunities, including service misconfigurations, weak permissions, and abuse functions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Import-Module PowerUp.ps1 | Loads the PowerUp script (assumes PowerUp.ps1 is in current directory or path) | Yes |
| Invoke-AllChecks | Executes all PowerUp checks without additional parameters | Yes |

## Examples

### Basic Usage

```powershell
Import-Module PowerUp.ps1; Invoke-AllChecks
```

### With Execution Policy Bypass

```powershell
powershell.exe -ExecutionPolicy Bypass -File PowerUp.ps1; Invoke-AllChecks
```

## Expected Output

A detailed console report with sections like "Service Permissions", "Abuse Functions", and "Unquoted Service Paths". For example:

Service Permissions              : VulnService (FullControl)
Abuse Functions                  : SERVICE_CHANGE_CONFIG on TargetService

Look for services listed under abuse functions where current user has modify access.

## Related

- [[procedures/Search-and-Exploit-Service-Abuse-Functions]]
- [[tools/PowerSploit]]
