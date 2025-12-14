---
id: p-save-changes-location-dialog
tags:
  - persistence
  - concrete-cms
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
updated_at: '2025-12-14T03:16:20.629Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Changes-in-Location-Dialog

## Summary

This procedure saves the modified Location dialog in Concrete CMS, persisting the injected XSS payload in the page's location attributes for later execution by other users.

## Description

After injecting the payload, confirming and saving the dialog stores the malicious input server-side without sanitization, ensuring it is retrieved and rendered in JavaScript when the dialog is reopened, enabling the stored XSS attack.

## Requirements

1. Location dialog open with payload entered.
2. Valid edit permissions on the page.
3. No server-side validation blocking saves.

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation and escaping before database storage.
- Audit page attribute changes for suspicious content.

## Objectives

1. Commit the payload to persistent storage.
2. Ensure no immediate execution or errors.
3. Prepare for victim interaction.

## Instructions

### Step 1: Review and Confirm Changes

**Context**: Verify the payload is in place before saving.

Inspect the Additional URLs field to confirm the injected string.

> The dialog shows the unsanitized input.

### Step 2: Execute Save Operation

**Context**: Submit the changes to store the payload.

Click the 'Save' or 'OK' button in the dialog.

> Dialog closes with a success confirmation; payload is now stored in the backend.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- persistence
- concrete-cms
