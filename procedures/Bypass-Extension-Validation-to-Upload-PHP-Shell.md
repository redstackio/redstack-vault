---
tags:
  - file-upload
  - bypass
  - php-shell
  - rce
  - imce
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 5ce7c89c-5a86-4a09-8111-5b813c187030
created_at: '2025-12-14T05:32:10.073Z'
updated_at: '2025-12-14T05:32:10.073Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
---
# Bypass-Extension-Validation-to-Upload-PHP-Shell

## Summary

This procedure exploits weak file validation in the IMCE module by appending an allowed image extension to a malicious PHP file, enabling arbitrary code upload that could lead to remote code execution if the server interprets it as a script.

## Description

The IMCE file manager restricts uploads to image types (jpg, png, gif) but fails to properly validate content or double-extensions, allowing files like shell.php.gif to be uploaded. Once inserted into a signature, the file is stored on the server and potentially accessible via URL. In a PHP/Drupal environment, if MIME checks are absent, this could execute as PHP. Related to CVE-2006-7109, impacts include RCE, XSS (via JS files), or resource exhaustion.

## Requirements

1. Access to IMCE interface via authenticated session
2. Malicious file prepared (e.g., PHP shell: <?php system($_GET['cmd']); ?> saved as shell.php)
3. Ability to rename files or use browser dev tools to manipulate uploads

## Defense

Defensive measures and detection strategies:

- Enforce strict MIME type and content validation on uploads
- Store uploads outside web root or with no-execute permissions
- Scan uploaded files with antivirus and monitor for anomalous extensions
- Patch Drupal IMCE module to address CVE-2006-7109

## Objectives

1. Upload arbitrary executable file
2. Bypass extension and type restrictions
3. Achieve server-side code execution or client-side injection

## Instructions

### Step 1: Prepare Malicious File

**Context**: Create or select a PHP file with shell code to upload.

No specific command; Use a text editor to create shell.php with content like <?php echo shell_exec($_GET['cmd']); ?>.

> Save the file locally for upload.

### Step 2: Bypass and Upload

**Context**: In IMCE, submit the file with appended allowed extension to evade checks.

No specific command; Rename to shell.php.gif or use browser tools to alter the filename during upload in the IMCE interface at https://forum.acronis.com/imce?.... Select and upload the file.

> IMCE accepts the file as a .gif, stores it (e.g., in /sites/default/files/imce/...), and allows insertion into signature.

### Step 3: Verify Upload

**Context**: Confirm the file is uploaded and test for execution.

No specific command; After insertion, save profile and access the uploaded file URL directly (e.g., append ?cmd=whoami to test RCE).

> If successful, server executes PHP, returning output like system info.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[bypass]]
- [[rce]]
