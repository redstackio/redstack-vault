---
data: sqlite3 db.sqlite3
tags:
  - database
  - sqlite
type: command
output: SQLite command prompt (sqlite>)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.650Z'
id: 27e16d41-779a-46a5-b520-a0e76013127c
verified: false
validated: true
submitted: true
---
# sqlite3-open-db

## Command

```bash
sqlite3 db.sqlite3
```

## Description

Opens the SQLite database shell for the specified file, allowing interaction with Django's database for cache manipulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| db.sqlite3 | Path to the SQLite database file | Yes |

## Examples

### Basic Usage

```bash
sqlite3 db.sqlite3
```

### Advanced Usage

```bash
sqlite3 -header db.sqlite3
```

> Adds headers to query output.

## Expected Output

SQLite command prompt (sqlite>).

## Related

- [[Related Procedure]]
