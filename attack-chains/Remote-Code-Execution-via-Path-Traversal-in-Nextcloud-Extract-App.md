---
tags:
  - path-traversal
  - rce
  - nextcloud
  - zip-extraction
  - file-overwrite
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/access-rce-url]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-Nextcloud-VM-Environment]]'
  - '[[procedures/Create-Low-Privilege-User]]'
  - '[[procedures/Upload-Malicious-Zip-Payload]]'
  - '[[procedures/Intercept-Zip-Extraction-Request]]'
  - '[[procedures/Modify-Request-for-Path-Traversal]]'
  - '[[procedures/Execute-Commands-via-Modified-Files-App]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Hijack Execution Flow]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:26:22.523Z'
description: >-
  Multi-stage attack exploiting path traversal in Nextcloud's Extract app to
  overwrite files and achieve RCE as www-data user.
skill_level: intermediate
impact_level: high
id: fa65a2bb-e1c3-4c80-9387-d8ed401b90d5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Hijack Execution Flow]]'
  - '[[Command-Line Interface]]'
---
# Remote Code Execution via Path Traversal in Nextcloud Extract App

Multi-stage attack chain demonstrating a complete attack workflow exploiting a path traversal vulnerability in the Nextcloud Extract app, allowing arbitrary file overwrites and remote code execution as the www-data user. The attack involves uploading a malicious zip, intercepting the extraction request, injecting path traversal payloads, and executing commands through the modified files app.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Environment] --> B[Initial Access: Create User]
    B --> C[Upload Payload]
    C --> D[Intercept Extraction]
    D --> E[Path Traversal Overwrite]
    E --> F[Execute RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Burp Suite or similar proxy for request interception

### Target Environment

- Nextcloud installed on Linux (e.g., via official VM image)
- Extract app enabled
- Files app present
- Web access to Nextcloud instance

### Initial Access Requirements

- Access to create users (admin privileges initially, but attack uses low-priv user)
- Network access to upload files and intercept requests
- No prior access needed beyond web interface

## Detailed Attack Procedures

### Step 1: Setup Nextcloud Environment
procedure: [[procedures/Install-Nextcloud-VM-Environment]]

**Objective**: Prepare a vulnerable Nextcloud instance using the official VM for testing the Extract app vulnerability.

**Instructions**: Download and boot the official Nextcloud VM image, ensuring default settings with extra security options enabled. Access the web interface at the default URL.

**Expected Output**: Running Nextcloud instance accessible via browser.

**Success Indicators**:
- VM boots successfully
- Web login page loads

### Step 2: Create Low-Privilege User
procedure: [[procedures/Create-Low-Privilege-User]]

**Objective**: Establish initial access as a standard user without special privileges to simulate realistic attack conditions.

**Instructions**: Log in as admin, navigate to user settings, and create a new user with no group assignments. Log out and log in as the new user.

**Expected Output**: Successful login as the new user.

**Success Indicators**:
- New user created and login works
- No admin privileges assigned

### Step 3: Upload Malicious Zip Payload
procedure: [[procedures/Upload-Malicious-Zip-Payload]]

**Objective**: Introduce the exploit payload by uploading a crafted zip file containing a modified App.php for command execution.

**Instructions**: As the low-priv user, navigate to the root folder in the files interface and upload the prepared nextcloud-shell.zip file.

**Expected Output**: Zip file appears in the root folder.

**Success Indicators**:
- Upload completes without errors
- File visible in file list

### Step 4: Intercept Zip Extraction Request
procedure: [[procedures/Intercept-Zip-Extraction-Request]]

**Objective**: Capture the extraction request to allow modification for path traversal exploitation.

**Instructions**: Right-click the uploaded zip and select 'Extract here'. Configure your proxy (e.g., Burp) to intercept the POST request to /index.php/apps/extract/ajax/extractHere.php.

**Expected Output**: Intercepted POST request visible in proxy tool.

**Success Indicators**:
- Request captured before completion
- Original parameters visible (nameOfFile, directory)

### Step 5: Modify Request for Path Traversal
procedure: [[procedures/Modify-Request-for-Path-Traversal]]

**Objective**: Inject path traversal sequences to overwrite files outside the intended directory, targeting the files app library.

**Instructions**: In the intercepted request, modify the body to: nameOfFile=../../../../../../mnt/ncdata/normaluser/files/nextcloud-shell.zip&directory=/../../../../var/www/nextcloud/apps/files/lib&external=0. Replace 'normaluser' with the actual username. Forward the request.

**Expected Output**: Extraction completes, overwriting App.php in the files app.

**Success Indicators**:
- No extraction errors
- Modified file placed in target directory (verifiable via server access)

### Step 6: Execute Commands via Modified Files App
procedure: [[procedures/Execute-Commands-via-Modified-Files-App]]

**Objective**: Leverage the overwritten App.php to execute arbitrary commands as www-data, demonstrating full RCE.

**Instructions**: Visit https://[host]/apps/files/?dir=/&poc_cmd=whoami using [[commands/access-rce-url]] or browser. Replace poc_cmd with any command (e.g., id, ls).

**Expected Output**: Command output displayed, e.g., 'www-data' for whoami.

**Success Indicators**:
- Command executes and output appears
- Arbitrary commands run successfully

## Attack Chain Summary

### Key Achievements

1. Bypassed path validation in Extract app to overwrite core files
2. Achieved RCE as www-data, enabling file access and PII modification
3. Demonstrated full compromise of Nextcloud installation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Hijack Execution Flow]] Hijack Execution Flow
- [[Command-Line Interface]] Command and Scripting Interpreter

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
