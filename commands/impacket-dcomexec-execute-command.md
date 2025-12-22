---
id: 8fd246e1-5781-4b4a-b93f-020c8b289f8e
name: impacket-dcomexec-execute-command
type: command
executor: bash
data: 'dcomexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP'
output: null
created_at: '2023-04-06T03:56:30.837339+00:00'
updated_at: '2023-10-10T20:37:57.936960+00:00'
platforms:
  - Windows
tags:
  - impacket
  - remote-execution
  - dcom
verified: true
validated: true
---

# impacket-dcomexec-execute-command

## Command

```bash
dcomexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP
```

## Description

Executes commands via DCOM/RPC on remote Windows systems, providing a semi-interactive shell. Relies on RPC endpoint mapper (port 135) and dynamic ports.

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
dcomexec.py DOMAIN/user:pass@192.168.1.100
```

## Expected Output

Impacket v0.9.24 - Copyright 2020 SecureAuth Corporation

[*] RPC Pipe DCERPC-WMI available
Microsoft Windows [Version 10.0.19041.1320]
(c) Microsoft Corporation. All rights reserved.

C:\Windows\system32>

## Related

- [[procedures/Remote-Command-Execution-with-Impacket-Using-Credentials]]
- [[tools/Impacket]]
