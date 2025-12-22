---
id: e93c0f46-f787-492e-ad79-30df40af468d
name: Bypass-Admin-Login-via-MySQL-Injection-and-Truncation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.886383+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - '[[tags/SQL-Injection]]'
  - '[[tags/MySQL]]'
  - '[[tags/Authentication-Bypass]]'
  - '[[tags/Truncation-Attack]]'
commands:
  - '[[commands/curl-test-mysql-injection]]'
  - '[[commands/curl-admin-truncation-payload]]'
platforms:
  - Web
tools: []
validated: true
---

# Bypass-Admin-Login-via-MySQL-Injection-and-Truncation

## Summary

This procedure demonstrates how to exploit a SQL injection vulnerability in a web application's admin login form using MySQL, combined with string truncation to bypass authentication. By injecting a crafted username payload that leverages field length limitations (e.g., varchar truncation), an attacker can force the query to authenticate as the admin user without knowing the password.

## Description

The attack targets login forms where user input is directly concatenated into SQL queries without sanitization, such as SELECT * FROM users WHERE username = '$input' AND password = '$pass'. In MySQL, truncation occurs if the input exceeds the column's varchar length, effectively shortening the injected string. For example, if the username column is varchar(10), a payload like 'admin' followed by padding and a comment (e.g., 'admin     ' -- ) truncates to 'admin' -- , commenting out the password check. This procedure assumes a vulnerable PHP/MySQL web app like DVWA or a custom form. It maps to MITRE ATT&CK technique T1190 (Exploit Public-Facing Application) under tactic TA0001 (Initial Access). Use in controlled environments only.

## Requirements

1. Access to the target web application's login form (e.g., http://target.com/login.php) via browser or proxy.
2. Knowledge of the backend database (MySQL) and potential column lengths (probe via error messages or assume common varchar(10-20)).
3. Tools like curl for automated requests or Burp Suite for manual interception; no elevated privileges needed.
4. Valid target URL and basic understanding of HTTP POST requests for login.

## Defense

- Use prepared statements or parameterized queries (e.g., PDO in PHP) to prevent injection.
- Implement input validation and sanitization, limiting username length and escaping special characters.
- Enable MySQL strict mode to avoid silent truncation; log all SQL errors.
- Deploy Web Application Firewalls (WAF) to detect injection patterns like quotes and comments.

## Objectives

1. Confirm SQL injection vulnerability in the login form.
2. Craft and submit a truncation-based payload to bypass authentication as admin.
3. Gain unauthorized access to the admin dashboard or sensitive data.

## Instructions

### Step 1: Test for SQL Injection Vulnerability

**Context**: Send a basic injection probe to the login form to elicit SQL errors or unexpected behavior, confirming the vulnerability. This step verifies if inputs are unsanitized and reveals database type (MySQL).

**Command** ([[commands/curl-test-mysql-injection]]):
```bash
curl -X POST http://target.com/login.php -d "username=admin'" -d "password=pass" -c cookies.txt
```

> This sends a single quote in the username to break the SQL query, potentially causing a syntax error. Replace http://target.com/login.php with the actual login endpoint. The -c flag saves cookies for session persistence. Look for MySQL errors like "You have an error in your SQL syntax" in the response.

**Expected Output**: HTTP response with SQL error messages indicating MySQL backend, or a generic error differing from invalid credentials.

### Step 2: Craft and Submit Truncation Payload for Admin Bypass

**Context**: Based on the vulnerability, construct a payload that pads the username to exploit truncation (e.g., for varchar(10), use 'admin' + 5 spaces + "' -- " to truncate to 'admin' -- , commenting out password check). Submit via POST to authenticate as admin.

**Command** ([[commands/curl-admin-truncation-payload]]):
```bash
curl -X POST http://target.com/login.php -d "username=admin               '--" -d "password=anything" -b cookies.txt -c cookies.txt
```

> This payload assumes truncation at 20 characters (adjust padding spaces based on probed length). The "' --" closes the string and comments the rest of the query. Use -b to load prior cookies if needed. If successful, the response redirects to admin dashboard.

**Expected Output**: Successful login response, such as HTML for admin panel or a welcome message for admin user, without password validation errors.

### Step 3: Verify Admin Access

**Context**: After login, confirm elevated privileges by accessing admin-only features, such as viewing user lists or settings.

**Instructions**: Navigate to /admin.php or similar endpoint using the session cookies. Check for indicators like "Welcome, Admin" or access to restricted data.

**Expected Output**: Access to admin dashboard with sensitive information visible.

**Success Indicators**:
- No authentication failure; redirect to privileged area.
- Ability to perform admin actions (e.g., add users).
