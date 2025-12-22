---
id: proc-uuid-004
tags:
  - submission
  - trigger
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
updated_at: '2025-12-14T03:16:36.854Z'
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
# Submit-Worksheet-and-Trigger-Stored-XSS

## Summary

This procedure covers submitting the payload-laden worksheet to store the XSS and then triggering execution by viewing it, simulating victim interaction in the DoD application.

## Description

Submission stores the unsanitized inputs server-side. Triggering involves accessing the worksheet via ticket or modification view, causing the browser to render and execute the JavaScript in the viewer's context. This exploits the stored nature for persistent attacks on legal personnel. Prerequisites: Submitted form; outcomes: Payload execution and potential data exfil.

## Requirements

1. Completed form with payloads
2. Ticket number from submission
3. Victim-like session (authenticated viewer role)

## Defense

Defensive measures and detection strategies:

- Scan stored content for malicious patterns before rendering
- Use sandboxed iframes or no-script modes for user-generated content
- Alert on anomalous views of worksheets (e.g., from unexpected IPs)

## Objectives

1. Successfully store payloads via submission
2. Trigger execution in a victim context
3. Confirm persistence across views

## Instructions

### Step 1: Finalize and Submit

**Context**: Commit the worksheet.

Click "Finish."

> Stores data. Expected output: Confirmation and ticket.

### Step 2: Access for Trigger

**Context**: Simulate victim view.

Click ███████ or search by ticket in ████████ page.

> Renders fields. Expected output: JS executes (e.g., form appears).

### Step 3: Verify Trigger

**Context**: Check multiple access points.

Modify via █████ area.

> Consistent execution. Expected output: Payload fires again.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[trigger]]
- [[stored]]
