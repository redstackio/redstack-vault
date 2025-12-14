---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - rce-execution
  - php-execution
  - file-retrieval
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Python]]'
updated_at: '2025-12-14T05:32:10.294Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Python]]'
---
# Retrieve-and-Execute-Uploaded-File

## Summary

This procedure involves inspecting the page source after upload to extract the direct path to the malicious PHP file and accessing it via the browser to execute the code, confirming remote code execution on the server.

## Description

Post-upload, the website embeds the full path to the uploaded file in the HTML source (e.g., in an <img> src attribute). By viewing the source, attackers can copy this path and navigate to it directly, causing the PHP web server to interpret and execute the file. For example, accessing https://careers.mtn.cm/en/user/images/users/-13-04-2021-20-15-16-payload.php?cmd=whoami would run system commands, demonstrating full RCE capabilities.

## Requirements

1. Successful upload from prior procedure
2. Web browser with developer tools for source inspection
3. Knowledge of the uploaded file's payload

## Defense

Defensive measures and detection strategies:

- Avoid exposing full file paths in client-side HTML; use relative paths or proxies
- Disable direct execution of uploaded files by configuring server MIME handling or .htaccess rules
- Log and alert on direct access to upload directories, especially non-image files

## Objectives

1. Locate the exact URL path of the uploaded executable
2. Trigger server-side execution of the PHP code
3. Validate RCE by observing payload output

## Instructions

### Step 1: Inspect Page Source

**Context**: After upload, examine the HTML to find the embedded file path.

Right-click on the page and select 'View Page Source' or use F12 developer tools. Search for the uploaded filename or image src attributes to locate the full path (e.g., /en/user/images/users/-13-04-2021-20-15-16-payload.php).

### Step 2: Copy the Full URL

**Context**: Construct the complete accessible URL using the base domain.

Prepend the domain: https://careers.mtn.cm + extracted path.

### Step 3: Access and Execute

**Context**: Navigate to the URL to invoke PHP execution.

Paste the URL into the browser address bar and load. Append query parameters if needed (e.g., ?cmd=id) to test commands. Observe output like PHP execution results or command echoes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Python]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce-execution]]
- [[php-execution]]
- [[file-retrieval]]
