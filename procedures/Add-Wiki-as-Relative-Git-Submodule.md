---
id: proc-uuid-2
tags:
  - gitlab
  - git-submodule
  - relative-path
type: procedure
tools:
  - '[[tools/git]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/git-submodule-add-relative]]'
  - '[[commands/git-add-submodule]]'
  - '[[commands/git-commit-message]]'
  - '[[commands/git-push-changes]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:23.336Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Add-Wiki-as-Relative-Git-Submodule

## Summary

This procedure adds the wiki repository as a relative git submodule to the main project, generating the .gitmodules file which will later be abused for XSS payload injection.

## Description

To exploit the stored XSS, the wiki must be linked as a submodule using a relative path. This creates .gitmodules with a modifiable URL field. The procedure assumes initialized repositories and uses relative paths to avoid absolute URL validation issues. Expected outcome: Submodule integrated into the project structure.

## Requirements

1. Initialized project and wiki repositories locally
2. Working directory in the project root
3. Git configured with upstream remote

## Defense

Defensive measures and detection strategies:

- Validate submodule URLs during push to block relative or suspicious schemes
- Require code reviews for .gitmodules changes
- Scan for submodule additions in CI/CD pipelines

## Objectives

1. Integrate wiki as a submodule for directory visibility in Files overview
2. Create editable .gitmodules file for payload insertion
3. Maintain project integrity for victim interaction

## Instructions

### Step 1: Add Submodule with Relative Path

**Context**: Link the wiki using a relative path to create the submodule.

**Command** ([[commands/git-submodule-add-relative]]):
```bash
git submodule add ../project.wiki wiki
```

> Adds the submodule at path 'wiki'. Expected output: .gitmodules file created with relative URL.

### Step 2: Stage and Commit Submodule

**Context**: Prepare the submodule addition for commit.

**Command** ([[commands/git-add-submodule]]):
```bash
git add wiki
```

**Command** ([[commands/git-commit-message]]):
```bash
git commit -am "Added relative wiki module"
```

> Commits the .gitmodules and submodule reference. Expected output: Commit created.

### Step 3: Push Changes

**Context**: Upload the submodule configuration to GitLab.

**Command** ([[commands/git-push-changes]]):
```bash
git push
```

> Pushes to remote. Expected output: Changes synchronized.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/git-submodule-add-relative]]
- [[commands/git-add-submodule]]
- [[commands/git-commit-message]]
- [[commands/git-push-changes]]

## Tools Used

- [[tools/git]]

## Tags

- [[gitlab]]
- [[git-submodule]]
- [[relative-path]]
