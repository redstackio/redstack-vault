---
tags:
  - rce
  - execution
  - php
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-access-php-file]]'
platforms:
  - Web
  - PHP
techniques:
  - '[[Python]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: cf1fa233-798a-46b6-8b68-e33afa73fe13
created_at: '2025-12-14T05:32:13.229Z'
updated_at: '2025-12-14T05:32:13.229Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Execute-Uploaded-PHP-for-RCE

## Summary

This procedure triggers the execution of the uploaded malicious PHP file in ExpressionEngine to perform remote command execution, compromising the server.

## Description

Once uploaded, the PHP file is served by the web server and executed upon access. The payload interprets commands passed via GET parameters, injecting and running arbitrary code. This exploits the lack of execution restrictions on uploaded files, leading to full server control.

## Requirements

1. Successful upload of PHP payload with known URL
2. Web access to the file path (e.g., /images/uploads/shell.php)
3. Target commands to execute (e.g., reconnaissance or persistence)

## Defense

Defensive measures and detection strategies:

- Disable PHP execution in upload directories via .htaccess
- Scan uploads with antivirus and monitor file access logs
- Implement runtime application self-protection (RASP)

## Objectives

1. Invoke the PHP code to run system commands
2. Verify RCE with output
3. Escalate to further compromise

## Instructions

### Step 1: Locate File URL

**Context**: Identify the web-accessible path of the uploaded file from upload response.

Typically /system/expressionengine/images/uploads/shell.php or similar.

> Confirm via browser without parameters first.

### Step 2: Execute Command

**Context**: Access the file with a command parameter to trigger RCE.

**Command** ([[commands/curl-access-php-file]]):
```bash
curl "https://target.com/images/uploads/shell.php?cmd=id"
```

> Expected output: uid=33(www-data) gid=33(www-data) or similar, confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-php-file]]

## Tools Used


## Tags

- [[rce]]
- [[php]]
- [[Execution]]
