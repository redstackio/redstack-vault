---
id: 62b9fa1d-a790-41bc-8215-cabc185701d4
name: impacket-wmiexec-execute-with-password
type: command
executor: bash
data: 'wmiexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP'
output: null
created_at: '2023-04-06T03:56:30.837321+00:00'
updated_at: '2023-10-10T20:37:57.936960+00:00'
platforms:
  - Windows
tags:
  - impacket
  - remote-execution
  - wmi
verified: true
validated: true
---

# impacket-wmiexec-execute-with-password

## Command

```bash
wmiexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP
```

## Description

Executes commands on remote Windows via WMI using plaintext password authentication. Provides output directly without interactive shell, suitable for scripted operations.

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
wmiexec.py DOMAIN/user:pass@192.168.1.100
```

## Expected Output

Impacket v0.9.24 - Copyright 2020 SecureAuth Corporation

[*] Connecting to 192.168.1.100...
[*] Executing command...
user\domain

## Related

- [[procedures/Remote-Command-Execution-with-Impacket-Using-Credentials]]
- [[tools/Impacket]]
