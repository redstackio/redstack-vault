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
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
updated_at: '2025-12-14T05:32:10.190Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Access-and-Execute-Uploaded-PHP-File

## Summary

This procedure accesses the URL of the previously uploaded PHP file to trigger server-side execution, achieving remote code execution and demonstrating server compromise through output of sensitive configuration data.

## Description

Once a malicious PHP file is uploaded to the vulnerable directory on apps.owncloud.com, directly accessing its URL causes the web server to interpret and execute it as PHP code. This results in RCE, allowing attackers to run arbitrary commands, read databases, or exfiltrate data. The initial test uses phpinfo() to verify execution without causing further damage.

## Requirements

1. Successful completion of the upload procedure
2. Knowledge of the uploaded file's path (e.g., CONTENT/content-pre1/)
3. Web browser to access the direct URL

## Defense

Defensive measures and detection strategies:

- Disable PHP execution in upload directories using .htaccess rules (e.g., RemoveHandler .php)
- Implement web application firewalls (WAF) to block direct access to uploaded files
- Log and alert on HTTP requests to .php files in user-upload directories
- Use content security policies (CSP) and sandboxing for served files

## Objectives

1. Trigger execution of uploaded code on the server
2. Observe output to confirm RCE capability
3. Identify potential for further exploitation like database access

## Instructions

### Step 1: Construct Access URL

**Context**: Build the direct link to the uploaded file based on the known directory structure.

Use the format: https://apps.owncloud.com/CONTENT/content-pre1/[filename], where [filename] is "171172-1.php5".

### Step 2: Access the URL

**Context**: Load the URL in a browser to execute the PHP code server-side.

Open https://apps.owncloud.com/CONTENT/content-pre1/171172-1.php5 in a web browser.

> Expected output: Detailed PHP configuration page from phpinfo(), indicating successful execution and server compromise.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Python]] PHP

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[php-execution]]
