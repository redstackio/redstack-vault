---
id: proc-trigger-mirror-update
tags:
  - rce
  - queue-trigger
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
updated_at: '2025-12-14T04:09:00.695Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
---

# Trigger Mirror Update for Payload Execution

## Summary

This procedure sends a POST to initiate mirroring, processing the injected Redis queue and executing the RCE payload via GitlabShellWorker.

## Description

After payload injection, triggering the mirror update enqueues the job in system_hook_push, leading to class_eval execution of the Python reverse shell code on the GitLab server.

## Requirements

1. Injected mirror with payload
2. Authenticated session
3. Access to project mirror endpoint

## Defense

Defensive measures and detection strategies:

- Validate mirror URLs before processing
- Monitor Resque queues for anomalous jobs
- Log and alert on class_eval usage in workers

## Objectives

1. Activate the mirroring process
2. Execute injected Redis transaction
3. Trigger RCE payload

## Instructions

### Step 1: Send Update Request

**Context**: POST to mirror update endpoint.

**Command** (curl simulate):
```bash
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" "https://{gitlab}/ {username}/{project}/mirror/update_now?sync_remote=true" --cookie "_gitlab_session=..."
```

> Use session cookie from browser. Expected output: 200 OK, mirroring initiated.

### Step 2: Monitor for Execution

**Context**: Check GitLab logs or wait for shell.

**Command** (tail logs):
```bash
# On target: tail -f /var/log/gitlab/gitlab-rails/production.log | grep worker
```

> Expected output: Job processed without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[queue-trigger]]

