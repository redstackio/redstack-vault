---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - xss
  - stored-xss
  - rce
  - slack
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Desktop
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.555Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Slack-Posts

## Summary

This procedure exploits a stored XSS vulnerability in Slack's files.slack.com Posts feature by injecting unsanitized JavaScript payloads, which are stored on the backend and executed when viewed in the Slack desktop client, potentially leading to remote code execution via Electron APIs.

## Description

The attack targets inadequate input validation in the Posts functionality of files.slack.com, allowing attackers to upload files and attach comments containing malicious scripts. When a victim accesses the file or post through the Slack desktop application (built on Electron), the payload renders and executes in the client's context, bypassing web security due to the desktop environment. This can escalate to RCE by leveraging browser APIs or Electron-specific modules to run system commands. The vulnerability was reported via HackerOne and fixed server-side without client changes.

## Requirements

1. Valid Slack account with upload and posting permissions in a workspace
2. Access to files.slack.com via web browser
3. Victim using vulnerable Slack desktop client version
4. Basic knowledge of JavaScript and XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement strict backend input sanitization and output encoding for all user-generated content in Posts and files
- Use Content Security Policy (CSP) to restrict script execution in client renders
- Monitor for anomalous script injections in file metadata or comments via logging
- Educate users on avoiding suspicious file shares

## Objectives

1. Store malicious JavaScript in Slack's backend without detection
2. Achieve code execution in the victim's desktop client context
3. Escalate to RCE for arbitrary command execution on the victim's machine

## Instructions

### Step 1: Prepare the Payload

**Context**: Craft a JavaScript payload that tests XSS and can be extended for RCE. Start with a simple alert for proof-of-concept, then use Electron's `require('electron').remote` or similar to execute system code.

No specific command; use Slack's web UI to input the payload directly.

Example payload:

```html
<img src=x onerror="alert('Stored XSS in Slack Posts'); // For RCE: require('child_process').exec('calc.exe');">
```

> This payload triggers on error in an image tag, storing the script server-side. In the desktop client, it executes due to relaxed validation.

### Step 2: Inject via Files and Posts

**Context**: Upload a file to files.slack.com and attach the payload in the Posts/comments section to store it persistently.

Use the Slack web interface:

1. Log in at slack.com
2. Go to Files > Upload a file (e.g., a harmless PNG)
3. In the post/comment field, insert the payload
4. Submit; the backend stores it without validation

> Expected: File uploads successfully, payload visible in source but not executed in web view.

### Step 3: Trigger Execution

**Context**: Share the file link in a channel to entice the victim to open it in the desktop client.

Share the file URL via Slack message.

> When victim clicks and views in desktop app, the payload executes, showing alert or running code.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[rce]]
- [[slack]]
