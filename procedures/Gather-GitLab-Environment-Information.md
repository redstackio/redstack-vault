---
tags:
  - recon
  - env-info
type: procedure
tools:
  - '[[tools/ssh]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[System Information Discovery]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: a498f236-cd4a-411c-b69d-01ae25292beb
created_at: '2025-12-11T03:47:39.995Z'
updated_at: '2025-12-11T03:47:39.995Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1082]]'
---
# Gather GitLab Environment Information

## Summary

This procedure gathers detailed environment and configuration information from a compromised GitLab instance using rake tasks.

## Description

After gaining access, run gitlab-rake to display system details like versions of Ruby, Git, and GitLab components for further exploitation or reconnaissance.

## Requirements

1. Shell access to GitLab server as git user
2. GitLab rake installed

## Defense

- Limit rake task execution to authorized users
- Monitor for unusual rake commands

## Objectives

1. Collect system and GitLab config details
2. Support post-exploitation activities

## Instructions

### Step 1: Run Rake Task

**Context**: Execute the environment info task.

Execute [[commands/gitlab-rake-env-info]]:

```bash
gitlab-rake gitlab:env:info
```

> Displays GitLab environment details.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques

## Commands Used

- [[commands/gitlab-rake-env-info]]

## Tools Used

- #gitlab-rake

## Tags

- #recon
