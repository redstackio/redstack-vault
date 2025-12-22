---
tags:
  - information-disclosure
  - api-leak
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:25:18.051Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: a4192875-6ad7-4f6e-a548-df42ab29f968
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Extract-2FA-Secret-from-API-Response

## Summary

This procedure replays an intercepted API request in a proxy tool to capture and parse the response, extracting the leaked Google Authenticator 2FA secret (gauth_secret) for further exploitation.

## Description

Targeting the Algolia support renewal endpoint, the attacker uses Burp Suite's Repeater to send the request and examine the JSON response body, where the application erroneously includes the TOTP secret without redaction. This disclosure occurs due to improper API response handling. Prerequisites: Intercepted request from prior steps and Burp Suite. Outcomes: Copied secret value ready for TOTP import, enabling 2FA bypass.

## Requirements

1. Intercepted Renew request in Burp Suite
2. Knowledge of JSON structure in responses
3. Text editor or clipboard for copying the secret

## Defense

Defensive measures and detection strategies:

- Redact sensitive fields like 2FA secrets from API responses using server-side filtering
- Implement rate limiting on support endpoints and log all renew actions for anomaly detection
- Use response encryption or tokenization for secrets, ensuring they are never transmitted in plain text

## Objectives

1. Replay the request to obtain the full API response
2. Identify and extract the gauth_secret value
3. Validate the secret's format for TOTP compatibility

## Instructions

### Step 1: Send to Repeater

**Context**: Move the intercepted request to a module for controlled replay.

No specific command; in Burp Suite Proxy, right-click the intercepted Renew request and select 'Send to Repeater'.

> Repeater tab opens with the request loaded, ready for modification if needed.

### Step 2: Replay the Request

**Context**: Execute the request to fetch the server response.

No specific command; Click 'Send' in Repeater to forward the request.

> Response appears in the lower pane, typically a 200 OK JSON body.

### Step 3: Inspect and Extract Secret

**Context**: Parse the response for the vulnerable field.

No specific command; Scroll through the JSON response body to locate the key 'gauth_secret' and copy its value (e.g., a 16-32 character base32 string).

> Extracted value should look like 'JBSWY3DPEHPK3PXP'. Verify by checking if it's a valid TOTP secret format.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unprotected Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- information-disclosure
- api-leak
