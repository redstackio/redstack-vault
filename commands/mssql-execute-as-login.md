---
id: 41318e61-cf9e-437d-8138-06daf7f7c7ef
name: mssql-execute-as-login
type: command
executor: sql
data: EXECUTE AS LOGIN = '$_TARGET_LOGIN';
output: null
created_at: '2023-04-06T03:56:21.034204+00:00'
updated_at: '2023-04-10T20:36:37.208885+00:00'
platforms:
  - Windows
tags:
  - impersonation
  - mssql
  - privilege-escalation
verified: true
validated: true
---

# mssql-execute-as-login

## Command

```sql
EXECUTE AS LOGIN = '$_TARGET_LOGIN';
```

## Description

This command switches the execution context to the specified login, allowing queries to run under its privileges. Requires IMPERSONATE permission on the target login.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_LOGIN | Name of the login to impersonate (e.g., 'adminuser') | Yes |

## Examples

### Basic Usage

```sql
EXECUTE AS LOGIN = 'adminuser';
```

### With Domain Login

```sql
EXECUTE AS LOGIN = 'domain\\adminuser';
```

## Expected Output

No output on success; errors if permission denied, e.g., 'Principal "lowpriv" does not have permission to impersonate "adminuser".'

## Related

- [[procedures/mssql-impersonation-credential-check]]
- [[commands/mssql-select-original-login]]
