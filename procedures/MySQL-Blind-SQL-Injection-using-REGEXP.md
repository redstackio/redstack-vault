---
id: 3a64b1c3-2d9f-4463-be91-208d41e0cd56
type: procedure
name: MySQL-Blind-SQL-Injection-using-REGEXP
description: >-
  A time-based blind SQL injection technique using MySQL's REGEXP function to
  infer database information through response delays without direct output.
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.590604+00:00'
updated_at: '2023-04-10T20:22:55.212108+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - mysql
  - blind-sqli
  - time-based
  - regexp
  - sql-injection
commands:
  - '[[commands/curl-send-mysql-blind-sqli]]'
platforms:
  - Web
  - MySQL
tools: []
validated: true
---

# MySQL-Blind-SQL-Injection-using-REGEXP

## Summary

This procedure demonstrates a time-based blind SQL injection attack on MySQL databases using the REGEXP function to perform binary searches or pattern matching on data, inferring information from response delays caused by conditional SLEEP statements. It is effective for extracting sensitive data from vulnerable web applications where error messages or direct query outputs are suppressed, allowing attackers to bypass basic security measures without knowing the full database schema.

## Description

In a blind SQL injection scenario, the application does not return database errors or query results, making traditional SQLi less effective. This technique leverages MySQL's REGEXP for pattern matching (e.g., checking if a value starts with a specific character) combined with time-based delays via SLEEP to confirm true/false conditions. For example, an attacker can query if a username starts with 'a' by injecting a condition that sleeps only if the REGEXP matches, measuring response time to deduce bits of information. This is particularly useful in black-box testing where direct access is limited, enabling gradual data exfiltration such as database names, table structures, or user credentials. The attack targets input fields like search parameters or IDs in web forms, assuming the backend uses unsanitized user input in SQL queries.

## Requirements

1. Access to a vulnerable web application with a MySQL backend and an injectable parameter (e.g., GET/POST ID or search field).
2. Knowledge of basic SQL injection principles and the application's query structure (e.g., via error-based testing or educated guesses).
3. Tools for sending HTTP requests and measuring response times, such as curl or Burp Suite.
4. A stable network connection to observe timing differences (delays of 3-5 seconds).

## Defense

- Implement strict input validation and parametized queries (e.g., using prepared statements in PHP/Python) to prevent injection.
- Use web application firewalls (WAFs) to detect and block anomalous SQL patterns like REGEXP or SLEEP in payloads.
- Enable database logging and monitor for unusual query delays or high SLEEP function usage.
- Conduct regular vulnerability scans and code reviews focusing on dynamic SQL construction.

## Objectives

1. Confirm the presence of a blind SQL injection vulnerability in a MySQL-backed application.
2. Extract database information (e.g., table names, user data) character-by-character using time-based inference.
3. Bypass output-suppressing security controls to achieve data exfiltration without visible errors.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Determine a vulnerable parameter by testing for SQL injection basics, such as appending quotes or logical operators to see if the application behaves differently (e.g., generic errors or page changes). This step ensures the endpoint is injectable before proceeding to blind techniques.

Use manual testing or a scanner to probe parameters. For example, append ' OR 1=1 -- to a URL parameter like ?id=1.

**Expected Output**: Application returns all records or a different page structure, indicating injection potential without errors for blind confirmation.

### Step 2: Craft and Send Time-Based Blind SQLi Payload Using REGEXP

**Context**: Construct a payload that uses REGEXP to check a condition (e.g., if a value matches a pattern) and SLEEP to create a detectable delay only if true. This allows binary inference: measure response time to determine if the condition holds. Start with simple checks like database version or table existence, then extract data bit-by-bit.

**Command** ([[commands/curl-send-mysql-blind-sqli]]):

Send the payload via curl to the vulnerable endpoint, replacing placeholders with actual values. For a GET parameter example targeting a 'name' field in an 'items' table:

```bash
curl "http://vulnerable-app.com/search?q=1' AND IF((SELECT COUNT(*) FROM items WHERE name REGEXP '^a')>0, SLEEP(5), 0)-- -w "%{time_total}s\n" -s -o /dev/null
```

> This command injects into the 'q' parameter. The REGEXP '^a' checks if any 'name' starts with 'a'. If true, SLEEP(5) delays the response by 5 seconds; otherwise, it responds immediately. Run multiple times to confirm timing (average response >5s indicates true). Adjust the REGEXP pattern (e.g., '^a[0-9]') for binary search on characters. Use -w for timing output.

**Expected Output**: Response time around 5+ seconds if the condition is true (e.g., a matching record exists), or <1 second if false. No direct data in response, but timing confirms inference.

### Step 3: Iterate for Data Exfiltration

**Context**: Once confirmed, systematically build queries to extract full data. For example, determine database name length first, then characters via REGEXP on ASCII values or direct patterns. Automate with scripts if manual timing is tedious, but verify each step.

Build on the previous payload, e.g., to check the first character of a username:

Use the same curl command structure, modifying the REGEXP: REGEXP '^[a-m]' for first half of alphabet, narrowing down with each test.

**Expected Output**: Consistent delays allowing reconstruction of data (e.g., after 7 tests per character, reveal 'admin' as username).

**Success Indicators**:
- Reliable timing differences (true: delay; false: no delay).
- Successful inference of at least one data point (e.g., table existence).
- No application crashes or blocks from WAF.
