---
id: cb75ef2b-9879-48c3-986f-3128f6bdb9bb
name: Clone Wiki Repository and Add Malicious RMD File
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:13.206Z'
updated_at: '2025-12-11T06:10:13.206Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Command-Line Interface]]'
sub_techniques: []
tags:
  - gitlab
  - repo-clone
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
  - Linux
tools:
  - '[[tools/git]]'
  - '[[tools/Kramdown]]'
  - '[[tools/Rouge]]'
  - '[[tools/Redis-rb]]'
  - '[[tools/GetProcessMem]]'
  - '[[tools/GitHub::Markup]]'
  - '[[tools/nc]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---

# Clone Wiki Repository and Add Malicious RMD File

## Summary

Clone the wiki repo and add a .rmd file with malicious Kramdown options for class instantiation.

## Description

The .rmd file uses syntax_highlighter_opts to load arbitrary Ruby classes like Redis, enabling payload execution.

## Requirements

1. Git installed
2. Wiki clone URL
3. Payload path from previous step

## Defense

Defensive measures and detection strategies:

- Validate Kramdown options in rendering
- Monitor git operations on wikis

## Objectives

1. Clone repo
2. Create malicious .rmd
3. Stage file

## Instructions

### Step 1: Clone Repo

**Context**: Clone the wiki repository.

**Command** ([[commands/git-clone-wiki-repo]]):
```bash
git clone git@gitlab-docker.local:root/proj1.wiki.git
```

> Repo cloned.

### Step 2: Add RMD File

**Context**: Create page1.rmd with inline options referencing payload.

No command, manually create file with Kramdown syntax.

> File added.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/git-clone-wiki-repo]]

## Tools Used

- [[tools/git]]
- [[tools/Kramdown]]

## Tags

- [[gitlab]]
- [[commands/git-clone-wiki-repo]]
