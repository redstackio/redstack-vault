---
id: proc-uuid-4
tags:
  - xss
  - trigger
  - slack
  - zendesk
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
updated_at: '2025-12-14T03:16:14.586Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# View Submitted Ticket to Trigger XSS

## Summary

This procedure views the created help ticket, causing the profile name to be rendered without proper encoding, executing the stored XSS payload as self-XSS.

## Description

In the Zendesk-integrated ticket view, the user's name is displayed unsanitized, leading to JavaScript execution in the viewer's browser. Impact limited to self-XSS (attacker's session only). Requires prior ticket creation. Expected outcome: Prompt or arbitrary JS execution.

## Requirements

1. Existing ticket from previous step.
2. Access to ticket view page.
3. Browser session with JS enabled.

## Defense

Defensive measures and detection strategies:

- Apply output encoding (e.g., HTML entity escaping) to all user inputs in views.
- Use strict CSP to block unsafe scripts.
- Monitor for JS errors or unexpected prompts in logs.

## Objectives

1. Load the ticket view page.
2. Trigger and observe XSS execution.
3. Confirm self-XSS nature (no cross-user impact).

## Instructions

### Step 1: Access Ticket View

**Context**: Navigate to the specific ticket page.

No command; direct URL or UI:

- Go to: `https://yourworkspace.slack.com/help/requests/[ticket-id]`.
- Or click from help requests list.

> Page renders; name displayed, triggering onerror in img tag.

### Step 2: Observe Execution

**Context**: Verify the payload fires.

- Watch for prompt(12) dialog.
- Inspect console for JS errors if needed.

> Expected: Alert box with "12"; confirms XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-trigger
- ticket-view
- self-xss
