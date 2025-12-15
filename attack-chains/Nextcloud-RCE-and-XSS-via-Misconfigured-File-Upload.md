---
tags:
  - rce
  - xss
  - nextcloud
  - file-upload
  - misconfiguration
  - php
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Login-to-Nextcloud-User-Account]]'
  - '[[procedures/Upload-Malicious-PHP-Script-to-Nextcloud]]'
  - '[[procedures/Access-Uploaded-PHP-File-Directly-for-RCE]]'
  - '[[procedures/Execute-Malicious-Code-and-Observe-Impact]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
  - '[[Python]]'
  - '[[JavaScript]]'
description: >-
  Authenticated attack exploiting Nextcloud's default data directory
  misconfiguration to upload and execute PHP for RCE, alongside XSS via HTML
  files, and a secondary admin check flaw.
skill_level: intermediate
impact_level: high
id: bd02ff26-cc62-48b6-8aa5-f8e17e7e52b4
created_at: '2025-12-14T17:23:24.061Z'
updated_at: '2025-12-14T17:23:24.061Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
  - '[[Python]]'
  - '[[JavaScript]]'
---
# Nextcloud RCE and XSS via Misconfigured File Upload

Multi-stage attack chain demonstrating a complete attack workflow exploiting Nextcloud's default configuration where the data directory is inside the web root, allowing authenticated users to upload executable PHP files for remote code execution (RCE) and HTML files for cross-site scripting (XSS). A secondary configuration issue in admin settings fails to detect misconfigurations on non-HTTPS ports.

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
    A[Initial Access: Login] --> B[Persistence: Upload Malicious File]
    B --> C[Execution: Direct Access]
    C --> D[Impact: RCE/XSS Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for authentication and file upload
- Text editor to craft malicious PHP/HTML payloads

### Target Environment

- Nextcloud instance with default configuration (data directory in web root, e.g., /var/www/nextcloud/data)
- Apache web server without proper .htaccess enforcement (AllowOverride All not set on port 80)
- Ports: 80 (HTTP), 443 (HTTPS)
- Services: Nextcloud on PHP/Apache

### Initial Access Requirements

- Valid non-admin user credentials with file upload permissions
- Network access to the Nextcloud web interface
- No prior access needed beyond authentication

## Detailed Attack Procedures

### Step 1: Initial Access
procedure: [[procedures/Login-to-Nextcloud-User-Account]]

**Objective**: Authenticate as a user to gain file upload permissions.

**Instructions**: Use a web browser to log in to the Nextcloud instance with a non-admin user account.

**Expected Output**: Successful login redirect to the user dashboard.

**Success Indicators**:
- User dashboard loads
- File upload interface is accessible

### Step 2: Persistence
procedure: [[procedures/Upload-Malicious-PHP-Script-to-Nextcloud]]

**Objective**: Upload a malicious PHP script to the user's data directory.

**Instructions**: Navigate to the Files app in Nextcloud and upload a PHP file containing malicious code, such as a simple shell executor.

**Expected Output**: File upload confirmation; file appears in the user's files list.

**Success Indicators**:
- File stored in /data/<username>/files/shell.php
- No upload errors

### Step 3: Execution
procedure: [[procedures/Access-Uploaded-PHP-File-Directly-for-RCE]]

**Objective**: Directly access the uploaded file via URL to bypass Nextcloud's protections and execute the PHP code.

**Instructions**: Construct and navigate to the direct URL of the uploaded file in the browser.

**Expected Output**: PHP code executes, displaying output or performing actions like shell access.

**Success Indicators**:
- Direct URL loads without Nextcloud's text viewer
- Malicious code runs (e.g., system command output)

### Step 4: Impact
procedure: [[procedures/Execute-Malicious-Code-and-Observe-Impact]]

**Objective**: Leverage RCE for data theft, config changes, or server takeover; test XSS with HTML uploads.

**Instructions**: Interact with the executed script to run commands; for XSS, upload and access an HTML file with JavaScript.

**Expected Output**: Arbitrary code execution results; JavaScript alerts or redirects in browser.

**Success Indicators**:
- Server files modified or data exfiltrated
- XSS payload triggers in victim browser

## Attack Chain Summary

### Key Achievements

1. Authenticated RCE via direct PHP execution in misconfigured data directory
2. XSS exploitation through direct HTML file access
3. Exploitation of admin settings flaw allowing attacks over HTTP ports

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]
- [[Python]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
