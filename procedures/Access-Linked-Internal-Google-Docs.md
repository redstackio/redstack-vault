---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567894
tags:
  - google-docs
  - chained-access
  - edit-permissions
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - GCP
  - Google Workspace
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:29:28.472Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Access-Linked-Internal-Google-Docs

## Summary

This procedure exploits links from exposed GCS files to access internal Google Documents, some with edit permissions, allowing further unauthorized data viewing or modification.

## Description

Files like mindmap.txt in the bucket contain URLs to Google Docs. Attackers follow these to pub or edit endpoints. Target: Google Workspace integrated with GCP. Prerequisites: Downloaded mindmap.txt. Outcomes: Access to internal docs, potential edits leading to tampering or more leaks.

## Requirements

1. Web browser for accessing Doc URLs
2. Prior exfiltration of linking files from GCS
3. No credentials if links are public/shared

## Defense

Defensive measures and detection strategies:

- Revoke public/edit shares on Google Docs
- Monitor Doc access logs for unauthorized IPs
- Avoid embedding sensitive links in public storage

## Objectives

1. View published internal documents
2. Attempt edits on shared documents
3. Chain to additional sensitive information

## Instructions

### Step 1: Parse Linking File

**Context**: Extract URLs from downloaded files like mindmap.txt.

Open mindmap.txt and note links such as https://docs.google.com/document/d/e/2PACX-1vSNzTLkZMqILVYoey4dnSLYdk0Jmsd8pFu7ygLJ57RQ1c8XlZDbzaG45rQMOrDbHRWCQa5LN7DZid8s/pub.

### Step 2: Access and Edit Documents

**Context**: Navigate to links to view or modify content.

Visit pub URLs for read; edit URLs like https://docs.google.com/document/d/14APaSKwYpwutujISnkbLOnjdQ5RG-hIQXulasZT7h6s/edit for changes.

> Expected output: Document loads; edits save if permissions allow, exposing or altering internal data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[google-docs]]
- [[internal-access]]
- [[misconfiguration]]
