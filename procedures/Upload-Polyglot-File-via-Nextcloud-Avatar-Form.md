---
id: proc-uuid-avatar-upload-bypass-001
tags:
  - upload-bypass
  - nextcloud
  - avatar
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2024-10-05T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:10.154Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Polyglot-File-via-Nextcloud-Avatar-Form

## Summary

This procedure uploads the polyglot PHP-JPEG file through Nextcloud's avatar upload form, exploiting validation flaws in `/core/controller/avatarcontroller.php` to bypass checks and store potentially malicious content on the server.

## Description

Nextcloud's avatar controller validates uploads using `$image->valid()` (structural check) and MIME type detection for image/jpeg or image/png, ignoring the .php extension. The polyglot passes these, gets uploaded, and renamed to 'avatar_upload', mitigating immediate RCE but leaving risk if renaming fails or configs allow PHP execution in the storage directory.

## Requirements

1. Authenticated session in Nextcloud
2. Access to the user profile/avatar upload interface
3. Polyglot file prepared (e.g., image1.php)

## Defense

Defensive measures and detection strategies:

- Add file extension blacklisting (e.g., block .php) before validation
- Use sandboxed upload processing to scan for embedded code
- Monitor for uploads with mismatched extensions and MIME types
- Update Nextcloud to versions with enhanced validation

## Objectives

1. Bypass MIME and structural checks
2. Successfully store file on server
3. Achieve potential for code execution via misconfiguration

## Instructions

### Step 1: Access Upload Form

**Context**: Log in and navigate to avatar settings.

Go to your Nextcloud profile settings and select the avatar upload option.

### Step 2: Submit File

**Context**: Upload the renamed polyglot, triggering the vulnerable controller.

Select `image1.php` and submit. The system detects it as image/jpeg via magic bytes, calls `$image->valid()` which succeeds, and processes the upload.

**Expected Output**: Success message; avatar updated to the image.

### Step 3: Verify Upload

**Context**: Check server-side storage.

Inspect the upload directory (typically data/user/files/avatars/) for 'avatar_upload' file. Confirm it contains the polyglot content.

**Expected Output**: File present, renders as image, but hex view shows PHP code.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- upload-bypass
- nextcloud
- avatar
