---
id: proc-trigger-fpd-exception
tags:
  - path-disclosure
  - exception-handling
  - debug-mode
  - information-leak
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-head-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:06.559Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Trigger-Path-Disclosure-Exception

## Summary

This procedure accesses an uploaded .htaccess file in Nextcloud to force Apache to process it, resulting in an unhandled exception that discloses full server paths when debug mode is active.

## Description

Once the .htaccess file is uploaded, requesting it via HTTP causes Apache to apply its directives. Incompatible or erroneous directives lead to a PHP exception in Nextcloud's handling code. With debug mode enabled, the error output includes detailed stack traces revealing absolute paths to application files, such as configuration directories and data stores. This provides reconnaissance value for further attacks like path traversal.

## Requirements

1. Uploaded .htaccess file in accessible Nextcloud directory
2. Nextcloud configured with debug mode (impacts only non-production setups)
3. HTTP access to the file's URL
4. Apache web server processing .htaccess in the upload directory

## Defense

Defensive measures and detection strategies:

- Enforce debug mode disablement and use proper error logging without path exposure
- Restrict .htaccess processing in user-upload directories via Apache AllowOverride None
- Implement WAF rules to block requests to uploaded .htaccess files and monitor for error responses containing paths

## Objectives

1. Provoke an exception during .htaccess processing
2. Capture disclosed paths from error output
3. Use paths for mapping server structure

## Instructions

### Step 1: Access the File

**Context**: Send an HTTP request to the uploaded .htaccess file to trigger Apache's parsing and potential exception.

**Command** ([[commands/curl-head-request]]):
```bash
curl -I 'https://nextcloud.example.com/remote.php/dav/files/username/test.htaccess'
```

> This HEAD request fetches headers and may trigger processing without full body download. Expected output: HTTP 500 Internal Server Error with body containing stack trace if exception occurs.

### Step 2: Inspect Response for Paths

**Context**: Review the error response for leaked paths; use full GET if HEAD doesn't trigger fully.

**Command** ([[commands/curl-get-response]]):
```bash
curl 'https://nextcloud.example.com/remote.php/dav/files/username/test.htaccess' --verbose
```

> The verbose flag shows full response. Look for lines like "in /var/www/nextcloud/lib/private/AppInfo/Application.php on line 123". Success if paths like /var/www/ are visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-head-request]]
- [[commands/curl-get-response]]

## Tools Used

- [[tools/curl]]

## Tags

- path-disclosure
- exception
- apache
