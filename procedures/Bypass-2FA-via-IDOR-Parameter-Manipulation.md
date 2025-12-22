---
id: 528273ec-5365-45d9-bea6-41f65b5210e7
name: Bypass-2FA-via-IDOR-Parameter-Manipulation
type: procedure
verified: true
submitted: false
created_at: '2020-08-04T16:54:38.989773+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - authentication-bypass
  - 2fa-bypass
  - idor
  - owasp
  - owasp-top-10
  - web-applications
  - broken-authentication
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Bypass-2FA-via-IDOR-Parameter-Manipulation

## Summary

This procedure demonstrates a simple bypass of two-factor authentication (2FA) in a web application by exploiting an insecure direct object reference (IDOR) vulnerability in the post-login URL parameter. After authenticating with a username and password, the application requires a 4-digit 2FA code, but modifying the 'id' parameter in the '/my-account' URL allows access to another user's account without providing the 2FA code, assuming the attacker has the victim's username.

## Description

Many web applications implement 2FA as an additional security layer after username/password authentication, typically sending a time-based code via email or SMS. However, if the application fails to properly validate session ownership or user context after the initial login, attackers can manipulate client-side parameters to access other accounts. In this scenario, the vulnerability occurs in the '/my-account' endpoint, where the 'id' query parameter directly references the username without server-side checks tying it to the authenticated session. This allows an attacker with partial credentials (username/password for any account) to pivot to a target account by altering the URL. The technique relies on the application's assumption that the parameter is trustworthy, leading to unauthorized access. This is particularly effective in environments with shared login flows and weak session management, mapping to broken authentication issues in OWASP Top 10.

## Requirements

1. Valid username and password for any account on the target application (attacker's own or compromised via other means).
2. Knowledge of the target victim's username (e.g., 'carlos' in the example).
3. Access to a web browser or proxy tool like Burp Suite for URL manipulation and request interception.
4. Network access to the target web application (e.g., https://example.web-security-academy.net).
5. No 2FA code for the target account, as the bypass avoids this step.

## Defense

Defensive measures and detection strategies:

- Implement server-side validation to ensure the 'id' parameter matches the authenticated user's session ID or username.
- Use anti-CSRF tokens and bind session cookies strictly to user contexts.
- Enable logging of parameter changes and anomalous access patterns (e.g., accessing '/my-account' with mismatched IDs).
- Monitor for rapid account switches or unauthorized parameter tampering via web application firewall (WAF) rules.
- Enforce 2FA code validation at every sensitive endpoint, not just login.

## Objectives

1. Authenticate to the application using known credentials to establish a session.
2. Identify and manipulate the vulnerable URL parameter to access a target account.
3. Gain unauthorized access to the victim's account data without completing 2FA.

## Instructions

### Step 1: Create and Authenticate an Attacker Account

**Context**: Establish a valid session on the application using your own credentials. This simulates having partial access and allows observation of the normal login flow, including the 2FA prompt.

Navigate to the login page of the target application (e.g., https://acb81ffb1ef18e01807124ef00d10021.web-security-academy.net/login). Enter a newly created username (e.g., 'wiener') and password to log in. The application will prompt for a 4-digit 2FA security code sent to the registered email.

Retrieve the code from the email and enter it to complete authentication.

**Expected Output**: Successful login redirecting to the dashboard or account page, confirming session establishment.

### Step 2: Observe the Vulnerable URL Parameter

**Context**: After login, navigate to a sensitive endpoint like '/my-account' to identify exposed parameters that reference the user identity. This reveals the IDOR opportunity.

Click on 'My Account' or directly access https://acb81ffb1ef18e01807124ef00d10021.web-security-academy.net/my-account. Inspect the URL in the browser address bar or use developer tools (F12) to view the full request.

Look for query parameters like '?id=wiener', where 'wiener' is your username.

**Expected Output**: URL displays the current user's username in the 'id' parameter, e.g., https://acb81ffb1ef18e01807124ef00d10021.web-security-academy.net/my-account?id=wiener, with account details loaded.

### Step 3: Attempt 2FA Login with Victim Credentials

**Context**: Simulate the attacker's possession of the victim's username and password (obtained via phishing or other means). Log in but stop at the 2FA prompt to prepare for bypass.

Return to the login page and enter the victim's username (e.g., 'carlos') and password. Submit to reach the 2FA code prompt. Do not enter a code yet.

Optionally, use a proxy like [[tools/Burp-Suite]] to intercept the login request and observe session cookies.

**Expected Output**: Application prompts for the 4-digit 2FA code, with a partial session established but access blocked.

### Step 4: Manipulate URL to Bypass 2FA

**Context**: With the 2FA prompt active, modify the URL to reference the victim's account directly, exploiting the lack of server-side validation. This grants access without the code.

In the browser, append or modify the URL to include the victim's username in the 'id' parameter: https://acb81ffb1ef18e01807124ef00d10021.web-security-academy.net/my-account?id=carlos.

If using a proxy, intercept the request to '/my-account', alter the 'id' parameter, and forward it.

**Expected Output**: The application loads the victim's account details (e.g., profile information) without requiring the 2FA code, confirming the bypass.

### Step 5: Verify Access and Extract Data

**Context**: Confirm unauthorized access and document any sensitive information exposed, such as personal details or session tokens.

Interact with the loaded account page to view or download data. Check for further endpoints accessible under the hijacked session.

**Expected Output**: Full access to victim's 'My Account' page, displaying their information without authentication errors.

## Expected Output

Successful execution results in unauthorized access to the target account's sensitive data via the manipulated URL, bypassing the 2FA requirement entirely. No 2FA code is needed, and the session remains active for further actions.
