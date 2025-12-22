---
tags:
  - rce
  - imagetragick
  - ghostscript
  - imagemagick
  - file-upload
  - postscript
type: attack_chain
tools:
  - '[[tools/ImageMagick]]'
  - '[[tools/Ghostscript]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/send-malicious-image-patch]]'
platforms:
  - Web
  - Linux
complexity: medium
procedures:
  - '[[procedures/Exploit-ImageTragick-v2-for-RCE]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
description: >-
  A single-stage attack exploiting ImageTragick v2 vulnerability in Ghostscript
  invoked by ImageMagick to achieve remote code execution through a malicious
  JPEG upload to a web endpoint.
skill_level: intermediate
impact_level: high
id: 8b2bfa00-78f1-4b37-bde4-f788ae9f3018
created_at: '2025-12-14T17:23:49.536Z'
updated_at: '2025-12-14T17:23:49.536Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# RCE via ImageTragick v2 in ImageMagick Ghostscript Processing on Booth.pm

## Overview

This attack chain demonstrates a remote code execution (RCE) vulnerability exploited through ImageTragick v2, where a malicious JPEG file embeds PostScript code that tricks Ghostscript—invoked by ImageMagick during image processing—into executing arbitrary commands. The attacker targets the /design endpoint on manage.booth.pm by submitting the file via a PATCH request, leading to the execution of a curl command that contacts an external server, confirming RCE and potentially enabling data exfiltration or further compromise.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Submit Malicious JPEG] --> B[RCE via Ghostscript]
    B --> C[Command Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]] (for sending the HTTP request)
- Text editor or script to craft the malicious JPEG file

### Target Environment

- Web application with image upload functionality using ImageMagick and Ghostscript
- Vulnerable endpoint: PATCH /design on manage.booth.pm
- Server running unpatched ImageMagick/Ghostscript without policy.xml restrictions on PS formats

### Initial Access Requirements

- Network access to the target host (manage.booth.pm)
- Ability to send authenticated or unauthenticated PATCH requests (depending on endpoint protections)
- No prior credentials needed if endpoint is public-facing

## Detailed Attack Procedures

### Step 1: Submit Malicious Image for Processing
procedure: [[procedures/Exploit-ImageTragick-v2-for-RCE]]

**Objective**: Upload a crafted JPEG containing embedded PostScript code to trigger Ghostscript RCE during image processing.

**Instructions**: First, create a malicious JPEG file (imagetragick.jpeg) by prepending standard JPEG headers (e.g., FF D8 FF) to the PostScript payload. The payload undefines setpagedevice to bypass policies, handles legal checks, and pipes output to a curl command. Then, use [[commands/send-malicious-image-patch]] to submit it via multipart/form-data to the /design endpoint:

```bash
curl -X PATCH https://manage.booth.pm/design \
  -F "shop[header]=@imagetragick.jpeg"
```

**Expected Output**: The server processes the image, invoking Ghostscript, which executes the embedded curl to https://avtohanter.ru/qwetest, sending server data or confirming RCE.

**Success Indicators**:
- HTTP response from server (e.g., 200 OK or image processing acknowledgment)
- External server (attacker's) receives curl request, indicating RCE success
- No immediate error; monitor for delayed exfiltration if data is sent

## Attack Chain Summary

### Key Achievements

1. Bypassed ImageMagick's delegation to Ghostscript using embedded PS in JPEG
2. Achieved arbitrary command execution via output pipe to curl
3. Demonstrated full server compromise on unpatched systems

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
