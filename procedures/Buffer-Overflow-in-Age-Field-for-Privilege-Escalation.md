---
id: proc-uuid-10
tags:
  - buffer-overflow
  - privilege-escalation
type: procedure
tools:
  - '[[tools/Browser-Dev-Tools]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:55.508Z'
skill_level: advanced
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Buffer-Overflow-in-Age-Field-for-Privilege-Escalation

## Summary

This procedure exploits a buffer overflow in the age field of the signup manager by using scientific notation to bypass length checks, overflowing into the admin flag for privilege escalation and flag access.

## Description

Age is checked as string length <3 before int parse; 1e3 is valid int 1000 but >3 chars, shifting lastname buffer (15 Y's) to overwrite admin=Y. Targets vulnerable PHP forms.

## Requirements

1. Form submission access
2. Browser or POST tool
3. Understanding of buffer parsing

## Defense

Defensive measures and detection strategies:

- Validate inputs server-side strictly
- Use safe parsing without overflows
- Bound buffer sizes

## Objectives

1. Bypass length validation
2. Overflow admin flag
3. Access admin.php flag

## Instructions

### Step 1: Craft Overflow Payload

**Context**: Prepare fields to trigger shift.

Set age=1e3, lastname=YYYYYYYYYYYYYYY.

> Submits to /signup-manager; overflow sets admin=Y.

### Step 2: Access Admin

**Context**: Redirect to admin.php.

Visit admin.php post-submission.

> Flag displayed.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Browser-Dev-Tools]]

## Tags

- [[buffer-overflow]]
- [[privilege-escalation]]
