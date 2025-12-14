---
tags:
  - file-upload-bypass
  - php
  - expressionengine
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - PHP
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b19a98f9-fcec-4234-9dde-03439f02ba4b
created_at: '2025-12-14T17:23:36.826Z'
updated_at: '2025-12-14T17:23:36.826Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-PHP-Upload-Restrictions-in-ExpressionEngine

## Summary

This procedure exploits inadequate file extension validation in ExpressionEngine's 'import channel field' upload functionality, allowing an authenticated administrator to upload a malicious PHP file by evading the .php block, enabling subsequent code execution if stored accessibly.

## Description

In vulnerable ExpressionEngine installations, the upload handler checks for .php extensions but lacks robust sanitization, such as MIME type verification or content inspection. Attackers with admin access can disguise the file (e.g., via double extensions or encoding) to bypass this, storing it in a temporary directory. This sets up webshell deployment or direct RCE in PHP environments where temp folders are web-exposed. Prerequisites include admin login and knowledge of the upload interface; outcomes include arbitrary file placement on the server.

## Requirements

1. Authenticated administrative access to ExpressionEngine control panel
2. Malicious PHP payload prepared (e.g., simple system command executor)
3. Access to the channel import feature without additional restrictions

## Defense

Defensive measures and detection strategies:

- Implement comprehensive file validation including MIME types and content scanning
- Store uploads outside web root and use random, non-predictable naming
- Enable web application firewall (WAF) rules to block suspicious upload patterns
- Monitor upload logs for admin-initiated file placements in temp dirs

## Objectives

1. Successfully upload executable PHP code to the server
2. Evade built-in extension checks without triggering errors
3. Position file for later access and execution

## Instructions

### Step 1: Prepare Malicious Payload

**Context**: Create a simple PHP webshell to test execution, ensuring it's small and evades basic checks.

Craft the file content:

```php
<?php if(isset($_GET['cmd'])) { system($_GET['cmd']); } ?>
```

Save as a file with a disguised extension, e.g., shell.php.txt or use null byte (%00) in filename if supported.

### Step 2: Access Upload Interface

**Context**: Log in and navigate to the vulnerable feature to initiate upload.

Log in to the ExpressionEngine admin panel at /admin.php. Go to Channels > Channel Fields > Import, and locate the file upload option for importing field definitions.

### Step 3: Submit Bypassed Upload

**Context**: Use the form to upload the disguised file, confirming bypass.

Select the prepared file in the import form and submit. If successful, no extension error occurs, and the file is processed to temp storage.

**Expected Output**: Confirmation message for successful import, with file placed in temporary directory.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[bypass]]
- [[rce-prep]]
