---
id: proc-trigger-file-deletion-attachment
tags:
  - file-deletion
  - wordpress
  - path-traversal
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data Destruction]]'
updated_at: '2025-12-14T17:24:56.522Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data Destruction]]'
---
# Trigger-Arbitrary-File-Deletion-by-Deleting-Attachment

## Summary

This procedure finalizes the exploitation by deleting the tainted attachment, invoking WordPress core functions that use the injected path traversal metadata to delete arbitrary server files, such as critical configuration files.

## Description

Upon deletion via the admin interface, wp_delete_attachment in wp-includes/post.php retrieves the metadata, constructs $thumbfile via str_replace(basename($file), $meta['thumb'], $file), joins it to the upload path, and applies @unlink without boundary checks. This deletes files like wp-config.php (forcing RCE via setup with attacker DB) or .htaccess (enabling directory browsing). The @ suppresses errors, and metadata is cleaned post-deletion, reducing detectability. Requires the prior metadata injection.

## Requirements

1. Attachment with injected traversal payload
2. Authenticated access to delete media
3. Target file path adjusted in payload (e.g., '../../../../wp-config.php')

## Defense

Defensive measures and detection strategies:

- Validate file paths in wp_delete_attachment against uploads dir using realpath or basename checks
- Monitor unlink calls via filesystem auditing (e.g., auditd on Linux)
- Alert on deletion of attachments with non-standard metadata

## Objectives

1. Execute deletion to trigger tainted path unlink
2. Remove critical files for impact (RCE/info disclosure)
3. Confirm exploitation success via site behavior change

## Instructions

### Step 1: Access Attachment in Media Library

**Context**: Locate the uploaded attachment for deletion.

Log in to wp-admin/upload.php, find the image by title or ID.

### Step 2: Delete the Attachment

**Context**: Trigger the wp_delete_attachment function.

Select the attachment and click 'Delete Permanently'. This processes the metadata, constructs the malicious path, and unlinks the target file.

**Expected Output**: Success message like '1 item permanently deleted'; no PHP errors due to suppression.

### Step 3: Validate File Deletion

**Context**: Check impacts to confirm success.

Access the site root; if wp-config.php deleted, expect WordPress setup screen. For .htaccess, browse /wp-content/uploads/ for exposed listings.

**Expected Output**: Target file missing (e.g., 404 or setup prompt).

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Data Destruction]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- file-deletion
- wordpress
- path-traversal
