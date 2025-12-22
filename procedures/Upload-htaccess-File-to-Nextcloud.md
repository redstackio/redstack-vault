---
id: proc-upload-htaccess-nextcloud
tags:
  - file-upload
  - nextcloud
  - htaccess
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-upload-file]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:06.569Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-htaccess-File-to-Nextcloud

## Summary

This procedure demonstrates uploading a .htaccess file to a Nextcloud instance using its web interface or WebDAV API, exploiting lax file type restrictions to place Apache configuration files in user directories.

## Description

In vulnerable Nextcloud setups, the file upload feature allows .htaccess files without sanitization, enabling attackers to influence Apache's behavior for the directory. This step sets up the condition for path disclosure by placing the file where it can be processed during access attempts. The attack targets environments with debug mode enabled, where exceptions reveal stack traces with absolute paths. Prerequisites include access to the upload functionality, typically requiring user authentication.

## Requirements

1. Access to Nextcloud web interface or WebDAV endpoint
2. Valid credentials if authentication is enforced
3. .htaccess file prepared with directives that may cause processing errors (e.g., invalid rewrites)
4. Target in debug mode for full disclosure impact

## Defense

Defensive measures and detection strategies:

- Disable debug mode in production (set 'debug' => false in config/config.php)
- Implement file type whitelisting to block .htaccess uploads
- Monitor upload logs for suspicious file types and audit Apache access logs for .htaccess processing errors

## Objectives

1. Place .htaccess in Nextcloud's user file space
2. Ensure the file is accessible via HTTP for triggering
3. Prepare for exception-based information leakage

## Instructions

### Step 1: Prepare .htaccess File

**Context**: Create a .htaccess file with content that Apache will attempt to parse, potentially leading to an exception.

**Command** ([[commands/echo-create-file]]):
```bash
echo -e "RewriteEngine On\nRewriteRule ^(.*)$ /nonexistent [L]" > .htaccess
```

> This command generates a basic .htaccess with a rewrite rule pointing to a nonexistent path, which can trigger errors during processing.

### Step 2: Upload via WebDAV

**Context**: Use curl to upload the file to Nextcloud's DAV endpoint, simulating the web upload.

**Command** ([[commands/curl-upload-file]]):
```bash
curl -X PUT -u username:password 'https://nextcloud.example.com/remote.php/dav/files/username/test.htaccess' --data-binary '@.htaccess' -H 'Content-Type: text/plain'
```

> Replace username/password with valid credentials. Expected output: HTTP 201 Created or 207 Multi-Status indicating successful upload. Verify in Nextcloud UI that the file is listed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/echo-create-file]]
- [[commands/curl-upload-file]]

## Tools Used

- [[tools/curl]]

## Tags

- file-upload
- nextcloud
- webdav
