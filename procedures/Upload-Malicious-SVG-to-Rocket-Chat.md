---
tags:
  - svg-upload
  - file-upload
  - rocket-chat
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: a33a176a-4573-4991-b0b3-ec15443e674f
created_at: '2025-12-14T05:32:10.324Z'
updated_at: '2025-12-14T05:32:10.324Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Malicious-SVG-to-Rocket-Chat

## Summary

This procedure involves crafting and uploading an SVG file embedded with JavaScript to a Rocket.Chat chat, exploiting the lack of sanitization to generate a preview URL that can later be used for malicious JS execution.

## Description

Rocket.Chat's file upload feature allows users to attach files to messages, automatically generating preview URLs for media types like SVG. Without proper sanitization, SVGs containing JavaScript (e.g., redirect scripts) are served inline from Google Cloud Storage under the Rocket.Chat domain. This procedure focuses on the upload step, preparing the payload for subsequent exploitation. The target environment is any accessible Rocket.Chat instance with file uploads enabled. Expected outcomes include a shareable URL that bypasses same-origin restrictions when accessed.

## Requirements

1. Valid user account in Rocket.Chat
2. Access to a chat room with file upload permissions
3. Text editor to create the SVG payload
4. Web browser for uploading

## Defense

Defensive measures and detection strategies:

- Disable SVG uploads or sanitize files for script tags
- Serve uploaded files with Content-Security-Policy (CSP) headers blocking inline JS
- Monitor for unusual file uploads containing <script> tags

## Objectives

1. Upload unsanitized SVG with embedded JS
2. Obtain preview URL for social engineering
3. Set up for JS execution in victim browsers

## Instructions

### Step 1: Craft Malicious SVG

**Context**: Create an SVG file with JavaScript payload, such as a redirect to a phishing site.

Open a text editor and write:

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
  <script>window.location.href = 'https://phishingsite.com';</script>
</svg>
```

Save as `malicious.svg`.

> This embeds JS that executes on load, performing an open redirect.

### Step 2: Upload to Rocket.Chat

**Context**: Attach the file to a chat message to trigger URL generation.

Log into Rocket.Chat, navigate to a chat, click the attachment icon, and select `malicious.svg` to upload.

> Rocket.Chat processes the upload and generates a URL like `https://open.rocket.chat/file-upload/ID/malicious.svg`.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[svg-upload]]
- [[file-upload]]
- [[rocket-chat]]
