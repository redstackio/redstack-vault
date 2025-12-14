---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567895
tags:
  - misconfiguration
  - command-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:32.349Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Configure-Antivirus-Path-for-RCE

## Summary

This procedure sets the clamscan AV path in the files_antivirus plugin to a malicious concatenation of the PHP interpreter and uploaded file path, enabling shell execution without validation.

## Description

The plugin's Protection settings allow arbitrary input for the AV binary path, intended for tools like clamscan. By setting it to /usr/bin/php /path/to/shell.php, saving triggers shell execution of the PHP code. escapeshellarg does not mitigate this as it's direct path execution, not argument injection, in ownCloud 10.4.1.3 on LAMP.

## Requirements

1. Installed files_antivirus plugin
2. PHP interpreter path and uploaded file path from prior steps
3. Access to Protection settings

## Defense

Defensive measures and detection strategies:

- Validate AV path input to whitelist only approved binaries
- Log configuration changes to plugin settings
- Disable custom AV path configuration for non-admins

## Objectives

1. Input malicious path into AV configuration
2. Bypass lack of sanitization for shell chaining
3. Prepare for execution on save

## Instructions

### Step 1: Access Protection Settings

**Context**: Locate the AV configuration field.

In admin settings, go to Protection > Antivirus and find the "Path to clamscan" field.

> The field is editable. Expected output: Interface ready for input.

### Step 2: Enter Malicious Path

**Context**: Construct and input the exploitable path.

Enter: /usr/bin/php /var/www/owncloud/data/files/shell.php (replace with actual paths).

> No validation errors occur. The field accepts the full string, setting up for execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- misconfiguration
- command-injection
