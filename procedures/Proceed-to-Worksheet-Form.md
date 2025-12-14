---
id: proc-proceed-worksheet-form
tags:
  - web
  - form-access
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
updated_at: '2025-12-14T17:33:06.194Z'
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
# Proceed-to-Worksheet-Form

## Summary

Advances the user to the full worksheet input form, exposing text fields for potential XSS injection.

## Description

Clicking continue loads the detailed form with multiple input areas. This step bridges navigation to exploitation, confirming form accessibility in the DoD app.

## Requirements

1. Worksheet creation page loaded
2. Preliminary data ready if needed

## Defense

- Require CAPTCHA on form load
- Track form access frequency

## Objectives

1. Load editable form
2. Access text fields
3. Prepare for input testing

## Instructions

### Step 1: Initiate Form Load

**Context**: Proceed past introductory screens.

```plaintext
Click `Continue`
```

> Form appears. Expected: Text areas visible.

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
- [[form-access]]
