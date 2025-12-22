---
id: dc6d91bb-4c9a-4d4c-a2ae-646b65f6b31a
name: Identifying SQL Injection
type: procedure
verified: true
submitted: true
created_at: '2020-07-21T14:43:10.239045+00:00'
updated_at: '2023-05-26T01:00:57.530761+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Web Shell]]'
sub_techniques: []
tags:
  - injection
  - owasp
  - owasp top 10
  - SQL
  - sqli
  - Web Applications
commands:
  - '[[commands/curl-inject-single-quote]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/cURL]]'
validated: true
---

# Identifying SQL Injection

## Summary

This procedure demonstrates how to identify potential SQL injection vulnerabilities in web applications by injecting special characters, such as a single quote ('), into user input fields or URL parameters. By observing the application's response for database error messages or unexpected behavior, attackers can confirm if the input is being directly concatenated into SQL queries without proper sanitization.

## Description

SQL injection occurs when user-supplied input is not properly sanitized and is directly embedded into SQL statements executed by the backend database. This procedure focuses on the initial identification phase, where an attacker tests for vulnerability by injecting a single quote to disrupt the SQL syntax, potentially causing syntax errors that reveal database details. It is typically used during web application penetration testing or reconnaissance to map out injectable points like login forms, search fields, or query parameters. Success indicates a high-risk vulnerability that could lead to data extraction, modification, or full compromise if exploited further. This aligns with manual testing before automated tools like sqlmap are employed.

## Requirements

1. Network access to the target web application (e.g., via browser or proxy).
2. Basic knowledge of HTTP requests and web forms.
3. Tools such as a web browser, [[tools/cURL]], or a proxy like [[tools/Burp-Suite]] for intercepting and modifying requests.
4. No elevated privileges required, but the application must accept user input (e.g., forms, URLs).

## Defense

Defensive measures and detection strategies:

- Implement prepared statements and parameterized queries in application code to separate SQL logic from user input.
- Use web application firewalls (WAFs) to detect and block common injection patterns, including single quotes and SQL keywords.
- Enable database error logging without exposing details to users; suppress error messages in production responses.
- Conduct regular input validation, sanitization, and code reviews using tools like static analysis scanners.

## Objectives

1. Identify input fields or parameters vulnerable to SQL injection by triggering syntax errors.
2. Confirm the presence of unsanitized SQL queries in the backend.
3. Gather indicators of the underlying database type from error messages (e.g., MySQL, PostgreSQL).
4. Expected outcome: Database error responses confirming vulnerability for further exploitation.

## Instructions

### Step 1: Identify Input Points

**Context**: Locate user input fields such as login forms, search boxes, or URL parameters that interact with the database. This step ensures you're targeting areas likely to process SQL queries.

Manual inspection: Navigate the application and note fields like username, password, or search terms. No command needed here; use browser developer tools to inspect form actions.

### Step 2: Inject Single Quote

**Context**: Append or insert a single quote (') into the input to break the SQL statement syntax, causing an error if the input is not escaped.

**Command** ([[commands/curl-inject-single-quote]]):
```bash
curl -X POST -d "username=admin'" -d "password=test" http://target.com/login
```

> This command sends a POST request with a single quote in the username field. Replace the URL and fields as needed. If using GET, append to the URL like `http://target.com/search?q=test'`. The quote disrupts the query (e.g., `SELECT * FROM users WHERE name='admin''`), leading to a syntax error.

### Step 3: Observe Response

**Context**: Analyze the server's response for signs of SQL errors, such as stack traces, syntax warnings, or database-specific messages, which confirm the vulnerability.

Use [[tools/Burp-Suite]] or browser console to view the full response. Look for keywords like "SQL syntax error", "unclosed quotation", or database names (e.g., "MySQL server has gone away").

If no error appears, try variations like `')` or `' OR 1=1--` to test further, but stick to identification in this procedure.

### Step 4: Verify and Document

**Context**: Confirm the error is due to SQL injection, not other issues, by testing non-vulnerable inputs and comparing responses.

Repeat Step 2 without the quote (e.g., `username=admin`). If the error only occurs with the quote, it's a strong indicator. Document the injectable endpoint, error message, and potential database type for escalation.
