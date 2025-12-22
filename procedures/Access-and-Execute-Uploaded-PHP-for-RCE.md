---
tags:
  - rce
  - webshell
  - php-execution
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
  - '[[Web Shell]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 08a23238-1ca0-404d-9446-32b079dc265a
created_at: '2025-12-14T17:23:36.799Z'
updated_at: '2025-12-14T17:23:36.799Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Web Shell]]'
---
# Access-and-Execute-Uploaded-PHP-for-RCE

## Summary

This procedure accesses the predicted temporary location of an uploaded malicious PHP file in ExpressionEngine and executes it via direct web request, achieving remote code execution if the system folder is web-accessible.

## Description

After upload and prediction, the attacker crafts a URL to the temp file path. If not following best practices (e.g., system folder in web root), the PHP executes on access, allowing command injection via parameters. This leads to server compromise, such as running system commands, file reads, or persistence. Requires web accessibility; outcomes include arbitrary code run on the server.

## Requirements

1. Predicted full path to the uploaded PHP file
2. Web-accessible temporary/system directory
3. Malicious PHP with parameter-based execution (e.g., GET cmd)

## Defense

Defensive measures and detection strategies:

- Move system and temp folders above web root
- Disable PHP execution in upload/temp directories via .htaccess
- Implement runtime application self-protection (RASP) for anomalous code
- Monitor HTTP requests to temp paths and log executions

## Objectives

1. Trigger execution of the uploaded PHP code
2. Inject and run arbitrary system commands
3. Confirm server compromise via output or side effects

## Instructions

### Step 1: Construct Access URL

**Context**: Build the direct web path to the file using the predicted location.

Combine base URL with path: e.g., http://target.com/system/expressionengine/cache/tmp_1696152000/shell.php

### Step 2: Initiate Execution

**Context**: Visit the URL with parameters to run code.

Use browser or tool to GET the URL with query: http://target.com/.../shell.php?cmd=whoami

If successful, PHP processes and executes system('whoami').

### Step 3: Verify RCE

**Context**: Check response for command output.

Look for server username or error; escalate with commands like id, ls, or cat sensitive files.

**Expected Output**: HTTP response body containing command results, e.g., 'www-data' from whoami.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Web Shell]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Execution]]
- [[webshell]]
- [[rce]]
