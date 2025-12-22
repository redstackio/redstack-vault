---
id: 8e9c5e05-d77a-4754-a71f-9c37ca7b2c96
name: new-pssession
type: command
executor: powershell
data: >-
  $session = New-PSSession -ComputerName $_COMPUTER_NAME -Credential
  $_CREDENTIAL
output: null
created_at: '2023-04-06T03:56:31.141189+00:00'
updated_at: '2023-04-10T20:37:59.190248+00:00'
platforms:
  - Windows
tags:
  - pssession
  - remote
verified: true
validated: true
---

# new-pssession

## Command

```powershell
$session = New-PSSession -ComputerName $_COMPUTER_NAME -Credential $_CREDENTIAL
```

## Description

Creates a persistent PowerShell session to a remote Windows machine for subsequent command execution. Requires pre-configured WinRM and trusted hosts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_COMPUTER_NAME | Target hostname or IP | Yes |
| $_CREDENTIAL | PSCredential object (from Get-Credential) | Yes |

## Examples

### Basic Usage

```powershell
$cred = Get-Credential
$session = New-PSSession -ComputerName DC01 -Credential $cred
```

### Multiple Targets

```powershell
$sessions = New-PSSession -ComputerName DC01, CLIENT1 -Credential $cred
```

## Expected Output

Id Name            ComputerName    State         ConfigurationName         Availability
-- ----            ------------    -----         -----------------         ------------
1   Session1       DC01            Opened        Microsoft.PowerShell      Available

## Related

- [[procedures/windows-powershell-remoting-with-pssession]]
- [[commands/invoke-command-on-pssession]]
