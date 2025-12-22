---
tags:
  - 2fa-bypass
  - response-tampering
  - business-logic
  - auth-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Modify Authentication Process]]'
updated_at: '2025-12-14T17:24:47.635Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 246411ba-fe28-4edb-921f-79b69f1ab91f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
---
# Tamper-with-2FA-Disable-API-Response

## Summary

This procedure exploits a business logic flaw in the 2FA removal process of the 8x8 web application by intercepting and modifying API responses, allowing an attacker to disable two-factor authentication without providing the correct password, leading to potential account takeover.

## Description

The vulnerability arises from insufficient server-side validation in the 2FA disable endpoint. When a user attempts to remove 2FA with an incorrect password, the server should reject the request, but the client-side handling relies on the response payload. By using a proxy tool to tamper with the response (e.g., changing a failure status to success), the application incorrectly processes the request as valid. This occurs in an authenticated session targeting the account security features. Prerequisites include valid login credentials and access to a proxy for traffic interception. Expected outcomes include successful 2FA disablement, removing the multi-factor barrier and exposing the account to unauthorized access.

## Requirements

1. Authenticated session to the 8x8 web application with access to 2FA settings
2. Proxy tool like Burp Suite installed and configured to intercept HTTPS traffic (requires CA certificate installation in browser)
3. Knowledge of the API endpoint for 2FA disablement (typically /api/2fa/disable or similar, discovered via network inspection)

## Defense

Defensive measures and detection strategies:

- Implement server-side re-validation of all critical actions, including independent password checks post-response
- Use signed or encrypted responses to prevent tampering
- Monitor for anomalous API response patterns or proxy-like traffic anomalies in logs
- Enforce strict client-side integrity checks and rate limiting on auth changes

## Objectives

1. Bypass password verification during 2FA removal
2. Disable 2FA protection on the target account
3. Achieve full unauthorized access without multi-factor prompts

## Instructions

### Step 1: Setup Proxy Interception

**Context**: Configure a man-in-the-middle proxy to capture and modify traffic between the browser and the 8x8 API.

Use [[tools/Burp-Suite]] to intercept requests:

Install Burp Suite CA certificate in the browser to handle HTTPS. Set the browser proxy to point to Burp (default: 127.0.0.1:8080). Enable interception in Burp's Proxy tab.

> This setup allows viewing and editing requests/responses in real-time. Expected output: All web traffic routed through Burp without errors.

### Step 2: Trigger 2FA Disable Request

**Context**: Initiate the 2FA removal process with an incorrect password to generate a failing response that can be tampered.

Navigate to the account settings in the 8x8 application and attempt to disable 2FA. Enter an incorrect password and submit.

Intercept the outgoing POST request to the 2FA disable endpoint (e.g., POST /api/v1/2fa/disable with JSON payload including password hash).

> The request will include authentication tokens. Do not modify the request; forward it to the server. Expected output: Server responds with an error (e.g., 400 Bad Request or JSON {"success": false, "error": "Invalid password"}).

### Step 3: Tamper with Response

**Context**: Modify the intercepted response to simulate a successful 2FA disablement.

In Burp's Repeater or Proxy, edit the response body: Change {"success": false} to {"success": true}, remove error fields, and set status code to 200 if needed. Forward the tampered response to the client.

> This tricks the client-side application into believing the disable succeeded. Expected output: The UI updates to show 2FA as disabled, and backend state may not change due to the flaw, but client proceeds as if removed.

### Step 4: Verify Disablement

**Context**: Confirm the 2FA bypass by testing login without the second factor.

Log out and attempt to log in with the account credentials only. No 2FA prompt should appear.

> If successful, the account is now accessible without 2FA. Expected output: Direct login success, confirming takeover potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Modify Authentication Process]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- 2fa-bypass
- response-tampering
- business-logic
- auth-bypass
