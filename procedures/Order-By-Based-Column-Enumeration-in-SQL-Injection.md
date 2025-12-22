---
id: db2ba71a-0c6a-41b5-8b27-7761aeed6320
name: Order-By-Based-Column-Enumeration-in-SQL-Injection
type: procedure
verified: true
submitted: true
created_at: '2020-07-21T15:20:57.055714+00:00'
updated_at: '2023-05-26T15:58:29.272843+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - injection
  - owasp
  - owasp-top-10
  - sql
  - sqli
  - web-applications
commands:
  - '[[commands/curl-order-by-column-test]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Order-By-Based-Column-Enumeration-in-SQL-Injection

## Summary

This procedure outlines how to use the ORDER BY clause in a SQL injection attack to determine the number of columns in a vulnerable database query. By incrementally increasing the column number in the ORDER BY payload and observing when the database returns an error, attackers can identify the exact column count, which is essential for crafting subsequent UNION-based SQL injection payloads to extract sensitive data from the database.

## Description

SQL injection vulnerabilities occur when user input is not properly sanitized and is concatenated directly into SQL queries, allowing attackers to inject malicious SQL code. The ORDER BY technique exploits this by appending an ORDER BY clause with an ascending column number (e.g., ORDER BY 1, ORDER BY 2) to the injectable parameter. As long as the specified column number is within the query's actual column count, the query executes normally, sorting results accordingly. Once the column number exceeds the available columns, the database throws an error (e.g., "Unknown column 'x' in 'order clause'" for MySQL). This error threshold reveals the column count (error column - 1). This method is typically used in blind or error-based SQL injection scenarios on web applications where the injection point is in a search field, URL parameter, or form input. It assumes the attacker has identified a confirmed SQL injection point and is targeting a backend database like MySQL, PostgreSQL, or SQL Server. Success enables further exploitation, such as data enumeration via UNION SELECT.

## Requirements

1. Confirmed SQL injection vulnerability in a web application parameter (e.g., GET/POST search query).
2. Network access to the target web application.
3. Tools such as a web browser, [[tools/Burp-Suite]] for intercepting requests, or curl for automated testing.
4. Basic knowledge of SQL syntax and common database error messages.

## Defense

Defensive measures and detection strategies:

- Implement prepared statements or parameterized queries to separate user input from SQL code.
- Use web application firewalls (WAFs) to detect and block anomalous SQL patterns like ORDER BY injections.
- Enable database error logging and suppress detailed error messages from reaching the user.
- Perform input validation and sanitization, rejecting suspicious characters like single quotes and double hyphens.
- Monitor application logs for repeated failed queries with incremental ORDER BY clauses.

## Objectives

1. Confirm the ability to inject SQL via the ORDER BY clause without disrupting the query.
2. Incrementally test column numbers to identify the exact count in the vulnerable query.
3. Use the discovered column count to prepare for advanced exploitation techniques like UNION-based data extraction.
4. Expected outcome: Knowledge of the query structure to facilitate data leakage or manipulation.

## Instructions

### Step 1: Confirm SQL Injection Point and Test Initial ORDER BY Payload

**Context**: Begin by verifying that the target parameter is injectable and that a basic ORDER BY clause with a low column number (e.g., 1) executes without error. This establishes a baseline for normal query behavior. Use a tool like [[tools/Burp-Suite]] to intercept and modify requests if testing manually, or curl for scripted testing. The payload typically ends with a comment (e.g., -- for MySQL) to neutralize the rest of the query.

**Command** ([[commands/curl-order-by-column-test]]):
```bash
curl -s "$_TARGET_URL?q=' order by 1--"
```

> This command sends a GET request with the ORDER BY 1 payload. If successful, the response should mirror the normal page output (e.g., search results sorted by the first column), indicating no SQL error. Why: This tests if the injection point allows clause appending without breaking the query. If an immediate error occurs, the injection point may require URL encoding or a different comment style (e.g., # for MySQL). Proceed only if the response is normal.

### Step 2: Increment the Column Number and Monitor for Errors

**Context**: Systematically increase the column number in the ORDER BY payload (e.g., 2, 3, 4) while observing the response. Continue until an SQL error is returned, which indicates the payload exceeds the query's column count. This step requires repeating the request multiple times, potentially automating with a script or Burp Intruder if the column count is unknown (typically 1-20 for web apps). Decision point: If no error after a high number (e.g., 50), the vulnerability may not support ORDER BY or the database handles excess columns gracefully—switch to alternative enumeration like UNION SELECT with NULLs.

**Command** ([[commands/curl-order-by-column-test]]):
```bash
curl -s "$_TARGET_URL?q=' order by $_COLUMN_NUM--"
```

> Replace $_COLUMN_NUM with incremental values starting from 2. Expected output for valid columns: Normal page content. For invalid: An error page or message like "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' order by 7--' at line 1" or "Unknown column '7' in 'order clause'". Why: Each increment probes the query structure; the first error pinpoints the boundary. Use -v flag in curl for headers if needed to confirm HTTP 200 vs. 500 status.

### Step 3: Calculate and Verify Column Count

**Context**: Once the error threshold is found (e.g., error at ORDER BY 7), subtract 1 to get the column count (6 in this case). Verify by re-testing the last successful payload (ORDER BY 6) to ensure it returns normal results. This count informs the number of NULL or data positions in a follow-up UNION SELECT payload. If using [[tools/Burp-Suite]], review the intercepted responses for consistency in error patterns.

> No specific command needed here, but re-run the successful payload from Step 2 for confirmation. Expected output: Normal response for ORDER BY N (where N = column count), confirming the calculation. Why: Validation ensures accuracy before advancing to data extraction. If discrepancies occur (e.g., due to subqueries), consider database-specific behaviors like PostgreSQL's different error phrasing.
