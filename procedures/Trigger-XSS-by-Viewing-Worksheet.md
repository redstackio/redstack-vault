---
id: proc-trigger-xss-viewing
tags:
  - xss
  - execution
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
updated_at: '2025-12-14T17:33:06.167Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Viewing-Worksheet

## Summary

Triggers the stored XSS by viewing or modifying the worksheet, executing payloads in the victim's browser.

## Description

Authorized users render fields, firing JS. Occurs on view or edit pages.

## Requirements

1. Ticket number from submission
2. Access as viewer (authorized personnel)

## Defense

- Sanitize on render
- JS execution monitoring

## Objectives

1. Execute payload
2. Confirm in victim context
3. Observe effects

## Instructions

### Step 1: Access Worksheet

**Context**: Use ticket to view.

```plaintext
Click `██████`, or return to `███████` page and enter info in `█████` area
```

> JS runs. Expected: Payload effects visible.

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
- [[Execution]]
