---
tags:
  - directory-traversal
  - path-traversal
  - slack
  - android
  - auth-token-disclosure
  - file-upload
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Credential Access]]'
commands: []
platforms:
  - Android
  - Web
complexity: medium
procedures:
  - '[[procedures/Upload-Specially-Crafted-File-to-Slack-Workspace]]'
  - '[[procedures/Induce-Victim-to-Open-File-on-Android-Device]]'
  - >-
    [[procedures/Exploit-Directory-Traversal-to-Overwrite-Config-and-Expose-Data]]
step_count: 3
techniques:
  - '[[Exploitation for Client Execution]]'
description: >-
  A multi-stage attack exploiting a directory traversal vulnerability in Slack's
  Android app to overwrite device configuration files and disclose
  authentication tokens to attacker-controlled websites.
skill_level: intermediate
impact_level: high
id: 6fae072e-91c0-4c47-a167-b453556eaf72
created_at: '2025-12-14T17:31:42.991Z'
updated_at: '2025-12-14T17:31:42.991Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Slack Android Directory Traversal Leading to Auth Token Disclosure

Multi-stage attack chain demonstrating a complete attack workflow exploiting a directory traversal vulnerability in Slack's Android app.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Upload Crafted File] --> B[Induce File Open]
    B --> C[Overwrite Config and Exfil]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (relies on Slack workspace access and social engineering)

### Target Environment

- Slack workspace with file sharing enabled
- Victim using Slack Android app (version vulnerable prior to patch)
- Android device for file opening

### Initial Access Requirements

- Attacker must have access to the same Slack workspace as the victim
- No external network access beyond Slack; requires user interaction

## Detailed Attack Procedures

### Step 1: Upload Specially-Crafted File
procedure: [[procedures/Upload-Specially-Crafted-File-to-Slack-Workspace]]

**Objective**: Upload a file with a malicious path traversal filename to the Slack workspace, ensuring it exceeds 1MB to trigger download on the victim's Android device.

**Instructions**: Create a benign file larger than 1MB (e.g., a large image or document) and rename it using traversal sequences like "../../../system/config" to exploit the lack of filename validation. Upload the file to a channel or direct message in the Slack workspace via the web interface or app.

**Expected Output**: File successfully uploaded and visible in the workspace; no immediate errors.

**Success Indicators**:
- File appears in Slack channel/DM
- File size confirmed >1MB

### Step 2: Induce Victim to Open File on Android Device
procedure: [[procedures/Induce-Victim-to-Open-File-on-Android-Device]]

**Objective**: Trick the victim into downloading and opening the crafted file using the Slack Android app, triggering the directory traversal during the file handling process.

**Instructions**: Use social engineering within the workspace, such as sending the file in a relevant context (e.g., "Check this report") and encouraging the victim to open it on their Android device. Ensure the victim uses the Android app, as the vulnerability is client-side.

**Expected Output**: Victim interacts with the file; Android app downloads and attempts to open it, invoking the OS file handler.

**Success Indicators**:
- Victim confirms opening the file
- No app crash (vulnerability silently exploits)

### Step 3: Exploit Directory Traversal to Overwrite Config and Expose Data
procedure: [[procedures/Exploit-Directory-Traversal-to-Overwrite-Config-and-Expose-Data]]

**Objective**: Leverage the traversal to overwrite Android configuration files, causing Slack auth tokens to be sent to an attacker-controlled website.

**Instructions**: The exploitation occurs automatically upon file open; the crafted filename causes the Android OS to interpret it as a path (e.g., traversing to /data/etc/ or similar config directories) and overwrite files. Pre-configure the overwrite to inject scripts or redirects that exfiltrate tokens via HTTP to your controlled domain.

**Expected Output**: Device config files modified; auth tokens transmitted to attacker site (monitor incoming requests).

**Success Indicators**:
- Incoming web requests from victim's IP containing Slack tokens
- Confirmation of file overwrite via device logs (if accessible)

## Attack Chain Summary

### Key Achievements

1. Bypassed filename validation in Slack Android app
2. Achieved arbitrary file overwrite on victim device
3. Disclosed sensitive auth tokens without direct device access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Credential Access]]

---
*Last updated: 2023-10-01*
