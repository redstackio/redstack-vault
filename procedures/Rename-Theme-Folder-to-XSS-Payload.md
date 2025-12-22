---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - xss
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-05T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.322Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Rename-Theme-Folder-to-XSS-Payload

## Summary

This procedure injects a stored XSS payload by renaming a broken WordPress theme folder to include malicious HTML/JavaScript, which is later reflected without sanitization on the themes page.

## Description

After breaking the theme, renaming its folder to a string like '<img src=x onerror=alert(1)>' stores the payload in the filesystem. When the admin views the themes page, WordPress displays the broken folder name in an error context without encoding, executing the JS in the browser. This is a stored XSS limited to users with the privileges to perform the rename.

## Requirements

1. Filesystem write access to rename folders in wp-content/themes/
2. A broken theme folder already present
3. Basic knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all filesystem-derived strings in admin templates
- Use WordPress hooks to validate theme folder names on scan
- Audit filesystem for suspicious folder names containing script tags

## Objectives

1. Store the XSS payload in a reflected context
2. Ensure payload survives theme detection
3. Enable execution upon page load

## Instructions

### Step 1: Craft Payload

**Context**: Select an effective XSS string.

Use '<img src=x onerror=alert(1)>' or similar; ensure it's URL-safe if needed.

### Step 2: Rename Folder

**Context**: Apply the payload as the new folder name.

Via file manager or SSH, rename the broken folder to the payload string.

> The rename persists until manual correction or WordPress cleanup.

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
- payload-injection
