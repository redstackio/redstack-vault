---
tags:
  - idor
  - gitlab
  - import-bypass
  - private-exposure
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Craft-Malicious-Project-JSON]]'
  - '[[procedures/Package-Tarball-for-Import]]'
  - '[[procedures/Import-Tarball-into-GitLab]]'
  - '[[procedures/Verify-Exposed-Private-Issues]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
description: >-
  Multi-stage attack exploiting an IDOR vulnerability in GitLab's project import
  to expose private issues and resources
skill_level: intermediate
impact_level: high
id: 58360ee2-d811-4fb0-b94f-b5c8b6f1e600
created_at: '2025-12-11T03:47:56.950Z'
updated_at: '2025-12-11T03:47:56.950Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1087]]'
---
# GitLab IDOR Bypass via Project Import to Expose Private Issues

Multi-stage attack chain demonstrating a complete attack workflow exploiting an Insecure Direct Object Reference (IDOR) in GitLab's project import feature. This bypasses a previous fix by indirectly setting '_ids' attributes within the 'attributes' field in project.json, allowing linkage and exposure of private issues from other users. The attack enables access to random resources by traversing incremental ID spaces, potentially leading to unauthorized data exposure.

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
    A[Step 1: Craft JSON] --> B[Step 2: Package Tarball]
    B --> C[Step 3: Import Tarball]
    C --> D[Step 4: Verify Exposure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual file editing and GitLab web interface)

### Target Environment

- Web platform
- GitLab instance with project import functionality
- Access to GitLab account for importing projects

### Initial Access Requirements

- Valid GitLab user account
- Ability to upload and import project tarballs
- Knowledge of target issue IDs (e.g., via enumeration)

## Detailed Attack Procedures

### Step 1: Craft Malicious Project JSON - [[procedures/Craft-Malicious-Project-JSON]]

**Procedure**: [[procedures/Craft-Malicious-Project-JSON]]

**Objective**: Create a modified project.json file that indirectly sets issue_ids to bypass validation and link private issues.

**Expected Output**: A crafted project.json file ready for packaging.

**Success Indicators**:
- JSON file contains 'attributes' field with 'issue_ids' set to target IDs
- No direct '_ids' attributes are used to avoid previous fix blocks

### Step 2: Package Tarball for Import - [[procedures/Package-Tarball-for-Import]]

**Procedure**: [[procedures/Package-Tarball-for-Import]]

**Objective**: Bundle the malicious project.json into a tarball format acceptable for GitLab import.

**Expected Output**: An exploit.tar.gz file containing the crafted JSON.

**Success Indicators**:
- Tarball is created without errors
- File structure matches GitLab's expected import format

### Step 3: Import Tarball into GitLab - [[procedures/Import-Tarball-into-GitLab]]

**Procedure**: [[procedures/Import-Tarball-into-GitLab]]

**Objective**: Upload and process the tarball using GitLab's import feature to apply the malicious relations.

**Expected Output**: Successful import of the project with linked private issues.

**Success Indicators**:
- Import completes without validation errors
- Project is created or updated in GitLab

### Step 4: Verify Exposed Private Issues - [[procedures/Verify-Exposed-Private-Issues]]

**Procedure**: [[procedures/Verify-Exposed-Private-Issues]]

**Objective**: Check the imported project's issues tab to confirm access to previously private objects.

**Expected Output**: Visibility of specified private issues in the project.

**Success Indicators**:
- Target issue (e.g., ID 29279725) appears in the issues list
- Ability to access and view details of exposed resources

## Attack Chain Summary

### Key Achievements

1. Bypassed IDOR validation fix in GitLab import
2. Exposed private issues and objects from other users
3. Enabled traversal of incremental ID spaces for broader resource access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

*Last updated: 2023-10-01*
