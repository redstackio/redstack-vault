---
id: 7adfef57-6810-42d8-a634-98a0fc9c86b5
name: Push Changes and Trigger Wiki Rendering
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:13.208Z'
updated_at: '2025-12-11T06:10:13.208Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploitation for Client Execution]]'
sub_techniques: []
tags:
  - gitlab
  - push-trigger
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
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1203]]'
---

# Push Changes and Trigger Wiki Rendering

## Summary

Commit and push the malicious file, then load the wiki page to trigger rendering and exploitation.

## Description

Pushing updates the wiki, and loading the page calls Kramdown, instantiating classes and executing code.

## Requirements

1. Cloned repo with added file
2. Git access

## Defense

Defensive measures and detection strategies:

- Sanitize inline options in Kramdown
- Log and alert on wiki rendering errors

## Objectives

1. Commit and push
2. Load page
3. Trigger RCE

## Instructions

### Step 1: Stage Changes

**Context**: Stage all changes.

**Command** ([[commands/git-add-all]]):
```bash
git add -A .
```

> Changes staged.

### Step 2: Commit

**Context**: Commit with message.

**Command** ([[commands/git-commit-message]]):
```bash
git commit -m "page1.rmd"
```

> Committed.

### Step 3: Push

**Context**: Push to remote.

**Command** ([[commands/git-push]]):
```bash
git push
```

> Pushed.

### Step 4: Load Page

**Context**: Refresh and click page1 in UI.

No command, use GitLab UI.

> Exploitation triggered.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques



## Commands Used

- [[commands/git-add-all]]
- [[commands/git-commit-message]]
- [[commands/git-push]]

## Tools Used

- [[tools/git]]

## Tags

- [[gitlab]]
- [[commands/git-push]]
