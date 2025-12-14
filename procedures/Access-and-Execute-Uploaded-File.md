---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - rce
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T05:32:13.459Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Windows Command Shell]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Access-and-Execute-Uploaded-File

## Summary

This procedure accesses the uploaded malicious SHTML file via its temporary URL to trigger server-side code execution, disclosing sensitive information such as intranet IPs, server paths, and configuration files.

## Description

Once uploaded, the SHTML file is stored in a web-accessible temp directory on the IIS server. Accessing it executes the embedded code, leveraging server variables to output details like REMOTE_ADDR (intranet IP 10.92.29.50), physical path (D:\TrustHX\STBKSERM101\www_app), and web.config contents, enabling further attacks like phishing.

## Requirements

1. Successful upload from previous procedure, providing temp file path
2. Web browser or HTTP client for GET request
3. No additional authentication needed

## Defense

Defensive measures and detection strategies:

- Disable execution of uploaded files by isolating temp directories
- Monitor access logs for unusual file requests in temp paths
- Implement content security policies and file integrity checks

## Objectives

1. Execute uploaded code on the server
2. Retrieve and exfiltrate server information
3. Validate RCE for potential escalation

## Instructions

### Step 1: Construct Access URL

**Context**: Use the returned temp file path to build the full URL.

For example, /recruitjob/tempfiles/temp_uploaded_34afb246-02f1-4cb0-978d-15805c2a05c8.shtml.

### Step 2: Request the File

**Context**: Send a GET request to trigger execution.

Open the URL in a browser: http://ecjobsdc.starbucks.com.cn/recruitjob/tempfiles/temp_uploaded_34afb246-02f1-4cb0-978d-15805c2a05c8.shtml.

**Expected Output**: Browser displays executed output, including 1111, SERVER_SOFTWARE (Microsoft-IIS/8.5), REMOTE_ADDR (10.92.29.50), and web.config contents.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

- [[Windows Command Shell]]

## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[information-disclosure]]
