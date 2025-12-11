---
tags:
  - gitlab
  - hash-calculation
  - repository-path
type: procedure
tools:
  - '[[tools/fake_server.py]]'
  - '[[tools/Flask]]'
  - '[[tools/Browser-Console]]'
  - '[[tools/Digest::SHA2]]'
  - '[[tools/Git]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - GitLab.com
techniques:
  - '[[Data from Information Repositories]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: e647a2f4-04af-495a-82a7-9a053c46a63d
created_at: '2025-12-11T03:47:59.555Z'
updated_at: '2025-12-11T03:47:59.555Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1213]]'
---
# Calculate GitLab Repository Path from Project ID

## Summary

This procedure computes the hashed storage path for a GitLab repository using the project ID, enabling attackers to target specific local repositories for exploitation.

## Description

GitLab stores repositories in hashed directories based on the SHA256 hash of the project ID. By calculating this hash, an attacker can construct the exact file path needed for 'file://' protocol injection. This is a preparatory step for exploiting import vulnerabilities, targeting environments like GitLab.com or self-hosted instances.

## Requirements

1. Knowledge of the target project ID
2. Ruby environment or tool for SHA256 hashing
3. Access to GitLab to verify project existence (optional)

## Defense

Defensive measures and detection strategies:

- Monitor for unusual repository access patterns in GitLab logs
- Restrict import features to trusted sources and validate URLs strictly

## Objectives

1. Generate accurate repository path for exploitation
2. Enable precise targeting of private projects
3. Prepare payload for import bypass

## Instructions

### Step 1: Obtain Project ID

**Context**: Identify the target project's ID from GitLab (e.g., via API or URL).

Create a private project and note its ID, e.g., 38006449.

### Step 2: Compute SHA256 Hash

**Context**: Use Digest::SHA2 to hash the project ID string.

**Command** ([[commands/sha256-hash-project-id]]):
```ruby
Digest::SHA2.hexdigest("38006449")
```

> This computes the hash 'b174103b399555239923697fbe124faa61de4d441bd5c5678275eb0a5a27a562'.

### Step 3: Construct Path

**Context**: Build the full path using hash bucketing.

Format as '@hashed/xx/yy/hash.git', where xx and yy are the first two pairs of hash digits (e.g., b1/74).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques



## Commands Used

- [[commands/sha256-hash-project-id]]

## Tools Used

- [[tools/Digest::SHA2]]

## Tags

- #gitlab
- #hash-calculation
- #repository-path
