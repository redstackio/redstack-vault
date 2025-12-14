---
id: p2b3c4d5-e6f7-8901-bcde-f2345678901
tags:
  - wordpress
  - path-traversal
  - permissions
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:30:47.350Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Trigger-WordPress-wp-mkdir-p-for-Permission-Escalation

## Summary

This procedure triggers the wp_mkdir_p() function during a media upload to exploit path traversal, propagating 777 permissions from a writable parent directory to the web root and intermediates, bypassing hardening.

## Description

The wp_mkdir_p() function in WordPress creates directories recursively but lacks sanitization for traversed paths. When invoked via a media upload with a traversal upload_path, it uses dirname() iteratively to find a writable parent (e.g., /var/tmp with 0777), copies those permissions, and if umask differs, explodes the target path and applies chmod(0777) to each segment relative to the parent. This can make the entire web root writable, even if initially non-writable.

## Requirements

1. Traversal upload_path already set
2. Admin access to media uploader
3. Writable /var/tmp or similar on the server

## Defense

Defensive measures and detection strategies:

- Patch WordPress to validate paths in wp_mkdir_p()
- Monitor chmod calls and permission changes via file integrity monitoring (e.g., Tripwire)
- Disable direct admin uploads or use hardened hosting

## Objectives

1. Escalate directory permissions to 777
2. Make theme and web directories writable
3. Overcome safe mode and permission restrictions

## Instructions

### Step 1: Initiate Media Upload

**Context**: Use the media uploader to invoke the directory creation chain.

Go to wp-admin/media-new.php and select a test image file to upload.

### Step 2: Trigger wp_mkdir_p

**Context**: The upload calls wp_upload_dir() then wp_mkdir_p($target), applying traversals.

Proceed with the upload. The function will set $target_parent to '/var/tmp/' and chmod segments like '../../../../../../../var/tmp/content/../../../../../../home/simon/html/wordpress/' to 0777.

> Upload may fail, but permissions change. Check server logs for chmod operations.

### Step 3: Validate Permissions

**Context**: Confirm writability post-trigger.

Attempt to create a test file in the web root or theme directory to verify 777 permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- wordpress
- path-traversal
- permissions
