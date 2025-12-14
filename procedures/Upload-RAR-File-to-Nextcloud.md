---
id: proc-upload-rar
tags:
  - file-upload
  - nextcloud
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
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:24:08.708Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-RAR-File-to-Nextcloud

## Summary

This procedure uploads a benign RAR file to Nextcloud, setting the stage for triggering the vulnerable extraction process that allows command injection.

## Description

Upload via the standard file interface prepares the file for 'Extract Here' action, which invokes the vulnerable endpoint. Target any Nextcloud with file upload enabled. Expected outcome: File ready for exploitation without raising alarms.

## Requirements

1. Authenticated Nextcloud session
2. A sample RAR file (benign archive)
3. Web browser

## Defense

Defensive measures and detection strategies:

- Scan uploaded files for malware
- Limit file types or sizes
- Log upload events for anomalies

## Objectives

1. Place a file in the target environment
2. Enable triggering of extraction vulnerability
3. Maintain low detection risk

## Instructions

### Step 1: Upload the File

**Context**: Use Nextcloud's upload feature to add the RAR file.

No command required; use web interface.

> Drag-and-drop or select sample.rar in the Files section. Expected output: File appears in directory listing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- file-upload
- nextcloud
