---
tags:
  - xss-execution
  - client-side
  - data-directory-access
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T05:32:09.963Z'
sub_techniques: []
id: 00eba3bd-7b8f-4e57-bbb6-f8ef92065663
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Accessing-Uploaded-File

## Summary

This procedure accesses the uploaded malicious HTML file via direct URL to the Nextcloud data directory, causing the browser to execute embedded JavaScript for XSS impact, such as data exfiltration.

## Description

Once uploaded, files in Nextcloud's data/themed* paths are served directly without sanitization, rendering HTML content and executing scripts client-side. This targets users (including admins) who access these paths, potentially leading to session theft or phishing. Applicable to web browsers interacting with PHP/Nextcloud, with no server-side execution possible (e.g., PHP uploads are treated as text). Builds on prior upload success.

## Requirements

1. Knowledge of the uploaded file's exact path (e.g., ../data/themedinstancelogo/malicious.png)
2. Web browser to visit the constructed URL
3. The Nextcloud instance must serve data directory files publicly

## Defense

Defensive measures and detection strategies:

- Block direct access to /data/ paths via .htaccess or nginx config (e.g., deny all)
- Sanitize served files by forcing image MIME types or stripping scripts
- Monitor access logs for unusual requests to themed* paths and alert on script execution attempts

## Objectives

1. Load the file as HTML in the browser
2. Execute the JavaScript payload
3. Observe impact like alerts or network requests

## Instructions

### Step 1: Construct Access URL

**Context**: Build the direct link to the stored file.

Determine the path from upload (e.g., themedinstancelogo for logo). Form URL: http://example.com/nextcloud/data/themedinstancelogo/malicious.png.

> URL ready; even with .png, it renders as HTML due to content.

### Step 2: Visit and Execute

**Context**: Trigger client-side rendering and script execution.

Open the URL in a browser. The HTML loads, and any <script> tags execute immediately.

> Payload runs: e.g., alert pops or cookie sent to attacker server, confirming XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-execution
- client-side
- data-directory-access
