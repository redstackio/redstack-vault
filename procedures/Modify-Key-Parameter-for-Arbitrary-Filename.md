---
id: proc-uuid-4
tags:
  - arbitrary-file-upload
  - parameter-tampering
  - nextcloud
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:51.874Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Key-Parameter-for-Arbitrary-Filename

## Summary

This procedure tampers with the 'key' parameter in the intercepted Nextcloud upload request to control the stored filename, enabling arbitrary file placement and potential path disclosure.

## Description

The 'key' parameter in the theming upload POST request directly influences the filename on the server due to insufficient validation. By modifying it to an arbitrary value (e.g., a path traversal string), an attacker can place files in unintended locations within the web directory. Error responses may disclose internal paths, aiding further reconnaissance. This exploits PHP's file handling in Nextcloud and requires the prior interception step.

## Requirements

1. Intercepted request in Burp Suite
2. Knowledge of desired filename or path
3. Admin session active

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all user-controlled parameters in uploads
- Use secure file naming (e.g., UUIDs) instead of modifiable keys
- Audit error logs for path exposures and block verbose responses

## Objectives

1. Control the uploaded file's name and location
2. Achieve arbitrary file write in web directory
3. Extract path information from errors

## Instructions

### Step 1: Inspect and Edit Parameter

**Context**: Locate the 'key' in the request body and alter it.

No specific command; in Burp's Repeater or Intercept, find the 'key=original_value' in the POST body.

> Change to 'key=../../arbitrary.txt' or similar, ensuring the file content is preserved.

### Step 2: Forward and Observe Response

**Context**: Send the modified request and analyze results.

No specific command; click Forward in Burp to submit.

> Server responds with success or error; check for file placement (e.g., via server logs) and path leaks in errors like 'Failed to write to /var/www/nextcloud/data/'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[arbitrary-file-upload]]
- [[parameter-tampering]]
- [[nextcloud]]
- [[web]]
