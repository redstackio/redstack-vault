---
type: code
language: sql
verified: true
platforms:
  - PostgreSQL
tags:
  - file-discovery
  - version-check
validated: true
---

# postgresql-list-dir-and-read-version-file

## Code

```sql
select pg_ls_dir('./');
select pg_read_file('PG_VERSION', 0, 200);
```

## Description

This SQL snippet lists the current directory contents and reads the first 200 bytes of the PG_VERSION file to confirm the PostgreSQL version during reconnaissance.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| './' | Directory path for listing | '/etc/' |
| 'PG_VERSION' | File to read | '/etc/passwd' |
| 0 | Starting offset | 0 |
| 200 | Bytes to read | 1000 |

## Usage

Execute in psql or via SQL injection after gaining database access. Use to map the file system and verify the target PostgreSQL installation before deeper exfiltration.

## Detection

- Log analysis for pg_ls_dir or pg_read_file executions.
- Anomalous queries accessing PG_VERSION or system paths.
- Privilege escalation attempts via these functions.

## Related

- [[procedures/Read-Files-via-PostgreSQL-Server-Functions]]
