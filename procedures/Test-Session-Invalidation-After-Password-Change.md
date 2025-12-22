---
id: 32e5da02-e91b-4852-84ce-1bfa30f6542c
name: Test-Session-Invalidation-After-Password-Change
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T15:43:14.482448+00:00'
updated_at: '2023-05-26T18:23:50.080804+00:00'
platforms:
  - Web
tags:
  - '[[tags/Session Management]]'
  - '[[tags/Web Applications]]'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Steal Web Session Cookie]]'
sub_techniques: []
commands: []
tools: []
validated: true
---

# Test-Session-Invalidation-After-Password-Change

## Summary

This procedure tests whether a web application's session management properly invalidates active sessions upon a password change. If the session remains valid in another browser instance after changing the password, it indicates a vulnerability that could allow an attacker to maintain unauthorized access and impersonate the user.

## Description

Proper session management requires that changing a user's password invalidates all existing sessions to prevent session hijacking. In vulnerable applications, an attacker who has obtained a valid session cookie (e.g., via XSS or interception) can continue using it even after the legitimate user changes their password. This procedure simulates the scenario by logging in with the same credentials in two separate browser sessions, changing the password in one, and verifying if the other session remains active. This is particularly relevant for web applications handling user authentication, where weak session handling can lead to account takeover. The test targets session cookies or tokens that are not properly tied to password changes or lack server-side invalidation mechanisms.

## Requirements

1. Access to the target web application with valid user credentials that allow password changes.
2. Two separate web browsers or browser instances (e.g., incognito windows or different browsers like Chrome and Firefox) to simulate concurrent sessions.
3. Optional: A proxy tool like [[tools/Burp-Suite]] to intercept and inspect session cookies and requests.
4. Basic knowledge of the application's login and password change flows.

## Defense

Defensive measures include implementing server-side session invalidation on password changes, using short-lived session tokens, binding sessions to additional factors like IP address or user-agent, and enabling logging of session activities for anomaly detection.

- Enforce session termination on password reset via server-side checks.
- Use secure, HttpOnly, and SameSite cookies to mitigate client-side theft.
- Monitor for concurrent logins from multiple sessions and flag suspicious activity.

## Objectives

1. Verify if active sessions are invalidated after a password change.
2. Identify potential for session hijacking if invalidation fails.
3. Document the vulnerability for remediation, such as updating session handling logic.

## Instructions

### Step 1: Establish Concurrent Sessions

**Context**: Log in to the application using the same credentials in two separate browser instances to create two valid sessions sharing the same account.

Open two browsers (or incognito windows). In both, navigate to the login page of the target application. Enter the same username and password to authenticate. After login, confirm access to a protected resource (e.g., user dashboard) in both sessions to verify valid sessions are established. Note the session cookies (e.g., via browser developer tools under Application > Cookies) for reference.

### Step 2: Change Password in One Session

**Context**: Initiate a password change in one browser to trigger any session invalidation mechanisms on the server.

In the first browser session, navigate to the account settings or password change page. Enter the current password, then provide a new password and confirm it. Submit the change and verify the password update succeeds (e.g., by attempting to log in with the old password in a new browser, which should fail).

### Step 3: Verify Session Validity in Second Browser

**Context**: Check if the second browser session remains active after the password change, indicating improper invalidation.

In the second browser, refresh the page or navigate to a protected resource. Attempt actions requiring authentication, such as viewing profile data or making changes. If the session is still valid (no logout or redirect to login), the vulnerability is confirmed. Optionally, inspect the session cookie in developer tools to see if it has changed or expired.

### Step 4: Document and Test Edge Cases

**Context**: Capture evidence of the failure and test variations to assess the vulnerability's scope.

Take screenshots of both sessions before and after the password change, showing continued access in the second session. Test additional scenarios, such as logging out and back in, or changing the password multiple times, to see if invalidation occurs under other conditions. If using a proxy, capture the HTTP requests to analyze how the server handles the password change without invalidating the session ID.
