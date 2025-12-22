---
tags:
  - xss
  - gallery-view
  - nextcloud
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
updated_at: '2025-12-13T23:52:20.808Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: 6d469fe3-b70a-49a3-9c46-4ac5fe164155
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Victim-Opens-Shared-Folder-in-Gallery-View

## Summary

This procedure simulates the victim accessing the shared malicious folder and switching to Gallery view, where the directory name is rendered but not yet executed.

## Description

As the victim, opening the shared folder in Nextcloud and selecting Gallery view displays the folder contents with thumbnails, including the unsanitized directory name from the parameter regression. This sets the stage for payload execution on further interaction.

## Requirements

1. Access to shared folder invitation
2. Authenticated victim session
3. Gallery app available

## Defense

Defensive measures and detection strategies:

- Train users to inspect shared content before opening
- Log Gallery view accesses for anomaly detection
- Sanitize display names in all views

## Objectives

1. Load the shared folder in victim's browser
2. Render the malicious name in Gallery mode
3. Avoid premature execution

## Instructions

### Step 1: Access Shared Folders

**Context**: Victim locates the shared item.

Log in to Nextcloud and go to Shared with You or click the share link.

### Step 2: Open Folder and Switch View

**Context**: Enter Gallery view to display the name.

Open the malicious folder. Click the view selector (three lines or icons) and choose Gallery.

### Step 3: Confirm Display

**Context**: Verify the name is shown.

Thumbnails load; the folder title shows `<img src=x onerror=alert(1)>` without executing.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- nextcloud
- gallery-view
