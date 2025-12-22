---
tags:
  - file-upload
  - slack
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 923fea6d-82b5-424f-9cb6-f9671cf3ecd5
created_at: '2025-12-14T03:46:14.549Z'
updated_at: '2025-12-14T03:46:14.549Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Malicious-File-to-Slack

## Summary

This procedure delivers a malicious Office file to a Slack workspace, triggering backend preview processing that activates the LibreOffice LFI vulnerability for credential exposure.

## Description

Slack's file upload feature processes uploads for thumbnails using LibreOffice, making it a vector for exploits like CVE-2019-17400. The attacker uses standard upload mechanisms in channels or DMs, relying on automatic processing. This step requires only basic user access and assumes the crafted file from prior procedures. Outcomes include initiation of the exploit chain without alerting the user.

## Requirements

1. Valid Slack account with file upload permissions
2. Crafted malicious Office file
3. Web access to Slack interface

## Defense

Defensive measures and detection strategies:

- Implement file type whitelisting and content scanning pre-upload
- Disable auto-preview for Office files or use isolated processing
- Monitor upload logs for high-risk file patterns

## Objectives

1. Successfully deliver exploit payload to backend
2. Trigger processing without upload rejection
3. Maintain stealth in communication channels

## Instructions

### Step 1: Access Slack Workspace

**Context**: Log into the target Slack workspace via web or app.

Navigate to a channel or start a DM where uploads are permitted.

### Step 2: Initiate File Upload

**Context**: Use the upload button to select and submit the malicious Office file.

Ensure the file name and description appear innocuous to avoid scrutiny.

### Step 3: Confirm Upload and Processing

**Context**: Observe the upload progress and preview attempt.

The backend will invoke LibreOffice for thumbnail generation, starting the exploit.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[slack]]
