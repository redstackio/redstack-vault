---
tags:
  - discovery
  - verification
type: procedure
tools:
  - '[[tools/ImageMagick]]'
  - '[[tools/Ghostscript]]'
  - '[[tools/Netcat]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/postscript-payload-rce]]'
  - '[[commands/bash-reverse-shell]]'
  - '[[commands/ls-directory-list]]'
  - '[[commands/whoami-user-identification]]'
  - '[[commands/cat-hosts-file]]'
platforms:
  - Web
techniques:
  - '[[System Information Discovery]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: b3972a50-d9a2-475e-bc31-ede6c97b661d
created_at: '2025-12-11T06:10:33.128Z'
updated_at: '2025-12-11T06:10:33.128Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1082]]'
---
# Verify Server Identity

## Summary

This procedure verifies the compromised server as a Semrush instance by accessing specific URLs and correlating with shell output.

## Description

After gaining shell access, navigate to Semrush-specific URLs to confirm files and paths match the ls output, ensuring the target is correctly identified.

## Requirements

1. Active reverse shell.
2. Output from ls and /etc/hosts commands.
3. Web access to Semrush URLs.

## Defense

Defensive measures and detection strategies:

- Monitor access to internal paths.
- Use anomaly detection for unusual URL accesses.

## Objectives

1. Confirm server ownership.
2. Validate exploitation success.
3. Prepare for further actions.

## Instructions

### Step 1: Access Verification URLs

**Context**: Browse to specific Semrush report URLs to match shell findings.

Navigate to https://www.semrush.com/my_reports/████ and https://www.semrush.com/my_reports/████████.

> Compare with ls output to confirm.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[Discovery]]
- [[verification]]
