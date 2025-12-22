---
type: procedure
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1190 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Authentication bypass]]'
  - '[[tags/SQL Injection]]'
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
validated: true
---

# SQL-Injection-Authentication-Bypass

## Summary

This procedure demonstrates how to bypass authentication mechanisms in a web application using SQL injection (SQLi) techniques. By injecting malicious SQL payloads into login form fields, an attacker can manipulate the underlying database query to always return a valid user, granting unauthorized access without knowing legitimate credentials. This is commonly targeted at poorly sanitized input fields in authentication endpoints and can lead to full account takeover or further exploitation.

## Description

SQL injection occurs when user-supplied input is not properly sanitized and is concatenated directly into SQL queries, allowing attackers to alter the query's logic. In authentication bypass scenarios, the goal is to inject payloads that make the query evaluate to true for any input, such as appending ' OR 1=1 -- to the username field. This technique targets web applications using databases like MySQL, PostgreSQL, or SQL Server, often in login forms where credentials are verified via queries like SELECT * FROM users WHERE username = '$input' AND password = '$input'. Success grants session access, potentially exposing sensitive data or enabling lateral movement. This procedure assumes a vulnerable public-facing web app and focuses on manual injection for educational purposes in controlled environments.

## Requirements

1. Access to a web application's login form that is vulnerable to SQL injection (e.g., via browser or proxy).
2. Knowledge of basic SQL syntax and common database types (MySQL preferred for comment-based payloads).
3. Tools for intercepting and modifying HTTP requests, such as a browser developer console or proxy (though not strictly required for basic tests).
4. Target URL of the authentication endpoint.

## Defense

Defensive measures and detection strategies:

- Use prepared statements and parameterized queries to separate SQL code from user input.
- Implement web application firewalls (WAFs) to detect and block common SQLi patterns.
- Enforce strict input validation and sanitization, escaping special characters.
- Enable database logging to monitor anomalous queries and enable application-level error handling to avoid leaking database details.

## Objectives

1. Identify and confirm SQL injection vulnerability in the authentication form.
2. Inject payloads to bypass login and gain unauthorized access.
3. Verify access by accessing protected resources post-bypass.

## Instructions

### Step 1: Identify the Vulnerable Input Field

**Context**: Determine which field in the login form (typically username or password) accepts unsanitized input. Test by submitting simple payloads to observe error messages or behavior changes that indicate SQL processing.

Navigate to the login page and enter a single quote (') in the username field, leaving password blank. Submit the form.

**Expected Output**: Database error (e.g., syntax error near ''') or unusual page behavior, confirming input reaches the SQL query.

### Step 2: Test for Boolean-Based SQL Injection

**Context**: Use boolean conditions to confirm injection by crafting payloads that alter query logic without errors. This step verifies the vulnerability before attempting bypass.

In the username field, enter: admin' AND 1=1 --

Submit with any password.

**Expected Output**: Successful login if the query becomes true, or no error if injection works silently.

If it fails, try variations like admin' OR 1=1 -- for the username field.

### Step 3: Execute Authentication Bypass Payload

**Context**: Inject a payload from the collection of tested SQLi strings to force the query to authenticate any input as valid. Reference the payload code for common variants tailored to different SQL dialects and comment styles.

Use [[codes/SQL-Auth-Bypass-Payloads]] and select a payload like ' OR 1=1 -- for the username field, with blank or arbitrary password.

Submit the form.

**Expected Output**: Redirect to the authenticated dashboard or session cookie set, indicating bypass success.

### Step 4: Verify Access and Extract Data

**Context**: Confirm the bypass by accessing user-specific resources. If possible, extend the injection to dump user data via UNION SELECT.

Once logged in, check account details or attempt to query more data, e.g., append ' UNION SELECT username, password FROM users -- to extract hashes.

**Expected Output**: Access to protected pages or visible user data in responses.

**Success Indicators**:
- No authentication prompt after payload submission.
- Session established with admin or user privileges.
