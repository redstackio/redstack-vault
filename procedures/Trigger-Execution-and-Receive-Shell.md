---
id: proc-trigger-shell-001
tags:
  - execution
  - privilege-escalation
  - reverse-shell
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
  - '[[DLL Search Order Hijacking]]'
updated_at: '2025-12-14T17:29:19.629Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
---
# Trigger-Execution-and-Receive-Shell

## Summary

This procedure involves starting a listener, waiting for an admin to launch Acronis True Image (triggering DLL load), and receiving the resulting reverse shell with elevated privileges.

## Description

Once the malicious DLL is in place, an admin running TrueImage.exe as administrator will load tcmalloc.dll from C:\Python27, executing the payload. The attacker listens for the reverse connection to gain an admin shell. Prerequisites: DLL deployed, listener configured. Expected outcome: Interactive shell as local administrator (e.g., 'John').

## Requirements

1. Listener tool (netcat, Metasploit) on attacker machine
2. Malicious DLL in C:\Python27
3. Admin user to launch Acronis

## Defense

Defensive measures and detection strategies:

- Run applications with least privilege; avoid admin for non-essential apps
- Monitor outbound connections from TrueImage.exe (network logs, firewall)
- Use EDR to detect anomalous DLL loads (e.g., unsigned DLLs in PATH)

## Objectives

1. Trigger payload via legitimate app execution
2. Establish elevated shell connection
3. Verify and maintain access

## Instructions

### Step 1: Start Listener

**Context**: Prepare to catch the reverse shell.

On attacker: `nc -lvnp [Attacker-port]` or use Metasploit multi/handler.

### Step 2: Induce Admin Execution

**Context**: Socially engineer or wait for admin to run Acronis.

Admin launches via Start Menu or shortcut as administrator.

> TrueImage.exe searches PATH, loads malicious DLL.

### Step 3: Receive and Interact with Shell

**Context**: Confirm escalation in the incoming session.

Accept connection; run `whoami /priv` to check privileges.

> Expected: Output shows administrator group, SeDebugPrivilege enabled.

### Step 4: Validate Escalation

**Context**: Test elevated actions.

Execute `net localgroup administrators` to list admins.

> Success: Full admin shell from low-priv user action.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[DLL Search Order Hijacking]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- trigger
- shell
- escalation
