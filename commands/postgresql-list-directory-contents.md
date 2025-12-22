---
type: command
executor: sql
data: SELECT pg_ls_dir('/etc/');
output: null
platforms:
  - PostgreSQL
tags:
  - discovery
  - file-enumeration
verified: true
validated: true
---

# postgresql-list-directory-contents

## Command

```sql
SELECT pg_ls_dir('/etc/');
```

## Description

Lists the contents of a directory on the PostgreSQL server's file system. Requires superuser privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| '/etc/' | Path to list (absolute or relative to data dir) | Yes |

## Examples

### Basic Usage

```sql
SELECT pg_ls_dir('./');
```

### Advanced Usage

```sql
SELECT pg_ls_dir('/var/log/');
```

## Expected Output

A single-column result with file/directory names, e.g.:

name
----
passwd
shadow
sudoers

## Related

- [[procedures/Read-Files-via-PostgreSQL-Server-Functions]]
