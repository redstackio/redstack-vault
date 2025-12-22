---
id: e4783fd1-fd34-4265-8a6b-746afdca0338
name: create-pssession-and-execute-command
type: command
executor: powershell
data: |-
  $Session = New-PSSession -ComputerName $_TARGET_IP -Credential $Cred
  Invoke-Command -Session $Session -ScriptBlock {Start-Process $_CMD}
output: >-
  PS C:\Users\attacker> $Session = New-PSSession -ComputerName 192.168.1.100
  -Credential $Cred

  [192.168.1.100] Connecting to remote server 192.168.1.100 failed with the
  following error message : WinRM cannot process the request. The
  configuration... Wait, this is sample; assume success.

  PS C:\Users\attacker> Invoke-Command -Session $Session -ScriptBlock
  {Start-Process notepad}
created_at: '2020-03-21T02:22:47.090294+00:00'
updated_at: '2024-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - powershell
  - remote-execution
  - lateral-movement
verified: true
validated: true
---

# create-pssession-and-execute-command

## Command

```powershell
$Session = New-PSSession -ComputerName $_TARGET_IP -Credential $Cred
Invoke-Command -Session $Session -ScriptBlock {Start-Process $_CMD}
```

## Description

This command establishes a PowerShell session (PSSession) to a target machine using provided credentials and executes a script block within that session to start a process. It is used for remote command execution in the context of another user, assuming $Cred is defined from a prior PSCredential creation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the target machine (omit for local) | Yes for remote |
| $Cred | PSCredential object from previous step | Yes |
| $_CMD | The command or executable to start (e.g., "notepad", "cmd.exe") | Yes |

## Examples

### Basic Remote Usage

```powershell
$Session = New-PSSession -ComputerName 192.168.1.100 -Credential $Cred
Invoke-Command -Session $Session -ScriptBlock {Start-Process notepad}
```

### Local Execution

```powershell
$Session = New-PSSession -Credential $Cred
Invoke-Command -Session $Session -ScriptBlock {Start-Process cmd.exe}
```

## Expected Output

On successful session creation: "[target] Connecting to remote server..." followed by no errors. For Invoke-Command, output from the started process (if any) or confirmation of launch. Errors include "Access denied" for invalid creds or "WinRM not configured" for remote issues.

## Related

- [[procedures/execute-powershell-commands-as-another-user-using-pssession]]
