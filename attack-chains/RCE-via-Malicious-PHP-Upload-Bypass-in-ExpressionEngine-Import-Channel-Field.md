---
tags:
  - rce
  - file-upload-bypass
  - php
  - expressionengine
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - PHP
complexity: medium
procedures:
  - '[[procedures/Bypass-PHP-Upload-Restrictions-in-ExpressionEngine]]'
  - '[[procedures/Predict-Temporary-Folder-for-Uploaded-File]]'
  - '[[procedures/Access-and-Execute-Uploaded-PHP-for-RCE]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Web Shell]]'
description: >-
  Authenticated administrator exploits file upload vulnerability in
  ExpressionEngine's import channel field to upload a malicious PHP file,
  predict its temporary storage location, and achieve remote code execution if
  the system folder is web-accessible.
skill_level: intermediate
impact_level: high
id: 8e88082b-8ac3-4afd-9b71-d01695810a39
created_at: '2025-12-14T17:23:36.832Z'
updated_at: '2025-12-14T17:23:36.832Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Web Shell]]'
---
# RCE via Malicious PHP Upload Bypass in ExpressionEngine Import Channel Field

## Overview

This attack chain exploits a vulnerability in ExpressionEngine CMS where an authenticated administrator can upload a malicious PHP file through the 'import channel field' feature. The upload function restricts .php extensions but can be bypassed, allowing the file to be stored in a predictable temporary folder exposed via the source code. If the system's temporary folder is web-accessible (e.g., not moved above the web root as per best practices), the attacker can access the file directly to execute arbitrary PHP code, leading to full server compromise including data exfiltration, further malware deployment, or persistence.

The chain requires administrative access to the CMS and knowledge of the source code for folder prediction. It demonstrates a classic file upload to RCE escalation in PHP-based web applications.

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
    A[Upload Malicious PHP] --> B[Predict Temp Folder]
    B --> C[Execute for RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser for authenticated access (e.g., Firefox or Chrome with developer tools)
- Text editor for crafting malicious PHP payload

### Target Environment

- ExpressionEngine CMS (vulnerable versions with exposed source code)
- PHP-enabled web server
- Web-accessible system/temporary folders (non-standard configuration)

### Initial Access Requirements

- Valid administrative credentials to the ExpressionEngine backend
- Direct network access to the web application
- Ability to view or access the CMS source code for the naming algorithm

## Detailed Attack Procedures

### Step 1: Bypass Upload Restrictions
procedure: [[procedures/Bypass-PHP-Upload-Restrictions-in-ExpressionEngine]]

**Objective**: Upload a malicious PHP file disguised to evade the .php extension check in the import channel field feature.

**Instructions**: Log in as an administrator to the ExpressionEngine control panel. Navigate to the channel management section and use the 'import channel field' functionality to attempt uploading a file. Craft a PHP payload (e.g., a simple webshell like `<?php system($_GET['cmd']); ?>`) and rename or encode the extension to bypass the check, such as using double extensions (.php.txt) or null byte injection if applicable. Submit the upload form.

**Expected Output**: The file is accepted and stored in a temporary folder without triggering the extension block.

**Success Indicators**:
- Upload succeeds without error
- No .php rejection message appears

### Step 2: Predict Temporary Folder Location
procedure: [[procedures/Predict-Temporary-Folder-for-Uploaded-File]]

**Objective**: Identify the exact path of the temporary folder where the uploaded file resides using the predictable naming from source code.

**Instructions**: Review the ExpressionEngine source code, particularly the upload function and temporary folder generation algorithm (often based on timestamps, session IDs, or hashes exposed in comments or logs). Calculate the folder name manually or via a simple script based on the current time or known variables. Common patterns include /system/expressionengine/cache/ or similar temp dirs with predictable prefixes.

**Expected Output**: A guessed path like /path/to/system/tmp/upload_1234567890.php.

**Success Indicators**:
- Folder name matches the algorithm logic
- Path can be constructed without trial-and-error beyond prediction

### Step 3: Access and Execute PHP File
procedure: [[procedures/Access-and-Execute-Uploaded-PHP-for-RCE]]

**Objective**: Directly access the uploaded file via web request to trigger remote code execution.

**Instructions**: If the system folder is web-accessible, construct the full URL to the predicted temporary file path (e.g., http://target.com/system/tmp/predicted_folder/malicious.php?cmd=whoami). Use a browser or curl to visit the URL and pass parameters to execute commands. Monitor for output indicating code execution, such as system command results.

**Expected Output**: PHP code runs, displaying command output or webshell interface.

**Success Indicators**:
- HTTP response contains executed command results
- Server-side effects like file creation or logs confirm RCE

## Attack Chain Summary

### Key Achievements

1. Bypassed file upload restrictions to place executable code on the server
2. Predicted storage location using exposed source code logic
3. Achieved arbitrary code execution leading to server compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Web Shell]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01*
