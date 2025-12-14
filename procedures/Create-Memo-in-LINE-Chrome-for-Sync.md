---
id: 69cebee7-1a89-41e7-90c2-e2466e287913
name: Create-Memo-in-LINE-Chrome-for-Sync
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:21.769Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Supply Chain Compromise]]'
tags:
  - line-app
  - chrome
  - memo-sync
platforms:
  - Web
tools:
  - '[[tools/PoC-Android-Application]]'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Supply Chain Compromise]]'
---

# Create-Memo-in-LINE-Chrome-for-Sync

## Summary

This procedure creates a new memo in the LINE for Chrome extension, which syncs as a ZIP file to the LINE Keep service, setting up a target for later replacement in the Android app.

## Description

In the attack scenario, the attacker uses LINE for Chrome to generate a syncable file that appears in the Android app's Keep section. This memo is stored as a ZIP file containing the note content. The procedure requires access to a LINE account via the Chrome extension and relies on the sync feature between web and mobile. Expected outcome is a ZIP file ready for interception on the Android side, enabling the path traversal exploit.

## Requirements

1. LINE account with Chrome extension installed
2. Internet access for syncing to LINE Keep service
3. Target Android device with LINE app logged into the same account

## Defense

Defensive measures and detection strategies:

- Monitor unusual memo creations in LINE logs
- Disable cross-device syncing if not needed
- Use app sandboxing to limit sync impacts

## Objectives

1. Generate a syncable ZIP file via memo creation
2. Ensure the file appears in Android LINE Keep
3. Prepare for malicious replacement without alerting the user

## Instructions

### Step 1: Open LINE for Chrome

**Context**: Launch the LINE extension to access the Keep service.

No specific command; use the browser interface to open LINE for Chrome.

> Navigate to the Keep section.

### Step 2: Create New Memo

**Context**: Add content to create a ZIP-syncable file.

No command; in the UI, select 'New Memo', add text (e.g., "Test note"), and save.

> The memo syncs automatically as a ZIP to LINE Keep.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Supply Chain Compromise]] Supply Chain Compromise

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/PoC-Android-Application]]

## Tags

- [[line-app]]
- [[chrome]]
- [[memo-sync]]
