---
id: proc-deploy-payload
tags:
  - git
  - push
  - deploy
type: procedure
tools:
  - '[[tools/git]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/git-add-wiki]]'
  - '[[commands/git-commit-wiki]]'
  - '[[commands/git-push]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:50.167Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Deploy-Wiki-Payload-via-Git

## Summary

This procedure stages, commits, and pushes the malicious wiki file to the GitLab repository, updating the server-side content for rendering.

## Description

Using git in the cloned wiki repo, this adds the payload file and synchronizes with the remote. Authentication is required for push. Upon push, GitLab prepares the wiki for rendering, but execution occurs on view. Prerequisites: Cloned repo with hello.wiki; outcomes: Payload live on server, ready for trigger.

## Requirements

1. Local git repo cloned from wiki
2. Authenticated git remote (HTTPS token or SSH)
3. hello.wiki file in working directory

## Defense

Defensive measures and detection strategies:

- Review wiki commit messages and diffs for Lua code
- Block pushes containing <lua> tags via pre-receive hooks
- Log all wiki pushes and alert on suspicious patterns

## Objectives

1. Upload payload without errors
2. Trigger server update for rendering
3. Maintain stealth in commit message

## Instructions

### Step 1: Stage File

**Context**: Add the malicious file to git staging.

**Command** ([[commands/git-add-wiki]]):
```bash
git add hello.wiki
```

> Stages changes. Expected output: 'new file: hello.wiki'.

### Step 2: Commit Changes

**Context**: Record the addition with a benign message.

**Command** ([[commands/git-commit-wiki]]):
```bash
git commit -m 'Add exploit wiki page'
```

> Creates commit. Expected output: Commit hash and '1 file changed'.

### Step 3: Push to Remote

**Context**: Upload to GitLab server.

**Command** ([[commands/git-push]]):
```bash
git push
```

> Syncs with origin. Expected output: 'Branch master set up to track' and push counts.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/git-add-wiki]]
- [[commands/git-commit-wiki]]
- [[commands/git-push]]

## Tools Used

- [[tools/git]]

## Tags

- git
- push
- deploy
