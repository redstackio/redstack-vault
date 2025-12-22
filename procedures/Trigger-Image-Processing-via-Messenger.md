---
tags:
  - trigger
  - execution
type: procedure
tools:
  - '[[tools/ImageMagick]]'
  - '[[tools/Ghostscript]]'
  - '[[tools/Netcat]]'
  - '[[tools/curl]]'
  - '[[tools/Facebook-Messenger]]'
  - '[[tools/bash]]'
  - '[[tools/python]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/postscript-python-reverse-shell]]'
  - '[[commands/whoami]]'
  - '[[commands/ls]]'
  - '[[commands/cat-readme]]'
  - '[[commands/curl-aws-metadata-role]]'
  - '[[commands/curl-aws-credentials]]'
  - '[[commands/postscript-bash-reverse-shell]]'
platforms:
  - Web
techniques:
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 03cc4e1f-3e57-4cdf-b8a8-fe4a589e9915
created_at: '2025-12-11T06:10:32.462Z'
updated_at: '2025-12-11T06:10:32.462Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Trigger Image Processing via Messenger

## Summary

This procedure sends commands through Facebook Messenger to trigger server-side image processing, executing embedded payloads in uploaded files.

## Description

By sending specific commands, the Kit bot processes priority product images, invoking ImageMagick and Ghostscript on the malicious Postscript file, leading to code execution.

## Requirements

1. Prior integration with Messenger
2. Malicious file already uploaded
3. Listener ready for reverse shell

## Defense

Defensive measures and detection strategies:

- Rate limit Messenger commands
- Validate and sanitize all processed files

## Objectives

1. Execute the uploaded payload
2. Establish reverse shell connection
3. Confirm exploitation success

## Instructions

### Step 1: Send Trigger Commands

**Context**: Use Messenger to send commands that reference the priority products, forcing image processing.

> Send messages like product update requests to Kit bot.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Facebook-Messenger]]

## Tags

- trigger
- execution
