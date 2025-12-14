---
tags:
  - url-bypass
  - auth-bypass
  - info-disclosure
  - defense-evasion
  - web
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:28:59.303Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: e4c8753f-64bb-4d03-afdb-e7dff228e8a0
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Bypass-Protection-via-URL-Modification

## Summary

This procedure exploits a flaw in Cloudup's URL handling by removing the '/download' segment, bypassing password protection and enabling unauthorized file viewing and metadata disclosure.

## Description

The core vulnerability lies in the file view endpoint (https://cloudup.com/files/{file_id}/), which fails to enforce password authentication or user authorization, unlike the download endpoint. By modifying the URL while logged into an unauthorized account, attackers can directly access file contents and EXIF metadata (e.g., name, size, permissions, timestamps, paths). This leads to authentication bypass, privilege escalation across accounts, and information disclosure of sensitive data intended to be private.

## Requirements

1. Unauthorized account session (e.g., Account Y)
2. File ID from the download URL (e.g., iDQ23wk5p1O)
3. Web browser

## Defense

Defensive measures and detection strategies:

- Uniformly enforce authentication and password checks across all file endpoints
- Validate URL parameters server-side to prevent manipulation
- Monitor for anomalous access patterns, like view requests without prior authorization

## Objectives

1. Achieve authentication bypass to view protected contents
2. Escalate privileges for cross-account file access
3. Disclose sensitive metadata without credentials

## Instructions

### Step 1: Identify File ID

**Context**: Extract the unique identifier from the download URL.

From the link (e.g., https://cloudup.com/files/iDQ23wk5p1O/download), note the {file_id} segment (iDQ23wk5p1O).

### Step 2: Modify URL

**Context**: Alter the URL to target the vulnerable view endpoint.

Remove '/download' to form https://cloudup.com/files/{file_id}/ (e.g., https://cloudup.com/files/iDQ23wk5p1O/).

### Step 3: Load Modified URL

**Context**: Access the endpoint to trigger disclosure.

Paste and load the modified URL in the browser while logged in as the unauthorized account. Observe file contents and metadata display without prompts.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[url-bypass]]
- [[auth-bypass]]
- [[info-disclosure]]
- [[defense-evasion]]
- [[web]]
