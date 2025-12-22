---
tags:
  - zip
  - payload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:23:19.981Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: cc161dc2-656e-4a5b-9035-e889a798c409
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Compress-Files-into-Malicious-ZIP

## Summary

This procedure packages the created HTML decoy and PHP webshell into a ZIP archive, which the vulnerable plugin will extract without validation.

## Description

The ZIP format is used because the Articulate plugin processes ZIP uploads for Articulate content. No password or obfuscation is needed due to lack of validation. Run on a local Linux machine with zip utility. Expected outcome: A ZIP file containing both files, ready for upload to achieve file placement in the uploads directory.

## Requirements

1. Local Linux/Unix system with zip command installed
2. index.html and index.php from previous procedure
3. Disk space for small archive

## Defense

Defensive measures and detection strategies:

- Server-side ZIP extraction with content scanning (e.g., ClamAV)
- Restrict upload directories to non-executable paths
- Log all ZIP extractions and alert on PHP presence

## Objectives

1. Bundle malicious files into uploadable format
2. Ensure extraction places files in web-accessible path
3. Maintain payload integrity

## Instructions

### Step 1: Verify Files

**Context**: Confirm the malicious files exist before zipping.

**Command** (ls):
```bash
ls -la index.html index.php
```

> Expected output: Listing showing both files present.

### Step 2: Create ZIP Archive

**Context**: Use zip to compress the files into malicious.zip.

**Command** (zip):
```bash
zip malicious.zip index.html index.php
```

> Expected output: Adding files to archive message, ending with zipfile created.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- zip
- payload
