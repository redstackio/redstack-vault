---
id: f5566488-b6e4-40c1-b438-8edbbc9ddd85
name: Bypass-2FA-Using-Burp-Macros-and-Intruder
type: procedure
verified: true
submitted: false
created_at: '2020-08-04T18:02:46.716386+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Brute Force]]'
sub_techniques: []
tags:
  - authentication-bypass
  - broken-authentication
  - burp
  - owasp
  - owasp-top-10
  - web-applications
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Bypass-2FA-Using-Burp-Macros-and-Intruder

## Summary

This procedure demonstrates how to bypass two-factor authentication (2FA) on a web application by leveraging Burp Suite's Macros to automate the login sequence and Intruder to brute-force the 4-digit security code. It exploits the application's behavior after failed login attempts, replaying the authentication flow to test multiple codes efficiently.

## Description

Two-factor authentication adds an extra layer of security by requiring a time-sensitive or one-time code after username/password entry. However, if the application does not sufficiently rate-limit or lock out after failed 2FA attempts, an attacker can automate brute-forcing the code. This technique uses Burp Suite's session handling macros to simulate a valid login flow (including initial login and 2FA prompt) before each brute-force attempt via Intruder. The macro captures the dynamic 2FA code from the server's response and injects it into the final login request. This is particularly effective against short numeric codes (e.g., 4 digits, 0000-9999). The target environment is a web application with form-based authentication and 2FA enabled, assuming the attacker has valid username/password credentials for the victim account.

## Requirements

1. Valid username and password for the target account (obtained via phishing, credential stuffing, or other means).
2. Burp Suite Professional (Community edition lacks Macros and advanced Intruder features).
3. Network access to the target web application (no firewall blocking Burp traffic).
4. Proxy configuration on the browser to route traffic through Burp (intercept off for initial steps).
5. Basic familiarity with Burp Suite interface and HTTP request manipulation.

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on 2FA code submissions (e.g., lockout after 3-5 failed attempts).
- Use longer or non-numeric 2FA codes (e.g., 6-8 alphanumeric characters) to increase brute-force time.
- Monitor for anomalous login patterns, such as repeated failed 2FA attempts from the same IP or high-volume requests to login endpoints.
- Enable logging of authentication events and alert on brute-force indicators (e.g., via WAF rules for /login paths).
- Use adaptive MFA with device binding or push notifications instead of codes.

## Objectives

1. Automate the 2FA login flow using Burp Macros to extract and reuse dynamic session parameters.
2. Brute-force the 4-digit security code using Burp Intruder to identify the correct value.
3. Achieve successful authentication and session hijacking without alerting the user.
4. Expected outcome: Valid session cookie or token for the target account, granting access to protected resources.

## Instructions

### Step 1: Capture Initial Login Requests

**Context**: Log the normal login flow to capture the sequence of requests needed for the macro, including the 2FA prompt. This establishes the baseline HTTP interactions without triggering intercept.

Turn off intercept in Burp Proxy and configure your browser to proxy through Burp. Navigate to the login page and attempt login with the victim's credentials. The application should prompt for the 4-digit security code. Enter incorrect codes twice to trigger a failure and return to the login page. Review the HTTP history in Burp Proxy to identify key requests: GET /Login, POST /Login (credentials submission), and GET/POST /Login2 (2FA submission).

> This step ensures you have the exact request sequence for macro replay. Expected: HTTP history shows the full flow with 2FA prompt requests and error responses for incorrect codes.

### Step 2: Configure Session Handling with Macro

**Context**: Set up Burp's session handling rules to run a macro before targeted requests, automating the login and 2FA extraction.

In Burp, go to Project Options > Sessions > Add. Under Scope, include all URLs. In the Details tab, under Rule Actions, add "Run a macro." Select the captured requests (GET /Login, POST /Login with credentials, GET /Login2) from HTTP history. In the Macro Editor, test the macro to verify the final response contains the mfa-code parameter. Configure extraction rules to pull the mfa-code from the last macro response (e.g., using regex to match the code in the HTML or JSON response).

> The macro will replay the login, trigger the 2FA prompt, and extract the code for use in subsequent requests. Expected: Macro test succeeds with mfa-code visible in the editor's response preview.

### Step 3: Prepare Intruder for Brute-Force

**Context**: Send the 2FA submission request to Intruder and configure payloads to test all possible 4-digit codes, leveraging the macro for each attempt.

Right-click the POST /Login2 request in HTTP history and send to Intruder. Clear any default positions and mark the mfa-code parameter as a payload position (e.g., §mfa_code§). In Positions, ensure the session handling rule (with macro) is enabled. Under Payloads, select "Numbers" type, set from 0000 to 9999 (pad with zeros for consistency), and configure increment by 1.

> This automates testing 10,000 possibilities, with the macro running before each to refresh the session and code. Expected: Intruder payload list shows 0000-9999.

### Step 4: Execute and Analyze Brute-Force Attack

**Context**: Run the Intruder attack and identify the successful code based on response differences.

Start the attack in Intruder. Monitor responses for a 302 redirect (success) instead of 200 (ongoing) or 403/401 (failure). Sort results by status code or length to spot the hit. Once identified, copy the full request URL (including session tokens) and paste into your browser.

> Success is indicated by a 302 response leading to the dashboard or protected area. Expected: After ~10,000 requests (depending on rate), a single 302 appears; browser access grants full session.
