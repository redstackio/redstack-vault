---
id: proc-upload-html-nextcloud
tags:
  - xss
  - upload
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:24:40.149Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-HTML-to-Nextcloud

## Summary

This procedure involves creating and uploading an HTML file with an embedded JavaScript payload to a Nextcloud instance, exploiting the lack of sanitization for stored files that will later be rendered in the iOS app.

## Description

In the context of a stored XSS attack on Nextcloud, the attacker crafts an HTML file containing executable JavaScript, such as a base64-encoded script in a data URL. This file is uploaded via the Nextcloud web or app interface. The server stores it without modification, setting the stage for execution when viewed in the vulnerable iOS app. Prerequisites include a valid Nextcloud account and access to file upload functionality. Expected outcome: The file is persisted and accessible for sharing.

## Requirements

1. Valid credentials for a Nextcloud user account with upload permissions
2. Access to a text editor or HTML crafting tool to create the payload
3. Network connectivity to the Nextcloud server over HTTPS

## Defense

Defensive measures and detection strategies:

- Implement server-side file type validation and sanitization for uploads (e.g., strip executable content from HTML)
- Use content security policies (CSP) in client apps to block inline scripts
- Monitor upload logs for suspicious file types like HTML with script tags

## Objectives

1. Persist malicious HTML payload on the Nextcloud server
2. Ensure the file is stored without alteration for later execution
3. Prepare for sharing to enable victim interaction

## Instructions

### Step 1: Craft the Malicious HTML Payload

**Context**: Create the HTML file with an obfuscated JavaScript payload to evade basic filters.

Use a text editor to generate the file content:

```html
<!DOCTYPE html>
<html>
<body>
<a href="data:text/html;base64,PHNjcmlwdD5hbGVydCgiWFNTIik8L3NjcmlwdD4=">Click here to view content</a>
</body>
</html>
```

> This anchor tag, when clicked, decodes the base64 to execute <script>alert("XSS")</script>. Save as "malicious.html".

### Step 2: Upload the File to Nextcloud

**Context**: Transfer the crafted file to the server using the upload feature.

Log in to the Nextcloud web interface, navigate to a folder, and use the upload button to select and upload "malicious.html". Alternatively, use the iOS or desktop app's upload function.

> Expected output: Upload success message; file appears in the file list with HTML extension.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[upload]]
- [[nextcloud]]
