---
type: procedure
description: >-
  Perform time-based blind SQL injection on vulnerable MySQL databases using
  conditional statements to infer information like database version without
  direct query output.
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.608505+00:00'
updated_at: '2023-04-10T20:22:57.635352+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - mysql-injection
  - blind-sqli
  - time-based-injection
  - conditional-statements
commands: []
platforms:
  - Web
  - MySQL
tools: []
validated: true
---

# MySQL-Time-Based-Blind-SQL-Injection-Using-Conditionals

## Summary

MySQL time-based blind SQL injection using conditional statements is a technique to extract sensitive information from a vulnerable MySQL-backed web application when error messages or direct query results are not visible. By injecting payloads that cause database delays (via SLEEP) based on conditional logic (IF statements), attackers can infer data such as the database version, usernames, or passwords through response timing differences.

## Description

This procedure targets web applications with unsanitized user inputs that reach MySQL queries, such as login forms or search fields. In blind injection scenarios, the application does not reveal query results, so time-based methods use functions like IF, SUBSTRING, and VERSION() to test conditions. If the condition is true, SLEEP() delays the response (e.g., 5 seconds), allowing inference via timing. This is useful for confirming vulnerabilities and exfiltrating data bit-by-bit in reconnaissance or data collection phases. The approach assumes a numeric or string injection point, like a user ID in a SELECT query.

## Requirements

1. Access to a web application vulnerable to SQL injection (e.g., via browser, curl, or proxy like Burp Suite).
2. Ability to measure response times accurately (e.g., using curl with timing flags or a proxy).
3. Basic knowledge of MySQL syntax, including functions like VERSION(), SUBSTRING(), IF(), and SLEEP().
4. No direct database access; assumes black-box testing from an external network position.

## Defense

- Use prepared statements and parameterized queries to separate code from user input.
- Implement input validation and sanitization, escaping special characters.
- Deploy a Web Application Firewall (WAF) to detect and block injection patterns, including time delays.
- Enable MySQL query logging and monitor for anomalous delays or failed queries.
- Apply least privilege to database accounts used by the application.

## Objectives

1. Confirm the presence of a time-based blind SQL injection vulnerability.
2. Extract database metadata, such as the MySQL version, to assess exploit potential.
3. Infer additional sensitive data (e.g., user credentials) through sequential conditional tests.
4. Achieve data exfiltration without triggering visible errors.

## Instructions

### Step 1: Identify the Injection Point and Test Basic Vulnerability

**Context**: Locate a parameter vulnerable to SQL injection (e.g., a user ID field in a login or search form). Start with a simple payload to confirm injection without direct output, then escalate to time-based tests. This step verifies the query is injectable and measures baseline response time.

**Payload** ([[codes/MySQL-Time-Delay-Test]]):
```sql
1' OR SLEEP(5) --
```

> Inject this into the vulnerable parameter (e.g., via POST data or URL). Use a tool like curl to send the request and time it: `curl -w "%{time_total}s" -X POST -d "id=1' OR SLEEP(5) --" https://target.com/login`. If the response takes ~5 seconds longer than a normal request, the vulnerability is confirmed. Otherwise, try variations like appending `#` for comment or adjusting quotes.

### Step 2: Check if MySQL Version Starts with '5' Using Conditional Delay

**Context**: Once the injection point is confirmed, use a conditional IF statement to test specific data. Here, extract the first character of the VERSION() and delay if it matches '5' (common for MySQL 5.x). This infers version information without returning data directly. Repeat for other positions/characters as needed.

**Payload** ([[codes/MySQL-Blind-Version-Starts-With-5]]):
```sql
2100935' OR IF(SUBSTRING(VERSION(),1,1)='5',SLEEP(5),0)--
```

> Replace '2100935' with the original input value (e.g., a valid ID). Send via the same method as Step 1. A delay of ~5 seconds indicates the version starts with '5' (true condition triggers SLEEP). No delay means false. Monitor HTTP response codes; unusual errors (e.g., 500) may accompany delays in some configurations.

### Step 3: Check if MySQL Version Starts with '4' Using Conditional Delay

**Context**: Test alternative version prefixes to narrow down the exact MySQL version (e.g., '4' for older versions). This step builds on Step 2, using binary search-like logic across possible characters (0-9, a-z). If no delay in previous steps, iterate through characters systematically.

**Payload** ([[codes/MySQL-Blind-Version-Starts-With-4]]):
```sql
2100935' OR IF(SUBSTRING(VERSION(),1,1)='4',SLEEP(5),0)--
```

> Inject similarly to Step 2. A delay confirms the version starts with '4'. Use this to map the full version string by testing subsequent characters (e.g., SUBSTRING(VERSION(),2,1)). For efficiency, automate with scripts if manual timing is tedious, but verify manually first.

### Step 4: Extract Additional Information (e.g., Database Name)

**Context**: With version confirmed, extend conditionals to extract other data, like the current database name via DATABASE(). This demonstrates scalability to sensitive info like user tables.

**Payload** ([[codes/MySQL-Blind-Database-Name-Extraction-Example]]):
```sql
2100935' OR IF(SUBSTRING(DATABASE(),1,1)='t',SLEEP(5),0)--
```

> Test for 't' as the first character of the DB name (adjust based on expected values). Delays indicate matches. Proceed character-by-character to reconstruct the full name. Success is measured by consistent inference without application crashes.
