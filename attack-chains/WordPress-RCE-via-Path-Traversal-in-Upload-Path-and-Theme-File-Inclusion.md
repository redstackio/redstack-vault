---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - wordpress
  - rce
  - path-traversal
  - file-upload
  - lfi
  - php
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Set-WordPress-Upload-Path-to-Traversal-Payload]]'
  - '[[procedures/Trigger-WordPress-wp-mkdir-p-for-Permission-Escalation]]'
  - '[[procedures/Set-WordPress-Upload-Path-to-Theme-Directory]]'
  - '[[procedures/Upload-Malicious-PHP-Shell-to-WordPress-Theme]]'
  - '[[procedures/Execute-PHP-Shell-via-WordPress-Post-Meta-Inclusion]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:30:47.354Z'
description: >-
  Multi-stage attack exploiting path traversal in WordPress upload_path to
  escalate permissions, upload a PHP shell to the theme directory, and execute
  it via post meta inclusion for remote code execution.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
  - '[[Remote File Copy]]'
---
# WordPress RCE via Path Traversal in Upload Path and Theme File Inclusion

Multi-stage attack chain demonstrating a complete attack workflow exploiting WordPress's wp_mkdir_p() function to bypass file permissions and achieve remote code execution (RCE).

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Set Traversal Upload Path] --> B[Trigger Permission Escalation]
    B --> C[Redirect Upload to Theme]
    C --> D[Upload PHP Shell]
    D --> E[Execute via Post Meta]
    E --> F[RCE Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for admin access
- No external tools required

### Target Environment

- WordPress installation on Linux with PHP
- Admin privileges on the WordPress site
- Services: Web server (e.g., Apache/Nginx) on port 80/443
- Non-writable theme directories hardened with file permissions

### Initial Access Requirements

- Valid administrator credentials for WordPress
- Direct network access to the WordPress admin panel
- No prior shell access needed

## Detailed Attack Procedures

### Step 1: Set Traversal Upload Path
procedure: [[procedures/Set-WordPress-Upload-Path-to-Traversal-Payload]]

**Objective**: Configure the upload_path option to a crafted path traversal string that tricks wp_mkdir_p() into identifying a writable parent directory.

**Instructions**: Log in as an administrator and navigate to the WordPress admin panel. Access the options page and update the upload_path setting to a traversal payload like '../../../../../../../var/tmp/content/../../../../../../home/simon/html/wordpress/../../../../../../var/tmp/content'. This sets up the path for the subsequent permission escalation.

**Expected Output**: The upload_path option is updated successfully, visible in the database via get_option('upload_path').

**Success Indicators**:
- Option saved without errors
- _wp_upload_dir() returns the traversed path when tested

### Step 2: Trigger Permission Escalation
procedure: [[procedures/Trigger-WordPress-wp-mkdir-p-for-Permission-Escalation]]

**Objective**: Invoke wp_mkdir_p() during a media upload to propagate 777 permissions from a writable directory (/var/tmp) to the web root and intermediate paths, making protected directories writable.

**Instructions**: With the traversal upload_path set, attempt to upload any media file through the WordPress media uploader. This calls wp_upload_dir() followed by wp_mkdir_p($target), which iterates dirname() to find /var/tmp as the writable parent, copies its 0777 permissions, and applies chmod to each path segment, including the web root (e.g., chmod('../../../../../../../var/tmp/content/../../../../../../home/simon/html/wordpress/', 0777)).

**Expected Output**: Upload attempt may fail or partially succeed, but file system permissions on the web directory are now 777, verifiable via server access or error logs.

**Success Indicators**:
- Web root and theme directories become writable
- No permission denied errors on subsequent file operations

### Step 3: Redirect Upload to Theme
procedure: [[procedures/Set-WordPress-Upload-Path-to-Theme-Directory]]

**Objective**: Update the upload_path to point directly to the now-writable theme directory, enabling uploads to sensitive locations.

**Instructions**: Return to wp-admin/options.php and change the upload_path option to the theme directory path, such as 'wp-content/themes/current-theme/'. Save the changes.

**Expected Output**: upload_path updated to the theme directory, confirmed by querying get_option('upload_path').

**Success Indicators**:
- Option saved successfully
- Media uploader now targets the theme directory

### Step 4: Upload PHP Shell
procedure: [[procedures/Upload-Malicious-PHP-Shell-to-WordPress-Theme]]

**Objective**: Upload a malicious PHP file disguised as a text file to the theme directory, leveraging the modified upload_path.

**Instructions**: Use the WordPress media uploader to upload a file named 'shell.txt' containing PHP code like '<?php phpinfo(); ?>' or a full shell. Due to the upload_path, it places the file in wp-content/themes/current-theme/shell.txt.

**Expected Output**: File uploaded successfully to the theme directory, visible in the file system.

**Success Indicators**:
- File appears in theme directory
- No upload errors due to permissions

### Step 5: Execute via Post Meta
procedure: [[procedures/Execute-PHP-Shell-via-WordPress-Post-Meta-Inclusion]]

**Objective**: Include and execute the uploaded PHP shell by setting the _wp_page_template post meta to its path, triggering RCE during post rendering.

**Instructions**: Edit a post or page in WordPress and set the custom field '_wp_page_template' to the full path of the shell, e.g., '/wp-content/themes/current-theme/shell.txt'. Save and view the post to trigger the inclusion.

**Expected Output**: The PHP code executes, displaying output like phpinfo() or shell functionality when the post is loaded.

**Success Indicators**:
- Arbitrary PHP code runs on the server
- Web server user context for execution confirmed

## Attack Chain Summary

### Key Achievements

1. Bypassed file permission hardening using path traversal in wp_mkdir_p()
2. Uploaded executable PHP to a protected theme directory
3. Achieved RCE via arbitrary file inclusion in post meta, defeating safe mode and disabled edits

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]
- [[Remote File Copy]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T12:00:00Z*
