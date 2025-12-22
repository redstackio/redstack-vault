---
id: f5f9aecc-0c39-4b7e-a826-3880d993d4dd
name: Perform-SQLite-Boolean-Error-Based-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.115907+00:00'
updated_at: '2023-04-10T20:24:29.207741+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - '[[tags/Boolean - Error based]]'
  - '[[tags/SQLite Injection]]'
  - sql-injection
  - boolean-based
commands: []
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# Perform-SQLite-Boolean-Error-Based-Injection

## Summary

This procedure demonstrates how to perform a boolean-error based SQL injection attack on an SQLite database to extract sensitive information. By injecting boolean conditions that trigger errors or normal responses based on true/false outcomes, attackers can infer data from the database without direct query results, often leveraging SQLite's load_extension function to create detectable errors when conditions are false.

## Description

SQLite databases are commonly embedded in applications, making them vulnerable to injection attacks if user inputs are not properly sanitized. Boolean-error based injection exploits this by crafting payloads that use conditional logic (e.g., CASE WHEN) to test database conditions. If the boolean query is true, the response is normal (e.g., returns 1); if false, it triggers an error via load_extension, allowing the attacker to distinguish outcomes and systematically extract data like usernames, passwords, or other confidential information. This technique is useful in blind injection scenarios where no direct data is returned, and it maps to exploiting public-facing applications for initial access and data collection. The attack requires identifying a vulnerable input point, such as a web form or API endpoint that interacts with the SQLite backend.

## Requirements

1. Access to a vulnerable application or endpoint that uses SQLite and accepts user-controlled input in SQL queries (e.g., via a web form, URL parameter, or API).
2. Knowledge of the base SQL query structure and injection point (e.g., through error messages or trial-and-error).
3. Tools for sending crafted requests, such as a browser, curl, or Burp Suite for web-based injections.
4. Understanding of boolean logic to construct incremental queries (e.g., checking if a character's ASCII value is greater than a threshold).

## Defense

- Use parameterized queries or prepared statements to separate SQL code from user input, preventing injection entirely.
- Limit database user privileges to the minimum required, avoiding permissions for loading extensions like load_extension.
- Implement web application firewalls (WAFs) to detect and block anomalous SQL patterns.
- Regularly update SQLite and the application framework to patch known vulnerabilities, and enable query logging for anomaly detection.
- Validate and sanitize all user inputs, rejecting suspicious patterns like boolean expressions or function calls.

## Objectives

1. Identify and confirm a boolean-error based injection vulnerability in an SQLite-backed application.
2. Extract sensitive data from the database by inferring boolean responses through normal vs. error outputs.
3. Escalate access or compromise data confidentiality by chaining extractions to reconstruct full records.

## Instructions

### Step 1: Identify the Injection Point and Confirm Vulnerability

**Context**: Locate an input field (e.g., login form, search box) where user input is concatenated into an SQLite query without sanitization. Test for injection by appending a simple boolean condition that always evaluates to true vs. false to observe response differences.

Inject a basic payload to check for boolean behavior:

Use the following SQL snippet in the vulnerable parameter: [[codes/SQLite-Boolean-Error-Injection-Payload]]

```sql
AND CASE WHEN (1=1) THEN 1 ELSE load_extension(1) END
```

> This tests a true condition (1=1), which should return normally (e.g., page loads without error). Replace with a false condition like (1=2) to trigger an error from load_extension, confirming the technique works. Why: This verifies the injection point allows conditional logic and error triggering without crashing the app.

### Step 2: Enumerate Database Structure

**Context**: Use boolean queries to determine the number of columns, database names, or table structures by testing conditions that cause errors or normal responses based on metadata queries.

Craft a payload to test column count, assuming the injection is after a SELECT statement:

Use the following SQL snippet: [[codes/SQLite-Boolean-Error-Injection-Payload]]

```sql
AND CASE WHEN ((SELECT COUNT(*) FROM sqlite_master)=1) THEN 1 ELSE load_extension(1) END
```

> Increment the expected count (e.g., =0, =1, =2) until you find the true response. Why: Understanding structure allows targeting specific tables for data extraction. Expected: Normal response when count matches, error otherwise.

### Step 3: Extract Sensitive Data

**Context**: Systematically extract data character-by-character using binary search on ASCII values. For example, to extract a username from a users table.

Build a boolean query for the first character:

Use the following SQL snippet: [[codes/SQLite-Boolean-Error-Injection-Payload]]

```sql
AND CASE WHEN (ASCII(SUBSTR((SELECT username FROM users LIMIT 1),1,1))>64) THEN 1 ELSE load_extension(1) END
```

> Adjust the position (1,1 for first char) and threshold (e.g., >64 for uppercase letters) to narrow down the character via true/false responses. Repeat for each position until the full string is reconstructed. Why: Boolean-error allows blind extraction without direct output. Expected: Sequence of normal/error responses revealing the data.

### Step 4: Verify and Chain Extraction

**Context**: Once initial data is extracted (e.g., a password), validate it and use it to query further, such as loading extensions for additional exploits if permitted.

Test extracted credentials in the application or extend to extract more fields:

Adapt the payload for additional columns:

```sql
AND CASE WHEN (SUBSTR((SELECT password FROM users WHERE username='extracted_user'),1,1)='a') THEN 1 ELSE load_extension(1) END
```

> Why: Validates the technique and enables broader compromise. Expected: Consistent boolean responses confirming data accuracy.
