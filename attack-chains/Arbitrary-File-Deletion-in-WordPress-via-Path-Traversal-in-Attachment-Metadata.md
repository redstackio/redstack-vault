---
id: ac-wordpress-file-deletion-path-traversal
tags:
  - wordpress
  - path-traversal
  - file-deletion
  - rce
  - information-disclosure
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
  - PHP
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Upload-Image-Attachment-in-WordPress]]'
  - '[[procedures/Inject-Path-Traversal-Payload-into-Attachment-Metadata]]'
  - '[[procedures/Trigger-Arbitrary-File-Deletion-by-Deleting-Attachment]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data Destruction]]'
updated_at: '2025-12-14T17:24:56.531Z'
description: >-
  Multi-stage attack exploiting a path traversal vulnerability in WordPress core
  to achieve arbitrary file deletion, enabling remote code execution or
  information disclosure.
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data Destruction]]'
---
# Arbitrary File Deletion in WordPress via Path Traversal in Attachment Metadata

Multi-stage attack chain demonstrating exploitation of an arbitrary file deletion vulnerability in WordPress core through unsanitized user input in the 'thumb' metadata field of attachments. An authenticated user with media editing permissions can upload an image, inject a path traversal payload into its thumbnail metadata, and delete the attachment to remove any server file, such as wp-config.php for RCE or .htaccess for directory listing exposure.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Upload Attachment] --> B[Inject Payload]
    B --> C[Delete to Exploit]
    C --> D[File Deletion Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- WordPress installation (core vulnerability in versions prior to patch)
- PHP web server with MySQL database
- Authenticated access to WordPress admin with media upload/edit permissions

### Initial Access Requirements

- Valid WordPress admin or contributor credentials
- Direct network access to the WordPress site (e.g., http://target.com/wp-admin)
- No prior access beyond authentication needed

## Detailed Attack Procedures

### Step 1: Upload Image Attachment
procedure: [[procedures/Upload-Image-Attachment-in-WordPress]]

**Objective**: Create a new attachment post in WordPress to serve as the vector for metadata manipulation.

**Instructions**: Log in to the WordPress admin dashboard and use the media uploader to add a benign image file, such as a JPG. This generates an attachment ID stored in the posts table with initial metadata in postmeta.

**Expected Output**: Successful upload confirmation, with the image visible in the Media Library and an associated post ID (e.g., 123).

**Success Indicators**:
- Image appears in Media Library
- Post ID retrievable from URL or database query

### Step 2: Inject Path Traversal Payload
procedure: [[procedures/Inject-Path-Traversal-Payload-into-Attachment-Metadata]]

**Objective**: Update the attachment's thumbnail metadata with a path traversal string to target a sensitive file like wp-config.php.

**Instructions**: Access the edit form for the attachment via wp-admin/post.php, extract the post ID and nonce, then use [[commands/curl-update-wordpress-attachment-metadata]] to submit the malicious 'thumb' value:

```bash
curl 'http://target.com/wp-admin/post.php?post=123&action=editattachment&_wpnonce=abc123' -H 'User-Agent: Mozilla/5.0' -H 'Cookie: wordpress_logged_in=valid_session' -d 'thumb=../../../../wp-config.php' --compressed
```

Verify the update by checking the database (_wp_attachment_metadata) or re-editing the attachment.

**Expected Output**: HTTP 200 or redirect to edit page, with metadata updated in the database without sanitization.

**Success Indicators**:
- No errors in response
- 'thumb' field in database reflects the payload (e.g., '../../../../wp-config.php')

### Step 3: Trigger Arbitrary File Deletion
procedure: [[procedures/Trigger-Arbitrary-File-Deletion-by-Deleting-Attachment]]

**Objective**: Delete the attachment to invoke wp_delete_attachment, which uses the tainted metadata to construct and unlink the target file path.

**Instructions**: From the WordPress admin Media Library or post edit screen, select and delete the uploaded attachment. This triggers the wp_delete_attachment function, applying str_replace on the file path with the malicious 'thumb' value, joining it to the upload directory, and executing unlink on the traversed path.

**Expected Output**: Attachment deletion success message; target file (e.g., wp-config.php) removed from server filesystem.

**Success Indicators**:
- Attachment disappears from Media Library
- Target file no longer exists (e.g., 404 on wp-config.php access or forced WordPress setup screen)

## Attack Chain Summary

### Key Achievements

1. Bypassed input validation in attachment metadata to store arbitrary paths
2. Achieved arbitrary file deletion outside uploads directory
3. Enabled follow-on impacts like RCE via wp-config.php deletion or info disclosure via .htaccess removal

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Data Destruction]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T00:00:00Z*
