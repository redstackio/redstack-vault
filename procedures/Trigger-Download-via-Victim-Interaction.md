---
tags:
  - user-interaction
  - download-trigger
  - path-traversal
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:42.969Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 9cf8feac-5654-40d0-b861-f848581f7451
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Trigger-Download-via-Victim-Interaction

## Summary

This procedure relies on victim actions to open the shared note and click the attachment, exploiting the app's download handler to write the file via unsanitized path traversal.

## Description

The victim receives the deeplink and invitation. Opening the link (first click) loads the note in the Evernote app. Clicking the attachment (second click) initiates download, where the React Native code parses the Content-Disposition header (`attachment; filename="../../../lib-1/libjnigraphics.so"`) without sanitization, resulting in overwrite at `/data/data/com.evernote/lib-1/libjnigraphics.so`.

## Requirements

1. Victim with Evernote app installed
2. Sent deeplink and invitation
3. Vulnerable app version (pre-sanitization patch)

## Defense

Defensive measures and detection strategies:

- Sanitize header filenames in download logic (e.g., strip traversal in Hermes bytecode)
- Prompt users before downloading attachments from shared notes
- Monitor app logs for anomalous file writes to lib directories

## Objectives

1. Achieve two-click execution without auth bypass
2. Overwrite native library in app data
3. Avoid detection during download phase

## Instructions

### Step 1: Distribute Link to Victim

**Context**: Socially engineer the victim to engage with the link.

Send the deeplink via email: "Check out this important note: [link]".

### Step 2: Victim Performs Clicks

**Context**: Guide or observe victim actions to trigger download.

Victim opens link to access note, then clicks attachment to download.

> Download writes to traversal path; no visible errors if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- victim-interaction
- download-exploit
- android
