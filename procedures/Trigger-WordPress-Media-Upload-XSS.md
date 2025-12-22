---
tags:
  - xss
  - wordpress
  - media-upload
  - file-upload
  - javascript-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.359Z'
sub_techniques: []
id: f0f20ed2-8764-464b-904a-fff73594a46b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Trigger-WordPress-Media-Upload-XSS

## Summary

This procedure exploits two cross-site scripting (XSS) vulnerabilities in WordPress 4.7.2 by uploading an oversized media file with a malicious JavaScript payload embedded in the filename, triggering unescaped error messages that execute arbitrary code in the administrator's browser context.

## Description

The attack targets the media upload interface in wp-admin/media-new.php, where filenames from oversized files (e.g., >2MB or >100MB) are interpolated into error messages without HTML or JavaScript escaping. Specifically, in script-loader.php, the uploader_l10n array defines messages like file_exceeds_size_limit, which are replaced with fileObj.name and appended to the DOM via jQuery in handlers.min.js (e.g., uploadSizeError function). A second vector occurs for very large files in big_upload_failed. An authenticated administrator viewing the error executes the payload, potentially leading to session theft or site compromise. Prerequisites include admin access and a vulnerable WordPress instance.

## Requirements

1. Authenticated access to WordPress 4.7.2 admin panel
2. Ability to create files larger than upload limits (e.g., 20MB for standard, 100MB+ for big upload)
3. Modern web browser to interact with the Plupload JavaScript uploader

## Defense

Defensive measures and detection strategies:

- Update WordPress to version 4.7.3 or later, where filename escaping was added
- Implement content security policy (CSP) to restrict inline JavaScript execution
- Monitor admin panel logs for unusual upload attempts or JavaScript errors
- Sanitize all user-supplied filenames server-side before DOM insertion

## Objectives

1. Inject and execute arbitrary JavaScript in the admin browser context
2. Demonstrate potential for session hijacking or credential theft
3. Highlight risks of unescaped user input in error handling

## Instructions

### Step 1: Create Malicious Oversized File

**Context**: Prepare a file that exceeds size limits with an XSS payload in the filename to exploit interpolation in error messages.

No specific command required; use a text editor or script to create a file named 'payload<img src=x onerror=alert(document.cookie)>.jpg' filled with 20MB of dummy data (e.g., repeated text or binary padding).

> Verify file size with `ls -lh filename.jpg` (expected: >2MB) and inspect filename for payload.

### Step 2: Access and Authenticate to Media Upload

**Context**: Log in and navigate to the vulnerable upload interface to set up the attack.

Navigate to http://target.com/wp-admin/media-new.php after admin login. Confirm Plupload loads by inspecting page source for handlers.min.js.

> Expected: Upload UI visible; no errors on page load.

### Step 3: Submit the File for Upload

**Context**: Trigger the size limit error by attempting to upload, causing unsafe filename insertion.

Select the file via 'Select Files' or drag-and-drop in the media library. The upload fails, firing events like FileExceedsSizeLimit or BigUploadFailed.

> Expected: Error div appears with interpolated filename, e.g., via pluploadL10n.replace('%s', file.name).

### Step 4: Validate XSS Execution

**Context**: Observe and confirm JavaScript execution from the two vectors (standard and big upload errors).

Watch for alert popup or use browser console to log execution. Inspect #media-items for injected HTML.

> Expected: alert(document.cookie) reveals session data; DOM shows unescaped <img> tag.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- wordpress
- media-upload
- file-upload
- javascript-injection
