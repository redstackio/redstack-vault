---
id: proc-execute-commands-docker
tags:
  - rce
  - execution
  - bash
  - docker
type: procedure
tools:
  - '[[tools/Portainer]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Docker
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:28.045Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Execute Arbitrary Commands on Docker Containers

## Summary

This procedure leverages Portainer's console feature to run bash commands inside Docker containers, achieving RCE and potential compromise of services like Nextcloud's production environment.

## Description

With admin access, the Portainer UI allows selecting a container and opening a shell session to execute commands, such as reconnaissance or payload deployment. In the Nextcloud case, this enabled interaction with 17 containers, risking malware or DDoS. Prerequisites: container access via Portainer. Outcomes: full control over container processes.

## Requirements

1. Authenticated Portainer session with container visibility
2. Target container running and accessible
3. Knowledge of Unix shell commands

## Defense

Defensive measures and detection strategies:

- Disable console access in Portainer for non-admin users
- Run containers with minimal privileges and read-only filesystems
- Audit logs for unusual command executions in containers

## Objectives

1. Run arbitrary code within containers
2. Verify execution control
3. Escalate to service takeover or data exfiltration

## Instructions

### Step 1: Select and Open Container Console

**Context**: Choose a target container to initiate a shell session.

In the Containers list, click on a container (e.g., production), then select 'Console'.

> A terminal-like interface opens, ready for command input.

### Step 2: Execute Bash Commands

**Context**: Input and run commands to test and exploit.

Type and execute: `whoami` or `bash -c 'ls -la /'`.

> Output appears in the console, confirming RCE; extend to `curl` for external callbacks or script deployment.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Portainer]]

## Tags

- [[rce]]
- [[Execution]]
