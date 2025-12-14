---
tags:
  - git
  - clone
  - gitlab
  - wiki
type: procedure
tools:
  - '[[tools/Git]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/git-clone-gitlab-wiki]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
id: c65cb923-e85f-4480-a91e-74b29275c61d
created_at: '2025-12-13T23:52:55.066Z'
updated_at: '2025-12-13T23:52:55.066Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Clone GitLab Wiki Repository

## Summary

This procedure clones a GitLab project's wiki repository locally, providing the foundation for subsequent modifications in an attack chain targeting stored XSS via commit metadata.

## Description

In the context of exploiting GitLab's wiki rendering vulnerability, cloning the wiki repo allows an attacker with push access to prepare malicious changes. The wiki is stored as a separate Git repository (e.g., project.wiki.git), and cloning via SSH ensures authenticated access. This step requires GitLab project membership and configured SSH keys.

## Requirements

1. Git installed on local machine
2. SSH key added to GitLab account for git@gl.local access
3. Target project path (e.g., root/test)

## Defense

Defensive measures and detection strategies:

- Restrict wiki push access to trusted users via GitLab project permissions
- Monitor Git clone/push logs for anomalous activity from low-privilege accounts

## Objectives

1. Gain local access to wiki files for editing
2. Prepare environment for injecting malicious Git config
3. Enable commit-based payload storage

## Instructions

### Step 1: Execute Clone Command

**Context**: Clone the target wiki repository using SSH URL to authenticate and download the repo.

**Command** ([[commands/git-clone-gitlab-wiki]]):
```bash
git clone git@gl.local:root/test.wiki.git
```

> This command creates a local directory 'test.wiki' with the repo contents. Expected output includes progress messages and completion without authentication errors.

### Step 2: Navigate to Directory

**Context**: Change into the cloned repo to perform further operations.

**Command** (cd):
```bash
cd test.wiki
```

> Verifies access; use `ls` to confirm Markdown files like home.md are present.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/git-clone-gitlab-wiki]]

## Tools Used

- [[tools/Git]]

## Tags

- [[tools/Git]]
- [[clone]]
- [[gitlab]]
- [[wiki]]
