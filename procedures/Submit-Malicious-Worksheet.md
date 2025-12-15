---
id: proc-submit-malicious-worksheet
tags:
  - xss
  - persistence
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:33:06.179Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit-Malicious-Worksheet

## Summary

Submits the form with injected XSS payloads, storing them in the backend for later execution.

## Description

Final submission persists data; app issues ticket. Enables stored aspect of XSS.

## Requirements

1. All fields populated with payloads
2. Form validation passed

## Defense

- Server-side payload scanning on submit
- Quarantine suspicious submissions

## Objectives

1. Store malicious data
2. Obtain ticket for tracking
3. Confirm persistence

## Instructions

### Step 1: Finalize and Send

**Context**: Complete submission.

```plaintext
Click `Finish`
```

> Confirmation shown. Expected: Ticket number received.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Persistence]]
