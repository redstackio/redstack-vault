---
id: proc-uuid-1
tags:
  - gitlab
  - git-init
  - repository-setup
type: procedure
tools:
  - '[[tools/git]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/git-clone-repository]]'
  - '[[commands/touch-file]]'
  - '[[commands/git-add-file]]'
  - '[[commands/git-commit-message]]'
  - '[[commands/git-push-changes]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:47:23.338Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Initialize-GitLab-Project-and-Wiki-Repositories

## Summary

This procedure sets up local GitLab project and wiki repositories by cloning them and adding initial commits, preparing the environment for adding submodules and injecting payloads in a stored XSS attack.

## Description

In the context of exploiting a stored XSS in GitLab's Files overview, this procedure creates working local copies of the project and its wiki. It involves cloning via SSH, initializing empty repositories with dummy files, and pushing initial commits. This ensures the repositories are active and ready for submodule operations. Prerequisites include a GitLab account with push access and SSH keys configured.

## Requirements

1. GitLab account with create/push permissions
2. SSH access to GitLab (git@gitlab.com)
3. Local Git installation
4. Network connectivity to GitLab

## Defense

Defensive measures and detection strategies:

- Enforce repository initialization policies requiring code reviews for initial commits
- Monitor for unusual clone/push patterns from new repositories
- Use GitLab's audit logs to track repository creation and initial pushes

## Objectives

1. Establish local development environment for the target project
2. Ensure wiki repository is initialized for submodule linking
3. Prepare for secure payload injection without triggering early validation

## Instructions

### Step 1: Clone Project Repository

**Context**: Create a local copy of the main project repository to work on.

**Command** ([[commands/git-clone-repository]]):
```bash
git clone git@gitlab.com:user/project
```

> Clones the repository to a local 'project' directory. Expected output: Local copy with Git history.

### Step 2: Initialize Project with Initial File

**Context**: Add a dummy file to enable committing and pushing.

**Command** ([[commands/touch-file]]):
```bash
touch some-file
```

**Command** ([[commands/git-add-file]]):
```bash
git add some-file
```

**Command** ([[commands/git-commit-message]]):
```bash
git commit -am "Added file to initialize project repository"
```

**Command** ([[commands/git-push-changes]]):
```bash
git push
```

> Creates and pushes an initial commit. Expected output: Commit hash and push confirmation.

### Step 3: Repeat for Wiki Repository

**Context**: Clone and initialize the wiki similarly.

**Command** ([[commands/git-clone-repository]]):
```bash
git clone git@gitlab.com:user/project.wiki
```

**Command** ([[commands/touch-file]]):
```bash
touch some-file
```

**Command** ([[commands/git-add-file]]):
```bash
git add some-file
```

**Command** ([[commands/git-commit-message]]):
```bash
git commit -am "Added file to initialize wiki repository"
```

**Command** ([[commands/git-push-changes]]):
```bash
git push
```

> Expected output: Wiki repository initialized and pushed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/git-clone-repository]]
- [[commands/touch-file]]
- [[commands/git-add-file]]
- [[commands/git-commit-message]]
- [[commands/git-push-changes]]

## Tools Used

- [[tools/git]]

## Tags

- [[gitlab]]
- [[git-init]]
- [[repository-setup]]
