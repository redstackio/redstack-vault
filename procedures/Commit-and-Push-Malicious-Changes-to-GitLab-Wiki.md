---
tags:
  - git-commit
  - git-push
  - gitlab
type: procedure
tools:
  - '[[tools/Git]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/git-add-all]]'
  - '[[commands/git-commit-message]]'
  - '[[commands/git-push-origin-main]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
sub_techniques: []
id: 80d1e248-bf23-4d0c-b1c8-db2f54219e65
created_at: '2025-12-13T23:52:55.059Z'
updated_at: '2025-12-13T23:52:55.059Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Commit and Push Malicious Changes to GitLab Wiki

## Summary

This procedure stages, commits, and pushes wiki modifications to the GitLab server, embedding the XSS payload in the commit author email for persistent storage and rendering exploitation.

## Description

The commit process records the local Git config email as the author, which GitLab uses unsanitized in wiki_page_version.rb. Pushing updates the remote repo, making the tainted page available for viewing and triggering XSS in show.html.haml line 10.

## Requirements

1. Modified wiki files staged
2. Push access to the wiki repo
3. Remote origin configured (default after clone)

## Defense

Defensive measures and detection strategies:

- Sanitize all Git metadata on server-side before rendering
- Use webhooks to scan commits for malicious patterns in author fields
- Enforce signed commits to verify author integrity

## Objectives

1. Persist the payload in Git history
2. Update the live wiki page
3. Enable victim interaction for execution

## Instructions

### Step 1: Stage Changes

**Context**: Add all modifications to the Git index for commit.

**Command** ([[commands/git-add-all]]):
```bash
git add .
```

> Stages files like home.md. Expected output: No files to stage if none modified, or confirmation.

### Step 2: Commit Changes

**Context**: Create a commit with the malicious author email.

**Command** ([[commands/git-commit-message]]):
```bash
git commit -m "Update home page"
```

> Records the commit with tainted email. Expected output: Commit hash and summary.

### Step 3: Push to Remote

**Context**: Upload the commit to GitLab's wiki repo.

**Command** ([[commands/git-push-origin-main]]):
```bash
git push origin main
```

> Syncs changes remotely. Expected output: Push successful, branch updated.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/git-add-all]]
- [[commands/git-commit-message]]
- [[commands/git-push-origin-main]]

## Tools Used

- [[tools/Git]]

## Tags

- [[git-commit]]
- [[git-push]]
- [[gitlab]]
