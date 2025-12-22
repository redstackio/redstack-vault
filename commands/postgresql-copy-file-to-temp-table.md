---
type: command
executor: sql
data: COPY temp_passwd FROM '/etc/passwd';
output: null
platforms:
  - PostgreSQL
tags:
  - import
  - file-copy
verified: true
validated: true
---

# postgresql-copy-file-to-temp-table

## Command

```sql
COPY temp_passwd FROM '/etc/passwd';
```

## Description

Imports data from a server-side file into a table using COPY.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| temp_passwd | Target table | Yes |
| '/etc/passwd' | Source file path | Yes |

## Examples

### Basic Usage

```sql
COPY temp_passwd FROM '/etc/passwd' WITH (FORMAT text, DELIMITER ',');
```

### Advanced Usage

```sql
COPY temp_logs FROM '/var/log/auth.log';
```

## Expected Output

COPY X (number of rows imported). Errors if file not readable.

## Related

- [[procedures/Read-Files-via-PostgreSQL-Server-Functions]]
