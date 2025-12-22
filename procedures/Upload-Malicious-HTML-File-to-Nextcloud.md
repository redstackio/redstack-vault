---
tags:
  - xss
  - file-upload
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-09-18T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T03:16:25.154Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: dcf38ada-c980-4718-af4c-e3c95a622fdc
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-HTML-File-to-Nextcloud

## Summary

This procedure involves creating and uploading an HTML file with an embedded XSS payload to a Nextcloud instance, leveraging the server's file storage without immediate rendering on web or Android clients.

## Description

The Nextcloud platform allows file uploads via its web interface. By crafting an HTML file with a JavaScript payload disguised in a data URI (e.g., base64-encoded script), the file is stored harmlessly on the server but becomes dangerous when rendered in the vulnerable iOS app. This step sets up the stored XSS attack, where the payload persists until accessed by the victim. Prerequisites include a valid Nextcloud account with upload permissions. Expected outcomes include successful file storage without triggering web-based sanitization.

## Requirements

1. Access to Nextcloud web interface with login credentials
2. Ability to create and edit HTML files locally
3. No special tools required; standard web browser suffices

## Defense

Defensive measures and detection strategies:

- Implement server-side file type validation to block or sanitize HTML uploads
- Use content security policies (CSP) in client apps to prevent JavaScript execution from files
- Monitor upload logs for suspicious file types like HTML with encoded payloads

## Objectives

1. Store a malicious payload in Nextcloud for later exploitation
2. Ensure the file does not execute on upload to avoid detection
3. Prepare for sharing with victims targeting iOS users

## Instructions

### Step 1: Create the Malicious HTML File

**Context**: Design an HTML snippet that embeds JavaScript via a data URI to bypass basic filters.

Craft the file content:

```html
<a href="data:text/html;base64,PHNjcmlwdD5hbGVydCgiWFNTIik8L3NjcmlwdD4=">Click for hack</a>
```

> This anchor tag links to a base64-encoded HTML that includes `<script>alert("XSS")</script>`. Save as `malicious.html`.

### Step 2: Upload the File to Nextcloud

**Context**: Use the web interface to store the file on the server.

Log in to Nextcloud, navigate to the files section, and drag-and-drop or use the upload button to add `malicious.html`.

> Verify upload by checking the file list; the web preview should not render the HTML or execute JS.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[file-upload]]
- [[nextcloud]]
