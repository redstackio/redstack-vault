---
id: ac-ubiquiti-edgeos-privesc-001
tags:
  - privilege-escalation
  - linux
  - ubiquiti
  - edgeos
  - session-hijacking
  - file-exposure
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/EdgeOS-Operator-to-Ubnt-Escalation]]'
  - '[[procedures/EdgeOS-Ubnt-to-Root-Session-Hijacking]]'
step_count: 3
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:27.972Z'
description: >-
  Multi-stage privilege escalation in Ubiquiti EdgeOS exploiting file-system
  vulnerabilities to hijack sessions and gain root access from a read-only
  operator account.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
---
# EdgeOS Privilege Escalation from Operator to Root via File-System Exposure and Session Hijacking

Multi-stage attack chain demonstrating privilege escalation in Ubiquiti EdgeOS version 1.9.1 and prior, where lack of file-system protections allows an attacker with read-only operator access to expose sensitive information, hijack non-interactive sessions, and achieve root control.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Operator Access] --> B[File-System Exploitation]
    B --> C[Session Hijacking to Ubnt]
    C --> D[Root Escalation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (built-in Linux commands)

### Target Environment

- Ubiquiti EdgeOS version 1.9.1 or prior
- Linux-based router OS
- Operator (read-only) account access

### Initial Access Requirements

- Valid operator credentials
- SSH or console access to the device
- No prior root access required

## Detailed Attack Procedures

### Step 1: Gain Operator Access

procedure: [[procedures/EdgeOS-Login-as-Operator]]

**Objective**: Establish initial read-only access to the EdgeOS system.

**Instructions**: Use SSH to connect with operator credentials. This provides limited read access but no write or execute privileges.

```bash
ssh operator@edgeos-device-ip
```

**Expected Output**: Successful login prompt to the EdgeOS shell.

**Success Indicators**:
- Shell access granted
- User context shows 'operator' privileges

### Step 2: Exploit File-System Exposure for Ubnt Escalation

procedure: [[procedures/EdgeOS-Operator-to-Ubnt-Escalation]]

**Objective**: Leverage lack of file-system protections to read sensitive files and hijack a non-interactive session to the 'ubnt' user.

**Instructions**: Navigate to exposed directories and read configuration or session files that reveal 'ubnt' credentials or active sessions. Use file reading commands to extract data.

```bash
ls -la /var/run/
cat /var/run/ubnt-session-file  # Example exposed session file
```

Then, hijack the session by impersonating the 'ubnt' process using the exposed information.

**Expected Output**: Access to 'ubnt' user context, with elevated privileges over operator.

**Success Indicators**:
- Sensitive files readable without restrictions
- Successful switch to 'ubnt' user shell

### Step 3: Escalate to Root via Session Hijacking

procedure: [[procedures/EdgeOS-Ubnt-to-Root-Session-Hijacking]]

**Objective**: From 'ubnt' context, hijack a non-interactive root session to gain full administrative control.

**Instructions**: Identify running root processes or sudo sessions via exposed proc files, then inject or hijack using the lack of protections.

```bash
ps aux | grep root
cat /proc/[pid]/environ  # Read environment from root process PID
sudo -i  # Attempt non-interactive hijack if sudoers exposed
```

**Expected Output**: Root shell prompt (#).

**Success Indicators**:
- Root privileges confirmed via 'id' command
- Full system control achieved

## Attack Chain Summary

### Key Achievements

1. Initial operator access established
2. Privilege escalation to 'ubnt' via file exposure
3. Root access via session hijacking, enabling full administrative control

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---
*Last updated: 2023-10-01T00:00:00Z*
