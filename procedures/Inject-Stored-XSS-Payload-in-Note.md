---
id: proc-inject-xss-payload-001
tags:
  - xss
  - injection
  - stored-xss
type: procedure
tools:
  - '[[tools/Simplenote-Desktop-App]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/confirm-xss-dialog]]'
verified: false
platforms:
  - Desktop
  - Electron
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:28.409Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-Note

## Summary

This procedure injects a stored XSS payload into a Simplenote note, leveraging insufficient sanitization to embed HTML/JavaScript that persists and executes on print.

## Description

In Simplenote 1.1.3, note content is stored and rendered during print without full sanitization, allowing tags like <details> to trigger JS on events like ontoggle. The payload is crafted to inject via closing tags (e.g., ">) and executes in the Electron context when File > Print is selected, confirming XSS before RCE escalation.

## Requirements

1. Installed Simplenote 1.1.3 with Markdown disabled
2. Access to create notes
3. Basic knowledge of HTML/JS payloads

## Defense

Defensive measures and detection strategies:

- Sanitize user input in note rendering
- Disable print preview for untrusted notes
- Log anomalous JS execution in Electron apps

## Objectives

1. Embed executable JS in note content
2. Ensure payload survives storage
3. Prepare for trigger during print

## Instructions

### Step 1: Create New Note

**Context**: Start a fresh note to avoid interference.

Launch Simplenote and select 'New Note'.

> Empty note editor opens.

### Step 2: Input XSS Payload

**Context**: Inject the basic payload to test stored XSS.

**Command** ([[commands/confirm-xss-dialog]]):
Enter the following in the note: `1"><details open ontoggle=confirm('XSS')>`

> Note saves with injected HTML; no immediate execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/confirm-xss-dialog]]

## Tools Used

- [[tools/Simplenote-Desktop-App]]

## Tags

- xss
- injection
