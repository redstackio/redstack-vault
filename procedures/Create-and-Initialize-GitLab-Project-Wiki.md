---
id: 794c159b-f6ef-40d9-9599-4199ddabb508
name: Create and Initialize GitLab Project Wiki
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:13.169Z'
updated_at: '2025-12-11T06:10:13.169Z'
tactics:
  - '[[Persistence]]'
techniques:
  - '[[Exploitation for Client Execution]]'
sub_techniques: []
tags:
  - gitlab
  - wiki-setup
commands:
  - '[[commands/ruby-puts-hello]]'
  - '[[commands/ruby-echo-tmp-file]]'
  - '[[commands/git-clone-wiki-repo]]'
  - '[[commands/git-add-all]]'
  - '[[commands/git-commit-message]]'
  - '[[commands/git-push]]'
  - '[[commands/cat-tmp-vakzz]]'
  - '[[commands/ps-memory-injection]]'
  - '[[commands/ruby-echo-inject-tmp]]'
  - '[[commands/id]]'
  - '[[commands/hostname-a]]'
  - '[[commands/ps-auxww]]'
  - '[[commands/exit]]'
  - '[[commands/nc-reverse-shell]]'
platforms:
  - Web
tools:
  - '[[tools/git]]'
  - '[[tools/Kramdown]]'
  - '[[tools/Rouge]]'
  - '[[tools/Redis-rb]]'
  - '[[tools/GetProcessMem]]'
  - '[[tools/GitHub::Markup]]'
  - '[[tools/nc]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1203]]'
---

# Create and Initialize GitLab Project Wiki

## Summary

This procedure creates a new GitLab project and initializes its wiki for hosting malicious content.

## Description

Setting up the wiki allows cloning and pushing of .rmd files that exploit Kramdown vulnerabilities during rendering.

## Requirements

1. GitLab account with project creation access
2. Access to GitLab UI

## Defense

Defensive measures and detection strategies:

- Limit project creation for untrusted users
- Monitor wiki initializations

## Objectives

1. Create project
2. Initialize wiki
3. Obtain clone command

## Instructions

### Step 1: Create Project

**Context**: Create a new project in GitLab UI.

No command, use UI.

> Project created.

### Step 2: Create Wiki Page

**Context**: Initialize wiki with default home page.

Use UI to create home page.

> Wiki initialized.

### Step 3: Get Clone Command

**Context**: Obtain git clone command for wiki repo.

Use UI to copy clone command.

> Clone command ready.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/git]]

## Tags

- [[gitlab]]
- [[wiki-setup]]
