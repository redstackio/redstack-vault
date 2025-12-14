---
tags:
  - idor
  - parameter-tampering
  - access-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
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
id: 351e2cf1-1103-4ced-bcc3-25f03c25e4f3
created_at: '2025-12-14T17:25:23.333Z'
updated_at: '2025-12-14T17:25:23.333Z'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Modify-Request-ID-for-IDOR-in-Veris

## Summary

This procedure involves editing the intercepted HTTP request in the Veris application to replace the authenticated user's terminal/gatekeeper ID with that of a target user, exploiting the IDOR vulnerability due to missing authorization checks.

## Description

Once the request is intercepted, the attacker uses the proxy tool's editor to alter the ID parameter, which directly references user-specific terminal objects. The Veris API fails to verify if the requesting user has permission to access the targeted ID, allowing arbitrary object access. This step targets the web-based API endpoint for terminal data retrieval. Prerequisites include the intercepted request from the prior step. Expected outcomes: A tampered request that, when sent, will fetch unauthorized data without server-side rejection.

## Requirements

1. Intercepted request from Veris terminal data endpoint
2. Knowledge of target user's ID (e.g., via enumeration or guesswork)
3. Proxy tool with request editing capabilities (e.g., Burp Repeater)

## Defense

Defensive measures and detection strategies:

- Enforce server-side access controls to validate user ownership of requested objects
- Use indirect object references (e.g., hashed IDs) instead of direct user IDs
- Log and monitor API requests for ID mismatches between user session and requested parameter

## Objectives

1. Tamper with the ID to target unauthorized terminal data
2. Preserve request integrity to avoid detection
3. Enable data retrieval for privilege escalation or information exposure

## Instructions

### Step 1: Drop Request to Editor

**Context**: Move the intercepted request to a tool for safe modification without forwarding prematurely.

**Instructions**: In Burp Suite's Proxy Intercept, click "Drop" if needed, then right-click the request and select "Send to Repeater". This opens the request in the Repeater tab for editing.

> Expected output: Request loaded in Repeater with original parameters visible.

### Step 2: Edit the ID Parameter

**Context**: Change the terminal/gatekeeper ID to the target's value to exploit the direct reference.

**Instructions**: Locate the ID parameter in the request (e.g., in query string: terminal_id=12345 or body JSON: {"gatekeeper_id": "abc123"}). Replace it with the target ID (e.g., terminal_id=67890). Do not alter authentication headers like cookies or tokens.

> As shown in proof-of-concept screenshots, this modification targets another user's data. Expected output: Updated request with new ID, ready for testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[parameter-tampering]]
- [[access-bypass]]
