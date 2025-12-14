---
id: proc-uuid-3
tags:
  - privilege-escalation
  - response-manipulation
  - bypass
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
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:18.042Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Modify-Response-to-Bypass-Status-Check

## Summary

This procedure modifies the intercepted API response from the temp password request to flip the status to true, tricking the client-side Angular app into allowing access to the reset flow.

## Description

Client-side controls in the UPS site check the 'status' field in the JSON response; no server-side enforcement exists for UI rendering. By altering the response in Burp, the JS proceeds as if the user exists, exposing the /resetPassword endpoint. This leads to admin access without tokens.

## Requirements

1. Intercepted response from previous step
2. Burp Suite Repeater or Inspector
3. Knowledge of JSON structure

## Defense

Defensive measures and detection strategies:

- Add server-side tokens/CSRF for all sensitive UI loads
- Detect proxy tampering via response integrity checks (e.g., signatures)

## Objectives

1. Bypass client-side validation
2. Enable unauthorized UI progression
3. Maintain attack chain without alerting

## Instructions

### Step 1: Edit Response in Burp

**Context**: Locate the JSON body in the intercepted response and change status.

No command; in Burp, edit body to: {"status":true,"errorMessage":"Username does not exist. Please enter correct Username."}

> Preserve headers like Cache-Control: no-cache, Content-Type: application/json.

### Step 2: Forward Modified Response

**Context**: Release the altered response to the client.

Click 'Forward' in Burp Proxy.

> Client receives modified response; JS checks pass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[privilege-escalation]]
- [[response-manipulation]]
- [[bypass]]
