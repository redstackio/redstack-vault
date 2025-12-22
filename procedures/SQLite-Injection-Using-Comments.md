---
id: 8f3c5c95-55e5-409a-86ce-034fc1bd2bfd
name: SQLite-Injection-Using-Comments
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:36.924525+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - sql-injection
  - sqlite
  - comments
  - bypass-validation
commands:
  - '[[commands/curl-sqlite-injection-test]]'
platforms:
  - Web
tools: []
validated: true
---

# SQLite-Injection-Using-Comments

## Summary

SQLite Injection using comments is a SQL injection technique that exploits vulnerabilities in applications using SQLite databases by injecting malicious SQL payloads that incorporate comments to neutralize or bypass input validation filters, allowing attackers to alter query logic, extract data, or execute unauthorized commands.

## Description

This procedure targets web applications or embedded systems using SQLite, a lightweight database common in mobile apps, IoT devices, and small-scale web backends. Attackers identify injectable parameters (e.g., login forms, search fields) and append SQL comments like '--' or '/* */' to truncate the original query or hide malicious code from simplistic filters. For example, in a login query like 'SELECT * FROM users WHERE username = '$input' AND password = '$pass'', injecting 'admin' -- ' comments out the password check, bypassing authentication. This can lead to data exfiltration (e.g., dumping user tables) or command execution if the app allows stacked queries. The technique relies on poor input sanitization and is effective against apps that strip keywords but miss comments. Expected outcomes include unauthorized access or data theft, with risks amplified in unpatched or legacy systems.

## Requirements

1. Network access to the target application (e.g., via browser or proxy like Burp Suite).
2. Identification of a potentially injectable input field (e.g., through error messages revealing SQLite usage).
3. Basic knowledge of SQL syntax and SQLite specifics (e.g., no full DBMS privileges like in MySQL).
4. Tools for sending HTTP requests (e.g., curl) and intercepting traffic.

## Defense

Defensive measures and detection strategies:

- Use prepared statements or parameterized queries to separate SQL code from user input.
- Implement web application firewalls (WAFs) to detect comment-based payloads and anomalous SQL patterns.
- Sanitize inputs by escaping special characters and validating against whitelists.
- Enable SQLite query logging and monitor for unusual database activity, such as unexpected comment usage in logs.

## Objectives

1. Identify and confirm SQL injection vulnerability in a SQLite-backed application.
2. Bypass input validation using SQL comments to alter query execution.
3. Achieve unauthorized data access or manipulation, such as extracting sensitive records.

## Instructions

### Step 1: Identify Vulnerable Input

**Context**: Probe the application to find injectable parameters, looking for error messages that indicate SQLite (e.g., 'SQLite error' or syntax hints). Focus on forms like login or search.

Use a basic test payload to check for injection points without comments first.

**Command** ([[commands/curl-sqlite-injection-test]]):
```bash
curl -X POST http://target.com/login -d "username=admin'" -d "password=test"
```

> This sends a single quote to trigger a syntax error if vulnerable. Look for database errors in the response confirming SQLite usage.

### Step 2: Test Injection with Comments

**Context**: Append SQL comments to neutralize the rest of the query. For a login bypass, use '--' to comment out the password clause, or '/* */' for multi-line bypassing if the app filters single-line comments.

Incorporate the comment payload from [[codes/SQL-Comment-Payload-For-Injection]] into your request.

**Command** ([[commands/curl-sqlite-injection-test]]):
```bash
curl -X POST http://target.com/login -d "username=admin' --" -d "password=test"
```

> If successful, the app treats 'admin' --' as the full username input, ignoring the password check. Expected response: Successful login without valid password.

### Step 3: Extract Data Using Stacked Queries

**Context**: If basic bypass works, chain commands with comments to dump data. SQLite supports limited stacked queries (semicolon-separated), so use comments to hide them from filters.

**Command** ([[commands/curl-sqlite-injection-test]]):
```bash
curl -X POST http://target.com/search -d "q=1; SELECT * FROM users --"
```

> This executes a data dump after the original query. Verify by checking response for leaked user data like emails or hashes.
