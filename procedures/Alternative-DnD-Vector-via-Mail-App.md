---
id: proc-alt-dnd-mail-001
name: Alternative-DnD-Vector-via-Mail-App
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.760Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploitation for Client Execution]]'
tags:
  - dnd-vector
  - email-delivery
platforms:
  - macOS
  - Browser
tools:
  - '[[tools/Mail.app]]'
commands: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploitation for Client Execution]]'
---

# Alternative-DnD-Vector-via-Mail-App

## Summary

This alternative procedure delivers the malicious chrome://brave URL via Mail.app email, allowing direct DnD of the link to Brave without creating shortcut files, achieving the same origin bypass and exploit.

## Description

For scenarios where .webloc creation is restricted, sending the URL in an email enables DnD from Mail.app, which Chromium handles similarly, triggering navigation and MITM injection. This maintains user interaction but simplifies delivery. Expected outcome: Identical to primary DnD vector.

## Requirements

1. Mail.app configured on macOS
2. Active Brave session

## Defense

Defensive measures and detection strategies:

- Scan emails for suspicious URLs with mail filters
- Restrict DnD from apps to browser via UI policies

## Objectives

1. Deliver payload via email for DnD
2. Trigger same exploit without files

## Instructions

### Step 1: Send Malicious Link

**Context**: Compose email with URL.

In Mail.app: New message with body/link 'chrome://brave/etc/passwd'.

> Expected output: Email sent/received.

### Step 2: DnD from Mail

**Context**: Drag link to Brave tab.

Select and drag the URL from email to browser.

> Expected output: Navigation and exploit trigger.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mail.app]]

## Tags

- dnd-vector
- email-delivery
