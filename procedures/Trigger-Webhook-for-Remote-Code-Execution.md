---
tags:
  - rce
  - webhook-trigger
type: procedure
tools:
  - '[[tools/post-auth-nosqli-py]]'
  - '[[tools/requests]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Execution through API]]'
updated_at: '2025-12-14T17:32:20.432Z'
sub_techniques: []
id: 8d0af05c-60e2-42ab-bd97-9a68463f60b1
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Execution through API]]'
---
# Trigger-Webhook-for-Remote-Code-Execution

## Summary

This procedure sends HTTP requests to the malicious webhook URL with payloads that trigger arbitrary command execution on the Rocket.Chat server as the 'rocketchat' user.

## Description

The webhook processes incoming messages, executing the embedded script which spawns child processes for shell commands. No security boundaries allow full RCE, including file access and network operations.

## Requirements

1. Webhook URL and secret
2. Payload crafting for script injection
3. HTTP client for POST

## Defense

- Remove script execution from webhooks
- Network ACLs on internal services
- Monitor for anomalous child process spawns

## Objectives

1. Execute remote commands
2. Gain shell access
3. Compromise instance

## Instructions

### Step 1: Craft Trigger Payload

**Context**: Embed command in message.

**Instructions**: POST {"text": "exec: whoami"} to webhook URL with Authorization: secret.

> Expected: Command runs server-side.

### Step 2: Interact for Shell

**Context**: Chain for interactive access.

**Instructions**: Script provides shell loop via repeated POSTs.

> Expected: Interactive command execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript
- [[Execution through API]] Native API (child_process)

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/requests]]

## Tags

- rce-trigger
