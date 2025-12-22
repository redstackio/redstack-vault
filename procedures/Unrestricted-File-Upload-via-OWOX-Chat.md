---
tags:
  - unrestricted-file-upload
  - rce
  - web-vulnerability
  - intercom
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:10.581Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: f9729aab-c889-47aa-8b12-81702ad8e9ce
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
---
# Unrestricted-File-Upload-via-OWOX-Chat

## Summary

This procedure exploits an unrestricted file upload vulnerability in the OWOX application's chat window, integrated with Intercom, by uploading dangerous file types like .php or .rb without any extension validation, potentially enabling server-side code execution, XSS, or other exploits if the files are processed or downloaded by users or systems.

## Description

The OWOX BI application at https://bi.owox.com/ features a chat interface powered by the third-party Intercom service that lacks proper file upload restrictions. Attackers with authenticated access can upload arbitrary files, including executable scripts, which are hosted on Intercom's infrastructure. While not directly executable in the OWOX context, these files could facilitate web shells for RCE, client-side attacks via XSS if downloaded, or chaining with other vulnerabilities. The attack requires only basic user authentication and a web browser, making it accessible to low-skill adversaries. Expected outcomes include successful file transmission and potential compromise of server or client environments depending on further exploitation.

## Requirements

1. Valid OWOX user credentials for authentication
2. Web browser with JavaScript enabled for chat interaction
3. Local access to a malicious file (e.g., .php web shell or .rb script)
4. Direct internet access to https://bi.owox.com/

## Defense

Defensive measures and detection strategies:

- Implement strict file extension whitelisting (e.g., allow only .jpg, .pdf) and MIME type validation on uploads
- Scan uploaded files with antivirus or static analysis tools before hosting
- Monitor Intercom logs for anomalous file uploads, especially dangerous extensions
- Use content security policies (CSP) to prevent execution of uploaded scripts
- Rate-limit chat uploads and require admin approval for attachments

## Objectives

1. Upload unrestricted malicious files to third-party hosting
2. Establish persistence or exfiltration vectors via hosted content
3. Enable code execution or client compromise through file processing

## Instructions

### Step 1: Authenticate to OWOX

**Context**: Establish an authenticated session to access the chat feature.

Navigate to https://bi.owox.com/ in your web browser and log in with valid credentials.

> Successful login grants access to the application dashboard.

### Step 2: Access Chat Window

**Context**: Open the vulnerable Intercom-powered chat interface.

Locate the chat widget (typically in the bottom-right corner) and click to open it.

> The chat window loads, revealing the file attachment option.

### Step 3: Attach Malicious File

**Context**: Select a dangerous file to bypass validation.

Click the attachment icon in the chat input and choose a file like a .php web shell from your local filesystem.

> The file is added to the message without type checking.

### Step 4: Send Upload

**Context**: Submit the file to confirm unrestricted upload.

Optionally add a message, then click send to transmit the file.

> The upload succeeds, and the file is hosted on Intercom; check for any shared link or confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[unrestricted-file-upload]]
- [[rce]]
- [[web-vulnerability]]
- [[intercom]]
