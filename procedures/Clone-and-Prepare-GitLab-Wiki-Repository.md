---
id: proc-002
tags:
  - gitlab
  - wiki-clone
  - git
type: procedure
tools:
  - '[[tools/Git]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/git-clone-gitlab-wiki]]'
  - '[[commands/cd-to-wiki-directory]]'
verified: false
platforms:
  - Linux
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:37.775Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Clone-and-Prepare-GitLab-Wiki-Repository

## Summary

This procedure clones the GitLab wiki repository locally and navigates into it, preparing the environment for creating and committing malicious HTML files that exploit the XSS vulnerability.

## Description

GitLab wikis are separate Git repositories, allowing attackers to clone, modify, and push content. This step sets up the local workspace on an attacker-controlled machine, typically Linux or macOS with Git installed. Prerequisites include SSH access to GitLab. Once prepared, files like index.html can be added with XSS payloads that execute when viewed publicly.

## Requirements

1. Git installed (version 2.0+)
2. SSH key added to GitLab account
3. Network access to gitlab.com

## Defense

Defensive measures and detection strategies:

- Restrict wiki push access to trusted users
- Log and alert on wiki clone/push from external IPs
- Implement rate limiting on Git operations

## Objectives

1. Secure a local copy of the wiki for modification
2. Position the working directory for file creation
3. Verify Git connectivity without errors

## Instructions

### Step 1: Clone Wiki Repository

**Context**: Download the empty or existing wiki repo to local machine.

**Command** ([[commands/git-clone-gitlab-wiki]]):
```bash
git clone git@gitlab.com/dummy/test-wiki.git
```

> Clones the wiki repo via SSH. Expected output: 'Cloning into 'test-wiki'... done.' Directory created.

### Step 2: Navigate to Directory

**Context**: Enter the cloned directory to stage files.

**Command** ([[commands/cd-to-wiki-directory]]):
```bash
cd test-wiki
```

> Changes working directory. Expected output: Shell prompt updates to ~/test-wiki.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/git-clone-gitlab-wiki]]
- [[commands/cd-to-wiki-directory]]

## Tools Used

- [[tools/Git]]

## Tags

- gitlab
- wiki-clone
