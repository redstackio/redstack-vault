---
tags:
  - rce
  - imagemagick
  - file-upload
  - mvg
  - command-injection
type: attack_chain
tools:
  - '[[tools/ImageMagick]]'
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
  - '[[procedures/Prepare-Malicious-MVG-Payload-File]]'
  - '[[procedures/Upload-Malicious-File-as-Profile-Picture]]'
  - '[[procedures/Trigger-ImageMagick-Processing-for-RCE]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T05:32:13.347Z'
description: >-
  A multi-stage attack exploiting a remote code execution vulnerability in the
  profile picture upload feature by using a malicious MVG payload parsed by
  ImageMagick, leading to arbitrary command execution on the server.
skill_level: intermediate
impact_level: high
id: 2f21c1e7-94b0-43bf-9624-36df4645ed18
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
---
# RCE via ImageMagick MVG Payload in Profile Picture Upload

Multi-stage attack chain demonstrating a complete attack workflow exploiting a remote code execution vulnerability in the profile picture upload feature of a web application. The attack leverages ImageMagick's parsing of Magick Vector Graphics (MVG) in uploaded files to inject and execute arbitrary commands via a vulnerable curl delegate.

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
    A[Prepare Payload] --> B[Upload File]
    B --> C[Trigger Processing]
    C --> D[Command Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ImageMagick]] (server-side, exploited)
- Text editor for payload creation
- wget or similar for listening on attacker side (e.g., nc -lvp 1337)

### Target Environment

- Web application with profile picture upload at /settings/profile/edit
- Server running ImageMagick with vulnerable delegates.xml (https delegate using curl via bash)
- Network access to upload files and receive connections on port 1337

### Initial Access Requirements

- Valid user session or account to access profile edit page
- No special credentials beyond basic authentication
- Attacker-controlled server reachable from target (e.g., public IP 1.2.3.4:1337)

## Detailed Attack Procedures

### Step 1: Prepare Malicious MVG Payload File
procedure: [[procedures/Prepare-Malicious-MVG-Payload-File]]

**Objective**: Create an ASCII file disguised as an image containing MVG directives that trigger command injection via the 'image over' directive with an HTTPS URL.

**Instructions**: Use a text editor to craft the payload. The file must include push/pop graphic-context, viewbox, and the malicious 'image over' line embedding the command in backticks within the URL.

**Expected Output**: A file named x.gif containing the MVG code.

**Success Indicators**:
- File created without syntax errors
- Payload verifiable by manual inspection

### Step 2: Upload Malicious File as Profile Picture
procedure: [[procedures/Upload-Malicious-File-as-Profile-Picture]]

**Objective**: Submit the malicious file through the profile picture upload endpoint to bypass basic checks by naming it with a .gif extension.

**Instructions**: Navigate to /settings/profile/edit in the web application and use the standard upload form to submit x.gif. No special tools needed beyond a browser or curl for automation.

**Expected Output**: File uploaded successfully, profile picture updated (though it may not render).

**Success Indicators**:
- Upload confirmation from the application
- File stored on server for processing

### Step 3: Trigger ImageMagick Processing for RCE
procedure: [[procedures/Trigger-ImageMagick-Processing-for-RCE]]

**Objective**: Cause the server to process the uploaded file with ImageMagick, parsing the MVG and invoking the vulnerable HTTPS delegate to execute the injected command.

**Instructions**: Save or refresh the profile page to trigger image processing (e.g., thumbnail generation). Monitor the attacker server for incoming connection from the executed [[commands/wget-connect-back]].

**Expected Output**: Incoming HTTP request to attacker's server on port 1337, confirming RCE.

**Success Indicators**:
- Connection received on attacker side
- No errors in application logs indicating failed processing

## Attack Chain Summary

### Key Achievements

1. Successful injection of MVG payload via file upload
2. Exploitation of ImageMagick's delegate system for command execution
3. Demonstration of outbound connection capability for further exploitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Unix Shell]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
