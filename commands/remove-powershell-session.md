---
id: b87daec2-c7ac-4572-ab10-b4160676d15d
name: remove-powershell-session
type: command
executor: powershell
data: Remove-PSSession $Session
output: |-
  PS C:\> Remove-PSSession $Session
  Id Name            ComputerName    ComputerType    State
  -- ----            ------------    ------------    -----
  2  Session2        10.10.10.10     RemoteMachine   Closed
created_at: '2020-03-21T01:59:57.750419+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - powershell
  - cleanup
  - winrm
verified: true
validated: true
---

# remove-powershell-session

## Command

```powershell
Remove-PSSession $Session
```

## Description

This command terminates an active PowerShell remoting session, closing the connection to the remote host and freeing resources. Use it after remote command execution to minimize detection risks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $Session | The PSSession object to remove (from New-PSSession) | Yes |

## Examples

### Basic Usage

```powershell
Remove-PSSession $Session
```

### Advanced Usage (Remove All Sessions)

```powershell
Get-PSSession | Remove-PSSession
```

## Expected Output

Displays the closed session details.

```
Id Name            ComputerName    ComputerType    State
-- ----            ------------    ------------    -----
2  Session2        10.10.10.10     RemoteMachine   Closed
```

## Related

- [[procedures/execute-command-on-remote-system-with-winrm]]
- [[commands/create-powershell-session-and-execute-command]]
