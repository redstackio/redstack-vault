---
id: 19ab4b20-88fb-4ec4-868c-fe29d5f28576
name: invoke-sql-audit-priv-xp-dirtree
type: command
executor: powershell
data: Invoke-SQLAuditPrivXpDirtree
output: null
created_at: '2023-04-06T03:56:20.683320+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - privilege-escalation
  - directory-traversal
verified: true
validated: true
---

# invoke-sql-audit-priv-xp-dirtree

## Command

```powershell
Invoke-SQLAuditPrivXpDirtree
```

## Description

This PowerShell command tests for audit privileges by invoking the xp_dirtree extended stored procedure in MSSQL, enabling directory traversal and file listing to assess escalation potential.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (None) | Runs with default connected instance; no explicit parameters needed if session is established. | No |

## Examples

### Basic Usage

```powershell
Invoke-SQLAuditPrivXpDirtree
```

### Advanced Usage

Connect first via Invoke-Sqlcmd, then run the command in the session context.

## Expected Output

If successful, outputs a table of subdirectories and files, e.g.:

subdirectory | depth | file
------------|-------|-----
Program Files | 1 | NULL
Windows | 1 | NULL

Failure: Error message like "The EXECUTE permission was denied on the object 'xp_dirtree'.

## Related

- [[procedures/Identify-Trustworthy-Databases-in-MSSQL]]
- [[techniques/System Information Discovery|T1082]]
