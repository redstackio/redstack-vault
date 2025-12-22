---
type: command
executor: sql
data: SELECT VERSION();
output: null
platforms:
  - MySQL
tags:
  - database
  - version-check
verified: true
validated: true
---

# mysql-query-server-version

## Command

```sql
SELECT VERSION();
```

## Description

This SQL command queries the MySQL server to return its version string. Use this in a direct database session or adapt it for injection payloads to confirm compatibility with error-based techniques requiring MySQL 4.1 or higher.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Standard SELECT query; no parameters needed. | No |

## Examples

### Basic Usage

```sql
SELECT VERSION();
```

### In Injection Context

Adapt into a payload, e.g., in a numeric field: `1 AND (SELECT VERSION())`

## Expected Output

A single row with the version, e.g., `5.7.44-0ubuntu0.18.04.1` indicating MySQL 5.7.x, which is compatible.

## Related

- [[procedures/MySQL-Error-Based-SQL-Injection-with-Select-for-Version-Extraction]]
