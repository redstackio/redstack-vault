---
tags:
  - idor
  - data-exfiltration
  - unauthorized-access
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: e415d11b-6351-45c2-ba6a-93c9d8db0918
created_at: '2025-12-14T17:25:23.331Z'
updated_at: '2025-12-14T17:25:23.331Z'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Retrieve-Unauthorized-Terminal-Data-via-IDOR-in-Veris

## Summary

This procedure submits the modified HTTP request to the Veris API, resulting in the server returning the target user's sensitive terminal data due to the absence of permission checks on the ID parameter.

## Description

With the ID altered, the request is forwarded to the Veris server, which processes it as legitimate because it lacks validation tying the ID to the authenticated user. This exposes terminal data, potentially including configurations, sessions, or other confidential info. The attack occurs over standard web traffic to the terminal data endpoint. Prerequisites: Modified request from the previous step. Expected outcomes: Successful response with unauthorized data, confirming the IDOR impact.

## Requirements

1. Modified HTTP request with target ID
2. Active proxy session connected to Veris
3. Target user's ID confirmed

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) and verify permissions on every API call
- Rate-limit requests and audit logs for unusual data access patterns
- Use session-bound indirect references to prevent ID guessing or manipulation

## Objectives

1. Obtain the target user's terminal data remotely
2. Validate the IDOR vulnerability exploitation
3. Collect sensitive information for further attacks

## Instructions

### Step 1: Send the Modified Request

**Context**: Transmit the tampered request to the server for processing.

**Instructions**: In Burp Suite's Repeater tab, click "Send" to forward the modified request to the Veris API.

> The server will respond without checking ownership. Expected output: HTTP 200 response with terminal data payload.

### Step 2: Analyze the Response

**Context**: Inspect the returned data to confirm unauthorized access.

**Instructions**: View the response in the Repeater tab, checking for terminal details like IDs, configs, or user-specific info. Compare against known own data to verify it's from the target.

> As demonstrated in proof-of-concept screenshots, the response contains the target user's data. Expected output: JSON or HTML with sensitive terminal information, no auth errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[data-exfiltration]]
- [[unauthorized-access]]
