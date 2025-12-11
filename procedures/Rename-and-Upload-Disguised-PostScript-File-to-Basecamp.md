---
id: cba87349-fa81-49b3-a1f3-d09bcc364c43
name: Rename and Upload Disguised PostScript File to Basecamp
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:15.547Z'
updated_at: '2025-12-11T06:10:15.547Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - file-upload
  - rce
  - basecamp
commands:
  - '[[commands/ping-test-poc]]'
platforms:
  - Web
tools:
  - '[[tools/ImageMagick]]'
  - '[[tools/GraphicsMagick]]'
  - '[[tools/Ghostscript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---

# Rename and Upload Disguised PostScript File to Basecamp

## Summary

This procedure renames a malicious PostScript file to a GIF extension and uploads it to Basecamp's profile image feature, triggering server-side processing and RCE via vulnerable Ghostscript.

## Description

By changing the file extension to .gif, the upload bypasses basic validation while the content remains PostScript, processed by ImageMagick or GraphicsMagick invoking Ghostscript. This leads to arbitrary command execution on the server.

## Requirements

1. Malicious PostScript file from prior crafting step.
2. Valid Basecamp account credentials.
3. Web browser or API tool for upload.

## Defense

Defensive measures and detection strategies:

- Enforce content-based file validation beyond extensions.
- Monitor for anomalous image processing activity or unexpected network traffic.

## Objectives

1. Bypass upload restrictions.
2. Trigger server-side vulnerability exploitation.
3. Achieve remote code execution.

## Instructions

### Step 1: Rename File

**Context**: Change extension to mimic a valid image.

```bash
mv rce.ps rce.gif
```

> Ensures the file is accepted as an image upload.

### Step 2: Upload to Basecamp

**Context**: Use the profile image upload functionality.

Navigate to Basecamp profile settings, select rce.gif, and submit.

> Server processes the file, calling Ghostscript and executing the command.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ImageMagick]]
- [[tools/GraphicsMagick]]

## Tags

- [[file-upload]]
- [[rce]]
