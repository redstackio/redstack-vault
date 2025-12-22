---
id: 15032b86-0717-47dd-85f3-ddb36fee4cf2
name: Add Malicious RMD File to Wiki
type: procedure
verified: false
submitted: true
created_at: '2025-12-09T00:20:45.036Z'
updated_at: '2025-12-09T00:20:45.036Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Command-Line Interface]]'
sub_techniques: []
tags:
  - rce
  - kramdown
commands: []
platforms:
  - Linux
  - Docker
tools: []
skill_level: advanced
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---

# Add Malicious RMD File to Wiki

## Summary

This procedure adds a malicious .rmd file with exploitative Kramdown options to the Wiki repository and pushes it to the server.

## Description

The .rmd file contains inline options that exploit Kramdown's syntax highlighter to instantiate Ruby classes, enabling RCE via Redis driver and directory traversal to load payloads.

## Requirements

1. Cloned Wiki repository
2. Malicious .rmd file prepared with options like syntax_highlighter_opts
3. Git access

## Defense

Defensive measures and detection strategies:

- Sanitize Kramdown options in rendering
- Monitor Wiki pushes for unusual file extensions

## Objectives

1. Introduce exploit payload into Wiki
2. Enable rendering-based execution
3. Achieve arbitrary code exec

## Instructions

### Step 1: Stage Changes

**Context**: Add the malicious file.

**Command** (#git-add-all-changes):
```bash
git add -A .
```

> Stages all changes including the .rmd file.

### Step 2: Commit Changes

**Context**: Commit the file.

**Command** (#git-commit-changes):
```bash
git commit -m "page1.rmd"
```

> Commits with a message.

### Step 3: Push Changes

**Context**: Upload to server.

**Command** (#git-push-changes):
```bash
git push
```

> Pushes the malicious content.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- #git-add-all-changes
- #git-commit-changes
- #git-push-changes

## Tools Used

- #git

## Tags

- #rce
- #kramdown
