---
id: 49e92cda-7a3b-4ffb-848a-8eb2433a60e9
name: Bypass-2FA-via-Force-Browsing
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:53.960614+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques: []
tags:
  - '[[tags/2FA Bypasses]]'
  - '[[tags/Account Takeover]]'
  - '[[tags/Bypass 2FA by Force Browsing]]'
commands:
  - '[[commands/curl-perform-login]]'
  - '[[commands/curl-access-my-account]]'
platforms:
  - Web
tools: []
validated: true
---

# Bypass-2FA-via-Force-Browsing

## Summary

This procedure demonstrates how to bypass two-factor authentication (2FA) in web applications by force browsing to protected endpoints using an established session cookie from initial login. It exploits misconfigurations where 2FA checks are not enforced on all authenticated paths, allowing unauthorized access to account data without providing the 2FA code.

## Description

In many web applications, after a user enters their username and password, a session cookie is issued, and they are redirected to a 2FA verification page (e.g., /2fa/verify). If the application fails to enforce 2FA on subsequent requests to sensitive endpoints like /my-account, an attacker can use the session cookie to directly access those pages. This technique is effective against applications with inconsistent authorization logic and is commonly used in account takeover scenarios following phishing or credential stuffing. The target environment is typically a web application with cookie-based session management, such as those built on frameworks like Django, Rails, or custom PHP setups. Success relies on the session remaining valid post-login but pre-2FA completion.

## Requirements

1. Valid username and password for the target account.
2. Knowledge of the application's login endpoint URL (e.g., https://target.com/login) and protected endpoint (e.g., https://target.com/my-account).
3. Network access to the target web application.
4. Tools like curl for request manipulation or a browser with developer tools for cookie handling.

## Defense

Defensive measures and detection strategies:

- Enforce 2FA checks on all authenticated endpoints using middleware or session validation logic.
- Implement session flags to track 2FA completion status and invalidate sessions without it.
- Monitor for anomalous access patterns, such as direct requests to sensitive pages post-login without 2FA events in logs.
- Use web application firewalls (WAFs) to detect force browsing attempts via URL access logs.

## Objectives

1. Establish a valid session without completing 2FA.
2. Gain unauthorized access to protected account resources.
3. Extract sensitive user data or perform actions on the account.

## Instructions

### Step 1: Perform Initial Login to Obtain Session Cookie

**Context**: Log in with the target's credentials to create a session cookie, but do not proceed to 2FA submission. This step establishes the necessary authentication state.

**Command** ([[commands/curl-perform-login]]):
```bash
curl -c cookies.txt -d "username=$_USERNAME&password=$_PASSWORD" -X POST https://$_TARGET_URL/login
```

> This command sends a POST request to the login endpoint, saving the session cookie to cookies.txt. The response should indicate a successful login redirect or session creation, typically with a 302 status or a message like "2FA required." Verify the cookie file is created and contains a session ID.

### Step 2: Access Protected Endpoint Directly with Session Cookie

**Context**: Use the session cookie from the login to request the protected /my-account page, bypassing the 2FA verification step. This exploits the lack of 2FA enforcement on the endpoint.

**Command** ([[commands/curl-access-my-account]]):
```bash
curl -b cookies.txt https://$_TARGET_URL/my-account
```

> This command loads the session cookie and fetches the /my-account page. If successful, the response will contain account details (e.g., HTML with user info) without prompting for 2FA. Check for 200 OK status and absence of 2FA-related redirects or errors. If access is granted, the bypass succeeded.
