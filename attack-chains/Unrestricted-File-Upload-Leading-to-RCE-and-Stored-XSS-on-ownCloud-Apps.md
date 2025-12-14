---
tags:
  - rce
  - xss
  - file-upload
  - php
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Upload-Malicious-PHP-File-for-RCE]]'
  - '[[procedures/Access-and-Execute-Uploaded-PHP-Code]]'
  - '[[procedures/Upload-HTML-JS-for-Stored-XSS]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:25.032Z'
description: >-
  A multi-stage attack exploiting an unrestricted file upload vulnerability on
  apps.owncloud.com to achieve remote code execution via PHP files and stored
  XSS via HTML/JavaScript, enabling server compromise and client-side attacks.
skill_level: intermediate
impact_level: high
id: f3df914a-4c97-46eb-aa14-21604593f220
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
  - '[[JavaScript]]'
---
# Unrestricted File Upload Leading to RCE and Stored XSS on ownCloud Apps

Multi-stage attack chain demonstrating exploitation of an unrestricted file upload vulnerability on apps.owncloud.com, allowing malicious PHP uploads for remote code execution (RCE) and HTML/JavaScript for stored XSS, potentially leading to server takeover, data exfiltration, and client-side attacks on users.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Upload Malicious PHP] --> B[Execute PHP for RCE]
    B --> C[Upload HTML/JS for XSS]
    C --> D[Server Compromise & Client Attacks]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox) for accessing the upload feature

### Target Environment

- Web platform with PHP backend
- Access to apps.owncloud.com file upload feature
- No specific ports required beyond standard HTTP/HTTPS (80/443)

### Initial Access Requirements

- Public access to the website (no authentication needed)
- Ability to interact with the content upload form

## Detailed Attack Procedures

### Step 1: Upload Malicious PHP File
procedure: [[procedures/Upload-Malicious-PHP-File-for-RCE]]

**Objective**: Exploit the unrestricted file upload to store a malicious PHP file on the server, setting up for RCE.

**Instructions**: Navigate to the file upload feature on apps.owncloud.com. Create a simple PHP file with content `<?php phpinfo(); ?>` and upload it using the content upload form. The file will be stored in the CONTENT/content-pre1/ directory with a .php5 extension.

**Expected Output**: File uploaded successfully, accessible at a URL like https://apps.owncloud.com/CONTENT/content-pre1/[ID]-1.php5.

**Success Indicators**:
- Upload confirmation from the site
- File path revealed in response or logs

### Step 2: Access and Execute Uploaded PHP Code
procedure: [[procedures/Access-and-Execute-Uploaded-PHP-Code]]

**Objective**: Trigger execution of the uploaded PHP code to achieve RCE and reveal server information.

**Instructions**: Use a web browser to directly access the uploaded file's URL (e.g., https://apps.owncloud.com/CONTENT/content-pre1/171172-1.php5). The server will interpret and execute the PHP code.

**Expected Output**: Server information displayed via phpinfo(), confirming code execution.

**Success Indicators**:
- PHP output rendered in browser
- No 404 error; code runs server-side

### Step 3: Upload HTML/JS for Stored XSS
procedure: [[procedures/Upload-HTML-JS-for-Stored-XSS]]

**Objective**: Demonstrate persistence post-fix by uploading executable JavaScript, enabling stored XSS attacks on viewers.

**Instructions**: After any partial fixes, use the upload feature to submit a file with content `<script type="text/javascript">alert(document.cookie);</script>`. The file stores as .php5 but renders as HTML/JS when accessed.

**Expected Output**: When the URL (e.g., https://apps.owncloud.com/CONTENT/content-pre1/171177-1.php5) is visited, an alert pops up showing cookies, confirming XSS execution.

**Success Indicators**:
- JavaScript alert triggered
- Cookies accessible via script, enabling session hijacking

## Attack Chain Summary

### Key Achievements

1. Achieved RCE by uploading and executing arbitrary PHP code, exposing server details like phpinfo().
2. Enabled server compromise, including potential database access and full takeover.
3. Demonstrated stored XSS for client-side attacks, allowing cookie theft and session hijacking on authenticated users.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
