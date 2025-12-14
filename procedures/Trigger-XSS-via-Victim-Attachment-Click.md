---
id: proc-765679-xss-trigger
tags:
  - xss-execution
  - cookie-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Keylogging]]'
updated_at: '2025-12-13T23:52:49.703Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Keylogging]]'
---
# Trigger-XSS-via-Victim-Attachment-Click

## Summary

This procedure simulates the victim logging in and clicking attachments to execute the stored XSS payload, resulting in JavaScript execution and cookie theft.

## Description

As the victim, access the Inbox, view the conversation, and click attachments, which open in a new tab and trigger the onload event in the SVG. This executes arbitrary JavaScript in the victim's browser context, capturing session cookies for potential account takeover.

## Requirements

1. Victim account with received conversation
2. Authenticated victim session
3. Browser supporting SVG rendering

## Defense

Defensive measures and detection strategies:

- Render attachments in isolated iframes or sandboxes
- Block JavaScript in user-uploaded files
- Monitor for anomalous alerts or cookie access

## Objectives

1. Execute stored payload
2. Steal session cookies
3. Demonstrate account compromise potential

## Instructions

### Step 1: Victim Authentication

**Context**: Log in as the victim to access Inbox.

Navigate to https://app.outpost.co/sign-in, enter seq1@seq1.teamoutpost.com and password.

> Dashboard loads; session established.

### Step 2: Access and Click Attachments

**Context**: Interact with the malicious files.

Open Inbox, locate the conversation, click each attachment (Payload.png, etc.).

> New tab opens; onload triggers alert(document.cookie).

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Keylogging]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]
- [[cookie-theft]]
