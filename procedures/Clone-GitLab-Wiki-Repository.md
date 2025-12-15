---
id: proc-clone-wiki-repo
tags:
  - git
  - clone
type: procedure
tools:
  - '[[tools/git]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/git-clone-wiki-repo]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Standard Application Layer Protocol]]'
updated_at: '2025-12-14T17:24:15.056Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Standard Application Layer Protocol]]'
---
# Clone-GitLab-Wiki-Repository

## Summary

This procedure clones the GitLab wiki repository locally to allow modification and addition of exploit files.

## Description

GitLab wikis are Git repos with .wiki.git suffix. Cloning provides a local working copy for adding the malicious .rmd file before pushing changes back.

## Requirements

1. Git installed locally
2. SSH or HTTPS access to GitLab
3. Wiki repo URL from project settings

## Defense

Defensive measures and detection strategies:

- Monitor git clone activity from internal networks
- Enforce MFA for git access

## Objectives

1. Obtain local editable copy of wiki
2. Prepare for file injection

## Instructions

### Step 1: Obtain Clone URL

**Context**: Get the repository clone command from GitLab UI.

No command; in Project > Wiki > Clone repository button.

> Copy SSH URL like git@gitlab.example.com:root/proj1.wiki.git.

### Step 2: Execute Clone

**Context**: Clone the repo to local machine.

**Command** ([[commands/git-clone-wiki-repo]]):

```bash
git clone git@gitlab.example.com:root/proj1.wiki.git
```

> Clones the wiki repo; expected output: Cloning into 'proj1.wiki'...

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Standard Application Layer Protocol]] Application Layer Protocol (Git)

### Sub-Techniques


## Commands Used

- [[commands/git-clone-wiki-repo]]

## Tools Used

- [[tools/git]]

## Tags

- git
- clone
