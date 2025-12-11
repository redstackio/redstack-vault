---
tags:
  - info-gathering
  - post-exploitation
type: procedure
tools:
  - '[[tools/tree]]'
  - '[[tools/git]]'
  - '[[tools/docker]]'
  - '[[tools/cat]]'
  - '[[tools/ssh]]'
  - '[[tools/whoami]]'
  - '[[tools/gitlab-rake]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/tree-display]]'
  - '[[commands/git-archive-injected]]'
  - '[[commands/docker-exec-bash]]'
  - '[[commands/cat-file]]'
  - '[[commands/ssh-connect]]'
  - '[[commands/whoami-user]]'
  - '[[commands/gitlab-rake-env]]'
platforms:
  - Linux
techniques:
  - '[[System Information Discovery]]'
skill_level: beginner
impact_level: low
detection_risk: medium
sub_techniques: []
id: f2ec2cee-dd54-47b5-b87d-4c1679f80e2d
created_at: '2025-12-11T06:10:22.634Z'
updated_at: '2025-12-11T06:10:22.634Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1082]]'
---
# Gather Environment Information

## Summary

This procedure collects detailed information about the GitLab environment after gaining access.

## Description

Run GitLab-specific rake tasks to enumerate system details, useful for further exploitation or reconnaissance.

## Requirements

1. Shell access as git user.
2. GitLab rake installed.

## Defense

Defensive measures and detection strategies:

- Monitor rake task executions.
- Limit git user privileges.

## Objectives

1. Retrieve system info.
2. Identify versions and configurations.

## Instructions

### Step 1: Run Rake Task

**Context**: Execute the environment info command.

Execute [[commands/gitlab-rake-env]]:

```bash
gitlab-rake gitlab:env:info
```

> Displays GitLab and system details.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques



## Commands Used

- [[commands/gitlab-rake-env]]

## Tools Used

- [[tools/gitlab-rake]]

## Tags

- [[info-gathering]]
- [[post-exploitation]]
