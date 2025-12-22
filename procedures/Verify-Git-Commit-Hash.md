---
tags:
  - verification
  - git
type: procedure
tools:
  - '[[tools/git]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/git-rev-parse-head]]'
platforms:
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 3b3a0a4e-a869-4515-8b88-8698e7bb0a34
created_at: '2025-12-13T09:01:16.904Z'
updated_at: '2025-12-13T09:01:16.904Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify Git Commit Hash

## Summary

This procedure verifies the current Git commit hash to ensure the correct version of the Rails code is being used for testing the SSTI vulnerability.

## Description

Checking the commit hash confirms that the codebase matches a known vulnerable state, which is crucial for reproducible security testing and exploitation demonstrations.

## Requirements

1. Inside the cloned repository directory
2. Git installed

## Defense

Defensive measures and detection strategies:

- Track git operations in logs
- Version control auditing

## Objectives

1. Confirm code version
2. Ensure vulnerability presence

## Instructions

### Step 1: Run Rev-Parse

**Context**: Retrieve the SHA-1 hash of the current commit.

**Command** ([[commands/git-rev-parse-head]]):
```bash
git rev-parse HEAD
```

> Outputs the commit hash for verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/git-rev-parse-head]]

## Tools Used

- [[tools/git]]

## Tags

- verification
- git
