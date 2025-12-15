---
tags:
  - rce
  - log-analysis
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/inject-shell-via-env-var]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:23:53.984Z'
sub_techniques: []
id: 2ca27369-c922-445f-9d9d-c7ed0a1eaab6
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Gather Victim Host Information]]'
---
# Monitor-Task-Execution-and-Logs

## Summary

This procedure monitors the queued task's execution status and reviews live logs to confirm RCE, observing output from injected host commands like whoami and ls -lah.

## Description

After submission, tasks are picked up by workers running podman. Due to injection, the task fails, but logs capture host execution before container start. This reveals worker host details, confirming breakout from container isolation. Target is Taskcluster's log viewer; outcomes include evidence of internal access like GCP metadata.

## Requirements

1. Task ID from submission
2. Access to task status/logs page
3. Patience for queue processing (~1-5 minutes)

## Defense

Defensive measures and detection strategies:

- Isolate worker logs from user view or sanitize outputs
- Detect injection patterns in logs (e.g., unexpected shell commands)
- Use container namespaces to prevent host log leakage

## Objectives

1. Verify task run and failure
2. Extract RCE evidence from logs
3. Assess impact on host resources

## Instructions

### Step 1: Check Task Status

**Context**: Poll for execution start.

Navigate to task details page and refresh until status changes to 'running' then 'failed'.

> Expected output: Status updates; logs become available.

### Step 2: View Live Logs

**Context**: Inspect for injected command output using [[commands/inject-shell-via-env-var]] results.

Click 'Live Logs' tab to stream output.

> Expected output: Logs show 'whoami' (e.g., 'root'), 'ls -lah' directory listing, and 'echo hello' from container.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]
- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/inject-shell-via-env-var]]

## Tools Used


## Tags

- rce
- log-analysis
