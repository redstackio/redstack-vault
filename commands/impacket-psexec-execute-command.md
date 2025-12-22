---
id: 38309923-07c9-4754-b57e-99be35c5a09a
name: impacket-psexec-execute-command
type: command
executor: bash
data: 'psexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP'
output: null
created_at: '2023-04-06T03:56:30.836836+00:00'
updated_at: '2023-10-10T20:37:57.936960+00:00'
platforms:
  - Windows
tags:
  - impacket
  - remote-execution
  - psexec
verified: true
validated: true
---

# impacket-psexec-execute-command

## Command

```bash
psexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP
```

## Description

Implements PsExec functionality via Impacket, uploading a service binary for remote command execution and interactive shell. Requires SMB write access to ADMIN$.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain name | Yes (or empty for local) |
| $_USERNAME | Username for authentication | Yes |
| $_PASSWORD | Password for authentication | Yes |
| $_TARGET_IP | IP address or hostname of target | Yes |
| -debug | Enable debug output | No |

## Examples

### Basic Usage

```bash
psexec.py DOMAIN/user:pass@192.168.1.100
```

## Expected Output

Impacket v0.9.24 - Copyright 2020 SecureAuth Corporation

[*] Requesting shares on 192.168.1.100.....
[*] Found writable share ADMIN$
[*] Uploading file RemComSvc.exe
[*] Opening SVCManager on 192.168.1.100...
[*] Created \TEMP\RemComSvc
C:\Windows\system32>

## Related

- [[procedures/Remote-Command-Execution-with-Impacket-Using-Credentials]]
- [[tools/Impacket]]
