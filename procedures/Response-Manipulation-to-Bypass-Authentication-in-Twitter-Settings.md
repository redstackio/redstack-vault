---
id: proc-001
tags:
  - auth-bypass
  - response-manipulation
  - account-takeover
  - twitter
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:31:52.954Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
---
# Response-Manipulation-to-Bypass-Authentication-in-Twitter-Settings

## Summary

This procedure exploits a client-side trust issue in Twitter's authentication flows for updating email or phone numbers, allowing an attacker with a hijacked session to intercept and modify server responses, faking successful password validation and bypassing the prompt to change contacts, ultimately enabling account takeover.

## Description

In Twitter's web application, updating email or phone in Settings and Privacy -> Accounts requires password confirmation. Submitting invalid credentials sends a request with a flow token; the server responds with failure. By intercepting this via a proxy like Burp Suite, copying the flow token, and replacing the response with a crafted success JSON (including the token and flow-specific subtasks), the client proceeds as if authenticated. This works due to lack of additional server-side validation on subsequent requests. Applicable to both email (subtasks for email verification) and phone (subtasks including country codes). Prerequisites include a valid session cookie and proxy setup. Expected outcome: Updated contacts without password, allowing reset to attacker control.

## Requirements

1. Hijacked Twitter session (valid cookies in browser).
2. Web proxy tool like Burp Suite configured to intercept browser traffic.
3. Access to Twitter web app via proxied browser.
4. Knowledge of JSON structure for Twitter's flow responses.

## Defense

Defensive measures and detection strategies:

- Implement client-side fingerprinting or additional tokens to detect proxy tampering.
- Add server-side re-validation of password on contact update submission, not just response trust.
- Monitor for anomalous session behavior, like rapid contact changes without prior auth.
- Use certificate pinning to prevent easy proxy interception.

## Objectives

1. Bypass password prompt in contact update flows.
2. Update email/phone to attacker-controlled values.
3. Facilitate account takeover via password reset using new contacts.
4. Maintain persistence in the hijacked account.

## Instructions

### Step 1: Setup Proxy and Navigate to Vulnerable Flow

**Context**: Route traffic through a proxy and access the update interface to trigger the auth request.

**Instructions**: Configure browser to use Burp Suite as proxy. Log in with hijacked session, go to Settings and Privacy -> Accounts, then select Email or Phone update. This loads the password prompt.

> No specific command; manual browser navigation. Ensure proxy captures HTTPS traffic (install Burp CA certificate).

### Step 2: Submit Invalid Credentials to Generate Flow Token

**Context**: Trigger the server request to obtain a unique flow token.

**Instructions**: Enter a random password and click 'Next'. Intercept the outgoing request in the proxy.

> Request will include the flow token in headers or body (e.g., Authorization: Bearer <token> or flow_token param).

### Step 3: Extract Flow Token and Forward Request

**Context**: Capture the token needed for the fake response while allowing the real request to proceed for response structure.

**Instructions**: Copy the flow token from the intercepted request (e.g., up to the colon in 'flow_token:xyz'). Forward the request to the server.

> Token is session-specific; do not modify request.

### Step 4: Intercept and Analyze Server Response

**Context**: Examine the failure response to replicate its structure for the fake success.

**Instructions**: Intercept the returning server response (typically JSON with 'status': 'error' or similar).

> Note the overall JSON keys like 'flow_token', 'subtasks' for replication.

### Step 5: Craft and Send Modified Success Response

**Context**: Replace the response to simulate successful auth, varying subtasks for email (verification steps) or phone (country codes + verification).

**Instructions**: In the proxy, edit the response to HTTP 200 OK with JSON body: {
  "flow_token": "<pasted_token>",
  "status": "success",
  "subtasks": [
    // For email: {"subtask_id": "update_email", "element": "choice", ...}
    // For phone: {"subtask_id": "update_phone", "element": "choice", "country_codes": [...]}
  ]
}. Forward to client.

> Use Burp's Repeater or manual edit; ensure JSON is valid to avoid client errors.

### Step 6: Complete Update and Verify

**Context**: Exploit the bypassed state to add new contact and confirm.

**Instructions**: The client will now show the update form; enter new email/phone and verify via code sent to it.

> Success: New contact added; test by attempting password reset to confirm takeover path.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Persistence]] Persistence

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- auth-bypass
- response-manipulation
- twitter
- web
