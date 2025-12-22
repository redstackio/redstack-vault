---
id: cc4ca29f-dd1e-4ed1-8918-549b48d12d8b
name: Bypass-User-Role-via-Cookie-Parameter-Manipulation
type: procedure
verified: true
submitted: false
created_at: '2020-08-31T18:23:18.939853+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Web
tags:
  - access-control
  - authorization-bypass
  - web-applications
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
commands:
  - '[[commands/curl-access-admin-false-cookie]]'
  - '[[commands/curl-post-login]]'
  - '[[commands/curl-access-admin-true-cookie]]'
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Bypass-User-Role-via-Cookie-Parameter-Manipulation

## Summary

This procedure exploits insecure access control in web applications where user roles are determined by client-side cookie parameters without server-side validation. By modifying the 'Admin' cookie from 'false' to 'true', an attacker can gain unauthorized access to administrative functions, such as viewing or managing the admin panel.

## Description

Web applications sometimes store sensitive role information, like admin privileges, in cookies or request parameters that are accessible to the client. Without proper server-side enforcement, an attacker can tamper with these values during requests to elevate their privileges. This technique is common in legacy or poorly implemented authentication systems and can lead to full compromise of administrative features. The target environment is typically a web application with a login mechanism that sets role-based cookies upon authentication.

## Requirements

- Network access to the target web application (e.g., valid low-privilege user account).
- HTTP client tool like curl for testing requests.
- Optional: Proxy tool such as [[tools/Burp-Suite]] for intercepting and modifying live traffic in a browser session.
- Knowledge of the application's endpoints (e.g., /login and /admin).

## Defense

- Implement server-side authorization checks for all protected endpoints, ignoring client-supplied role indicators.
- Use secure, signed cookies (e.g., via HttpOnly and Secure flags) and store roles in server-side sessions.
- Enable web application firewall (WAF) rules to detect cookie tampering patterns.
- Log and monitor access to admin endpoints for anomalies, such as logins from unusual IPs or sudden role changes.

## Objectives

1. Confirm that admin access is restricted for standard users.
2. Identify and manipulate the role-controlling cookie parameter.
3. Gain and verify elevated access to administrative areas.

## Instructions

### Step 1: Attempt Access to Admin Panel with Default Cookie

**Context**: Test the admin endpoint with the default non-admin cookie to confirm access controls are in place. This verifies the vulnerability exists only after manipulation.

**Command** ([[commands/curl-access-admin-false-cookie]]):
```bash
curl -v -H "Cookie: Admin=false" "http://target.example.com/admin"
```

> This step sends a GET request to the admin panel with the Admin cookie set to false, simulating a standard user. The purpose is to observe the denial response, ensuring the endpoint is protected.

### Step 2: Perform Login to Obtain Session Cookie

**Context**: Authenticate with valid low-privilege credentials to establish a session and capture the default cookie value, which includes the Admin=false parameter.

**Command** ([[commands/curl-post-login]]):
```bash
curl -v -X POST -d "username=standarduser&password=standardpass" -c cookies.txt "http://target.example.com/login"
```

> This logs in and saves the session cookies to a file. Inspect cookies.txt to confirm the Admin=false value is set. If using [[tools/Burp-Suite]], intercept the POST request here to view the response-set cookie.

### Step 3: Modify Cookie and Access Admin Panel

**Context**: Tamper with the captured cookie by changing Admin to true, then re-request the admin endpoint to bypass controls and gain elevated access.

**Command** ([[commands/curl-access-admin-true-cookie]]):
```bash
curl -v -H "Cookie: Admin=true" "http://target.example.com/admin"
```

> Edit the cookie manually (e.g., via text editor on cookies.txt or directly in the header) to set Admin=true. This step elevates the request to admin level. Alternatively, use [[tools/Burp-Suite]] to intercept a browser request to /admin and modify the cookie inline for real-time testing.
