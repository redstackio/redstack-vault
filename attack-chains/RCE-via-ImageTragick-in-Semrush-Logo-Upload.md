---
tags:
  - rce
  - imagetragick
  - imagemagick
  - ghostscript
  - file-upload
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Semrush-Report-Constructor-Logo-Upload]]'
  - '[[procedures/Craft-ImageTragick-PostScript-Payload]]'
  - '[[procedures/Upload-Malicious-Image-to-Trigger-RCE]]'
  - '[[procedures/Establish-and-Interact-with-Reverse-Shell]]'
  - '[[procedures/Verify-Compromised-Server-Identity]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:24:17.750Z'
description: >-
  Multi-stage attack exploiting unpatched ImageMagick in Semrush's report
  constructor to achieve remote code execution via malicious logo upload.
skill_level: intermediate
impact_level: high
id: 43a18f20-b022-407d-a379-dcd90b465a9e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
  - '[[Unix Shell]]'
---
# RCE via ImageTragick in Semrush Logo Upload

Multi-stage attack chain demonstrating remote code execution on Semrush's production server by exploiting an unpatched ImageMagick vulnerability (ImageTragick) during logo upload in the report constructor feature. The attack involves crafting a PostScript payload disguised as a JPG, uploading it to trigger Ghostscript command execution, establishing a reverse shell, and verifying server compromise.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Upload Feature] --> B[Craft Payload]
    B --> C[Upload Malicious File]
    C --> D[Reverse Shell Interaction]
    D --> E[Verify Server Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Text editor for payload creation
- Netcat listener (nc) for reverse shell

### Target Environment

- Web platform with ImageMagick/Ghostscript
- Linux server
- Access to https://www.semrush.com/my_reports/constructor

### Initial Access Requirements

- Valid Semrush account for authenticated access to report constructor
- Attacker's IP reachable from target (for reverse shell)
- Port 8080 open on attacker's listener

## Detailed Attack Procedures

### Step 1: Access Logo Upload Feature
procedure: [[procedures/Access-Semrush-Report-Constructor-Logo-Upload]]

**Objective**: Navigate to the vulnerable logo upload endpoint in Semrush's report constructor.

**Instructions**: Open a web browser and log in to Semrush with a valid account. Navigate to the report constructor at https://www.semrush.com/my_reports/constructor and locate the logo upload input field.

**Expected Output**: Upload interface visible, ready for file selection.

**Success Indicators**:
- Page loads successfully
- Logo upload form is accessible

### Step 2: Craft PoC Payload
procedure: [[procedures/Craft-ImageTragick-PostScript-Payload]]

**Objective**: Create a malicious PostScript file disguised as a JPG to exploit ImageTragick.

**Instructions**: Use a text editor to write the PostScript payload and save it as test.jpg. The payload embeds a reverse shell command targeting the attacker's listener.

**Expected Output**: Malicious file test.jpg created on local system.

**Success Indicators**:
- File saved with .jpg extension
- Payload syntax verified (no errors in editor)

### Step 3: Upload Malicious File
procedure: [[procedures/Upload-Malicious-Image-to-Trigger-RCE]]

**Objective**: Submit the disguised payload to trigger ImageMagick processing and RCE.

**Instructions**: In the logo upload field, select and upload test.jpg. Submit the form to process the file.

**Expected Output**: File upload succeeds; reverse shell connects to listener on port 8080.

**Success Indicators**:
- No upload errors
- Incoming connection on listener

### Step 4: Interact with Reverse Shell
procedure: [[procedures/Establish-and-Interact-with-Reverse-Shell]]

**Objective**: Confirm RCE by executing commands in the established shell to explore the server.

**Instructions**: Set up a netcat listener with `nc -lvnp 8080`. Once connected, execute [[commands/list-directory]] to list files, [[commands/identify-current-user]] to check user, [[commands/list-specific-directory]] for app files, and [[commands/view-hosts-file]] to confirm domain.

```bash
nc -lvnp 8080
ls
whoami
ls [redacted dir]
cat /etc/hosts
```

**Expected Output**: Shell prompt appears; commands return server filesystem details.

**Success Indicators**:
- Shell access granted
- Commands execute without errors
- Server-specific files visible

### Step 5: Verify Server Ownership
procedure: [[procedures/Verify-Compromised-Server-Identity]]

**Objective**: Cross-verify the compromised server belongs to Semrush production.

**Instructions**: From shell outputs, note paths and hosts. Manually access https://www.semrush.com/my_reports/[redacted] and https://www.semrush.com/my_reports/[redacted] to confirm matching files. Check /etc/hosts for semrush.net entries.

**Expected Output**: Web pages show files from ls output; hosts file lists semrush.net.

**Success Indicators**:
- Files match between shell and web
- Domain confirmed in hosts file

## Attack Chain Summary

### Key Achievements

1. Exploited unpatched ImageMagick for RCE via logo upload
2. Established reverse shell on production server
3. Verified full compromise of Semrush environment

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Unix Shell]] Unix Shell

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Discovery]] Discovery

---
*Last updated: 2023-10-01T00:00:00Z*
