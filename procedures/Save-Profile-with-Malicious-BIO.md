---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - xss
  - storage
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
created_at: '2024-10-04T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:20.351Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Profile-with-Malicious-BIO

## Summary

This procedure persists the injected XSS payload by submitting the profile form, storing the malicious BIO content on the server without immediate execution.

## Description

Following payload injection, this step submits the profile edit form to store the unsanitized BIO data. The Khan Academy backend fails to properly escape the input, allowing the payload to remain dormant until re-rendered. This occurs in the web-based profile management system, with outcomes including successful save and no visible anomalies.

## Requirements

1. Payload already entered in BIO field
2. Active editing session
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Server-side escaping of stored user inputs using HTML entity encoding
- Validation of form submissions for script patterns
- Logging of profile changes for anomaly detection

## Objectives

1. Store the payload server-side
2. Confirm no immediate trigger
3. Maintain session integrity for next steps

## Instructions

### Step 1: Submit the Form

**Context**: Finalize the injection by saving the profile to persist the payload.

With the malicious payload in the BIO field, click the SAVE button on the profile editing page.

> Observe the page reload or confirmation message; no alert should appear, indicating the payload is stored but not yet executed.

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
- [[storage]]
