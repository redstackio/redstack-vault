---
tags:
  - xss
  - gitlab
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:39.274Z'
sub_techniques: []
id: 247dd428-a45d-458a-9a70-a4fff162482e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-XSS-via-Error-Message-Interaction

## Summary

This procedure exploits the rendered error message by interacting with the UI, executing the injected JavaScript payload from the data-disable-with attribute.

## Description

The error message includes a transparent overlay link (via class attributes allowed by Dompurify) with data-disable-with containing <img src=x onerror=alert(document.domain)>. Rails-js processes this on link disable, firing the onerror when clicked, even with CSP as no inline script is used.

## Requirements

1. Error message displayed with malicious job name
2. Victim interaction (click anywhere in modal)
3. No additional tools; browser executes JS

## Defense

Defensive measures and detection strategies:

- Remove or escape data-disable-with in v-safe-html rules
- Audit Dompurify config for attribute whitelisting
- Detect JS alerts or anomalous API calls post-interaction

## Objectives

1. Execute arbitrary JS on victim browser
2. Demonstrate impact like alerts or form submissions
3. Escalate via API if form payload used

## Instructions

### Step 1: Interact with Error Modal

**Context**: Cause payload execution via UI event.

In the error dialog, click anywhere (e.g., on the text or overlay).

> Expected output: alert(document.domain) pops, confirming XSS.

### Step 2: Verify Escalation (Optional)

**Context**: If using form payload, submit to escalate privileges.

For admin-escalate job, interaction submits form to /api/v4/users/1 with _method=put and admin=true.

> Expected output: User role updated if victim is admin viewing the error.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- trigger
- javascript
