---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: create-and-enter-powershell-session-with-credentials
type: command
executor: powershell
data: |-
  $Session = New-PSSession -Credential $Cred -ComputerName $_TARGET_IP
  Enter-PSSession $Session
output: '[$_TARGET_IP]: PS C:\Users\Administrator\Documents> '
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - powershell
  - remote-access
  - lateral-movement
verified: true
validated: true
---

# create-and-enter-powershell-session-with-credentials

## Command

```powershell
$Session = New-PSSession -Credential $Cred -ComputerName $_TARGET_IP
Enter-PSSession $Session
```

## Description

This command establishes a remote PowerShell session using provided credentials and enters it for interactive use. It leverages WinRM to connect to a target Windows machine, allowing remote command execution. Requires a pre-created $Cred object from create-windows-pscredential-object.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $Cred | PSCredential object containing username and password | Yes |
| $_TARGET_IP | IP address or hostname of the remote target | Yes |
| -Credential | Specifies the credentials for authentication | Built-in |
| -ComputerName | Specifies the remote computer | Built-in |

## Examples

### Basic Usage

```powershell
$Session = New-PSSession -Credential $Cred -ComputerName 10.10.10.10
Enter-PSSession $Session
```

### With Hostname

```powershell
$Session = New-PSSession -Credential $Cred -ComputerName TARGETSERVER
Enter-PSSession $Session
```

## Expected Output

First line: Id Name   ComputerName    State         ConfigurationName     Availability
---------- ----   ------------    -----         -----------------     ------------
1          Session 10.10.10.10      Opened        Microsoft.PowerShell     Available

Second line: [10.10.10.10]: PS C:\Users\Administrator\Documents> (interactive remote prompt)

Errors if WinRM is disabled or credentials invalid (e.g., "Connecting to remote server 10.10.10.10 failed with the following error message : Access is denied.").

## Related

- [[procedures/Spawn-Interactive-Shell-with-WinRM-on-Windows]]
