---
tags:
  - file-upload
  - concrete-cms
  - bypass
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - PHP
techniques:
  - '[[Remote File Copy]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6e62cb7d-b509-4c87-abbc-6c14131351e6
created_at: '2025-12-14T05:32:13.283Z'
updated_at: '2025-12-14T05:32:13.283Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-SVG-via-Concrete-CMS-File-Manager

## Summary

This procedure authenticates as an admin in Concrete CMS and uploads a malicious SVG via File Manager, exploiting the whitelist in concrete/config/concrete.php to bypass HTML restrictions.

## Description

The File Manager allows .svg uploads without scanning for embedded scripts, rooted in lines 86-88 of the config file. In the scenario, an attacker with admin access uploads the payload, confirming placement for later embedding. Expected outcome: File stored accessibly on the server.

## Requirements

1. Valid admin credentials for Concrete CMS
2. Access to the dashboard (e.g., via browser)
3. Pre-crafted malicious SVG file

## Defense

Defensive measures and detection strategies:

- Implement content-type and structure validation for uploads
- Log and review all admin file uploads
- Disable SVG uploads or use safe rendering libraries

## Objectives

1. Ingest malicious payload into the CMS
2. Verify storage path for embedding
3. Set up for XSS trigger

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Gain admin access to reach the upload interface.

Log in to Concrete CMS dashboard with admin credentials. From the main menu, select File Manager.

> Expected: Dashboard loads; File Manager opens showing current files.

### Step 2: Perform Upload

**Context**: Submit the SVG, which passes whitelist checks.

Click the upload button, select `malicious.svg`, and confirm. The file is accepted due to .svg extension.

> Expected: Upload progress completes; file lists in manager.

### Step 3: Confirm Path

**Context**: Note location for later use.

Right-click the file and select Properties to view the path (e.g., /application/files/.../malicious.svg).

> Expected: Path displayed, confirming server storage.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[concrete-cms]]
- [[bypass]]
