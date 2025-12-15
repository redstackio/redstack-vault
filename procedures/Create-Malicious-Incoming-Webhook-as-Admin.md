---
tags:
  - webhook
  - persistence
type: procedure
tools:
  - '[[tools/post-auth-nosqli-py]]'
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Additional Cloud Credentials]]'
updated_at: '2025-12-14T17:32:20.435Z'
sub_techniques: []
id: 67a036ca-b94f-409d-a8a0-ab1fa60b8afd
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Additional Cloud Credentials]]'
---
# Create-Malicious-Incoming-Webhook-as-Admin

## Summary

This procedure leverages admin privileges to create an incoming webhook integration configured with arbitrary script execution, serving as a backdoor for RCE.

## Description

Rocket.Chat allows admins to set up incoming webhooks that run scripts on incoming messages. A malicious payload is embedded in the script field, e.g., executing system commands, without sandboxing, running as the server user.

## Requirements

1. Admin authentication
2. Access to integrations UI or API
3. Script payload for command exec

## Defense

- Disable or sandbox webhook scripts
- Review all integrations regularly
- Log webhook creations and executions

## Objectives

1. Establish RCE vector
2. Obtain webhook URL/secret
3. Enable command injection

## Instructions

### Step 1: Configure Webhook

**Context**: Use admin panel.

**Instructions**: Create incoming integration named 'backdoor-9Fbd6E5A' with script: e.g., require('child_process').exec('command');

> Expected: Webhook URL like /api/v1/incoming/... with secret.

### Step 2: Test Configuration

**Context**: Verify setup.

**Instructions**: Send test message.

> Expected: Script runs if payload correct.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Additional Cloud Credentials]] Replication Through Removable Media (adapted for webhooks)

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/post-auth-nosqli-py]]

## Tags

- malicious-webhook
