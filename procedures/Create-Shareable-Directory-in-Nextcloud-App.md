---
id: uuid-proc-2
tags:
  - nextcloud
  - sharing
  - android
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:24:41.979Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Create Shareable Directory in Nextcloud App

## Summary

This procedure creates a folder within the Nextcloud Android app and configures it for public sharing, enabling leaked files to be accessible externally.

## Description

Public sharing in Nextcloud allows files to be exposed via links. This step prepares the landing zone for exploited uploads, targeting the app's sharing UI.

## Requirements

1. Authenticated Nextcloud app session
2. Write permissions on the target folder
3. Internet connectivity for share link generation

## Defense

Defensive measures and detection strategies:

- Disable public sharing in Nextcloud server config
- Monitor for unusual folder creations via audit logs
- Alert on public link generations

## Objectives

1. Establish a public vector for data exfiltration
2. Verify sharing permissions
3. Set up for file upload reception

## Instructions

### Step 1: Navigate and Create Folder

**Context**: Access file browser and add new directory.

In-app: Tap '+' > New folder > Name it (e.g., "LeakFolder").

**Expected Output**: Folder appears in list.

### Step 2: Enable Public Sharing

**Context**: Configure sharing options.

Long-press folder > Share > Public link > Enable.

**Expected Output**: Shareable URL generated.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[sharing]]
- [[folder-creation]]
