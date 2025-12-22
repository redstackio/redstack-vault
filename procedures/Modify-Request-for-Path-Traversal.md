---
tags:
  - path-traversal
  - file-overwrite
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
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:22.492Z'
sub_techniques: []
id: d47c52da-1967-4c41-95fc-cdd78f064a26
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Modify-Request-for-Path-Traversal

## Summary

Alter the intercepted extraction request to include ../ sequences, enabling overwrite of arbitrary files like the files app's App.php.

## Description

The Extract app fails to sanitize paths, allowing traversal from /mnt/ncdata/user/files to /var/www/nextcloud/apps/files/lib. This places the malicious App.php in the library, hijacking the files app for RCE.

## Requirements

1. Intercepted request in proxy
2. Knowledge of username and paths (e.g., /mnt/ncdata/normaluser)
3. Target directory confirmed

## Defense

Defensive measures and detection strategies:

- Path normalization and validation in extraction handlers
- WAF rules for ../ in parameters
- File integrity monitoring on app directories

## Objectives

1. Traverse to system directories
2. Overwrite critical files
3. Enable RCE payload

## Instructions

### Step 1: Edit Parameters

**Context**: Inject traversal in request body.

Change to: nameOfFile=../../../../../../mnt/ncdata/normaluser/files/nextcloud-shell.zip&directory=/../../../../var/www/nextcloud/apps/files/lib&external=0 (replace normaluser).

### Step 2: Forward Request

**Context**: Complete the modified extraction.

Forward the request in proxy and observe response.

**Expected Output**: 200 OK or success message; file overwritten.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- path-traversal
- file-overwrite
