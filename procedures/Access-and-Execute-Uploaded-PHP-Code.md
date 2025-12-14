---
id: proc-uuid-2
tags:
  - rce
  - php-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:25.020Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Unix Shell]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Access-and-Execute-Uploaded-PHP-Code

## Summary

This procedure triggers the execution of an uploaded PHP file on the server by accessing its direct URL, achieving remote code execution and demonstrating server-side code interpretation.

## Description

Following the upload of a malicious PHP file to apps.owncloud.com, directly accessing the file's URL causes the web server to process it as PHP, executing the embedded code. For example, a phpinfo() payload reveals sensitive server configuration, confirming RCE. This can escalate to arbitrary command execution, data exfiltration, or persistence. The target environment is a PHP-enabled web server without proper file handling restrictions.

## Requirements

1. Knowledge of the uploaded file's URL (e.g., from upload response).
2. Web browser to request the resource.
3. The file must be stored in a web-accessible, PHP-executable directory.

## Defense

Defensive measures and detection strategies:

- Disable PHP execution in upload directories via .htaccess or server config.
- Log and alert on direct access to uploaded files.
- Use WAF rules to block execution of user-uploaded content.
- Regularly scan web directories for anomalous files.

## Objectives

1. Execute the uploaded PHP code server-side.
2. Observe output to confirm RCE (e.g., server info disclosure).
3. Validate potential for further exploitation like command injection.

## Instructions

### Step 1: Identify File URL

**Context**: Obtain the direct path to the uploaded file from the upload confirmation.

The URL will resemble https://apps.owncloud.com/CONTENT/content-pre1/171172-1.php5.

> Ensure the extension (.php5) triggers PHP processing.

### Step 2: Access URL to Trigger Execution

**Context**: Request the file via browser to force server-side execution.

Open the URL in a web browser. The server interprets the .php5 file as PHP and runs the code.

> Successful execution displays phpinfo() output, including PHP version, extensions, and environment variables, proving RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques

- [[Unix Shell]] PowerShell (adapted to PHP context)

## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[php-execution]]
