---
id: proc-uuid-2
tags:
  - nextcloud
  - file-creation
  - sharing
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:28:58.703Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Create-and-Share-Protected-Folder

## Summary

This procedure creates a nested folder structure with image and text files as an admin user via WebDAV, ensuring they are automatically tagged as 'Secret', then shares the folder with an unprivileged user without edit permissions to test access controls.

## Description

Using the admin account, access Nextcloud via WebDAV to create 'Secret_Folder' containing 'Secret_Subfolder', and inside it, add 'Secret_Picture.jpeg' (image) and 'Secret_Text.txt' (text file). Files are tagged due to group rules. Share the folder with user 'user' (no edit rights). This sets up the protected assets for bypass testing. Direct access should be denied, but thumbnails and searches will bypass.

## Requirements

1. Admin credentials for WebDAV access
2. Unprivileged user 'user' created
3. Configured tagging and access rules from prior setup
4. WebDAV enabled on Nextcloud

## Defense

Defensive measures and detection strategies:

- Limit sharing to specific files instead of recursive folders
- Audit share logs for admin-to-unprivileged shares
- Enforce edit rights or viewer-only with stricter API checks
- Monitor file creation events for tagging accuracy

## Objectives

1. Populate protected files that trigger access rules
2. Share with unprivileged user to simulate insider threat
3. Verify direct access denial before bypass

## Instructions

### Step 1: Create Unprivileged User

**Context**: Create a new user without admin privileges.

No command; use Nextcloud admin web interface.

> User 'user' created. Expected output: User can log in but lacks admin tools.

### Step 2: Create Files via WebDAV

**Context**: As admin, use WebDAV to create folder structure and files, avoiding auto-preview generation.

Use curl or WebDAV client to MKCOL for folders and PUT for files.

> Example: curl -u admin -X MKCOL https://example.com/remote.php/dav/files/admin/Secret_Folder/

Expected output: Folders and files exist, tagged as 'Secret'.

### Step 3: Share Folder

**Context**: Share 'Secret_Folder' with 'user' without edit rights.

No command; use Nextcloud sharing interface.

> Share created. Expected output: 'user' sees folder but cannot access tagged files directly.

### Step 4: Verify Access Denial

**Context**: Test that 'user' cannot view files directly.

Attempt PROPFIND or GET as 'user'.

> Access denied errors. Expected output: 403 Forbidden for file contents.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- nextcloud
- file-creation
- sharing
