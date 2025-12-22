---
tags:
  - file-upload
  - rce
type: procedure
tools:
  - '[[tools/ImageMagick]]'
  - '[[tools/Ghostscript]]'
  - '[[tools/Netcat]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/postscript-payload-rce]]'
  - '[[commands/bash-reverse-shell]]'
  - '[[commands/ls-directory-list]]'
  - '[[commands/whoami-user-identification]]'
  - '[[commands/cat-hosts-file]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: cc28ccd7-0745-49fe-9603-df7aef1981af
created_at: '2025-12-11T06:10:33.208Z'
updated_at: '2025-12-11T06:10:33.208Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Upload Malicious File to Semrush

## Summary

This procedure uploads a malicious Postscript-disguised JPG file to Semrush's report constructor logo feature, triggering the RCE vulnerability in ImageMagick.

## Description

Uploading the file to https://www.semrush.com/my_reports/constructor causes ImageMagick to process it, invoking Ghostscript and executing the embedded command. Prerequisites include having the payload file ready and access to the upload endpoint.

## Requirements

1. Malicious file 'test.jpg' with Postscript payload.
2. Web browser or tool for uploading to the target URL.
3. Listener set up on attacker's side.

## Defense

Defensive measures and detection strategies:

- Validate and sanitize uploaded files.
- Use content-type checking and disable dangerous format processing.

## Objectives

1. Trigger vulnerability exploitation.
2. Initiate reverse shell connection.
3. Gain initial access to the server.

## Instructions

### Step 1: Perform Upload

**Context**: Upload the file via the web interface to exploit the vulnerability.

Navigate to https://www.semrush.com/my_reports/constructor and upload 'test.jpg' as the logo.

> This triggers processing and command execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/ImageMagick]]

## Tags

- [[file-upload]]
- [[commands/postscript-payload-rce]]
