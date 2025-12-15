---
id: proc-edgeos-op-to-ubnt-001
tags:
  - privilege-escalation
  - file-exposure
  - linux
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/ls-directory-list]]'
  - '[[commands/cat-file-read]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:27.968Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# EdgeOS Operator to Ubnt Escalation

## Summary

This procedure exploits the lack of file-system protections in Ubiquiti EdgeOS to escalate from a read-only operator account to the 'ubnt' user by reading exposed sensitive files and hijacking non-interactive sessions.

## Description

In EdgeOS version 1.9.1 and prior, the file-system lacks adequate protections, allowing operator users to read configuration files, session data, or credentials belonging to the 'ubnt' user. This exposure enables session hijacking without interactive authentication, granting elevated privileges for further exploitation.

## Requirements

1. Valid operator account credentials
2. SSH access to the EdgeOS device
3. Target running EdgeOS 1.9.1 or earlier

## Defense

Defensive measures and detection strategies:

- Implement file-system permissions (e.g., chmod 600 on sensitive files)
- Monitor access logs for unauthorized file reads in /var/run/ or /proc/
- Use SELinux or AppArmor to restrict read access

## Objectives

1. Read exposed sensitive information
2. Hijack 'ubnt' session
3. Achieve 'ubnt' user context

## Instructions

### Step 1: Identify Exposed Directories

**Context**: List directories to find unprotected session or config files.

**Command** ([[commands/ls-directory-list]]):
```bash
ls -la /var/run/ /proc/
```

> This reveals files readable by operator, such as session tokens or env vars.

### Step 2: Read Sensitive File

**Context**: Extract data from an exposed file to obtain session details.

**Command** ([[commands/cat-file-read]]):
```bash
cat /var/run/ubnt-session  # Hypothetical exposed session file
```

> Output includes session ID or credentials; use to impersonate 'ubnt'.

### Step 3: Hijack Session

**Context**: Use extracted data to switch to 'ubnt' context non-interactively.

**Command**:
```bash
export SESSION_ID=$(cat /var/run/ubnt-session | grep token)
su ubnt -c "whoami"
```

> Confirms escalation if output shows 'ubnt'.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/ls-directory-list]]
- [[commands/cat-file-read]]

## Tools Used


## Tags

- [[privilege-escalation]]
- [[linux]]
