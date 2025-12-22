---
id: proc-modify-id-001
tags:
  - idor
  - request-tampering
  - authorization-bypass
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
updated_at: '2025-12-14T17:25:23.715Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Request-ID-for-IDOR

## Summary

This procedure alters the numeric ID in the intercepted POST request to target another user's settings, exploiting the lack of authorization validation in the Stocky app.

## Description

The endpoint /settings_for_low_stock_variants/{ID} uses a simple numeric ID without checking if the authenticated user owns that ID. Swapping from 111111 (User A) to 111112 (User B) allows cross-store modification, as the app assumes the requestor is authorized based on session alone.

## Requirements

1. Intercepted request in Burp Repeater
2. Knowledge of victim's ID (obtained via similar access or enumeration)

## Defense

Defensive measures and detection strategies:

- Implement ID ownership checks (e.g., compare user_id with resource owner)
- Log ID mismatches for anomaly detection

## Objectives

1. Identify vulnerable ID parameter
2. Replace with target ID
3. Preserve request integrity

## Instructions

### Step 1: Locate ID in Request

**Context**: Examine the URL path.

In Burp, view the request line: POST /settings_for_low_stock_variants/111111 HTTP/1.1

> Expected output: ID visible in path.

### Step 2: Swap ID

**Context**: Target victim's resource.

Edit path to /settings_for_low_stock_variants/111112, keep body unchanged.

> Expected output: Updated request ready for forwarding.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
