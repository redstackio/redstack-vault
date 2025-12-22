---
id: e4783fd1-fd34-4265-8a6b-746afdca0338
name: create-powershell-session-and-execute-command
type: command
executor: powershell
data: |-
  $Session = New-PSSession -ComputerName $_TARGET_IP -Credential $Cred
  Invoke-Command -Session $Session -ScriptBlock {Start-Process $_CMD}
output: >-
  PS C:\> $Session = New-PSSession -ComputerName 10.10.10.10 -Credential $Cred

  Id Name            ComputerName    ComputerType    State

  -- ----            ------------    ------------    -----

  2  Session2        10.10.10.10     RemoteMachine   Opened


  PS C:\> Invoke-Command -Session $Session -ScriptBlock {Start-Process
  notepad.exe}
created_at: '2020-03-21T02:22:47.090294+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - powershell
  - remote-execution
  - winrm
verified: true
validated: true
---

# create-powershell-session-and-execute-command

## Command

```powershell
$Session = New-PSSession -ComputerName $_TARGET_IP -Credential $Cred
Invoke-Command -Session $Session -ScriptBlock {Start-Process $_CMD}
```

## Description

This command establishes a PowerShell remoting session to a remote Windows host using WinRM and executes a command via Invoke-Command. The Start-Process wrapper runs the command in the background; omit it for direct execution and output capture.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the remote system | Yes |
| $Cred | PSCredential object from credential creation | Yes |
| $_CMD | Command or executable to run (e.g., 'whoami' or 'notepad.exe') | Yes |
| -ComputerName | Specifies the target for the session | Yes |
| -Credential | Provides authentication credentials | Yes |
| -Session | References the established PSSession for invocation | Yes |
| -ScriptBlock | Defines the code to execute remotely | Yes |

## Examples

### Basic Usage

```powershell
$Session = New-PSSession -ComputerName 192.168.1.100 -Credential $Cred
Invoke-Command -Session $Session -ScriptBlock {whoami}
```

### Advanced Usage (Synchronous Execution)

Omit Start-Process for output:

```powershell
Invoke-Command -Session $Session -ScriptBlock {Get-Process}
```

## Expected Output

Session creation shows session details; invocation returns command output if synchronous.

```
Id Name            ComputerName    ComputerType    State
-- ----            ------------    ------------    -----
2  Session2        10.10.10.10     RemoteMachine   Opened

CONTOSO\user
```

## Related

- [[procedures/execute-command-on-remote-system-with-winrm]]
- [[commands/create-windows-pscredential-object]]
