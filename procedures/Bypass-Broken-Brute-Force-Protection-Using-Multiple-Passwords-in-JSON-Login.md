---
id: aba85d85-1216-4bc0-a6f3-95fa8e161543
name: Bypass-Broken-Brute-Force-Protection-Using-Multiple-Passwords-in-JSON-Login
type: procedure
verified: true
submitted: true
created_at: '2020-09-05T07:38:30.933941+00:00'
updated_at: '2023-05-26T15:55:46.530834+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Brute Force]]'
sub_techniques: []
tags:
  - broken-authentication
  - brute-force-bypass
  - web-applications
commands:
  - '[[commands/curl-send-json-login-with-array-passwords]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Bypass-Broken-Brute-Force-Protection-Using-Multiple-Passwords-in-JSON-Login

## Summary

This procedure exploits a broken brute force protection mechanism in web applications that accept JSON-formatted login credentials without proper validation of user-controlled fields. By modifying the JSON payload to include multiple password attempts in a single request (e.g., as an array in the password field), an attacker can bypass rate limiting or attempt limits designed for single credentials per request, potentially gaining unauthorized access to user accounts.

## Description

Many web applications submit login credentials via JSON POST requests to endpoints like /login, with payloads such as {"username": "user", "password": "pass"}. If the server does not strictly validate the structure of the JSON fields—such as enforcing that the password is a scalar string rather than an array or object—an attacker can manipulate the payload to test multiple passwords in one submission. This circumvents brute force protections that track attempts per request or per IP, as the server may process the array sequentially and return a success response (e.g., 302 redirect) if any password matches. This technique is effective during authentication testing on APIs or web apps lacking input sanitization, particularly those using custom JSON parsers without schema validation. It maps to MITRE ATT&CK technique T1110 (Brute Force) under the Credential Access tactic, as it enables credential guessing at scale without triggering defenses.

## Requirements

1. Network access to the target web application's login endpoint (e.g., via browser or proxy).
2. A proxy tool like [[tools/Burp-Suite]] to intercept and modify HTTP requests.
3. A wordlist of potential passwords (e.g., from SecLists: https://github.com/danielmiessler/SecLists/tree/master/Passwords).
4. Known username for the target account (e.g., from reconnaissance or enumeration).
5. Basic understanding of JSON structure and HTTP POST requests.

## Defense

Defensive measures and detection strategies:

- Implement strict JSON schema validation on the server side to ensure the password field is a single string, rejecting arrays or objects (use libraries like JSON Schema or framework validators).
- Apply rate limiting based on username and IP, counting attempts across all requests regardless of payload size.
- Log and monitor JSON payloads for anomalies, such as oversized or array-based password fields, using WAF rules (e.g., ModSecurity) to block suspicious patterns.
- Enforce CAPTCHA or multi-factor authentication (MFA) after a few failed attempts to deter automated guessing.
- Use account lockout mechanisms that persist across sessions and requests.

## Objectives

1. Identify if the login endpoint accepts and processes non-standard JSON payloads without validation.
2. Submit multiple password guesses in a single request to bypass per-request brute force limits.
3. Achieve successful authentication to the target account, gaining unauthorized access.
4. Expected outcome: A successful login response (e.g., 302 redirect to dashboard) confirming at least one password match.

## Instructions

### Step 1: Capture Legitimate Login Request

**Context**: Intercept a normal login attempt to analyze the JSON format and endpoint details. This establishes the baseline request structure for modification.

Use [[tools/Burp-Suite]] to proxy traffic and capture the POST request during a failed login with incorrect credentials.

> No specific command is needed for interception, as this is a GUI action in Burp's Proxy tab. Ensure Burp is configured to intercept requests to the target domain. Submit valid username with wrong password to trigger an error response (e.g., 401 or 403), confirming the JSON format like {"username": "targetuser", "password": "wrongpass"}.

### Step 2: Send Request to Repeater for Modification

**Context**: Transfer the captured request to Burp Repeater for safe experimentation and payload alteration without affecting the live application.

In Burp's HTTP History, right-click the login POST request and select "Send to Repeater." This allows isolated testing of modified payloads.

> Expected: The request loads in Repeater with original JSON body visible in the Raw or Params tab.

### Step 3: Modify JSON Payload with Multiple Passwords

**Context**: Alter the password field to an array containing multiple guesses. The server may iterate over the array, checking each one, and succeed if any matches—bypassing single-attempt limits.

**Command** ([[commands/curl-send-json-login-with-array-passwords]]):
```bash
curl -X POST $_URL -H "Content-Type: application/json" -d '{"username":"$_USERNAME","password":[$_PASSWORD_ARRAY]}'
```

> Replace $_URL with the login endpoint (e.g., https://target.com/login), $_USERNAME with the target (e.g., "admin"), and $_PASSWORD_ARRAY with a JSON array of passwords (e.g., ["pass1", "pass2", "correctpass"]) from your wordlist. This simulates the Burp modification or can be run directly via curl for automation. If using Burp Repeater, edit the JSON body manually to match this structure and click Send.

### Step 4: Submit and Analyze Response

**Context**: Execute the modified request and check for success indicators, such as a redirect or session cookie, confirming the bypass worked.

Submit the request in Burp Repeater or via the curl command above.

> Expected: If a correct password is in the array, the response will be a 302 Found redirect to a protected page (e.g., /dashboard), often with a Set-Cookie header for session management. On failure, expect a 401/403 with error message. Copy the redirect URL from the response Location header and load it in a browser to verify access.

### Step 5: Verify Access

**Context**: Confirm unauthorized access by accessing account-specific resources, ensuring the brute force bypass granted valid session.

Follow the redirect URL in a browser or use curl to fetch a protected endpoint with the session cookie from the response.

> Success: Dashboard or user profile loads with the target's data, indicating login success.
