---
id: f6b5c697-6670-4147-a0ee-5a275acf5618
name: Bypass-2FA-via-Verify-Parameter-Manipulation-and-Brute-Force
type: procedure
verified: true
submitted: true
created_at: '2020-09-05T05:40:56.124670+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Brute Force]]'
sub_techniques:
  - '[[Domain Accounts]]'
tags:
  - broken authentication
  - Web Applications
  - 2fa-bypass
  - brute-force
  - logic-flaw
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Bypass-2FA-via-Verify-Parameter-Manipulation-and-Brute-Force

## Summary

This procedure exploits a logic flaw in a web application's two-factor authentication (2FA) mechanism, where the 'verify' parameter in the authentication request determines the target user account. By manipulating this parameter to switch to a victim's username and brute-forcing the short 4-digit MFA code using Burp Suite's Intruder, an attacker can bypass 2FA and gain unauthorized access to the victim's account without needing their primary credentials or the actual MFA code sent to the victim.

## Description

In vulnerable web applications with 2FA enabled, the MFA verification endpoint may rely on a 'verify' parameter (often a username or email) to associate the submitted MFA code with the correct user session. If this parameter is not properly validated or bound to the authenticated session, an attacker who has completed their own login (including entering their own MFA code) can intercept the subsequent request, modify the 'verify' parameter to the victim's identifier, and then brute-force the 4-digit code. Since 4-digit codes have only 10,000 possibilities, this can be done quickly offline or via automated tools like Burp Intruder. This technique represents a broken authentication logic flaw, allowing account takeover in environments where users share the same application instance. It is commonly found in custom web apps and can lead to full compromise of user sessions, data access, or further lateral movement.

## Requirements

1. Valid credentials for an attacker-controlled account in the target web application to establish an authenticated session.
2. Access to the web application's login and 2FA endpoints (typically over HTTPS, port 443).
3. Burp Suite Professional (for Intruder functionality) or equivalent proxy tool capable of request interception and brute-forcing.
4. Knowledge of the target victim's username or email (e.g., 'carlos' in lab scenarios; in real-world, obtained via enumeration or social engineering).
5. Network access to the application without blocking from WAF or IP restrictions.

## Defense

Defensive measures and detection strategies:

- Bind MFA verification strictly to the session's authenticated user ID using secure session tokens or JWT claims that cannot be altered client-side.
- Implement rate limiting on MFA code submissions per user account to prevent brute-force attacks (e.g., lockout after 5 failed attempts).
- Use longer or time-based one-time passwords (TOTP) instead of short static codes sent via email/SMS.
- Validate that the 'verify' parameter matches the session's user identifier server-side, rejecting mismatches.
- Monitor for anomalous login patterns, such as multiple failed MFA attempts from the same IP or session, using tools like SIEM or web application firewalls (WAF).
- Enable logging of all authentication requests, including parameter values, to detect manipulation attempts.

## Objectives

1. Establish an authenticated session with the attacker's own credentials to access the MFA verification flow.
2. Identify and exploit the logic flaw in the 'verify' parameter to target a victim's account.
3. Brute-force the victim's 4-digit MFA code to complete unauthorized authentication.
4. Achieve session hijacking and access to the victim's account dashboard or resources.

## Instructions

### Step 1: Authenticate with Attacker Credentials and Intercept Login Flow

**Context**: Log in using your own valid credentials to reach the 2FA prompt, while proxying traffic through Burp Suite to capture the requests. This establishes a legitimate session that can later be manipulated.

Configure your browser to proxy requests through [[tools/Burp-Suite]] (set proxy to 127.0.0.1:8080). Navigate to the application's login page, enter your username and password, and submit. Intercept the login POST request if needed to observe the flow, then proceed to the 2FA page where a 4-digit code is requested.

Observe that the application sends an email with the 4-digit code to your registered email address. Retrieve and enter this code to complete your login, ensuring you now have an active session.

### Step 2: Identify the MFA Verification Request and Verify Parameter

**Context**: During the 2FA submission, intercept the request to analyze parameters. The key is the 'verify' parameter, which specifies the user for code validation, allowing potential manipulation.

With Burp Suite intercepting, submit your 4-digit code. In the intercepted POST request to the MFA endpoint (e.g., /login2fa or similar), note the 'verify' parameter set to your username and the 'mfa-code' parameter with the 4-digit value. Also, identify any preceding GET request to /Login2 that may contain session data.

Forward the request to complete your login. Confirm access to your account dashboard.

### Step 3: Prepare the Request for Intruder and Modify Verify Parameter

**Context**: Replay the GET /Login2 request (or the relevant session-maintaining request) to Burp's Intruder to set up brute-forcing. Change the 'verify' parameter to the victim's username to redirect the MFA validation to their account.

In Burp's Proxy history, right-click the GET /Login2 request after successful login and select "Send to Intruder." In the Intruder tab, go to the Positions sub-tab and clear all positions. Manually edit the 'verify' parameter in the raw request to the victim's username (e.g., 'carlos').

In the Positions sub-tab, highlight the 'mfa-code' value (e.g., §1234§) and click "Add §" to mark it as the payload position for brute-forcing.

### Step 4: Configure Payloads and Execute Brute-Force Attack

**Context**: Set up Intruder to test all possible 4-digit codes (0000-9999) against the victim's account. A successful match will return a 302 redirect, indicating valid authentication.

In the Payloads sub-tab, select "Numbers" as the payload type, set From to 0000 and To to 9999, with step 1 and no padding. Ensure the payload is injected into the 'mfa-code' position. Click "Start Attack" to launch the brute-force.

Monitor the results table for response codes. Most requests will return 401/403 (invalid code), but the correct code will yield a 302 Found redirect to the dashboard.

### Step 5: Extract Valid Code and Complete Victim Login

**Context**: Use the discovered MFA code to manually submit the modified request, bypassing 2FA for the victim's account and gaining unauthorized access.

Note the payload value (4-digit code) that produced the 302 response. Return to the Repeater tab in Burp (or manually craft the request), set 'verify' to the victim's username, 'mfa-code' to the discovered value, and forward/submit the request.

Follow the 302 redirect to access the victim's account dashboard, confirming successful takeover.
