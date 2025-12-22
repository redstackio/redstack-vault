---
id: 014e630e-7eee-4d27-ad35-fe71bcf8d5fa
name: invoke-sql-audit-priv-xp-fileexist
type: command
executor: powershell
data: Invoke-SQLAuditPrivXpFileexist
output: null
created_at: '2023-04-06T03:56:20.683465+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - privilege-escalation
  - file-existence
verified: true
validated: true
---

# invoke-sql-audit-priv-xp-fileexist

## Command

```powershell
Invoke-SQLAuditPrivXpFileexist
```

## Description

This PowerShell command checks audit privileges by executing xp_fileexist in MSSQL to determine if specific files exist, useful for reconnaissance in privilege escalation scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (None) | Defaults to a standard path check; customize path in module if needed. | No |

## Examples

### Basic Usage

```powershell
Invoke-SQLAuditPrivXpFileexist
```

### Advanced Usage

Run after SQL connection to probe sensitive files like C:\Windows\system32\config.

## Expected Output

Success: FileStatus (1 if exists, 0 if not), e.g.:

FileName | FileExists | FileIsDirectory | ParentDirectoryExists
--------|------------|-----------------|----------------------
C:\test.txt | 1 | 0 | 1

Failure: Permission denied error.

## Related

- [[procedures/Identify-Trustworthy-Databases-in-MSSQL]]
- [[techniques/System Information Discovery|T1082]]
