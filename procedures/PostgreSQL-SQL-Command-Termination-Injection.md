---
type: procedure
description: >-
  Demonstrates using SQL command termination symbols like semicolon and double
  pipe in PostgreSQL to inject malicious code.
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.396571+00:00'
updated_at: '2023-04-10T20:23:21.755395+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation of Remote Services]]'
sub_techniques: []
tags:
  - postgresql-injection
  - sqli
  - command-termination
commands:
  - '[[commands/curl-send-sql-payload]]'
tools:
  - '[[tools/sqlmap]]'
platforms:
  - Web
  - PostgreSQL
validated: true
---

# PostgreSQL-SQL-Command-Termination-Injection

## Summary

This procedure outlines how to exploit SQL injection vulnerabilities in PostgreSQL databases by using command termination symbols such as the semicolon (;) to prematurely end the original query and append malicious SQL code. It also covers the double pipe (||) operator for concatenation or logical OR operations to chain injections, enabling unauthorized data access, modification, or execution of additional commands.

## Description

PostgreSQL SQL injection attacks target web applications that fail to properly sanitize user inputs before incorporating them into database queries. By injecting termination symbols, attackers can close the intended SQL statement early and introduce their own logic. For instance, a semicolon terminates the query, allowing a follow-up command like a time-based blind injection (e.g., pg_sleep). The double pipe (||) can concatenate strings or act as a logical OR to bypass filters or append payloads. This technique is commonly used in scenarios where the application uses dynamic SQL construction, such as in login forms, search fields, or URL parameters. Success depends on identifying an injectable parameter and evading any basic input filtering. The procedure assumes a vulnerable public-facing application and focuses on crafting and delivering termination-based payloads.

## Requirements

1. Network access to the target web application with a PostgreSQL backend.
2. Identification of a potential SQL injection point (e.g., via error messages or boolean/time-based tests).
3. Tools like curl or [[tools/sqlmap]] for sending crafted HTTP requests.
4. Basic knowledge of PostgreSQL syntax and common injection vectors (e.g., GET/POST parameters).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to strip or escape special characters like ; and ||.
- Use parameterized queries or prepared statements to separate SQL code from user input.
- Limit database user privileges to the minimum required, preventing execution of administrative commands.
- Enable web application firewall (WAF) rules to detect and block common SQLi patterns, including termination symbols.
- Monitor database logs for anomalous queries containing unexpected semicolons or concatenated statements.

## Objectives

1. Prematurely terminate the original SQL query to inject and execute additional malicious commands.
2. Bypass input filters using logical operators like || to chain valid and malicious payloads.
3. Achieve unauthorized access to sensitive data, such as user tables, or perform actions like data modification/deletion.

## Instructions

### Step 1: Identify the SQL Injection Point

**Context**: Begin by probing the target application to confirm a SQL injection vulnerability exists. Look for parameters in URLs, forms, or headers that influence database queries. Use boolean or error-based tests to verify injectability.

Test with a simple payload like ' OR 1=1 -- to see if the query behavior changes (e.g., login bypass or error disclosure).

> If the application returns different results or errors, proceed; otherwise, the point may not be injectable.

### Step 2: Craft the Termination Payload

**Context**: Use SQL command termination symbols to end the original query and append your payload. Reference the symbols from [[codes/PostgreSQL-SQL-Command-Termination-Symbols]] for accurate syntax. The semicolon (;) must be placed within a string or identifier to avoid syntax errors, while || can concatenate or act as OR.

Incorporate into a payload, e.g., for a time-based test: whatever=1;(select 1 from pg_sleep(5)) or whatever=1||(select 1 from pg_sleep(5)).

> Expected: The database delays response by 5 seconds if successful, indicating injection worked. Adjust based on the injection type (union, blind, etc.).

### Step 3: Send the Payload via HTTP Request

**Context**: Deliver the crafted payload to the vulnerable endpoint using a tool like curl. This step tests the termination in a real request, observing response time or content changes.

**Command** ([[commands/curl-send-sql-payload]]):
```bash
curl -X GET "http://target.com/page?param=$_INJECTION_PAYLOAD" -v
```

> Replace $_INJECTION_PAYLOAD with your termination string, e.g., "1;(select 1 from pg_sleep(5))". Expected output includes a delayed response (e.g., 5+ seconds) or altered page content revealing injection success. If using POST, switch to -X POST -d "param=$_INJECTION_PAYLOAD".

### Step 4: Verify and Escalate

**Context**: Confirm success by extracting data or executing further commands. For example, use UNION to dump tables: ; UNION SELECT version() --. Monitor for errors or partial data leaks.

If time-based works, chain to extract info via conditional sleeps. Use [[tools/sqlmap]] for automation if manual testing succeeds.

> Success if you retrieve database info (e.g., version, users) or observe query execution beyond the original intent.
