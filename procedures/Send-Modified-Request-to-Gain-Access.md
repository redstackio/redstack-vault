---
tags:
  - request-forward
  - account-takeover
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:48.269Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: b874dbce-b68c-4e0d-b3a3-02e70a5a1c29
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Send-Modified-Request-to-Gain-Access

## Summary

Forward the altered POST request to the Grammarly authentication endpoint to complete the login and gain unauthorized access to the victim's account.

## Description

After modifications in Burp Suite, release the request to the server. Due to the exploited trust mechanism and invalidation bypass, the server authenticates without a valid MFA code, establishing a session. Impact: Full account takeover if preconditions met; no users affected in original report due to high barriers.

## Requirements

1. Modified request ready in Burp
2. Valid timing and artifacts

## Defense

Defensive measures and detection strategies:

- Implement request signing or CSRF tokens bound to MFA state
- Audit logs for mode mismatches or disabled secure flags

## Objectives

1. Finalize bypass for session creation
2. Access protected account resources
3. Validate exploitation success

## Instructions

### Step 1: Forward Request

**Context**: Submit to server for processing.

In Burp Proxy or Repeater, click 'Forward' or 'Send'.

> Expected: 200 OK response with session tokens.

### Step 2: Verify Access

**Context**: Confirm unauthorized entry.

Follow redirect to dashboard; check account details.

> Expected: Full access without additional auth.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[request-forward]]
- [[account-takeover]]
