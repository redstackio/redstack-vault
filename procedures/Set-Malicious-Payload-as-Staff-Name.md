---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - xss
  - payload-injection
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.424Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Set-Malicious-Payload-as-Staff-Name

## Summary

This procedure involves setting a staff member's display name to a stored XSS payload, exploiting lack of sanitization for later execution in activity logs.

## Description

Shopify renders staff names in HTML without proper encoding in activity entries. Using a payload like 'hunter'><svg/onload=alert(2)>', the attacker closes an HTML tag and injects script. This stores the payload persistently, triggering on admin view. Prerequisites: staff account access; outcomes: payload ready for execution.

## Requirements

1. Access to the staff member's profile.
2. Knowledge of XSS payloads.
3. Store admin privileges for editing.

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs in HTML contexts.
- Content Security Policy (CSP) to block inline scripts.
- Monitor for suspicious name characters like < >.

## Objectives

1. Inject cross-site scripting payload via name field.
2. Ensure persistence in database.
3. Set up for admin-context execution.

## Instructions

### Step 1: Edit Staff Profile

**Context**: Locate and modify the staff member's details.

No specific command; navigate to Users and permissions > Edit staff.

> Find the display name field.

### Step 2: Insert Payload and Save

**Context**: Enter the malicious string to exploit rendering flaws.

No specific command; set name to `hunter'><svg/onload=alert(2)>` and save.

> Verify update without errors; payload is now stored.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- stored-xss
- payload
