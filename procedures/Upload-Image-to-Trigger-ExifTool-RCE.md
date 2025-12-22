---
tags:
  - rce
  - image-upload
type: procedure
tools:
  - '[[tools/ExifTool]]'
  - '[[tools/Ruby]]'
  - '[[tools/Perl]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Linux
techniques:
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f7fbc689-e4da-411c-9adc-2e609121eabf
created_at: '2025-12-11T03:47:58.361Z'
updated_at: '2025-12-11T03:47:58.361Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Upload Image to Trigger ExifTool RCE

## Summary

This procedure uploads a crafted image to GitLab, triggering ExifTool to process it and execute injected Perl code due to insufficient escaping in DjVu annotations.

## Description

By creating a new snippet and attaching the PoC file, GitLab Workhorse passes it to ExifTool, which evals the annotation and runs arbitrary commands like writing to /tmp.

## Requirements

1. GitLab account
2. Crafted DjVu file (e.g., echo_vakzz.jpg)
3. Web browser access to GitLab

## Defense

Defensive measures and detection strategies:

- Restrict file types and extensions
- Monitor ExifTool execution logs for anomalies

## Objectives

1. Trigger RCE on GitLab server
2. Verify command execution via file creation
3. Achieve code injection as git user

## Instructions

### Step 1: Create Snippet and Attach File

**Context**: Use GitLab interface to upload the image, invoking [[commands/exiftool-process-image]].

Navigate to https://gitlab.com/-/snippets/new and attach echo_vakzz.jpg.

### Step 2: Execute Injected Command

**Context**: The upload executes [[commands/echo-vakzz-to-file]] via Perl eval.

```bash
echo vakzz >/tmp/vakzz
```

> This creates /tmp/vakzz on the server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/echo-vakzz-to-file]]
- [[commands/exiftool-process-image]]

## Tools Used

- [[tools/ExifTool]]
- [[tools/Perl]]

## Tags

- #rce
- #image-upload
