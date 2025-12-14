---
id: ac-nextcloud-fpd-htaccess
tags:
  - nextcloud
  - path-disclosure
  - information-leak
  - file-upload
  - debug-mode
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Upload-htaccess-File-to-Nextcloud]]'
  - '[[procedures/Trigger-Path-Disclosure-Exception]]'
step_count: 2
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:06.578Z'
description: >-
  A two-step attack exploiting Nextcloud's file upload feature to upload a
  .htaccess file, triggering an exception in debug mode that discloses sensitive
  server file and folder paths.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Nextcloud Full Path Disclosure via .htaccess Upload

Multi-stage attack chain demonstrating how to exploit a file upload vulnerability in Nextcloud to achieve full path disclosure of sensitive server directories when the application is running in debug mode.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Upload .htaccess File] --> B[Trigger Exception]
    B --> C[Path Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or [[tools/curl]]

### Target Environment

- Nextcloud instance running on PHP with Apache web server
- Application must be in debug mode (config setting 'debug' => true)
- Access to the file upload feature (authenticated or public upload enabled)

### Initial Access Requirements

- Valid user credentials for Nextcloud login (if authentication is required)
- Network access to the Nextcloud web interface
- No prior access needed beyond standard user permissions

## Detailed Attack Procedures

### Step 1: Upload .htaccess File
procedure: [[procedures/Upload-htaccess-File-to-Nextcloud]]

**Objective**: Upload a specially crafted .htaccess file to Nextcloud's file system to prepare for exception triggering.

**Instructions**: Log in to the Nextcloud web interface and navigate to the file upload section. Create a simple .htaccess file with content that forces an Apache rewrite or directive error, such as:

```apache
RewriteEngine On
RewriteRule ^(.*)$ /nonexistent [L]
```

Upload the file using the web interface or via curl if API access is available:

```bash
curl -X PUT -u username:password 'https://nextcloud.example.com/remote.php/dav/files/username/test.htaccess' --data-binary '@.htaccess'
```

**Expected Output**: Successful upload confirmation in the Nextcloud UI or HTTP 201 Created response from curl.

**Success Indicators**:
- File appears in the Nextcloud file list
- No immediate errors during upload

### Step 2: Trigger Path Disclosure
procedure: [[procedures/Trigger-Path-Disclosure-Exception]]

**Objective**: Access the uploaded .htaccess file to provoke an exception that leaks full server paths in debug mode.

**Instructions**: Navigate to the URL of the uploaded .htaccess file in the browser, e.g., https://nextcloud.example.com/remote.php/dav/files/username/test.htaccess. The Apache server will attempt to process the .htaccess directives, leading to an exception if incompatible. In debug mode, Nextcloud's error handler will output stack traces including absolute file paths like /var/www/nextcloud/lib/private/...

If using curl to simulate access:

```bash
curl -I 'https://nextcloud.example.com/remote.php/dav/files/username/test.htaccess'
```

**Expected Output**: HTTP response body containing error details with full paths, e.g., "Fatal error: ... in /full/server/path/to/file.php on line X".

**Success Indicators**:
- Error message reveals server paths (e.g., /var/www/...)
- Paths include sensitive directories like config or data folders

## Attack Chain Summary

### Key Achievements

1. Successful upload of .htaccess without restrictions
2. Triggered exception exposing internal file structure
3. Gained reconnaissance on server layout for potential further attacks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]] File and Directory Discovery
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
