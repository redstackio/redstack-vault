---
type: procedure
description: >-
  Perform SQL injection in DB2 databases using CASE statements to conduct
  boolean-based blind injection for data extraction.
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
  - sql-injection
  - db2
  - case-statement
  - blind-injection
commands: []
platforms:
  - Databases
  - DB2
tools: []
validated: true
---

# DB2-Injection-Using-CASE-Statement

## Summary

This procedure demonstrates how to exploit SQL injection vulnerabilities in IBM DB2 databases using CASE statements for boolean-based blind injection. By crafting conditional SQL queries, attackers can extract sensitive data bit by bit without direct output, such as testing conditions to infer database contents like usernames, passwords, or table structures.

## Description

DB2 injection targets vulnerabilities in applications connected to IBM DB2 relational databases, where user input is not properly sanitized and concatenated into SQL queries. The CASE statement technique leverages DB2's conditional logic to perform blind injection: the attacker injects payloads that evaluate true/false conditions, observing application behavior (e.g., response time, error messages, or content differences) to deduce data. This is particularly useful when the database does not return query results directly.

Technically, the CASE statement evaluates expressions and returns values based on matches, allowing boolean tests like checking if a substring matches a database value. For example, injecting into a login query can force conditional responses that reveal information without alerting the user. This method maps to exploiting public-facing applications and is common in web apps with DB2 backends.

In a typical scenario, an attacker identifies an injectable parameter (e.g., in a search form), then uses CASE to binary search data, such as extracting a password character by character. Success depends on the injection point allowing subqueries and the application's response varying based on query outcomes.

## Requirements

1. Valid SQL injection point in an application connected to a DB2 database (e.g., via a web form or API endpoint).
2. Network access to the application and database (direct DB2 access optional if exploiting via app).
3. Basic knowledge of SQL syntax and DB2 specifics (e.g., sysibm.sysdummy1 as a dummy table for testing).
4. Tools for sending crafted requests, such as a browser, [[tools/Burp-Suite]], or curl (though no specific CLI commands are required here).

## Defense

- Implement strict input validation, sanitization, and parameterization using prepared statements or stored procedures to prevent injection.
- Use web application firewalls (WAFs) to detect and block anomalous SQL patterns, including CASE-based payloads.
- Enable DB2 logging for all queries and monitor for unusual conditional statements or high query volumes from single sources.
- Regularly audit application code for concatenation vulnerabilities and apply least-privilege database accounts.

## Objectives

1. Identify and confirm a blind SQL injection vulnerability in a DB2-backed application.
2. Extract sensitive data (e.g., user credentials, table contents) using boolean conditions via CASE statements.
3. Bypass authentication or access controls without direct error-based feedback.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Locate a parameter vulnerable to SQL injection, such as a login field, search box, or URL query string. Test for vulnerability by appending a single quote (') and observing errors or behavior changes, confirming DB2 as the backend if specific errors appear.

Inject a basic test payload like ' OR 1=1 -- to see if the query alters (e.g., bypasses login). If no direct output, proceed to blind techniques.

**Expected Output**: Application response changes (e.g., all records returned for OR 1=1), or DB2-specific error like SQLCODE -104 for syntax issues.

### Step 2: Craft and Test Boolean-Based CASE Payload

**Context**: Use the CASE statement to test conditions that return distinguishable values based on true/false outcomes. This step builds a payload to probe database contents, such as checking if a condition holds for data extraction.

Reference the code snippet [[codes/db2-case-statement-boolean-test]] for the base payload. Modify the condition (e.g., replace (1=1) with a database-specific test like (SELECT substring(password,1,1) FROM users WHERE id=1)='a'). Inject into the vulnerable parameter and observe if the application returns 'AAAAAAAAAA' (true) or 'BBBBBBBBBB' (false), or alters behavior accordingly.

For example, in a URL parameter: http://target.com/search?q=' UNION SELECT CASE WHEN (condition) THEN 'A' ELSE 'B' END FROM sysibm.sysdummy1 --

```sql
select CASE WHEN (1=1) THEN 'AAAAAAAAAA' ELSE 'BBBBBBBBBB' END from sysibm.sysdummy1
```

**Expected Output**: Query returns 'AAAAAAAAAA' if condition is true, allowing inference of data (e.g., first password char is 'a'). In blind scenarios, true might delay response or show specific content.

### Step 3: Extract Data Iteratively

**Context**: Once confirmed, systematically extract data by iterating conditions (e.g., binary search for characters). This step automates or manually builds the full extraction, such as dumping a table.

Build payloads to test each position: CASE WHEN (ASCII(substring((SELECT password FROM users LIMIT 1),$_POSITION,1)) > $_ASCII_VALUE) THEN 'A' ELSE 'B' END. Adjust $_POSITION (1- length) and $_ASCII_VALUE (0-127) based on responses. Use tools like sqlmap for automation if direct access, but manually craft for precision.

**Expected Output**: Inferred full data string after multiple tests (e.g., password='secret'). Success if 100% of characters match without false positives.

### Step 4: Verify and Escalate

**Context**: Confirm extracted data by testing in context (e.g., use dumped creds for login) and check for further injection points to escalate (e.g., to admin tables).

Re-run a known true/false payload to validate consistency, then query system tables like syscat.tables for schema info.

**Expected Output**: Validated data enables further access, such as authenticated sessions or additional dumps.
