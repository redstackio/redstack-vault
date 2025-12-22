---
type: command
executor: sql
data: last_insert_rowid()>1
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Database
tags:
  - sql-injection
  - fingerprinting
verified: true
validated: true
---

# sqlite-last-insert-rowid-greater-test

## Command

```sql
last_insert_rowid()>1
```

## Description

Tests SQLite's last_insert_rowid() function (result depends on context; use for syntax check).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed | N/A |

## Examples

### Basic Usage

`' AND last_insert_rowid()>1 --`

## Expected Output

Varies; syntax success indicates SQLite.

## Related

- [[procedures/DBMS-Fingerprinting-via-SQL-Injection]]
- [[commands/sqlite-version-test]]
