---
id: 5dfef108-407e-4556-8e5b-f577c95715d9
name: Create Ticket and Trigger Stored XSS
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:15.464Z'
updated_at: '2025-12-11T06:10:15.464Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - execution
commands:
  - '[[commands/git-clone-trac-repo]]'
platforms:
  - Web
tools:
  - '[[tools/Git]]'
  - '[[tools/Web-Browser]]'
skill_level: beginner
impact_level: medium
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---

# Create Ticket and Trigger Stored XSS

## Summary

This procedure covers submitting the ticket with the injected payload to store and immediately trigger the XSS vulnerability in the current session.

## Description

Upon submission, the unescaped payload generates a malicious delete button, executing the JavaScript alert. This confirms the stored XSS, potentially allowing cookie theft in real scenarios.

## Requirements

1. Completed ticket form with injected payload
2. Web browser

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs before rendering
- Log and alert on suspicious ticket creations

## Objectives

1. Store the payload in the ticket
2. Trigger initial execution
3. Confirm vulnerability

## Instructions

### Step 1: Submit the Ticket

**Context**: Finalize and create the ticket to store the payload.

Using [[tools/Web-Browser]], click the enter button and then the Create Ticket button, resulting in an XSS alert being triggered.

> Expected: Ticket created and alert pops up with document.domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[xss]]
- [[Execution]]
