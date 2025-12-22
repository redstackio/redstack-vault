---
id: 723df26d-9051-46ba-9a55-46a10ad6734c
type: command
executor: bash
data: crackmapexec smb $_TARGET_IP -u $_USERNAME -p "$_PASSWORD"
output: null
created_at: '2023-04-06T03:56:30.721910+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - credential-testing
  - smb
  - password
verified: true
validated: true
---

# crackmapexec-smb-with-password

## Command

```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -p "$_PASSWORD"
```

## Description

Tests plaintext password for SMB authentication, suitable for password spraying or known credential validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target IP | Yes |
| -u $_USERNAME | Username | Yes |
| -p "$_PASSWORD" | Plaintext password (quoted if special chars) | Yes |
| smb | SMB protocol | Built-in |

## Examples

### Basic Usage

```bash
crackmapexec smb 192.168.1.100 -u Administrator -p "Password123?"
```

## Expected Output

Success:

SMB                 192.168.1.100:445     100       administrator:Password123?                       [+] Windows Server 2019 (name:DC01)

Failure:

SMB                 192.168.1.100:445     100       administrator:Password123?                       [-] STATUS: LOGON_FAILURE

## Related

- [[procedures/Test-Credentials-Against-Multiple-Protocols-with-CrackMapExec]]
