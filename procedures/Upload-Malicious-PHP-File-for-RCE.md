---
id: proc-uuid-1
tags:
  - unrestricted-file-upload
  - rce
  - php
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:10.192Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-PHP-File-for-RCE

## Summary

This procedure exploits the lack of file type validation in the upload feature of apps.owncloud.com to upload a malicious PHP file, setting the stage for remote code execution by allowing server-side interpretation of the uploaded content.

## Description

In the context of ownCloud's app marketplace, the file upload functionality does not restrict or sanitize file types, permitting PHP files to be uploaded to the CONTENT/content-pre1/ directory where they are served and executed by the PHP interpreter. This leads to full server compromise, including access to databases and arbitrary code execution. The procedure involves creating and uploading a simple PHP payload like phpinfo() to test execution feasibility.

## Requirements

1. Access to a web browser or HTTP client to interact with https://apps.owncloud.com
2. No authentication required; public upload endpoint
3. Basic knowledge of PHP syntax for payload creation

## Defense

Defensive measures and detection strategies:

- Implement strict file type whitelisting (e.g., only allow images or archives) and MIME type validation
- Scan uploads for executable code using tools like ClamAV or custom regex for PHP tags
- Serve uploaded files from a non-executable directory or with noexec mount options
- Monitor server logs for suspicious PHP executions in upload directories

## Objectives

1. Bypass upload restrictions to place executable code on the server
2. Confirm upload success and file placement
3. Prepare for subsequent RCE exploitation

## Instructions

### Step 1: Create Malicious PHP Payload

**Context**: Prepare a simple PHP file that executes to reveal server information, confirming the vulnerability.

Create a file named "171172-1.php5" with the following content:

```php
<?php phpinfo(); ?>
```

> This payload uses the built-in phpinfo() function to output PHP configuration, which will be executed if the file is interpreted as PHP.

### Step 2: Upload the File

**Context**: Use the web interface to upload the file without triggering any validation errors.

Navigate to the file upload section on https://apps.owncloud.com and select the prepared PHP file for upload.

> Expected output: Upload success message; the file is stored in CONTENT/content-pre1/ without rejection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[unrestricted-file-upload]]
- [[rce]]
- [[php]]
