---
tags:
  - information-disclosure
  - sidekiq
  - gitlab
type: procedure
tools:
  - '[[tools/Sidekiq]]'
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Linux
  - Web
techniques:
  - '[[Data from Local System]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[T1005.001]]'
id: 84917614-8669-475c-b0e0-ce41318f31d2
created_at: '2025-12-14T17:24:19.271Z'
updated_at: '2025-12-14T17:24:19.271Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Trigger-Sidekiq-Processing-to-Disclose-Data

## Summary

This procedure waits for or simulates the Sidekiq job execution on the overwritten file, resulting in the restoration of victim repository data into the attacker's project for unauthorized access.

## Description

Sidekiq unpacks the tar.gz in the shared directory, extracting repository objects (commits, files, history) and applying them to the target project. Since the file was overwritten, the attacker's project receives the victim's data. For reproduction, control Sidekiq timing by stopping/starting workers.

## Requirements

1. Sidekiq running on the GitLab instance.
2. Access to the first project's UI for monitoring.
3. For local repro: Admin access to stop/start Sidekiq.

## Defense

Defensive measures and detection strategies:

- Process imports synchronously or with immediate validation.
- Isolate upload storage per project/namespace.
- Alert on import jobs completing with mismatched data sizes or sources.

## Objectives

1. Execute the pending job to unpack overwritten contents.
2. Observe victim data integration into attacker's repo.
3. Validate disclosure by inspecting project contents.

## Instructions

### Step 1: Monitor Job Queue

**Context**: Wait for natural Sidekiq processing or force via restart.

Check GitLab admin or Sidekiq dashboard for the enqueued import job.

> Expected: Job status changes from pending to processing.

### Step 2: Simulate Delay for Reproduction

**Context**: In a local setup, stop Sidekiq to widen the race window.

Run `gitlab-ctl stop sidekiq` before uploads, then `gitlab-ctl start sidekiq` after second upload.

> Expected: Both jobs process the last (victim) file, duplicating contents in projects.

### Step 3: Verify Disclosure

**Context**: Inspect the restored project for victim data.

Clone or view the project repo in GitLab UI; check files, commits for foreign content.

> Expected: Victim's confidential repository fully restored, e.g., private code visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Local System]]

### Sub-Techniques

- [[T1005.001]]

## Commands Used



## Tools Used

- [[tools/Sidekiq]]

## Tags

- [[information-disclosure]]
- [[data-restoration]]
