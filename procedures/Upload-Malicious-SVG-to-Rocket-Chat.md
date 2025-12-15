---
id: proc-uuid-1
tags:
  - file-upload
  - svg
  - xss
  - rocket-chat
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:27.141Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Upload-Malicious-SVG-to-Rocket-Chat

## Summary

This procedure involves crafting and uploading a malicious SVG file with embedded JavaScript to a Rocket.Chat chat room, exploiting the platform's lack of file sanitization to store and serve executable content.

## Description

Rocket.Chat's file upload feature allows users to attach files to messages, which are stored on external services like Google Cloud Storage but served through platform-specific URLs. SVG files can embed JavaScript that executes when rendered in a browser. By uploading such a file, attackers position a payload that can redirect users or perform other client-side actions upon access. This targets web-based Rocket.Chat instances running on Node.js, requiring only standard user access.

## Requirements

1. Valid Rocket.Chat user account with upload permissions
2. Text editor to create the SVG file
3. Target chat room in the Rocket.Chat instance
4. Knowledge of the victim's interaction patterns for effective sharing

## Defense

Defensive measures and detection strategies:

- Sanitize SVG uploads by stripping or blocking JavaScript elements
- Serve files with Content-Security-Policy (CSP) headers to prevent JS execution
- Monitor file uploads for suspicious MIME types or content patterns
- Educate users on avoiding untrusted file links in chats

## Objectives

1. Deliver executable payload via legitimate file upload
2. Obtain a shareable URL that bypasses external storage restrictions
3. Set up for client-side exploitation on victim access

## Instructions

### Step 1: Craft Malicious SVG Payload

**Context**: Create an SVG file embedding JavaScript for the desired action, such as an open redirect.

Use a text editor to generate the file:

```html
<svg xmlns="http://www.w3.org/2000/svg">
  <script>window.location.href = 'https://attacker-controlled-phishing-site.com';</script>
</svg>
```

Save as `redirect.svg`. This script will execute onload when the SVG is rendered.

### Step 2: Upload to Rocket.Chat

**Context**: Use the chat interface to upload the file, triggering storage and URL generation.

1. Log in to Rocket.Chat.
2. Open or create a chat room.
3. Click the attachment icon and select `redirect.svg`.
4. Send the message with the file.

The platform stores the file on storage.googleapis.com but provides a URL like `https://open.rocket.chat/file-upload/{ID}/redirect.svg`.

**Expected Output**: File appears in chat with a clickable link.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[svg]]
- [[xss]]
- [[rocket-chat]]
