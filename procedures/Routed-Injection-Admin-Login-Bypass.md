---
type: procedure
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - routed-injection
  - sql-injection
commands:
  - '[[commands/curl-post-sql-injection-payload]]'
tools: []
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Routed-Injection-Admin-Login-Bypass

## Summary

The Routed Injection Admin Login Bypass procedure exploits SQL injection vulnerabilities in web application authentication mechanisms to bypass login requirements and gain unauthorized administrative access. By injecting a crafted SQL payload into the login form's username parameter, the technique forces the database query to return hardcoded administrator credentials, allowing direct access to privileged features without valid authentication.

## Description

This procedure targets web applications with unsanitized user inputs in login forms, particularly those using dynamic SQL queries to validate credentials against a backend database like MySQL or PostgreSQL. The attack leverages a UNION-based SQL injection to append a fabricated row of admin credentials to the query results, effectively tricking the application into authenticating the attacker as an admin user. It is commonly applicable in scenarios where the login endpoint is exposed publicly and lacks proper input validation, such as custom-built e-commerce or CMS platforms. Successful execution grants immediate access to sensitive administrative functions, potentially enabling data manipulation, user account control, or further exploitation. The technique assumes knowledge of a common admin username (e.g., 'admin') and uses a precomputed hash for a weak password like '1234' to minimize cracking efforts.

## Requirements

1. Network access to the target web application's login page (e.g., http://target.com/login).
2. A tool like curl or a proxy such as Burp Suite to intercept and modify HTTP requests.
3. Basic knowledge of the target's database type (e.g., MySQL) and common admin usernames.
4. The login form must use POST parameters for username and password that are directly concatenated into SQL queries.

## Defense

Defensive measures and detection strategies:

- Implement prepared statements or parameterized queries in the backend to separate SQL code from user input.
- Apply input validation and sanitization, escaping special characters like single quotes and rejecting suspicious patterns.
- Deploy a Web Application Firewall (WAF) to detect and block UNION SELECT or other injection signatures in requests.
- Enable database logging to monitor for anomalous queries and multi-factor authentication (MFA) for admin accounts to add an extra layer beyond SQL validation.

## Objectives

1. Identify and confirm SQL injection vulnerability in the login authentication query.
2. Inject a UNION SELECT payload to fabricate admin credentials and bypass authentication.
3. Gain administrative access to the web application dashboard or backend features.
4. Verify successful login and explore privileged functionalities.

## Instructions

### Step 1: Identify the Login Endpoint and Parameters

**Context**: Locate the login form's submission endpoint and inspect the parameters used for authentication. This step ensures you understand the structure of the HTTP request, typically a POST to /login with username and password fields.

Use browser developer tools or a proxy to capture the request. Look for the action URL and form fields.

### Step 2: Test for SQL Injection Vulnerability

**Context**: Probe the username parameter for SQL injection by appending a single quote or boolean condition to disrupt the query and observe error messages or behavior changes, confirming the vulnerability.

**Command** ([[commands/curl-post-sql-injection-payload]]):
```bash
curl -X POST -d "username=admin'" -d "password=test" http://target.com/login --cookie-jar cookies.txt
```

> This sends a malformed username to trigger a SQL syntax error if unsanitized. Expected output includes database error messages (e.g., "You have an error in your SQL syntax") or unexpected login behavior, confirming injectability.

### Step 3: Craft and Inject the Bypass Payload

**Context**: Use a pre-built SQL payload to neutralize the original query and union a fake admin row. The payload targets the username field, assuming the query structure is SELECT * FROM users WHERE username='$input' AND password='$pass'.

Embed the payload from [[codes/SQL-Union-Select-Admin-Bypass-Payload]] into the username parameter.

**Command** ([[commands/curl-post-sql-injection-payload]]):
```bash
curl -X POST -d "username=admin' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055'" -d "password=anything" http://target.com/login --cookie-jar cookies.txt -c cookies.txt
```

> The AND 1=0 ensures no match from the original table, while UNION ALL appends the admin row. Expected output is a successful login redirect to the admin dashboard, with session cookies set for authenticated access.

### Step 4: Verify Administrative Access

**Context**: Confirm the bypass by accessing protected admin routes and checking for elevated privileges.

Navigate to /admin or use the captured cookies in subsequent requests.

**Command** ([[commands/curl-post-sql-injection-payload]]):
```bash
curl -b cookies.txt http://target.com/admin
```

> Expected output displays admin-specific content, such as user management interfaces, without further authentication prompts.
