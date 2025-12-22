---
id: 37486bec-b5d1-430d-b728-c1d9aa7cc2b9
name: cobalt-strike-remote-exec
type: command
executor: cobalt-strike
data: 'remote-exec [module] [target] [command]'
output: null
created_at: '2023-04-06T03:56:16.551415+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - Lateral-Movement
  - Beacon
verified: true
validated: true
---

# cobalt-strike-remote-exec

## Command

```cobalt-strike
remote-exec [module] [target] [command]
```

## Description

The 'remote-exec' command in Cobalt Strike's Beacon executes arbitrary commands on a remote Windows host without deploying a full payload. It supports methods like PsExec, WinRM, or WMI for non-interactive remote command execution, ideal for quick reconnaissance or staging during lateral movement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| [module] | Execution method: psexec (SMB Service Control Manager), winrm (WinRM PowerShell), wmi (WMI PowerShell) | Yes |
| [target] | IP address or hostname of the remote system | Yes |
| [command] | The command string to execute remotely (e.g., "whoami", "net user") | Yes |

## Examples

### Basic Usage

```cobalt-strike
remote-exec psexec 192.168.1.100 "whoami"
```

Runs 'whoami' via PsExec and returns the output.

### Advanced Usage

```cobalt-strike
remote-exec wmi target.domain.com "net view /domain"
```

Executes domain enumeration via WMI.

## Expected Output

Returns the stdout/stderr from the remote command, e.g.:

```
user@target:> whoami

target\administrator
```

Errors appear as: "[*] Failed to execute: Access denied". Use for commands that produce concise output to avoid Beacon timeouts.

## Related

- [[procedures/Cobalt-Strike-Lateral-Movement-via-Beacon-Remote-Exploits-and-Executes]]
- [[commands/cobalt-strike-jump]]
