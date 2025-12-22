---
id: a60d5f8b-448e-4eb1-a53e-b7ff1bd55e55
name: mssql-select-original-login
type: command
executor: sql
data: SELECT ORIGINAL_LOGIN();
output: null
created_at: '2023-04-06T03:56:21.034371+00:00'
updated_at: '2023-04-10T20:36:37.208885+00:00'
platforms:
  - Windows
tags:
  - discovery
  - mssql
verified: true
validated: true
---

# mssql-select-original-login

## Command

```sql
SELECT ORIGINAL_LOGIN();
```

## Description

This command retrieves the original login used to connect to the SQL Server instance, useful after impersonation to track the session's root context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; executes in current context | Yes |

## Examples

### Basic Usage

```sql
SELECT ORIGINAL_LOGIN();
```

### Post-Impersonation

Run after EXECUTE AS to confirm original identity.

## Expected Output

The initial login name, e.g.:

ORIGINAL_LOGIN()
---------------
domain\\lowprivuser

## Related

- [[procedures/mssql-impersonation-credential-check]]
- [[commands/mssql-execute-as-login]]
