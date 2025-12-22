---
id: 06c60f55-5d85-4fcd-8953-84a5858de96d
name: Privilege Escalation via Direct URL Access
type: procedure
verified: true
submitted: true
created_at: '2020-07-27T18:14:21.196503+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Web
tags:
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Privilege Escalation]]'
  - '[[tags/privileges]]'
  - '[[tags/Web Applications]]'
  - broken-access-control
  - idor
tactics:
  - '[[Privilege-Escalation-via-Direct-URL-Access]]'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
sub_techniques: []
commands:
  - '[[commands/curl-web-login]]'
  - '[[commands/curl-access-admin-url]]'
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Privilege Escalation via Direct URL Access

## Summary

This procedure demonstrates a vertical privilege escalation technique in web applications by directly accessing URLs intended for higher-privilege users (e.g., admin functions) using a lower-privilege user session. It exploits broken access controls where the application fails to enforce authorization checks on the server side, allowing unauthorized functionality to load if the URL is known.

## Description

In many web applications, access to privileged features is controlled solely by hiding URLs from low-privilege users, without server-side enforcement. An attacker with a valid low-privilege session can escalate privileges by manually navigating to or requesting admin URLs (e.g., /admin/users). Success is indicated if the page loads and executes admin actions without prompting for re-authentication. This is a form of Insecure Direct Object Reference (IDOR) or broken access control, commonly seen in OWASP Top 10 (A01:2021 - Broken Access Control). The technique assumes the application uses session-based authentication where cookies persist across requests. It targets web apps with role-based access control (RBAC) flaws and requires reconnaissance to identify privileged endpoints.

## Requirements

1. Valid low-privilege user credentials (e.g., standard user account).
2. Knowledge of privileged URLs (e.g., via source code review, error messages, or directory brute-forcing).
3. Network access to the web application (direct or proxied).
4. Tools for session management, such as a web browser or [[tools/Burp-Suite]] for intercepting requests.
5. Optional: Proxy tool like [[tools/Burp-Suite]] to inspect and replay requests with session cookies.

## Defense

- Implement server-side authorization checks for every endpoint using RBAC or attribute-based access control (ABAC).
- Use indirect references (e.g., UUIDs) instead of predictable URLs for sensitive resources.
- Enable web application firewalls (WAFs) to detect anomalous URL access patterns.
- Log and monitor access to admin endpoints, alerting on low-priv sessions.
- Conduct regular access control testing with tools like OWASP ZAP or Burp Suite.

## Objectives

1. Authenticate as a low-privilege user to establish a valid session.
2. Access a privileged URL using the existing session to bypass authorization.
3. Verify elevated functionality loads, confirming privilege escalation.

## Instructions

### Step 1: Authenticate as Low-Privilege User

**Context**: Establish a valid session cookie for a standard user account. This step simulates logging in via the application's login form, capturing the session token for reuse.

**Command** ([[commands/curl-web-login]]):
```bash
curl -X POST -d "username=$_USERNAME&password=$_PASSWORD" -c cookies.txt $_LOGIN_URL
```

> This command sends a POST request to the login endpoint with credentials, saving the session cookie to a file (cookies.txt). Replace placeholders with actual values. Expected: A 200 OK response or redirect to dashboard, with cookies.txt containing the session ID (e.g., JSESSIONID or PHPSESSID). If login fails, check credentials or endpoint URL.

### Step 2: Access Privileged URL with Existing Session

**Context**: Use the captured session to request a URL intended for admin users (e.g., /admin/user-list). This tests if server-side checks are absent, allowing the low-priv session to load elevated content.

**Command** ([[commands/curl-access-admin-url]]):
```bash
curl -b cookies.txt $_ADMIN_URL
```

> This command loads the admin URL using the browser cookie jar. The session identifier remains the same, mimicking browser navigation. Expected: The response body contains admin functionality (e.g., user list table) without auth errors. If blocked, the app has proper controls; otherwise, escalation succeeds. Use [[tools/Burp-Suite]] to intercept and modify if needed for evasion.
