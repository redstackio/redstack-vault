---
id: eb5cc012-e3e3-4f2a-b3a9-3c37fa8a4a07
name: invoke-sql-unc-path-injection
type: command
executor: powershell
data: Invoke-SQLUncPathInjection
output: null
created_at: '2023-04-06T03:56:20.683386+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - privilege-escalation
  - unc-injection
verified: true
validated: true
---

# invoke-sql-unc-path-injection

## Command

```powershell
Invoke-SQLUncPathInjection
```

## Description

This PowerShell command tests for UNC path injection vulnerabilities in MSSQL by attempting to access remote shares via SQL, confirming network-based privilege escalation opportunities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (None) | Uses default UNC path; module may allow custom share specification. | No |

## Examples

### Basic Usage

```powershell
Invoke-SQLUncPathInjection
```

### Advanced Usage

Target a controlled SMB share for exfiltration testing.

## Expected Output

Success: Retrieved file contents or access confirmation, e.g. "File accessed via \\attacker\share\test.txt".

Failure: Access denied or path not found error.

## Related

- [[procedures/Identify-Trustworthy-Databases-in-MSSQL]]
- [[techniques/System Information Discovery|T1082]]
