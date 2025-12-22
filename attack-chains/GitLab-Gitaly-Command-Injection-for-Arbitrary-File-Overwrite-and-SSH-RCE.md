---
tags:
  - command-injection
  - file-overwrite
  - rce
  - gitlab
  - ssh
type: attack_chain
tools:
  - '[[tools/tree]]'
  - '[[tools/git]]'
  - '[[tools/docker]]'
  - '[[tools/cat]]'
  - '[[tools/ssh]]'
  - '[[tools/whoami]]'
  - '[[tools/gitlab-rake]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/tree-display]]'
  - '[[commands/git-archive-injected]]'
  - '[[commands/docker-exec-bash]]'
  - '[[commands/cat-file]]'
  - '[[commands/ssh-connect]]'
  - '[[commands/whoami-user]]'
  - '[[commands/gitlab-rake-env]]'
platforms:
  - Linux
  - Docker
complexity: medium
procedures:
  - '[[procedures/Create-Malicious-Repository-Structure]]'
  - '[[procedures/Trigger-Git-Archive-Download]]'
  - '[[procedures/Verify-File-Overwrite]]'
  - '[[procedures/Exploit-SSH-Access]]'
  - '[[procedures/Gather-Environment-Information]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
description: >-
  Exploitation of a command injection vulnerability in GitLab's Gitaly to
  overwrite arbitrary files and achieve remote code execution via SSH.
skill_level: intermediate
impact_level: high
id: 6adef9ee-3d0f-4e98-940d-9786e5b34352
created_at: '2025-12-11T06:10:22.650Z'
updated_at: '2025-12-11T06:10:22.650Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1059]]'
---
# GitLab Gitaly Command Injection for Arbitrary File Overwrite and SSH RCE

Multi-stage attack chain demonstrating exploitation of a command injection vulnerability in GitLab's Gitaly by injecting git archive options through a malicious repository path, leading to arbitrary file overwrite and remote code execution via SSH.

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
    A[Create Malicious Repo] --> B[Trigger Archive]
    B --> C[Verify Overwrite]
    C --> D[SSH Access]
    D --> E[Gather Info]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#8e44ad
```

## Prerequisites & Requirements

### Required Tools

- [[tools/tree]]
- [[tools/git]]
- [[tools/docker]]
- [[tools/cat]]
- [[tools/ssh]]
- [[tools/whoami]]
- [[tools/gitlab-rake]]

### Target Environment

- Linux-based GitLab server (version 11.11.0)
- Services: GitLab, Gitaly, SSH
- Docker container for GitLab instance

### Initial Access Requirements

- Ability to create repositories in GitLab
- Network access to GitLab web interface and SSH port
- Attacker's SSH key pair

## Detailed Attack Procedures

### Step 1: Create Malicious Repository Structure - [[procedures/Create-Malicious-Repository-Structure]]

**Procedure**: [[procedures/Create-Malicious-Repository-Structure]]

**Objective**: Set up a repository with a directory path that injects git archive options for file overwrite.

**Expected Output**: A repository structure that includes the malicious path and SSH public key.

Use [[commands/tree-display]] to visualize the structure:

```bash
tree
```

The directory path should start with '--output=/var/opt/gitlab/.ssh/authorized_keys/' and contain 'id_ed25519.pub' with the attacker's SSH public key.

**Success Indicators**:
- Directory tree shows the injected path.
- Public key file is present.

### Step 2: Trigger Git Archive Download - [[procedures/Trigger-Git-Archive-Download]]

**Procedure**: [[procedures/Trigger-Git-Archive-Download]]

**Objective**: Initiate the download of the malicious directory as a tar archive in GitLab, triggering the command injection.

**Expected Output**: The git archive command executes with the injected options, overwriting the target file.

Trigger the download, which internally runs [[commands/git-archive-injected]]:

```bash
git --git-dir=DIR_TO_REPO archive --format tar --prefix=/ COMMIT_ID --output=/var/opt/gitlab/.ssh/authorized_keys
```

This writes the archive content to '/var/opt/gitlab/.ssh/authorized_keys' on the server.

**Success Indicators**:
- No errors in GitLab interface.
- File overwrite occurs silently.

### Step 3: Verify File Overwrite - [[procedures/Verify-File-Overwrite]]

**Procedure**: [[procedures/Verify-File-Overwrite]]

**Objective**: Confirm that the authorized_keys file has been overwritten with the malicious content.

**Expected Output**: The file contains tar headers and the injected SSH public key.

Access the server using [[commands/docker-exec-bash]]:

```bash
docker exec -ti e1a bash
```

Then inspect with [[commands/cat-file]]:

```bash
cat /var/opt/gitlab/.ssh/authorized_keys
```

**Success Indicators**:
- Output shows tar headers and public key.
- No original content remains.

### Step 4: Exploit SSH Access - [[procedures/Exploit-SSH-Access]]

**Procedure**: [[procedures/Exploit-SSH-Access]]

**Objective**: Use the overwritten authorized_keys to gain SSH access as the git user.

**Expected Output**: Successful SSH connection and command execution.

Connect using [[commands/ssh-connect]]:

```bash
ssh -i ~/.ssh/id_ed25519 git@10.26.0.3
```

Verify user with [[commands/whoami-user]]:

```bash
whoami
```

**Success Indicators**:
- SSH connection succeeds without password.
- 'whoami' returns 'git'.

### Step 5: Gather Environment Information - [[procedures/Gather-Environment-Information]]

**Procedure**: [[procedures/Gather-Environment-Information]]

**Objective**: Collect details about the compromised GitLab environment.

**Expected Output**: System and GitLab configuration information.

Run [[commands/gitlab-rake-env]]:

```bash
gitlab-rake gitlab:env:info
```

**Success Indicators**:
- Output includes versions like Ruby 2.5.3, GitLab 11.11.0, etc.
- No execution errors.

## Attack Chain Summary

### Key Achievements

1. Successful command injection via git archive.
2. Arbitrary file overwrite leading to SSH key injection.
3. Remote code execution as git user.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01*
