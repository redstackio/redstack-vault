---
type: procedure
description: >-
  Extract sensitive files from the PostgreSQL server file system using built-in
  functions like pg_read_file, COPY, and large objects.
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
  - '[[techniques/Data from Local System|T1005 - Data from Local System]]'
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques: []
tags:
  - postgresql
  - file-read
  - sql-exploitation
  - database-exfiltration
commands:
  - '[[commands/postgresql-list-directory-contents]]'
  - '[[commands/postgresql-read-file-direct]]'
  - '[[commands/postgresql-create-temp-table-for-file-import]]'
  - '[[commands/postgresql-copy-file-to-temp-table]]'
  - '[[commands/postgresql-select-from-temp-table]]'
  - '[[commands/postgresql-import-file-as-large-object]]'
  - '[[commands/postgresql-retrieve-large-object-by-oid]]'
  - '[[commands/postgresql-list-all-large-objects]]'
platforms:
  - Linux
  - PostgreSQL
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Read-Files-via-PostgreSQL-Server-Functions

## Summary

This procedure exploits PostgreSQL's built-in file system access functions to read sensitive files on the server, such as /etc/passwd or configuration files. It is typically used in SQL injection scenarios or when an attacker has authenticated access to the database with sufficient privileges (e.g., superuser). Methods include direct file reading with pg_read_file, importing via COPY to a temp table, and using large objects with lo_import/lo_get.

## Description

PostgreSQL provides server-side functions that allow reading the file system when executed with appropriate privileges. This procedure covers multiple techniques to bypass restrictions and exfiltrate data: listing directories with pg_ls_dir, reading files directly, using COPY for text files, and large objects for binary or restricted files. It targets Linux-based PostgreSQL installations where the database runs with access to system files. Success depends on the database user's permissions; superuser access enables full file system read. This can lead to credential theft, configuration leakage, or further lateral movement.

## Requirements

1. Authenticated access to PostgreSQL (via psql or SQL injection vector) with superuser privileges or roles allowing file access (e.g., pg_read_server_files).
2. Target PostgreSQL version 8.1+ (pg_read_file) or 9.0+ (lo_import enhancements).
3. Knowledge of file paths on the target system (e.g., /etc/passwd for user enumeration).
4. SQL client like psql or a web-based injection tool.

## Defense

Defensive measures and detection strategies:

- Run PostgreSQL as a low-privilege user without file system access; use SELinux/AppArmor to restrict database to its data directory.
- Disable or revoke superuser privileges for application accounts; audit roles with pg_has_role.
- Enable logging of all SQL statements (log_statement = 'all') and monitor for pg_read_file, COPY FROM, lo_import calls.
- Use database firewalls (e.g., pgBadger for log analysis) and intrusion detection to flag anomalous file access queries.

## Objectives

1. Enumerate directories and identify sensitive files on the PostgreSQL server.
2. Extract contents of target files like /etc/passwd or postgresql.conf.
3. Exfiltrate data for further analysis or privilege escalation.

## Instructions

### Step 1: Enumerate Directory Contents

**Context**: Start by listing files in the PostgreSQL data directory or target paths to identify readable files. This uses pg_ls_dir to discover paths like /etc/ without direct OS access.

**Command** ([[commands/postgresql-list-directory-contents]]):
```sql
SELECT pg_ls_dir('/etc/');
```

> This command returns a list of files and directories in /etc/. It requires superuser privileges. Use relative paths like './' for the data directory if absolute paths are restricted.

### Step 2: Read File Directly

**Context**: For small text files, use pg_read_file to extract contents directly. This is the simplest method but limited to files readable by the postgres user and up to 1GB in size.

**Command** ([[commands/postgresql-read-file-direct]]):
```sql
SELECT pg_read_file('/etc/passwd', 0, 1000);
```

> The command reads up to 1000 bytes from /etc/passwd starting at offset 0. Adjust the path, offset, and length as needed. Success is indicated by the file contents returned as a text string.

### Step 3: Create Temporary Table for Import

**Context**: For files that can't be read directly (e.g., due to permissions), create a temp table to stage data via COPY, which can import from server-side files.

**Command** ([[commands/postgresql-create-temp-table-for-file-import]]):
```sql
CREATE TEMP TABLE temp_passwd (line TEXT);
```

> This creates a single-column temp table. Temp tables are session-scoped and auto-dropped on disconnect, avoiding permanent schema changes.

### Step 4: Copy File to Temp Table

**Context**: Use COPY to load the file into the temp table, effectively reading its contents into the database for querying.

**Command** ([[commands/postgresql-copy-file-to-temp-table]]):
```sql
COPY temp_passwd FROM '/etc/passwd';
```

> This imports each line of /etc/passwd as a row in temp_passwd. Requires the file to be readable by postgres; errors if not found or permission denied.

### Step 5: Query Imported Data

**Context**: Select from the temp table to view or exfiltrate the file contents. Use LIMIT for partial views if the file is large.

**Command** ([[commands/postgresql-select-from-temp-table]]):
```sql
SELECT * FROM temp_passwd LIMIT 5;
```

> This retrieves the first 5 lines. Full query with SELECT * FROM temp_passwd; dumps the entire file. Drop the table afterward with DROP TABLE temp_passwd;

### Step 6: Import File as Large Object (Alternative for Binary Files)

**Context**: For larger or binary files, import as a large object using lo_import, which returns an OID for retrieval.

**Command** ([[commands/postgresql-import-file-as-large-object]]):
```sql
SELECT lo_import('/etc/shadow');
```

> Returns the OID (e.g., 16420). Use this OID in the next step. Large objects bypass some COPY limitations but still require file readability.

### Step 7: Retrieve Large Object by OID

**Context**: Fetch the imported file data using lo_get with the OID from the previous step.

**Command** ([[commands/postgresql-retrieve-large-object-by-oid]]):
```sql
SELECT lo_get(16420);
```

> Replace 16420 with the actual OID. Returns the binary data as a bytea or text if applicable. Clean up with lo_unlink(OID);

### Step 8: List All Large Objects (Verification)

**Context**: Query pg_largeobject to verify imports and retrieve metadata or data for all OIDs.

**Command** ([[commands/postgresql-list-all-large-objects]]):
```sql
SELECT loid, pageno, data FROM pg_largeobject;
```

> This lists all large objects. Use WHERE loid = 16420; to filter. Avoid in production as it can expose all LOs.
