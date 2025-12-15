---
id: proc-restart-unicorn
tags:
  - persistence
  - gitlab
  - race-condition
type: procedure
tools:
  - '[[tools/gitlab-ctl]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/gitlab-ctl-restart-unicorn]]'
verified: false
platforms:
  - Linux
  - Docker
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Shortcut Modification]]'
updated_at: '2025-12-14T17:24:08.774Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Shortcut Modification]]'
---
# Restart-Unicorn-to-Persist-Overwrites

## Summary

This procedure handles race conditions by spamming API requests and restarting Unicorn to ensure file overwrites persist across service restarts.

## Description

In scenarios where truncation occurs before shutdown, parallel requests (e.g., 32) allow the last git log to complete writing before rev-list, then gitlab-ctl restarts the web server to lock in changes.

## Requirements

1. Server access for gitlab-ctl
2. Ability to spam API (scripted curl)
3. GitLab Omnibus installation

## Defense

Defensive measures and detection strategies:

- Rate limit API to prevent spamming
- Monitor service restarts and file changes
- Use container isolation for secrets

## Objectives

1. Mitigate truncation in races
2. Persist overwrites
3. Maintain access post-restart

## Instructions

### Step 1: Spam Requests

**Context**: Send multiple parallel injections to race the write.

No specific command; use tools like ab or parallel curl to hit the API 32 times targeting the secret.

> Ensures last write completes.

### Step 2: Restart Service

**Context**: Restart Unicorn to apply persistence.

**Command** ([[commands/gitlab-ctl-restart-unicorn]]):
```bash
gitlab-ctl restart unicorn
```

> Service restarts; overwrites survive.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Shortcut Modification]]

### Sub-Techniques


## Commands Used

- [[commands/gitlab-ctl-restart-unicorn]]

## Tools Used

- [[tools/gitlab-ctl]]

## Tags

- [[Persistence]]
- [[race-condition]]
