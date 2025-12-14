---
tags:
  - gitlab
  - commit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 771dd076-1f6f-4146-9097-808d50bf580f
created_at: '2025-12-14T03:46:09.478Z'
updated_at: '2025-12-14T03:46:09.478Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Add-Commit-to-Repository

## Summary

This procedure adds a commit to a GitLab repository to simulate push events, priming web hooks for testing in SSRF exploitation.

## Description

Commits trigger webhook events in GitLab, essential for exploiting the ToCToU race. This uses standard Git operations on a local clone, pushing changes to activate potential SSRF paths. Prerequisites include a created repository.

## Requirements

1. Local Git installation
2. Cloned repository
3. GitLab credentials for push

## Defense

Defensive measures and detection strategies:

- Rate limit push events
- Audit commit patterns for abuse

## Objectives

1. Trigger webhook activation
2. Set stage for test endpoint fuzzing
3. Validate repository functionality

## Instructions

### Step 1: Create Test File

**Context**: Add content to commit.

**Command** (Echo File):
```bash
echo "Test content" > test.txt
```

> Creates a file for staging.

### Step 2: Commit and Push

**Context**: Stage, commit, and push to trigger events.

**Command** (Git Add/Commit/Push):
```bash
git add test.txt && git commit -m "Test commit" && git push origin main
```

> Expected output: Commit pushed successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[commit]]
- [[push]]
