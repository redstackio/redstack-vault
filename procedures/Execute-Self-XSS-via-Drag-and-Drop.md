---
tags:
  - self-xss
  - social-engineering
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:32.157Z'
sub_techniques: []
id: 400fc563-baf3-4411-84e4-6f77d78b9f93
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute-Self-XSS-via-Drag-and-Drop

## Summary

This procedure uses social engineering to trick a victim into dragging a malicious file into Rocket.Chat's chat interface, exploiting the Self-XSS vulnerability to execute JavaScript and initiate session token theft.

## Description

The drag-and-drop functionality in Rocket.Chat fails to sanitize dropped content adequately, allowing HTML with JavaScript to run in the victim's authenticated browser context. The attacker delivers the payload via email or direct share, convincing the victim it's an image to upload. Upon drop, the script runs, exfiltrating the token without alerting the user. This requires no technical access but relies on victim interaction.

## Requirements

1. Victim access to Rocket.Chat chat
2. Malicious payload prepared and hosted (from prior procedure)
3. Social engineering channel (e.g., email, messaging) to deliver the file

## Defense

Defensive measures and detection strategies:

- Train users on verifying file types before uploading
- Enforce file type whitelisting and MIME-type checks on drag-and-drop
- Log and alert on JavaScript execution attempts in chat contexts

## Objectives

1. Trigger payload execution in victim's browser
2. Ensure token exfiltration without detection
3. Bridge to token retrieval phase

## Instructions

### Step 1: Deliver the Payload to Victim

**Context**: Convince the victim to download the disguised file.

No command; use social engineering: Send a message like "Check out this image from our chat - drag it in to share!" with the file attached.

> Victim downloads the file, believing it's an image.

### Step 2: Induce Drag-and-Drop

**Context**: Guide the victim to drop the file into the chat box.

No command; instruct via follow-up: "Just drag the image file directly into the chat window."

> Upon drop, the HTML executes, sending the token to the attacker's server.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- social-engineering
- drag-and-drop
