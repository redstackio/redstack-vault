---
id: d4b62d1b-9413-4876-ab3b-ead19477e9c6
name: MySQL-Blind-Injection-with-MAKE_SET-for-Auth-Bypass
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.630027+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/MySQL Blind]]'
  - '[[tags/MySQL Blind with MAKE_SET]]'
  - '[[tags/MySQL Injection]]'
  - sql-injection
  - blind-injection
  - auth-bypass
commands: []
platforms:
  - Web
  - MySQL
tools: []
validated: true
---

# MySQL-Blind-Injection-with-MAKE_SET-for-Auth-Bypass

## Summary

This procedure demonstrates a blind SQL injection attack on a MySQL database using the MAKE_SET function to bypass user authentication and extract sensitive information such as database version, login credentials, and concatenated password data. It leverages conditional comparisons in the injection payload to infer query results based on application responses, enabling data exfiltration without direct output visibility.

## Description

In a typical attack scenario, an attacker targets a web application with an insecure login form that concatenates user input directly into a MySQL query without proper sanitization. The blind injection uses MAKE_SET to create boolean conditions that alter the application's response (e.g., success vs. error pages) based on whether a subquery evaluates to true or false. Specifically, the payload compares subquery results (like string lengths or ASCII values) against a threshold, allowing the attacker to iteratively extract characters from database fields. This technique is effective against parameterized queries that fail to handle dynamic SQL functions like MAKE_SET. The target environment is a web-facing MySQL-backed application, often in e-commerce or authentication systems. Successful execution leads to unauthorized access to user data, potentially enabling further lateral movement or data theft.

## Requirements

1. Access to a vulnerable web application with a MySQL backend and an injectable login form (e.g., POST endpoint for username/password).
2. Knowledge of SQL injection basics and the MySQL MAKE_SET function, which constructs a string from bits set in a bitfield.
3. Tools for intercepting and modifying HTTP requests, such as a browser or proxy (though not strictly required for manual testing).
4. Understanding of blind injection inference techniques, including handling time-based or boolean responses.

## Defense

- Implement prepared statements or parameterized queries in the application code to prevent direct SQL concatenation.
- Use web application firewalls (WAFs) to detect and block common SQL injection patterns, including MAKE_SET usage.
- Sanitize and validate all user inputs, escaping special characters and limiting input lengths.
- Enable MySQL query logging and monitor for anomalous queries; implement least-privilege database accounts to restrict data access.
- Regularly audit application code and conduct penetration testing for injection vulnerabilities.

## Objectives

1. Bypass user authentication without valid credentials by injecting malicious SQL into the login query.
2. Extract database metadata, such as the MySQL version string length and content.
3. Infer sensitive user data, including lengths and individual characters of concatenated login and password fields.
4. Achieve unauthorized access to the database for potential data exfiltration or privilege escalation.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Locate the vulnerable input field in the login form, typically the username or password parameter, where user input is directly appended to a SELECT query like 'SELECT * FROM users WHERE login = '$username' AND password = '$password''. Test for injection by appending a single quote (') to observe SQL errors, confirming lack of sanitization.

Intercept the login request using browser developer tools or a proxy. Submit a test payload like username: admin' -- to comment out the password check and verify if it bypasses authentication.

**Expected Output**: If vulnerable, the application may return a successful login or altered response indicating query manipulation.

### Step 2: Inject Payload to Extract Version Length

**Context**: Use the MAKE_SET payload to determine the length of the MySQL version string via boolean inference. The payload injects into the username field, creating a condition that returns true (e.g., login success) only if the version length is less than a guessed value, allowing binary search for the exact length.

**Code** ([[codes/MySQL-Blind-MAKE_SET-Version-Length-Payload]]):

```sql
AND MAKE_SET(YOLO<(SELECT(length(version()))),1)
```

Replace YOLO with an integer guess (e.g., 1, 2, etc.) and iterate until the response changes, indicating the length threshold. For example, if responses differ at guess=10, the version length is 10.

**Expected Output**: Application response flips (e.g., from error to success) at the correct length value, confirming extraction.

### Step 3: Extract Version Characters

**Context**: Once the length is known, extract individual characters of the version string using ASCII values. Start from position 1 (POS=1) and guess ASCII values (32-126) until the condition triggers a distinguishable response.

**Code** ([[codes/MySQL-Blind-MAKE_SET-Version-Character-Payload]]):

```sql
AND MAKE_SET(YOLO<ascii(substring(version(),POS,1)),1)
```

Set POS to the current position and YOLO to guessed ASCII (e.g., 65 for 'A'). Repeat for each position up to the known length.

**Expected Output**: Response indicates true when the guessed ASCII matches the character at POS, building the full version string (e.g., '5.7.34').

### Step 4: Extract Login/Password Length

**Context**: Determine the length of the concatenated login and password fields from the users table, assuming the query targets a specific row (e.g., admin user).

**Code** ([[codes/MySQL-Blind-MAKE_SET-Login-Password-Length-Payload]]):

```sql
AND MAKE_SET(YOLO<(SELECT(length(concat(login,password)))),1)
```

Iterate YOLO guesses to find the length via response differences.

**Expected Output**: Boolean response flip reveals the total length of concat(login, password).

### Step 5: Extract Login/Password Characters

**Context**: Extract individual characters from the concatenated string, separating login and password based on known lengths or delimiters.

**Code** ([[codes/MySQL-Blind-MAKE_SET-Login-Password-Character-Payload]]):

```sql
AND MAKE_SET(YOLO<ascii(substring(concat(login,password),POS,1)),1)
```

Use POS from 1 to the known length, guessing ASCII values iteratively.

**Expected Output**: Reconstructed string of login and password, enabling full credential recovery (e.g., 'admin:secretpass').

### Step 6: Verify and Escalate

**Context**: Use extracted credentials to log in legitimately or further query the database for additional data.

Submit the recovered login/password to the application.

**Expected Output**: Successful authentication and access to protected resources.
