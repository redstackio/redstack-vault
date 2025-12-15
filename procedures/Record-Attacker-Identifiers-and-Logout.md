---
tags:
  - idor
  - web
  - identifier-extraction
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: e12c4796-4264-4956-bcfc-fba45e711882
created_at: '2025-12-14T17:25:47.557Z'
updated_at: '2025-12-14T17:25:47.557Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Record-Attacker-Identifiers-and-Logout

## Summary

This procedure extracts the attacker's user 'id' and 'email' from the captured request payload and logs out the session to switch to victim testing.

## Description

From the intercepted POST /app/updateUser JSON in Burp Suite, note the values for 'id' (e.g., '/###') and 'email' (e.g., 'redacted+attacker@wearehackerone.com'). This data is used for comparison in exploitation. Logging out ensures clean session management. Expected outcomes include documented identifiers ready for modification steps.

## Requirements

1. Captured request from previous step in [[tools/Burp-Suite]]
2. Access to attacker session

## Defense

Defensive measures and detection strategies:

- Obfuscate user IDs (e.g., use UUIDs instead of predictable paths)
- Log session logout events for anomaly detection
- Rotate session tokens on logout

## Objectives

1. Securely record attacker-specific identifiers
2. Maintain session hygiene by logging out
3. Prepare for victim account handling

## Instructions

### Step 1: Extract Identifiers from Payload

**Context**: Review the JSON in the captured request.

No specific command; manual inspection.

> In Burp, inspect the POST body and copy 'id' and 'email' values to a secure note. Expected output: Identifiers like 'id': '/###', 'email': 'redacted+attacker@wearehackerone.com' documented.

### Step 2: Logout from Attacker Session

**Context**: End the current session.

No specific command; use app UI.

> Click logout in the application interface. Expected output: Redirect to login page, session terminated.

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
- [[web]]
- [[identifier-extraction]]
