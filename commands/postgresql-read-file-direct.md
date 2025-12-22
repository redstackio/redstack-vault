---
type: command
executor: sql
data: 'SELECT pg_read_file(''/etc/passwd'', 0, 1000);'
output: null
platforms:
  - PostgreSQL
tags:
  - collection
  - file-read
verified: true
validated: true
---

# postgresql-read-file-direct

## Command

```sql
SELECT pg_read_file('/etc/passwd', 0, 1000);
```

## Description

Reads the contents of a file on the server file system directly into the query result.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| '/etc/passwd' | File path | Yes |
| 0 | Starting byte offset | Yes |
| 1000 | Number of bytes to read | Yes |

## Examples

### Basic Usage

```sql
SELECT pg_read_file('PG_VERSION', 0, 200);
```

### Advanced Usage

```sql
SELECT pg_read_file('/etc/hosts', 0, 4096);
```

## Expected Output

The file contents as a text string, e.g.:

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin

## Related

- [[procedures/Read-Files-via-PostgreSQL-Server-Functions]]
