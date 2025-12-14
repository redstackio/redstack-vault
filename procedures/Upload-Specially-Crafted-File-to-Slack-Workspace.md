---
tags:
  - file-upload
  - slack
  - path-traversal
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[T1566.001]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 4f9995eb-3074-48b7-8834-a699e6fc2f8d
created_at: '2025-12-14T17:31:42.988Z'
updated_at: '2025-12-14T17:31:42.988Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Upload Specially-Crafted File to Slack Workspace

## Summary

This procedure involves creating and uploading a file with a path traversal payload in its filename to a Slack workspace, exploiting the lack of validation to set up a client-side vulnerability trigger on Android devices.

## Description

In the context of Slack's Android app vulnerability (HackerOne #1378889), attackers with workspace access upload files larger than 1MB without proper filename sanitization. The crafted name uses directory traversal sequences (e.g., "../") to manipulate the Android OS during file opening, potentially overwriting configs. This step requires no special tools, only workspace membership, and positions the malicious file for victim interaction.

## Requirements

1. Active Slack workspace membership shared with the victim
2. Ability to upload files >1MB (e.g., generate a large dummy file like a 2MB text or image)
3. Knowledge of traversal syntax for Android paths (e.g., targeting /data or /system directories)

## Defense

Defensive measures and detection strategies:

- Enable file upload restrictions or scanning in Slack admin settings
- Train users on suspicious file requests in workspaces
- Monitor for anomalous file uploads with unusual names via Slack audit logs

## Objectives

1. Position a malicious file in the workspace for delivery
2. Ensure file triggers download on Android (size >1MB)
3. Avoid detection during upload phase

## Instructions

### Step 1: Create the Crafted File

**Context**: Generate a file that meets size requirements and embeds traversal in the name to exploit OS path interpretation.

Create a file using any editor or tool:

- Name example: `../../../../../data/etc/slack_config.txt` (adjust based on target config paths)
- Content: Benign data, e.g., random bytes to exceed 1MB (use `dd if=/dev/zero of=malicious.file bs=1M count=2` on Linux if available)

### Step 2: Upload to Slack

**Context**: Deliver the file via Slack's upload feature to a channel or DM targeting the victim.

- Log into Slack web or app
- Navigate to a shared channel/DM
- Click upload and select the crafted file
- Add enticing message, e.g., "Review this document on your phone"

**Expected Output**: File uploads successfully; link shared in workspace.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.001]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[slack]]
- [[path-traversal]]
