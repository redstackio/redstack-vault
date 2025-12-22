---
tags:
  - unicode
  - upload
  - sanitization
type: procedure
tools:
  - '[[tools/TamperData]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - PHP
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b9913271-01c3-444d-bf2e-0e849ede316f
created_at: '2025-12-13T23:56:03.276Z'
updated_at: '2025-12-13T23:56:03.276Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-File-with-Unicode-Filename

## Summary

This procedure uploads a malicious file using a Unicode-prepended filename to exploit sanitization flaws in WordPress, resulting in a numeric rename that enables XSS.

## Description

The `sanitize_file_name` function mishandles certain Unicode characters (e.g., ±), returning 0, which leads `wp_unique_filename` to save as '-1.png'. This occurs in `wp-admin/includes/file.php`. Bypassing client-side via tampering allows the flawed server-side processing.

## Requirements

1. Prepared malicious file from prior procedure
2. Active [[tools/TamperData]] for filename modification
3. Upload interface accessed

## Defense

Defensive measures and detection strategies:

- Update WordPress to patched versions (post-2016)
- Enhance filename sanitization to handle Unicode properly
- Log uploads with filename patterns for anomaly detection

## Objectives

1. Trigger sanitization bypass
2. Achieve numeric filename
3. Store file for later triggering

## Instructions

### Step 1: Select and Modify Filename

**Context**: Apply Unicode to exploit the flaw.

In the upload form, select the file. Intercept with [[tools/TamperData]] and change filename to '±malicious.png'.

### Step 2: Submit Upload

**Context**: Let server process the flawed name.

Forward the request. Monitor for success; file saves in `/wp-content/uploads/` as '-1.png'.

### Step 3: Verify Upload

**Context**: Confirm placement in media library.

Check Media library for the renamed file.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/TamperData]]

## Tags

- [[unicode]]
- [[upload]]
- [[sanitization]]
