---
id: proc-upload-image-wordpress
tags:
  - wordpress
  - upload
  - attachment
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:56.528Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Image-Attachment-in-WordPress

## Summary

This procedure uploads a benign image file to WordPress via the media library, creating an attachment post that can be later manipulated for vulnerability exploitation, such as path traversal in metadata handling.

## Description

In the context of exploiting WordPress core vulnerabilities, uploading an image establishes a foothold by generating a post ID and initial metadata in the wp_posts and wp_postmeta tables. This attachment serves as the entry point for editing unsanitized fields like 'thumb' in _wp_attachment_metadata. The procedure requires authenticated access and targets standard WordPress media upload functionality, expecting the file to be processed and stored in the uploads directory.

## Requirements

1. Authenticated WordPress session with upload permissions (e.g., admin or editor role)
2. Access to wp-admin media library
3. A valid image file (e.g., test.jpg) for upload

## Defense

Defensive measures and detection strategies:

- Restrict media upload roles to trusted users via capability checks
- Monitor database inserts into wp_postmeta for unusual attachment metadata
- Enable WordPress file upload validation plugins to scan for malicious files

## Objectives

1. Create a new attachment post with a retrievable ID
2. Store initial metadata for subsequent editing
3. Prepare vector for path traversal injection

## Instructions

### Step 1: Access Media Library

**Context**: Log in to the WordPress admin dashboard to reach the upload interface.

Navigate to wp-admin/upload.php and click 'Add New' to open the media uploader.

### Step 2: Upload Image File

**Context**: Select and upload a test image to generate the attachment.

Drag or select a JPG/PNG file and click 'Upload'. Note the generated post ID from the success message or Media Library URL (e.g., post=123).

**Expected Output**: Image thumbnail displayed in library with attachment details.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- wordpress
- upload
- attachment
