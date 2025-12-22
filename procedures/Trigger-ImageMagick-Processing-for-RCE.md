---
tags:
  - rce
  - imagemagick
  - command-injection
type: procedure
tools:
  - '[[tools/ImageMagick]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/wget-connect-back]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T05:32:13.339Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: e72b9eba-8b9c-40ad-bd35-af29f4d0e02f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
---
# Trigger-ImageMagick-Processing-for-RCE

## Summary

This procedure triggers the server's ImageMagick processing of the uploaded MVG file, causing it to parse the payload and execute the injected command via the vulnerable HTTPS delegate using curl and bash.

## Description

Once uploaded, the application processes the file with ImageMagick's convert utility, which interprets the ASCII as MVG and fetches the malicious URL. The delegates.xml configures HTTPS to use curl in bash, allowing backtick injection to run arbitrary commands like wget for a callback connection.

## Requirements

1. Uploaded file on server
2. Attacker server listening on port 1337 (e.g., nc -lvp 1337)
3. Server-side ImageMagick with vulnerable config

## Defense

Defensive measures and detection strategies:

- Update ImageMagick to patched version
- Restrict delegates.xml to safe invocations
- Monitor for outbound connections from image processing

## Objectives

1. Invoke ImageMagick parsing
2. Execute injected command
3. Confirm RCE via callback

## Instructions

### Step 1: Initiate Processing

**Context**: Trigger the application to process the image, such as by viewing or saving the profile.

Navigate to profile view or use curl to fetch a page that generates thumbnails:

```bash
curl https://target.com/profile -b "session=your_cookie"
```

> Expected output: Page loads, potentially with processed image.

### Step 2: Monitor for Execution

**Context**: Watch attacker server for the injected [[commands/wget-connect-back]] execution.

The command runs automatically on processing:

```bash
# On attacker side: nc -lvp 1337
```

> Expected output: Incoming connection from target server IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/wget-connect-back]]

## Tools Used

- [[tools/ImageMagick]]

## Tags

- rce
- command-injection
