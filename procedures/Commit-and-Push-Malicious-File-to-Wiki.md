---
id: proc-commit-push-malicious
tags:
  - git
  - push
type: procedure
tools:
  - '[[tools/git]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/git-add-commit-push]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Standard Application Layer Protocol]]'
updated_at: '2025-12-14T17:24:15.039Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Standard Application Layer Protocol]]'
---
# Commit-and-Push-Malicious-File-to-Wiki

## Summary

This procedure stages, commits, and pushes the malicious .rmd file to the remote wiki repository, making it available for rendering.

## Description

Using Git, add the exploit file to the wiki repo and push changes. This uploads the content that will trigger RCE upon wiki page load in the GitLab UI.

## Requirements

1. Local wiki repo with malicious file
2. Git configured with push access

## Defense

Defensive measures and detection strategies:

- Review wiki pushes for suspicious .rmd content
- Scan commits for Kramdown options

## Objectives

1. Deploy exploit file to server
2. Position for rendering trigger

## Instructions

### Step 1: Stage Changes

**Context**: Add all files including the malicious .rmd.

Part of [[commands/git-add-commit-push]].

### Step 2: Commit and Push

**Context**: Commit with message and push to remote.

**Command** ([[commands/git-add-commit-push]]):

```bash
git add -A . && git commit -m "page1.rmd" && git push
```

> Expected: [master abc1234] page1.rmd; To git@gitlab.example.com:root/proj1.wiki.git.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Standard Application Layer Protocol]] Application Layer Protocol

### Sub-Techniques


## Commands Used

- [[commands/git-add-commit-push]]

## Tools Used

- [[tools/git]]

## Tags

- git
- push
