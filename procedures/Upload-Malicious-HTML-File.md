---
id: proc-002
tags:
  - file-upload
  - malicious-payload
  - html-upload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:23:32.401Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-HTML-File

## Summary

This procedure exploits the lack of file type validation by uploading an HTML file embedding JavaScript for XSS and PHP for RCE potential, stored within the application's request system.

## Description

Targeting PHP web apps with unrestricted uploads, craft an HTML file with `<script>alert(document.cookie);</script>` for session-stealing XSS and `<?php if(isset($_GET['cmd'])){echo shell_exec($_GET['cmd']);} ?>` for a basic PHP shell. Upload via the form's browse function. Outcomes include file storage accessible via document ID, enabling later exploitation. Requires prior form access.

## Requirements

1. Crafted HTML file with XSS and PHP payloads
2. Active session on the upload page
3. Text editor (e.g., Notepad++) for payload creation

## Defense

Defensive measures and detection strategies:

- Enforce file type whitelisting (e.g., only PDF, DOC) and MIME validation
- Scan uploads for executable code patterns using antivirus or WAF

## Objectives

1. Deliver malicious content without rejection
2. Store file in application context for later access
3. Enable XSS and RCE vectors

## Instructions

### Step 1: Prepare Payload File

**Context**: Create the malicious HTML.

Use a text editor to save content as `unsure1.html` with XSS script and PHP shell.

> File ready for selection; size under any limits (typically <10MB).

### Step 2: Select and Queue Upload

**Context**: Use form to attach the file.

Click 'browse' on the attachment field and select `unsure1.html`.

> File appears in the upload preview without errors.

### Step 3: Validate Upload Readiness

**Context**: Ensure no client-side blocks.

Check form for any warnings; proceed if clear.

> Success: File is attached and form submittable.

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
- [[malicious-payload]]
