---
tags:
  - gitlab
  - idor
  - data-theft
  - import-vuln
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Craft-Malicious-GitLab-Export-Tarball]]'
  - '[[procedures/Import-Crafted-Tarball-into-New-Project]]'
  - '[[procedures/Access-Stolen-Private-Issues]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Information Repositories]]'
description: >-
  Exploitation of an IDOR vulnerability in GitLab's project import feature to
  steal private objects from other projects
skill_level: intermediate
impact_level: high
id: 88afad31-0acc-413d-bd71-59a5c61edcb0
created_at: '2025-12-11T03:47:57.187Z'
updated_at: '2025-12-11T03:47:57.187Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1213]]'
---
# GitLab Project Import IDOR to Steal Private Issues and Merge Requests

Multi-stage attack chain demonstrating exploitation of a vulnerability in GitLab's project import to steal private objects such as issues and merge requests.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Craft Malicious Tarball] --> B[Import Tarball]
    B --> C[Access Stolen Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- None specified; basic file editing tools (e.g., text editor) and GitLab access.

### Target Environment

- GitLab platform (web-based)
- Required services: GitLab project import functionality
- Network access: Access to a GitLab instance with project creation permissions

### Initial Access Requirements

- GitLab account with permission to create and import projects
- Knowledge of target issue IDs (e.g., via brute-forcing incremental IDs)

## Detailed Attack Procedures

### Step 1: Craft Malicious Export Tarball - [[procedures/Craft-Malicious-GitLab-Export-Tarball]]

**Procedure**: [[procedures/Craft-Malicious-GitLab-Export-Tarball]]

**Objective**: Create a modified export tarball that includes foreign object IDs to hijack private issues during import.

**Expected Output**: A crafted tarball file ready for import.

**Success Indicators**:
- The project.json file contains modified 'issue_ids' array with target IDs.
- The tarball is valid and can be uploaded without errors.

First, obtain or create a base GitLab export tarball. Extract it, modify the project.json file by adding foreign issue_ids, such as 'issue_ids': [27422144], while keeping the issues array empty. Use incremental IDs for brute-forcing to target multiple issues. Repackage the tarball.

### Step 2: Import Crafted Tarball - [[procedures/Import-Crafted-Tarball-into-New-Project]]

**Procedure**: [[procedures/Import-Crafted-Tarball-into-New-Project]]

**Objective**: Upload and process the malicious tarball into a new GitLab project to trigger the IDOR vulnerability.

**Expected Output**: Successful import of the project with assigned foreign objects.

**Success Indicators**:
- Import completes without validation errors.
- The new project is created and accessible.

Navigate to GitLab's project import feature and upload the crafted tarball. Allow the import process to run, which will assign the foreign issue IDs without proper sanitization.

### Step 3: Access Stolen Issues - [[procedures/Access-Stolen-Private-Issues]]

**Procedure**: [[procedures/Access-Stolen-Private-Issues]]

**Objective**: View and extract the stolen private issues from the imported project.

**Expected Output**: Display of private issues from other projects in the attacker's project.

**Success Indicators**:
- Issues page shows content from unauthorized projects.
- Sensitive data like CI variables or credentials is accessible.

Check the issues page of the newly imported project to view the stolen private issues, which may include sensitive information and disrupt the original projects.

## Attack Chain Summary

### Key Achievements

1. Successful crafting and import of malicious tarball exploiting IDOR.
2. Unauthorized access to private objects like issues and merge requests.
3. Potential leakage of sensitive data and disruption of target projects.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Information Repositories]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

*Last updated: [TIMESTAMP]*
