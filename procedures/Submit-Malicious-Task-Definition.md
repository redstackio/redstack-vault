---
tags:
  - rce
  - command-injection
type: procedure
tools:
  - '[[tools/podman]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/inject-shell-via-env-var]]'
  - '[[commands/echo-hello]]'
verified: false
platforms:
  - Web
  - Cloud
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:53.986Z'
sub_techniques: []
id: f06931d9-0692-4441-8da3-6cd9a148b8a8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
---
# Submit-Malicious-Task-Definition

## Summary

This procedure involves crafting a JSON task definition with a malicious environment variable name containing shell injection payload, submitting it to the 'proj-misc/tutorial' queue to exploit unsanitized input during podman command construction on the worker host.

## Description

Taskcluster workers use podman to run tasks, constructing commands like 'podman run -e "MALICIOUS_NAME=value" ...'. The env name lacks shell.escape sanitization, unlike image or command fields, allowing injection of commands such as '; whoami ; ls -lah'. This leads to RCE outside the container, potentially accessing GCP metadata. Prerequisites include authenticated access; the attack targets public queues on community-tc.services.mozilla.com.

## Requirements

1. Authenticated session in Taskcluster UI
2. Knowledge of queue ID ('proj-misc/tutorial')
3. Valid Docker image (e.g., ubuntu:latest)

## Defense

Defensive measures and detection strategies:

- Apply shell escaping to all env var names in podman run construction
- Validate env var names against allowlists (alphanumeric only)
- Log and alert on task failures with suspicious log patterns

## Objectives

1. Queue task with injected payload
2. Trigger podman execution with unsanitized env
3. Achieve host-level command execution

## Instructions

### Step 1: Prepare Task JSON

**Context**: Define task payload with malicious env name using [[commands/inject-shell-via-env-var]].

**Command** ([[commands/inject-shell-via-env-var]]):
```json
{
  "version": 1,
  "payload": {
    "image": "ubuntu:latest",
    "command": ["echo", "hello"],
    "env": [{"name": "test2 --help ; whoami ; ls -lah ;:'--help'", "value": "value"}]
  },
  "taskQueueId": "proj-misc/tutorial"
}
```

> This injects shell commands into the env name, which podman parses without escaping, executing on host.

### Step 2: Submit via UI

**Context**: Paste JSON into creation form and queue.

Visit https://community-tc.services.mozilla.com/tasks/create, input the JSON, set parameters, and click 'Save'.

> Expected output: Task queued, ID returned; status 'pending'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/inject-shell-via-env-var]]
- [[commands/echo-hello]]

## Tools Used

- [[tools/podman]]

## Tags

- rce
- command-injection
