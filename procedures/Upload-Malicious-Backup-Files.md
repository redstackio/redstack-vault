---
id: proc-002
tags:
  - file-upload
  - deserialization
  - malicious-payload
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
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:23:33.061Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-Backup-Files

## Summary

This procedure uploads crafted `structure.xml` and `data.dump` files containing a malicious serialized PHP object to the ownCloud Files section, preparing for backup inclusion and subsequent deserialization exploitation.

## Description

The OwnBackup app processes uploaded files during backup and restore. By crafting `structure.xml` to define a database table (e.g., `oc_accounts`) and `data.dump` with a serialized `Swift_Transport_SendmailTransport` object that writes a PHP webshell to `/tmp/pwned.php`, an attacker can introduce untrusted data. When restored, this leads to arbitrary file writes. Prerequisites include admin access and the app installed.

## Requirements

1. Admin session in ownCloud
2. Crafted files: `structure.xml` and `data.dump` with serialized payload
3. Access to Files interface

## Defense

Defensive measures and detection strategies:

- Validate and scan uploaded files for serialized objects
- Restrict file uploads to trusted formats and sizes
- Monitor file system for anomalous uploads in backup directories

## Objectives

1. Introduce malicious serialized data into the system
2. Ensure files are positioned for backup inclusion
3. Avoid detection during upload

## Instructions

### Step 1: Prepare Malicious Files

**Context**: Create the files with the payload before upload.

No command; manually craft `structure.xml` with table definition and `data.dump` using PHP serialization for `Swift_Transport_SendmailTransport` to execute file write.

> Files ready for upload.

### Step 2: Upload Files via UI

**Context**: Use the Files section to store the malicious files.

No specific command; in ownCloud Files, click Upload and select both files.

> Upload success message; files visible in the directory.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[deserialization]]
- [[malicious-payload]]
