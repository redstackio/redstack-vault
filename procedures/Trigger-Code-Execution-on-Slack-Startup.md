---
tags:
  - privilege-escalation
  - autostart-execution
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Registry Run Keys - Startup Folder]]'
  - '[[Hijack Execution Flow]]'
updated_at: '2025-12-14T17:29:19.975Z'
sub_techniques: []
id: 01462bae-ecf7-43e0-b3b2-428810457d65
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Registry Run Keys - Startup Folder]]'
  - '[[Hijack Execution Flow]]'
---
# Trigger-Code-Execution-on-Slack-Startup

## Summary

This procedure triggers the execution of the malicious payload by causing the victim's Slack client to start and load the tampered OpenSSL config.

## Description

Slack auto-starts on user login, attempting to load the config from the hardcoded path. This loads the malicious DLL via OpenSSL, executing code in the Slack process context, which can escalate privileges if the victim has higher access on shared systems.

## Requirements

1. Victim user login on the same machine
2. Slack configured for auto-start (default behavior)
3. Malicious config and DLL already deployed

## Defense

Defensive measures and detection strategies:

- Disable auto-start for applications like Slack via Task Manager
- Monitor process creation and DLL loads in Slack with EDR
- Implement least privilege for user accounts on multi-user systems

## Objectives

1. Execute payload in victim's process
2. Achieve privilege escalation to admin or other users
3. Exfiltrate data or maintain access post-execution

## Instructions

### Step 1: Ensure Setup is Complete

**Context**: Verify prior steps.

Confirm directories, config, and DLL are in place and correctly referenced.

### Step 2: Wait for Victim Login

**Context**: Leverage auto-start mechanism.

On a shared system, wait for the target user to log in, triggering Slack startup.

### Step 3: Validate Execution

**Context**: Confirm payload runs.

Monitor for payload indicators, like a spawned process or network connection from the DLL execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Registry Run Keys - Startup Folder]] Registry Run Keys / Startup Folder
- [[Hijack Execution Flow]] Hijack Execution Flow

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[privilege-escalation]]
- [[autostart-execution]]
