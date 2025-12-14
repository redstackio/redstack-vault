---
id: proc-access-php-nextcloud
tags:
  - rce
  - misconfiguration
  - nextcloud
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
  - '[[Python]]'
updated_at: '2025-12-14T03:16:02.597Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Directly-Access-Uploaded-PHP-File

## Summary

This procedure directly requests the uploaded PHP file via its URL, exploiting the data directory's placement in the web root to trigger execution.

## Description

Due to Nextcloud's default config placing 'datadirectory' inside /var/www/nextcloud/data, files are web-accessible. With Apache misconfigurations (e.g., AllowOverride not enabled on port 80), .htaccess protections are bypassed, allowing HTTP requests to execute PHP directly. This step assumes the file is at a known path and demonstrates the core vulnerability.

## Requirements

1. Knowledge of the uploaded file's URL path (/data/<username>/files/shell.php)
2. Network access to the server on port 80/443
3. Web browser or curl for HTTP requests

## Defense

Defensive measures and detection strategies:

- Move data directory outside web root (e.g., /var/nextcloud-data)
- Configure Apache with AllowOverride All and proper .htaccess rules
- Enable Nextcloud's security check for .htaccess on all ports

## Objectives

1. Confirm web accessibility of the data directory
2. Trigger PHP interpretation without Nextcloud mediation
3. Validate misconfiguration for RCE potential

## Instructions

### Step 1: Construct URL

**Context**: Build the direct path to the uploaded file.

Use: https://www.ournextclouddomain.com/data/attacker/files/shell.php

> Ensure HTTPS/HTTP matches the server's config.

### Step 2: Request the File

**Context**: Send an HTTP GET to execute the PHP.

Open the URL in a browser.

> Expect PHP to run; if it's a blank page or error, check server logs for execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Python]] PHP

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- misconfiguration
- nextcloud
