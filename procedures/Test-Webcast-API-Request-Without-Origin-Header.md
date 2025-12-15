---
tags:
  - csrf
  - bypass
  - test
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-without-origin]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.601Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 2948f891-ff8b-4757-9f52-b1def2ea663c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test Webcast API Request Without Origin Header

## Summary

This procedure tests the TikTok Webcast API by sending requests without the Origin header to confirm if they are accepted, revealing the CSRF bypass vulnerability.

## Description

The test simulates a cross-origin request lacking the Origin header, which the API processes without rejection due to incomplete CSRF validation. This step is crucial for verifying the flaw in an authenticated session, potentially allowing forged requests from malicious sites.

## Requirements

1. Valid authenticated session cookie for TikTok
2. Knowledge of target Webcast endpoint
3. HTTP client tool like curl

## Defense

Defensive measures and detection strategies:

- Enforce rejection of requests missing Origin header
- Log and alert on API calls without standard headers
- Implement same-site cookie policies

## Objectives

1. Verify acceptance of headerless requests
2. Confirm CSRF protection gap
3. Document bypass behavior

## Instructions

### Step 1: Prepare Authenticated Request

**Context**: Ensure session is active and endpoint is identified.

No command; validate session manually.

### Step 2: Send Request Omitting Origin

**Context**: Execute the test request to check for bypass.

**Command** ([[commands/curl-test-without-origin]]):
```bash
curl -X POST https://api.tiktok.com/webcast/endpoint \
  -H "Cookie: session=valid_session" \
  -d "data=test_payload"
```

> Omits Origin by default in curl; expects successful response without CSRF block.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-without-origin]]

## Tools Used

- [[curl]]

## Tags

- [[csrf]]
- [[bypass]]
- [[api]]
