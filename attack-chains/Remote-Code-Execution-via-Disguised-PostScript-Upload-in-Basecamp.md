---
id: 49008314-6b6a-44c9-8ec4-80d5fab7f74b
name: Remote Code Execution via Disguised PostScript Upload in Basecamp
type: attack_chain
description: >-
  Exploits a file upload vulnerability in Basecamp to achieve remote code
  execution through a crafted PostScript file processed by vulnerable
  Ghostscript.
verified: false
submitted: true
step_count: 4
created_at: '2025-12-11T06:10:15.551Z'
updated_at: '2025-12-11T06:10:15.551Z'
procedures:
  - '[[procedures/Craft-Malicious-PostScript-File-for-Ghostscript-RCE]]'
  - '[[procedures/Rename-and-Upload-Disguised-PostScript-File-to-Basecamp]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
tags:
  - rce
  - file-upload
  - ghostscript
  - imagemagick
platforms:
  - Web
tools:
  - '[[tools/ImageMagick]]'
  - '[[tools/GraphicsMagick]]'
  - '[[tools/Ghostscript]]'
commands:
  - '[[commands/ping-test-poc]]'
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1059]]'
---

# Remote Code Execution via Disguised PostScript Upload in Basecamp

Multi-stage attack chain demonstrating a complete attack workflow exploiting a vulnerability in Basecamp's profile image upload to achieve remote code execution via a crafted PostScript file disguised as a GIF, leveraging CVE-2017-8291 in Ghostscript.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access] --> B[File Crafting]
    B --> C[Upload and Execution]
    C --> D[Remote Shell]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Ghostscript]] (for testing locally, though exploited server-side)
- [[tools/ImageMagick]] (for understanding processing flow)

### Target Environment

- Target OS/Platform: Web (Basecamp.com)
- Required services/ports: Basecamp profile image upload service
- Network access requirements: Access to Basecamp user account and internet connectivity

### Initial Access Requirements

- Credential requirements: Valid Basecamp user account
- Network position: External internet access
- Prior access needed: None beyond user authentication

## Detailed Attack Procedures

### Step 1: Craft Malicious PostScript File - [[procedures/Craft-Malicious-PostScript-File-for-Ghostscript-RCE]]

**Procedure**: [[procedures/Craft-Malicious-PostScript-File-for-Ghostscript-RCE]]

**Objective**: Create a PostScript file embedding an arbitrary command to exploit Ghostscript's CVE-2017-8291 during server-side processing.

**Expected Output**: A functional PostScript file that, when processed, executes the embedded command.

**Success Indicators**:
- File starts with '%!' and contains the embedded command.
- Local testing with Ghostscript executes the command (e.g., ping traffic observed).

First, craft the file with an embedded command like [[commands/ping-test-poc]]:

```bash
# Example content in rce.ps file:
%!PS
... (PostScript code embedding system('ping -c1 attacker.com'))
```

Save the file as rce.ps.

### Step 2: Rename File to GIF Extension - [[procedures/Craft-Malicious-PostScript-File-for-Ghostscript-RCE]]

**Procedure**: [[procedures/Craft-Malicious-PostScript-File-for-Ghostscript-RCE]]

**Objective**: Disguise the PostScript file as a GIF to bypass upload validation.

**Expected Output**: File renamed to rce.gif while retaining PostScript content.

**Success Indicators**:
- File extension changed without altering content.
- File magic bytes still indicate PostScript.

Rename the file:

```bash
mv rce.ps rce.gif
```

### Step 3: Upload File as Profile Image - [[procedures/Rename-and-Upload-Disguised-PostScript-File-to-Basecamp]]

**Procedure**: [[procedures/Rename-and-Upload-Disguised-PostScript-File-to-Basecamp]]

**Objective**: Upload the disguised file to Basecamp's profile image endpoint.

**Expected Output**: Successful upload confirmation from Basecamp.

**Success Indicators**:
- Upload accepted without validation errors.
- Server begins processing the file.

Navigate to Basecamp profile settings and upload rce.gif as the profile image.

### Step 4: Trigger Server-Side Processing and RCE

**Procedure**: [[procedures/Rename-and-Upload-Disguised-PostScript-File-to-Basecamp]]

**Objective**: Allow server to process the file, invoking vulnerable Ghostscript for RCE.

**Expected Output**: Embedded command executes, e.g., ping to attacker.com observed.

**Success Indicators**:
- Network traffic or logs show command execution.
- Potential remote shell access gained.

Monitor for execution indicators, such as incoming ping from Basecamp servers.

## Attack Chain Summary

### Key Achievements

1. Successful crafting and upload of malicious file bypassing validation.
2. Exploitation of Ghostscript CVE-2017-8291 for arbitrary command execution.
3. Potential for privilege escalation and further server compromise.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: [TIMESTAMP]*
