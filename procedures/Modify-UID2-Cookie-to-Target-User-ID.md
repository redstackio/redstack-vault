---
id: p3c4d5e6-f7g8-9012-cdef-3456789012
tags:
  - cookie-tampering
  - modification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Use Alternate Authentication Material]]'
updated_at: '2025-12-14T17:25:23.668Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Application Access Token]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Use Alternate Authentication Material]]'
---
# Modify-UID2-Cookie-to-Target-User-ID

## Summary

This procedure alters the UID2 cookie value in an intercepted request to reference a different user's ID, enabling the IDOR exploitation.

## Description

The UID2 cookie directly maps to a user ID without server-side validation. Changing it from the attacker's ID (4820038) to a target's (4820036) bypasses access controls in the PHP profile endpoint, as the app trusts the cookie without ownership checks.

## Requirements

1. Intercepted profile request from prior step
2. Known target user ID (e.g., via enumeration or sequential guessing)
3. Proxy tool for request editing

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization checks comparing session user ID to requested ID
- Sign or encrypt cookies to prevent tampering
- Detect rapid ID changes in logs

## Objectives

1. Edit the cookie value accurately
2. Preserve request integrity
3. Prepare for replay

## Instructions

### Step 1: Pause Intercepted Request

**Context**: Halt the request for modification.

In Burp Proxy, intercept the profile request and drop it to edit.

> Expected output: Request editable in Repeater or Inspector tab.

### Step 2: Edit UID2 Value

**Context**: Replace the ID to target another user.

Locate the Cookie header, change UID2=4820038 to UID2=4820036.

> Expected output: Updated header: Cookie: UID2=4820036; other cookies intact.

### Step 3: Validate Modification

**Context**: Ensure no syntax issues.

Review the full request for correctness before forwarding.

> Expected output: No parsing errors in Burp validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Use Alternate Authentication Material]]

### Sub-Techniques

- [[Application Access Token]]

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[cookie-tampering]]
