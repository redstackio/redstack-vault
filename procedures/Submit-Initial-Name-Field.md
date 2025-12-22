---
id: proc-submit-initial-name
tags:
  - web
  - form-submission
type: procedure
tools: []
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
updated_at: '2025-12-14T17:33:06.189Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Initial-Name-Field

## Summary

Tests and submits the initial name field, which sanitizes basic XSS, to unlock subsequent vulnerable fields.

## Description

Enter name and submit; payloads like <script>alert(1)</script> are blocked here but allow form progression.

## Requirements

1. Form loaded
2. Valid name input

## Defense

- Consistent sanitization across all fields
- Input validation logging

## Objectives

1. Pass initial check
2. Access advanced fields
3. Confirm partial protections

## Instructions

### Step 1: Input and Submit

**Context**: Fill and send initial data.

```plaintext
Fill in your name and click `Submit`
```

> Advances form. Expected: No execution, progression granted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web]]
- [[form-submission]]
