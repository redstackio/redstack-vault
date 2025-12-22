---
tags:
  - arbitrary-file-read
  - ssrf
  - gitlab
  - credential-leak
  - path-traversal
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands: []
platforms:
  - Web
  - Cloud (GitLab.com)
complexity: medium
procedures:
  - '[[procedures/Import-Malicious-GitLab-Export-File]]'
  - '[[procedures/Wait-for-Import-Processing]]'
  - '[[procedures/Query-Import-API-Endpoint]]'
  - '[[procedures/Extract-Leaked-Data]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploitation of arbitrary file read and SSRF vulnerabilities in GitLab's
  project import feature to leak sensitive credentials
skill_level: intermediate
impact_level: high
id: fbf84ac0-ab0e-4b81-9356-af49969ac8be
created_at: '2025-12-11T03:47:56.796Z'
updated_at: '2025-12-11T03:47:56.796Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1190]]'
---
# Arbitrary File Read via GitLab Project Import Leading to Credential Leak

## Overview

This attack chain exploits an arbitrary file read vulnerability in GitLab's project import feature, stemming from misuse of the JSON schema validator and the open-uri library, which also enables SSRF. By crafting and importing a malicious 'import.tar.gz' file, attackers can leak up to 250 bytes of sensitive files such as database credentials, Rails secret_key_base, and SMTP credentials. This could grant access to internal APIs and admin tokens on self-hosted instances. The chain demonstrates the full workflow from importing the malicious file to extracting leaked data via the import API.

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
    A[Import Malicious File] --> B[Process Import]
    B --> C[Query API]
    C --> D[Extract Leaked Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (web-based interaction with GitLab.com)

### Target Environment

- GitLab.com or self-hosted GitLab instance
- Web platform with project import feature enabled
- Access to GitLab API

### Initial Access Requirements

- Valid GitLab account with permission to create and import projects
- Network access to GitLab.com
- Ability to upload files via the import feature

## Detailed Attack Procedures

## Step 1: Import Malicious File - [[procedures/Import-Malicious-GitLab-Export-File]]

**Procedure**: [[procedures/Import-Malicious-GitLab-Export-File]]

**Objective**: Upload a specially crafted 'import.tar.gz' file to exploit the JSON schema validator and open-uri during import.

**Expected Output**: Successful initiation of the import process.

**Success Indicators**:
- Import process starts without errors
- Project is created in GitLab

Use the GitLab import feature to upload the malicious 'import.tar.gz' file as a 'GitLab export'.

## Step 2: Process Import - [[procedures/Wait-for-Import-Processing]]

**Procedure**: [[procedures/Wait-for-Import-Processing]]

**Objective**: Allow GitLab to process the imported file, triggering the arbitrary file read and SSRF vulnerabilities.

**Expected Output**: Import completion notification.

**Success Indicators**:
- Import status changes to 'finished'
- No import failure errors

Wait for the import process to complete, which triggers the vulnerability in the background.

## Step 3: Query API - [[procedures/Query-Import-API-Endpoint]]

**Procedure**: [[procedures/Query-Import-API-Endpoint]]

**Objective**: Retrieve the import status via API, which includes leaked file contents.

**Expected Output**: API response containing leaked data.

**Success Indicators**:
- HTTP 200 response from API
- Leaked bytes visible in the response

Access the URL: https://gitlab.com/api/v4/projects/PROJECT_ID/import (replace PROJECT_ID with the imported project's ID).

```bash
curl https://gitlab.com/api/v4/projects/PROJECT_ID/import
```

## Step 4: Extract Data - [[procedures/Extract-Leaked-Data]]

**Procedure**: [[procedures/Extract-Leaked-Data]]

**Objective**: Observe and extract the leaked sensitive data from the API output.

**Expected Output**: Approximately 250 bytes of arbitrary file data, such as database credentials.

**Success Indicators**:
- Sensitive information like passwords or keys is present
- Data can be used for further exploitation

Review the API response for leaked contents, including connection information from GitLab's production database.

## Attack Chain Summary

### Key Achievements

1. Successful import of malicious file triggering vulnerability
2. Leakage of sensitive credentials via API
3. Potential access to internal resources via SSRF

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

*Last updated: 2023-10-01*
