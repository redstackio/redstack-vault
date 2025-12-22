---
tags:
  - unrestricted-file-upload
  - rce
  - xss
  - php
  - web
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Upload-Malicious-PHP-File-for-RCE]]'
  - '[[procedures/Access-and-Execute-Uploaded-PHP-File]]'
  - '[[procedures/Exploit-Stored-XSS-via-Uploaded-JavaScript]]'
step_count: 3
techniques:
  - '[[Remote File Copy]]'
  - '[[Python]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T05:32:10.196Z'
description: >-
  Multi-stage attack exploiting unrestricted file uploads on apps.owncloud.com
  to achieve remote code execution via PHP and, after partial mitigation, stored
  XSS via JavaScript.
skill_level: intermediate
impact_level: high
id: ea1d7a83-5c9c-4d95-b330-02c083d0bba3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[Python]]'
  - '[[JavaScript]]'
---
# Unrestricted File Upload Leading to RCE and Stored XSS in ownCloud Apps

Multi-stage attack chain demonstrating exploitation of unrestricted file uploads on apps.owncloud.com, starting with remote code execution via malicious PHP files and escalating to stored XSS after server-side fixes.

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
    B --> C[Exploit Stored XSS Post-Fix]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox) for file uploads and access
- Optional: Burp Suite or similar proxy for intercepting requests

### Target Environment

- Web platform with PHP backend
- Accessible file upload feature on https://apps.owncloud.com
- No authentication required for public uploads

### Initial Access Requirements

- Public internet access to the target site
- No credentials needed; the upload is unrestricted

## Detailed Attack Procedures

### Step 1: Upload Malicious PHP File
procedure: [[procedures/Upload-Malicious-PHP-File-for-RCE]]

**Objective**: Upload a PHP file containing executable code to bypass file type restrictions and prepare for server-side execution.

**Instructions**: Navigate to the file upload feature on https://apps.owncloud.com. Create a simple PHP file named "171172-1.php5" with content `<?php phpinfo(); ?>`. Upload it directly via the web interface.

**Expected Output**: File uploaded successfully to the CONTENT/content-pre1/ directory without errors.

**Success Indicators**:
- Upload confirmation message
- File appears in the directory listing if available

### Step 2: Access and Execute Uploaded PHP File
procedure: [[procedures/Access-and-Execute-Uploaded-PHP-File]]

**Objective**: Trigger server-side execution of the uploaded PHP code to achieve remote code execution and reveal server configuration.

**Instructions**: Construct the direct URL to the uploaded file: https://apps.owncloud.com/CONTENT/content-pre1/171172-1.php5. Access it in a web browser to execute the PHP code.

**Expected Output**: Browser displays PHP configuration information from phpinfo(), confirming code execution.

**Success Indicators**:
- phpinfo() output rendered
- No 404 or download prompt; instead, dynamic page generation

### Step 3: Exploit Stored XSS Post-Fix
procedure: [[procedures/Exploit-Stored-XSS-via-Uploaded-JavaScript]]

**Objective**: After PHP execution is blocked, upload HTML/JavaScript to achieve stored XSS, allowing client-side code execution in users' browsers.

**Instructions**: Upload a new file named "171177-1.php5" with content `<script type="text/javascript">alert(document.cookie);</script>`. Access it via https://apps.owncloud.com/CONTENT/content-pre1/171177-1.php5.

**Expected Output**: JavaScript alert box displaying document cookies, confirming XSS execution.

**Success Indicators**:
- Alert popup with cookie data
- JavaScript executes without server-side blocking

## Attack Chain Summary

### Key Achievements

1. Achieved full server compromise via PHP RCE, enabling database access and arbitrary code execution
2. Demonstrated persistence of vulnerability through incomplete fix, leading to stored XSS
3. Highlighted risks of unrestricted uploads in web applications

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Remote File Copy]]
- [[Python]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
