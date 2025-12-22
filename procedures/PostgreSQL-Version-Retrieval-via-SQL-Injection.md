---
id: 7b9e1adf-57f4-40e3-9bc2-dbd1d45f5c0c
name: PostgreSQL-Version-Retrieval-via-SQL-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.424813+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/PostgreSQL-injection]]'
  - '[[tags/PostgreSQL-Version]]'
  - sqli
  - database-enumeration
commands:
  - '[[commands/postgresql-select-version]]'
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# PostgreSQL-Version-Retrieval-via-SQL-Injection

## Summary

This procedure demonstrates how to retrieve the version of a PostgreSQL database through a SQL injection vulnerability in a public-facing web application. By injecting a simple SQL query, attackers can extract database metadata, which aids in identifying exploitable vulnerabilities for further compromise.

## Description

PostgreSQL is a widely used open-source relational database management system. In scenarios where a web application fails to properly sanitize user inputs, attackers can inject malicious SQL payloads to execute arbitrary queries. This procedure focuses on using the built-in `version()` function to obtain the exact PostgreSQL server version, including build details. This information is crucial for reconnaissance, as it allows attackers to research version-specific exploits, such as known CVEs in PostgreSQL or the application's backend. The technique assumes a blind or error-based SQL injection point, typically in login forms, search fields, or URL parameters. Success depends on the injection being union-based or time-based to extract the output. Defensive measures like prepared statements and input parameterization can prevent this, but misconfigurations often expose such flaws.

## Requirements

1. Access to a vulnerable web application with a SQL injection point connected to a PostgreSQL backend.
2. Tools for sending HTTP requests, such as a browser, curl, or Burp Suite, to deliver the injection payload.
3. Basic knowledge of the application's input fields (e.g., via manual testing or automated scanners like sqlmap).
4. Network connectivity to the target application without restrictions on outbound requests if using error-based extraction.

## Defense

- Implement strict input validation, sanitization, and parameterization (e.g., using PDO in PHP or psycopg2 in Python) to prevent SQL injection.
- Use web application firewalls (WAFs) to detect and block common SQL injection patterns.
- Enable database logging and monitor for anomalous queries, such as unexpected calls to system functions like `version()`.
- Regularly audit and patch PostgreSQL installations to mitigate version-specific vulnerabilities.
- Conduct penetration testing and use tools like OWASP ZAP to identify injection points proactively.

## Objectives

1. Identify and exploit a SQL injection vulnerability in a web application.
2. Execute a query to retrieve the PostgreSQL database version.
3. Use the version information for further reconnaissance or targeted exploitation.
4. Validate successful injection without causing denial of service.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Locate a user-controllable input field in the web application that interacts with the PostgreSQL database, such as a search box or login form. Test for injection by appending a single quote (`'`) and observing errors or unexpected behavior, confirming PostgreSQL-specific error messages like "syntax error at or near".

Use manual testing or a tool like Burp Suite to intercept and modify requests. No specific command is needed here; focus on error-based confirmation.

> If PostgreSQL errors are visible (e.g., via pg_exception_detail), proceed; otherwise, switch to blind injection techniques.

### Step 2: Inject the Version Query Payload

**Context**: Once the injection point is confirmed, craft a payload that appends the `version()` query to the original SQL statement. For union-based injection, combine it with a valid query structure. This step executes the query to fetch the database version, which can be extracted from the response.

**Command** ([[commands/postgresql-select-version]]):

Use the following SQL payload in the vulnerable parameter (e.g., via URL or POST data):

```sql
'; SELECT version() --
```

> This payload closes the original statement with a semicolon, injects the version query, and comments out the rest with `--`. Expected output in the application response (if error-based) or via union (if successful) will display something like "PostgreSQL 14.5 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 10.2.1 20210110, 64-bit". In blind scenarios, use conditional payloads to infer the version character-by-character.

**Code** ([[codes/PostgreSQL-Version-Query-SQL]]):

Embed the code snippet directly into the injection point as needed.

### Step 3: Extract and Verify the Output

**Context**: Analyze the application's response for the version string. If no direct output, use follow-up injections (e.g., substring extraction) to piece together the version. Verify by cross-referencing with known PostgreSQL release notes to identify potential exploits.

No additional command; manually inspect the response or use a proxy tool to log it.

> Success is confirmed if the version matches PostgreSQL format (e.g., starting with "PostgreSQL X.Y"). If extraction fails, refine the payload for the injection type (e.g., add `pg_sleep()` for time-based).
