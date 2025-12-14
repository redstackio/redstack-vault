---
tags:
  - xss
  - payload
  - file-prep
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 297400d1-77b2-4b2a-9d6a-d512bf9225ae
created_at: '2025-12-13T23:56:03.285Z'
updated_at: '2025-12-13T23:56:03.285Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Prepare-Malicious-XSS-File

## Summary

This procedure creates a seemingly benign image file with an embedded JavaScript payload that executes when the file is served as HTML due to filename sanitization flaws.

## Description

WordPress vulnerabilities allow files with numeric names to be rendered as HTML by Apache. Prepare a PNG file with XSS like `<script>alert('XSS')</script>` embedded in its content or metadata. This disguises the payload to pass upload checks but triggers execution on misrendering.

## Requirements

1. Text editor or hex editor for file modification
2. Basic image file (blank PNG)
3. Knowledge of XSS payloads for escalation (e.g., iframe for user creation)

## Defense

Defensive measures and detection strategies:

- Scan uploaded files for script tags using antivirus or custom scripts
- Enforce strict MIME type checking on serve
- Log and quarantine files with unusual content

## Objectives

1. Create a dual-purpose file (image + script)
2. Ensure payload survives upload
3. Enable execution on HTML rendering

## Instructions

### Step 1: Create Base File

**Context**: Start with a valid image to avoid immediate rejection.

Generate a blank PNG using an image editor or command-line tool like `convert -size 1x1 xc:white blank.png`.

### Step 2: Embed Payload

**Context**: Insert JavaScript without corrupting image validity.

Open the file in a hex editor and append or insert `<script>alert('XSS')</script>` at the end, or use steganography tools. For advanced, craft an iframe payload: `<iframe src="javascript:fetch('/wp-admin/user-new.php', {method:'POST', body:'user=admin&pass=hacked'})"></iframe>`.

### Step 3: Verify File

**Context**: Test the file's dual nature.

View in image viewer (should display) and text editor (should show script). Rename temporarily to numeric (e.g., '0.png') and serve locally via Apache to confirm execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload]]
- [[file-prep]]
