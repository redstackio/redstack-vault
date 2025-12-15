---
tags:
  - gitlab
  - arbitrary-file-read
  - symlink
  - rce
  - secrets-extraction
type: attack_chain
tools:
  - '[[tools/GNU-Tar]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-25T00:00:00Z'
procedures:
  - '[[procedures/Create-Legitimate-GitLab-Export]]'
  - '[[procedures/Modify-Export-with-Symlink-for-Partial-Read]]'
  - '[[procedures/Upload-Malicious-Export-for-Partial-File-Read]]'
  - '[[procedures/Modify-Export-with-Symlink-for-Full-Read]]'
  - '[[procedures/Upload-Malicious-Export-for-Full-File-Read]]'
  - '[[procedures/Exploit-Read-Secrets-for-RCE]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:24:08.387Z'
description: >-
  Multi-stage attack exploiting symlink vulnerabilities in GitLab's
  export/import feature to read arbitrary files, extract secrets, and achieve
  remote code execution via cookie manipulation.
id: 3e3c743f-bd7f-4fc3-9ed8-6597ce4b6344
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
  - '[[Command-Line Interface]]'
---
# Arbitrary File Read via Symlinks in GitLab Export Import Leading to RCE

Multi-stage attack chain demonstrating exploitation of symlink handling flaws in GitLab's project export/import feature to achieve arbitrary file reads, extract sensitive secrets, and escalate to remote code execution through cookie re-signing and internal token access.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Legitimate Export] --> B[Modify with Symlink for Partial Read]
    B --> C[Upload for Partial File Exposure]
    C --> D[Modify with Symlink for Full Read]
    D --> E[Upload for Full File Exposure]
    E --> F[Exploit Secrets for RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/GNU-Tar]]

### Target Environment

- GitLab instance (self-hosted or SaaS) with export/import enabled
- Access to project creation interface
- Linux-based attacker machine for tar manipulation

### Initial Access Requirements

- Valid GitLab account with project creation permissions
- No elevated privileges needed initially

## Detailed Attack Procedures

### Step 1: Create Legitimate Export
procedure: [[procedures/Create-Legitimate-GitLab-Export]]

**Objective**: Generate a baseline GitLab project export to understand and modify its structure.

**Instructions**: Log into GitLab, create a demo project, and trigger an export from the admin panel to obtain a tar.gz file containing VERSION, project.bundle, and project.json.

**Expected Output**: A downloadable tar.gz export file.

**Success Indicators**:
- Export file generated and downloaded successfully
- File contains expected structure upon extraction

### Step 2: Modify for Partial File Read
procedure: [[procedures/Modify-Export-with-Symlink-for-Partial-Read]]

**Objective**: Replace the VERSION file with a symlink to a target sensitive file like /etc/passwd to leak the first line during import validation.

**Instructions**: Extract the export using tar, create a symlink with `ln -s /etc/passwd VERSION`, inspect with [[commands/list-directory-with-symlinks]], then re-archive using [[commands/create-tar-gz-archive]]:

```bash
ln -s /etc/passwd VERSION
tar -czvf test.tar.gz .
```

**Expected Output**: Modified tar.gz with symlinked VERSION.

**Success Indicators**:
- Symlink created and visible in directory listing
- Archive re-created without errors

### Step 3: Upload for Partial File Read
procedure: [[procedures/Upload-Malicious-Export-for-Partial-File-Read]]

**Objective**: Trigger the import to exploit the VERSION check and expose the first line of the symlinked file in an error message.

**Instructions**: Navigate to GitLab's new project creation page (e.g., https://gitlab.example.com/projects/new), select "Import project" > "GitLab export", and upload the modified tar.gz.

**Expected Output**: Error message during version check revealing the first line (e.g., root:x:0:0).

**Success Indicators**:
- Import fails with version mismatch error containing file content
- Partial sensitive data leaked

### Step 4: Modify for Full File Read
procedure: [[procedures/Modify-Export-with-Symlink-for-Full-Read]]

**Objective**: Replace project.json with a symlink to read the entire contents of a sensitive file during JSON parsing.

**Instructions**: Re-extract the legitimate export, create symlink `ln -s /etc/passwd project.json`, inspect with [[commands/list-directory-with-symlinks]], keep VERSION intact, and re-archive using [[commands/create-tar-gz-archive]]:

```bash
ln -s /etc/passwd project.json
tar -czvf test.tar.gz .
```

**Expected Output**: Modified tar.gz with symlinked project.json.

**Success Indicators**:
- Symlink to project.json confirmed
- Archive includes all original files plus modification

### Step 5: Upload for Full File Read
procedure: [[procedures/Upload-Malicious-Export-for-Full-File-Read]]

**Objective**: Trigger full file read via symlink dereference during project.json restoration and expose contents in JSON decode error.

**Instructions**: Upload the modified tar.gz via the project import interface as in Step 3.

**Expected Output**: JSON parse error message containing the full file contents (e.g., entire /etc/passwd).

**Success Indicators**:
- Import error exposes complete file data
- Secrets like Rails config or tokens readable

### Step 6: Exploit Secrets for RCE
procedure: [[procedures/Exploit-Read-Secrets-for-RCE]]

**Objective**: Use extracted secrets to re-sign cookies for command execution and access internal tokens for repository manipulation.

**Instructions**: From leaked secrets (e.g., secret_key_base from config/secrets.yml), craft and sign malicious cookies to inject Ruby code for RCE; use shell tokens for git operations.

**Expected Output**: Successful command execution on the GitLab server or unauthorized repo access.

**Success Indicators**:
- Cookies re-signed and accepted
- RCE commands run (e.g., via marshal deserialization)
- Internal tokens validated for access

## Attack Chain Summary

### Key Achievements

1. Partial arbitrary file read via VERSION symlink
2. Full arbitrary file read via project.json symlink
3. Extraction of application secrets leading to RCE
4. Access to internal GitLab shell tokens for persistence

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[File and Directory Discovery]] File and Directory Discovery
- [[Command-Line Interface]] Command and Scripting Interpreter

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---

*Last updated: 2023-10-25T00:00:00Z*
