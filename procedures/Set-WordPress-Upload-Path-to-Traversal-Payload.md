---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - wordpress
  - path-traversal
type: procedure
tactics:
  - '[[Initial Access]]'
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
updated_at: '2025-12-14T17:30:47.352Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Set-WordPress-Upload-Path-to-Traversal-Payload

## Summary

This procedure configures the WordPress 'upload_path' option to a path traversal payload, setting the stage for permission escalation by causing wp_mkdir_p() to reference a writable external directory like /var/tmp.

## Description

In WordPress, the 'upload_path' option controls where media files are stored and is configurable by administrators via wp-admin/options.php. By setting it to a crafted string with multiple '../' traversals, such as '../../../../../../../var/tmp/content/../../../../../../home/simon/html/wordpress/../../../../../../var/tmp/content', the _wp_upload_dir() function returns a path that leads wp_mkdir_p() to identify /var/tmp as the writable parent. This inherits 777 permissions without initial validation, enabling downstream exploits in hardened environments.

## Requirements

1. Administrator access to WordPress
2. Access to wp-admin/options.php
3. Knowledge of the server's file structure (e.g., web root at /home/simon/html/wordpress/)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize upload_path inputs in plugins or custom code
- Monitor admin option changes via audit logs
- Restrict admin access and use role-based permissions

## Objectives

1. Prepare path for traversal-based permission inheritance
2. Bypass initial path checks in upload handling
3. Enable writable access to protected directories

## Instructions

### Step 1: Access Admin Options

**Context**: Log in to the WordPress dashboard as an admin to reach the options configuration.

Navigate to wp-admin/options.php in your browser.

### Step 2: Update Upload Path

**Context**: Set the upload_path to the traversal payload to trick directory creation functions.

Locate the 'upload_path' field and enter: '../../../../../../../var/tmp/content/../../../../../../home/simon/html/wordpress/../../../../../../var/tmp/content'. Click 'Save Changes'.

> This updates the option in the wp_options table. Verify by calling get_option('upload_path') in a test plugin or via database query.

### Step 3: Verify Configuration

**Context**: Confirm the path is set correctly before proceeding.

Attempt a test upload or inspect the returned path from _wp_upload_dir() to ensure it traverses to /var/tmp.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- wordpress
- path-traversal
