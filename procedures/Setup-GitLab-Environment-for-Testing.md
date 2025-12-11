---
tags:
  - gitlab
  - setup
type: procedure
tools:
  - '[[tools/Flask]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 04fb004d-cf2c-41e4-ae41-e1725729301a
created_at: '2025-12-11T03:48:06.015Z'
updated_at: '2025-12-11T03:48:06.015Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Setup GitLab Environment for Testing

## Summary

This procedure sets up a local GitLab instance, enables the bulk import feature, and starts log monitoring for testing vulnerabilities.

## Description

Involves spinning up GitLab, accessing the Rails console to enable features, and tailing logs to observe exploitation attempts. This is crucial for safely testing server-side vulnerabilities like command injection in a controlled environment.

## Requirements

1. Linux host (e.g., Ubuntu 20.04)
2. GitLab installed
3. Sudo access for commands

## Defense

Defensive measures and detection strategies:

- Monitor feature flag changes in Rails console
- Audit log access and unusual service starts

## Objectives

1. Prepare testable GitLab server
2. Enable bulk imports
3. Monitor for exploitation signs

## Instructions

### Step 1: Access Rails Console

**Context**: Open the GitLab Rails console to modify configurations.

**Command** ([[commands/gitlab-rails-console]]):
```bash
sudo gitlab-rails console
```

> Opens the interactive Rails console for feature management.

### Step 2: Enable Feature Flag

**Context**: Activate the bulk_import_projects feature.

**Command** ([[commands/enable-feature-flag]]):
```bash
::Feature.enable(:bulk_import_projects)
```

> Enables the feature, returning true on success.

### Step 3: Start Log Monitoring

**Context**: Tail GitLab logs to watch for activity during tests.

**Command** ([[commands/gitlab-ctl-tail]]):
```bash
sudo gitlab-ctl tail
```

> Streams logs in real-time.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/gitlab-rails-console]]
- [[commands/enable-feature-flag]]
- [[commands/gitlab-ctl-tail]]

## Tools Used

- #gitlab-rails
- #gitlab-ctl

## Tags

- #gitlab-rails
- #setup
