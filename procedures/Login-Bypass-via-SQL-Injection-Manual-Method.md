---
id: c3f11bc0-1722-479c-903d-a7a054b232f6
name: Login-Bypass-via-SQL-Injection-Manual-Method
type: procedure
verified: true
submitted: true
created_at: '2020-07-21T15:34:42.728844+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Web
tags:
  - '[[tags/injection]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/SQL]]'
  - '[[tags/sqli]]'
  - '[[tags/Web Applications]]'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
commands:
  - '[[commands/curl-simulate-login-bypass-sqli]]'
tools: []
validated: true
---

# Login-Bypass-via-SQL-Injection-Manual-Method

## Summary

This procedure demonstrates how to bypass authentication in a web application using SQL injection by manually injecting payloads into login form fields. The payloads manipulate the underlying SQL query to always evaluate to true, granting access without valid credentials. Common payloads include ' or '1'='1 and variations for single or double quotes, suitable for testing vulnerable login endpoints.

## Description

SQL injection in login forms typically targets queries like SELECT * FROM users WHERE username = '$input_username' AND password = '$input_password'. By injecting a payload such as ' or '1'='1 into both fields, the query becomes SELECT * FROM users WHERE username = '' or '1'='1' AND password = '' or '1'='1', which always returns true and logs in as the first user in the database (often an admin). This technique exploits poor input sanitization and is a classic OWASP Top 10 vulnerability (A03:2021 - Injection). It requires direct interaction with the login form via browser or tools like curl for simulation. Variations handle different quote escaping, such as using -- for comment termination or true-- to ignore trailing conditions. Success depends on the backend database (e.g., MySQL, PostgreSQL) and lack of prepared statements or WAF protection.

## Requirements

1. Network access to the target web application's login page (e.g., http://target.com/login).
2. Knowledge of the login form's HTTP method (usually POST) and field names (typically 'username' and 'password').
3. A tool like curl for command-line testing or a browser for manual form submission; optionally, a proxy like Burp Suite for interception.
4. Basic understanding of HTTP requests and SQL syntax.

## Defense

Defensive measures and detection strategies:

- Use prepared statements or parameterized queries to separate code from user input.
- Implement input validation and sanitization, escaping special characters.
- Deploy a Web Application Firewall (WAF) to detect and block SQLi patterns.
- Enable database logging to monitor anomalous queries; use tools like fail2ban for repeated failed logins.
- Conduct regular security testing with tools like sqlmap to identify vulnerabilities.

## Objectives

1. Identify a vulnerable login endpoint susceptible to SQL injection.
2. Inject payloads to bypass authentication and gain unauthorized access.
3. Verify successful login by accessing protected resources or admin panels.

## Instructions

### Step 1: Identify Login Form Details

**Context**: Examine the login page to determine the form action URL, method (GET/POST), and field names. This ensures accurate payload delivery. Use browser developer tools (F12) to inspect the form or intercept with a proxy.

No specific command required for inspection; manually review the HTML source for <form> attributes and input names.

> Expected: Confirmation of fields like <input name="username"> and <input name="password">, and the endpoint URL (e.g., /login.php).

### Step 2: Prepare SQLi Payloads

**Context**: Select an appropriate payload based on the application's quote handling. Start with simple ones and escalate to variations if needed. Common payloads include:

- ' or '1'='1 (single quotes)
- " or "1"="1 (double quotes)
- or true-- (comment termination)
- ' or 'x'='x
- ') or ('x')=('x

Inject the same payload into both username and password fields to make the entire WHERE clause true.

No command; manually note the payload for use in the next step.

> Expected: A list of 2-3 payloads ready for testing, starting with the most common.

### Step 3: Submit Payload via curl

**Context**: Simulate the login request using curl to inject the payload. This allows precise control over the HTTP request and easy iteration on payloads. Replace placeholders with actual values and observe responses for success (e.g., redirect or session cookie).

**Command** ([[commands/curl-simulate-login-bypass-sqli]]):
```bash
curl -X POST -d "username=' or '1'='1&password=' or '1'='1" $_TARGET_URL
```

> This command sends a POST request to the login endpoint with the SQLi payload in both fields. If vulnerable, the response will indicate successful authentication, such as a 302 redirect to a dashboard or HTML containing "Welcome" messages. If it fails, try alternative payloads like " or 1=1--. For manual browser testing, enter the payload directly into the form fields and submit.

### Step 4: Verify Access

**Context**: Confirm the bypass by checking for authenticated features, such as user profile or admin controls. If successful, the application treats you as a valid user (often the first in the DB).

No command; follow any redirect from the previous step or manually navigate to protected pages.

> Expected: Access to restricted areas without errors, possibly with a session cookie set (e.g., Set-Cookie: session=abc123).
