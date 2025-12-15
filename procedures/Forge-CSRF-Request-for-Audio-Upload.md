---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - csrf
  - web
  - upload
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:49.723Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Forge-CSRF-Request-for-Audio-Upload

## Summary

This procedure exploits a CSRF vulnerability in VK.com's audio recording upload feature by crafting a malicious HTML form that submits an upload request without the required hash validation, allowing unauthorized audio files to be added to a victim's account while they are authenticated.

## Description

The vulnerability arises from insufficient hash checks in the upload process, enabling attackers to forge POST requests to the audio upload endpoint. In a typical attack, the victim is tricked into visiting an attacker-controlled webpage that automatically submits the forged request using the victim's session. This leads to unauthorized uploads, potentially cluttering the account or enabling further abuse, though direct account compromise is not specified. The target environment is the VK.com web application, requiring the victim to be logged in via a browser.

## Requirements

1. Access to an attacker-controlled web server to host the malicious HTML
2. Victim authenticated session on VK.com (e.g., logged in browser)
3. Prepared audio file (e.g., MP3) to upload
4. Knowledge of the upload endpoint URL and form parameters from VK.com inspection

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens or SameSite cookies on all state-changing endpoints
- Enforce strict referrer checks or custom headers for upload requests
- Monitor for anomalous upload patterns in user accounts
- Educate users on phishing risks and avoiding untrusted links

## Objectives

1. Upload audio file to victim's VK.com account without consent
2. Demonstrate lack of CSRF protection in upload feature
3. Highlight potential for account manipulation

## Instructions

### Step 1: Inspect VK.com Upload Endpoint

**Context**: Use browser developer tools to capture the legitimate upload request and identify missing protections like hash parameters.

Navigate to VK.com's audio upload section while logged in, start an upload, and inspect the network tab for the POST request to the endpoint (e.g., /audio/upload).

**Expected Output**: Form data including file, session tokens, but no enforced hash.

### Step 2: Craft Malicious HTML Form

**Context**: Create an HTML page that auto-submits a form mimicking the upload request, embedding the audio file data.

Write and save the following HTML (replace placeholders with actual endpoint and file):

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf-form" action="https://vk.com/audio/upload" method="POST" enctype="multipart/form-data">
  <input type="hidden" name="audio" value="[BASE64_ENCODED_AUDIO_DATA]">
  <input type="hidden" name="hash" value="[FAKE_OR_EMPTY_HASH]">
  <!-- Other required params from inspection -->
</form>
<script>
  document.getElementById('csrf-form').submit();
</script>
</body>
</html>
```

Host this on your server.

**Expected Output**: Page ready for victim visit.

### Step 3: Lure and Execute

**Context**: Trick the victim into visiting the hosted page, triggering the auto-submit.

Send a phishing link to the victim. When visited with an active VK.com session open, the form submits, uploading the file.

**Expected Output**: Audio appears in victim's VK.com audio section.

**Success Indicators**:
- Upload success without user prompt
- File visible in account

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-vulnerability]]
- [[unauthorized-upload]]
