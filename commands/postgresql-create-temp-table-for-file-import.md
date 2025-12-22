---
type: command
executor: sql
data: CREATE TEMP TABLE temp_passwd (line TEXT);
output: null
platforms:
  - PostgreSQL
tags:
  - setup
  - temp-table
verified: true
validated: true
---

# postgresql-create-temp-table-for-file-import

## Command

```sql
CREATE TEMP TABLE temp_passwd (line TEXT);
```

## Description

Creates a temporary table to stage file data for import via COPY.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| temp_passwd | Table name | Yes |
| line TEXT | Column definition | Yes |

## Examples

### Basic Usage

```sql
CREATE TEMP TABLE temp_file (content TEXT);
```

### Advanced Usage

```sql
CREATE TEMP TABLE temp_logs (line TEXT, timestamp TIMESTAMP);
```

## Expected Output

No output; table created successfully. Verify with \dt in psql.

## Related

- [[procedures/Read-Files-via-PostgreSQL-Server-Functions]]
