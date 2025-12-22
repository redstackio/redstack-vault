---
id: 5f893737-d433-4d82-b138-a12a0e0f89eb
name: LDAP-Injection-Login-Bypass
type: procedure
verified: true
submitted: true
created_at: '2020-08-15T10:57:40.326777+00:00'
updated_at: '2023-05-26T01:26:13.355993+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - injection
  - LDAP Injection
  - owasp
  - owasp top 10
  - Web Applications
commands:
  - '[[commands/curl-send-ldap-injection-payload]]'
platforms:
  - Web
tools: []
validated: true
---

# LDAP-Injection-Login-Bypass

## Summary

This procedure demonstrates how to bypass authentication in a web application's login mechanism vulnerable to LDAP injection by crafting a malicious payload that alters the LDAP query to always evaluate to true, allowing unauthorized access without valid credentials.

## Description

LDAP injection occurs when user-supplied input is improperly sanitized and concatenated into LDAP queries, enabling attackers to manipulate the query logic. In a typical login form, the application constructs an LDAP filter like "(&(uid=$username)(userPassword=$password))". By injecting special LDAP characters such as parentheses and operators, an attacker can close the current query and append a tautology (e.g., "*") to force authentication success. This technique targets web applications using LDAP for user authentication, such as those integrated with Active Directory or OpenLDAP. Success grants access to the application as the targeted user, potentially leading to further exploitation like privilege escalation or data access. This procedure assumes a vulnerable login endpoint and focuses on form-based input; it maps to MITRE ATT&CK technique T1190 (Exploit Public-Facing Application) under Initial Access (TA0001).

## Requirements

1. Access to the web application's login page (e.g., via browser or API client).
2. Knowledge of a valid username in the LDAP directory (e.g., 'slisberger') to base the injection on.
3. Optional: Intercepting proxy like Burp Suite for request manipulation if direct form input is blocked.
4. Network connectivity to the target application.

## Defense

Defensive measures and detection strategies:

- Implement input validation and sanitization to escape LDAP special characters (e.g., *, (, ), & , | ).
- Use parameterized LDAP queries or LDAP filters that treat input as literal strings, avoiding concatenation.
- Enable LDAP query logging on the directory server to monitor for anomalous filters (e.g., tautologies like *).
- Deploy web application firewalls (WAFs) with rules to detect LDAP injection patterns in login requests.
- Conduct regular vulnerability scanning with tools like OWASP ZAP or Burp Suite to identify injection points.

## Objectives

1. Identify and exploit an LDAP injection vulnerability in the login form to bypass authentication.
2. Gain unauthorized access to the application using the injected payload.
3. Verify successful login without providing a valid password.

## Instructions

### Step 1: Identify the Login Endpoint

**Context**: Locate the login form or API endpoint to understand the input fields (typically 'username' or 'user' and 'password'). This step ensures you target the correct vulnerable point; inspect the page source or use developer tools to confirm it's an HTML form submitting to a POST endpoint like /login.

No specific command required for identification; use browser inspection.

### Step 2: Craft and Submit the LDAP Injection Payload

**Context**: Append LDAP operators to the username input to manipulate the query. Using a known username like 'slisberger', the payload "slisberger)(&))" closes the attribute filter and injects a universal match, effectively making the query return true for any password. This bypasses the need for valid credentials. Submit via the form or simulate with a tool if direct input is not possible.

**Command** ([[commands/curl-send-ldap-injection-payload]]):
```bash
curl -X POST http://target.com/login \
  -d "user=slisberger)(&))&pass=" \
  -v
```

> This command sends a POST request to the login endpoint with the injected username payload and an empty password. The -v flag provides verbose output to inspect the response. Replace http://target.com/login with the actual endpoint URL. If the application uses a different field name (e.g., 'username'), adjust the -d parameter accordingly. Expected output includes a successful login redirect (e.g., 302 to dashboard) or session cookie without errors.

### Step 3: Verify Successful Bypass

**Context**: After submission, check for authentication success indicators such as a welcome page, user dashboard, or session establishment. If intercepted with a proxy, confirm the response lacks authentication failure messages.

No specific command; inspect the response body or browser session for user-specific content (e.g., "Welcome, slisberger").
