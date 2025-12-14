---
tags:
  - rce
  - file-upload
  - wordpress
  - php
  - webshell
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/Burp-Suite]]'
  - '[[tools/autoxploiter]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-PHP-Webshell]]'
  - '[[procedures/Compress-Files-into-Malicious-ZIP]]'
  - '[[procedures/Upload-ZIP-to-Vulnerable-Endpoint]]'
  - '[[procedures/Access-and-Execute-Webshell-for-RCE]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:19.999Z'
description: >-
  Multi-stage exploit of the WordPress plugin 'Insert or Embed Articulate
  Content into WordPress' via arbitrary file upload to deploy a PHP webshell and
  achieve remote code execution on the server.
skill_level: intermediate
impact_level: high
id: 2e2d5eb3-41d8-4ef8-9ea8-94444677d879
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
  - '[[Unix Shell]]'
---
# Arbitrary File Upload in WordPress Articulate Plugin Leading to RCE

Multi-stage attack chain exploiting an arbitrary file upload vulnerability in the WordPress plugin 'Insert or Embed Articulate Content into WordPress' to upload a ZIP containing a PHP webshell, extract it, and execute arbitrary system commands for remote code execution on the server.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious Files] --> B[Compress to ZIP]
    B --> C[Upload ZIP]
    C --> D[Access and Execute Webshell]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- Text editor for creating PHP files

### Target Environment

- WordPress site with 'Insert or Embed Articulate Content into WordPress' plugin installed and active
- Vulnerable endpoint: /wp-json/articulate/v1/upload-data
- Web server with PHP execution enabled (e.g., Apache/Nginx on Linux)

### Initial Access Requirements

- Network access to the target WordPress site (public-facing)
- No authentication required for the upload endpoint
- Prior reconnaissance to confirm plugin presence

## Detailed Attack Procedures

### Step 1: Create Malicious Files
procedure: [[procedures/Create-Malicious-PHP-Webshell]]

**Objective**: Prepare a decoy HTML file and a PHP webshell capable of executing system commands via GET parameters.

**Instructions**: Use a text editor to create index.html with basic HTML and index.php with PHP code that runs commands from $_GET['cmd'].

**Expected Output**: Two files: index.html and index.php ready for zipping.

**Success Indicators**:
- Files created without syntax errors
- PHP code parses correctly (test locally if possible)

### Step 2: Compress Files into ZIP
procedure: [[procedures/Compress-Files-into-Malicious-ZIP]]

**Objective**: Package the malicious files into a ZIP archive that the plugin will extract without validation.

**Instructions**: Use zip command to bundle index.html and index.php into a .zip file.

```bash
zip malicious.zip index.html index.php
```

**Expected Output**: A single malicious.zip file.

**Success Indicators**:
- ZIP file created and contains both files (verify with unzip -l)
- File size reasonable for upload

### Step 3: Upload ZIP to Vulnerable Endpoint
procedure: [[procedures/Upload-ZIP-to-Vulnerable-Endpoint]]

**Objective**: Exploit the /wp-json/articulate/v1/upload-data endpoint to upload and extract the ZIP, placing the PHP file in an executable directory.

**Instructions**: Use [[commands/curl-upload-zip-to-articulate]] to POST the ZIP as multipart form data with random chunk parameters to bypass any chunking logic.

**Expected Output**: Server response indicating "Reading upload complete" or similar success message.

**Success Indicators**:
- HTTP 200 response
- No validation errors from the endpoint

### Step 4: Access and Execute Webshell for RCE
procedure: [[procedures/Access-and-Execute-Webshell-for-RCE]]

**Objective**: Access the extracted PHP webshell to run arbitrary system commands, confirming RCE.

**Instructions**: Navigate to the uploaded file path and append ?cmd=ls using [[commands/php-webshell-execute]].

**Expected Output**: Output of the ls command, listing directory contents.

**Success Indicators**:
- Command output displayed in browser/response
- Ability to run further commands like id or whoami

## Attack Chain Summary

### Key Achievements

1. Successful upload of malicious ZIP without authentication
2. Extraction of PHP webshell to /wp-content/uploads/articulate_uploads/
3. Remote execution of system commands on the WordPress server
4. Potential for full server compromise via escalated commands

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]
- [[Unix Shell]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
