---
id: 437e271e-ff91-4a92-b04e-99510349976d
name: MySQL-Union-Based-Injection-with-Error-Based-Detection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.307813+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Exploitation of Public-Facing Application|T1190 - Exploitation
    of Public-Facing Application]]
  - >-
    [[techniques/Exploitation for Credential Access|T1212 - Exploitation for
    Credential Access]]
sub_techniques: []
tags:
  - '[[tags/detect-column-number]]'
  - '[[tags/mysql-injection]]'
  - '[[tags/mysql-union-based]]'
  - '[[tags/using-order-by-or-group-by]]'
  - '[[tags/using-union-select-error-based]]'
commands:
  - '[[commands/mysql-union-column-detection-injection]]'
platforms:
  - Web
  - MySQL
tools: []
validated: true
---

# MySQL-Union-Based-Injection-with-Error-Based-Detection

## Summary

MySQL Union-Based Injection with Error-Based Detection is a technique used by attackers to gain unauthorized access to a MySQL database through a vulnerable web application. By injecting malicious SQL code via a UNION SELECT statement combined with error-based methods to determine column counts, attackers can manipulate queries to extract sensitive data such as usernames, passwords, and other confidential information without direct database access.

## Description

This procedure targets web applications backed by MySQL databases that fail to properly sanitize user inputs, allowing SQL injection. The attack begins by identifying an injectable parameter, then uses error-based techniques to probe the number of columns in the original query. Once determined, a UNION SELECT statement appends attacker-controlled data to the legitimate results, enabling data exfiltration. This is particularly effective against applications using dynamic SQL queries for searches or listings. The target environment is typically a web server (e.g., Apache/Nginx) with PHP or similar connecting to MySQL. Success allows dumping tables like users or credentials, leading to further compromise. Prerequisites include a vulnerable endpoint and basic knowledge of HTTP request manipulation.

## Requirements

1. A vulnerable web application with a MySQL backend database exposed via an injectable parameter (e.g., GET or POST input).
2. Knowledge of SQL injection fundamentals and MySQL syntax.
3. Access to a tool or browser for sending crafted HTTP requests, such as curl or Burp Suite.
4. Network access to the target web application.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization using prepared statements or ORM frameworks to prevent SQL injection.
- Use parameterized queries and stored procedures in application code to separate SQL logic from user input.
- Enable MySQL query logging and web application firewall (WAF) rules to monitor for anomalous SQL patterns, such as UNION SELECT or error messages containing database details.
- Regularly audit application code and database configurations for vulnerabilities using tools like SQLMap or static analysis.

## Objectives

1. Identify and confirm a SQL injection vulnerability in a MySQL-backed web application.
2. Determine the number of columns in the original query using error-based detection.
3. Inject a UNION SELECT statement to append and extract sensitive data from unauthorized tables.
4. Verify successful data retrieval without triggering application errors.

## Instructions

### Step 1: Identify Vulnerable Parameter

**Context**: Begin by testing potential injection points (e.g., search fields, ID parameters) to confirm SQL injection vulnerability. This step ensures the parameter reflects input back into a SQL query, often indicated by database errors or unexpected behavior.

Use a basic SQLi test payload to probe. For example, append a single quote to trigger a syntax error.

**Command** ([[commands/basic-sqli-test]]):

Assuming a GET parameter like `id=1` in `http://target.com/page?id=1`, test with:

```bash
curl "http://target.com/page?id=1'"
```

> This command sends a malformed request to elicit a MySQL error, confirming injection. Look for responses containing SQL syntax errors like "You have an error in your SQL syntax".

### Step 2: Determine Column Count Using Error-Based Detection

**Context**: With a confirmed injection point, use error-based payloads to iteratively guess the number of columns in the original SELECT query. MySQL will throw an error if the UNION SELECT has mismatched column counts, allowing deduction by incrementing placeholders.

**Code** ([[codes/MySQL-Error-Based-Column-Detection-Payload]]):

Inject payloads progressively, starting with one placeholder (`@`) and adding more until no error occurs.

> Expected output: Errors for mismatched columns (e.g., "The used SELECT statements have a different number of columns"), and normal response when columns match. For example, if 3 columns are needed, payloads with 1 or 2 @ will error, but 3 will succeed, confirming the count.

### Step 3: Construct and Execute UNION SELECT Injection

**Context**: Once the column count is known (e.g., 3), craft a UNION SELECT to match it and extract data. Use nulls or literals for non-target columns and database functions like `@@version` or `database()` for initial testing, then target tables like `users`.

**Command** ([[commands/mysql-union-column-detection-injection]]):

For a 3-column query:

```bash
curl "http://target.com/page?id=-1' UNION SELECT 1,@@version,database()-- -"
```

> This appends a UNION SELECT with matching columns, replacing the legitimate results. Expected output: Application renders the injected values (e.g., MySQL version and database name) instead of original data, confirming control. Proceed to extract from specific tables, e.g., `UNION SELECT username,password,1 FROM users-- -`.
