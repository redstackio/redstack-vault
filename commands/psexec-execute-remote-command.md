---
type: command
executor: cmd
data: psexec.exe \\$_TARGET -u $_USERNAME -p $_PASSWORD $_COMMAND
output: null
platforms:
  - Windows
tags:
  - psexec
  - remote-execution
verified: true
validated: true
---

# psexec-execute-remote-command

## Command

```cmd
psexec.exe \\$_TARGET -u $_USERNAME -p $_PASSWORD $_COMMAND
```

## Description

Executes a specified command on a remote Windows host using PSExec, authenticating with provided credentials. Useful for quick remote shell access or running diagnostics.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | Target hostname or IP (e.g., 192.168.1.100) | Yes |
| -u $_USERNAME | Username for authentication (e.g., Administrator) | Yes |
| -p $_PASSWORD | Password for the user | Yes |
| $_COMMAND | Command to execute (e.g., cmd.exe /c whoami) | Yes |

## Examples

### Basic Usage

```cmd
psexec.exe \\192.168.1.100 -u Administrator -p Pass123 cmd.exe /c whoami
```

### Advanced Usage

```cmd
psexec.exe \\target -u user -p pass -d -i net user hacker Pass123 /add
```

(-d for detached, -i for interactive)

## Expected Output

Command output from the remote host, e.g.:

target\\Administrator

If failed: 'Access denied' or connection errors.

## Related

- [[procedures/windows-impacket-psexec-remote-execution-with-credentials]]
- [[tools/PSExec]]
