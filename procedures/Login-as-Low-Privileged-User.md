---
id: proc-low-priv-login
tags:
  - initial-access
  - windows
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:27.122Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-as-Low-Privileged-User

## Summary

This procedure establishes a session as a standard, non-administrative user on a Windows system, confirming limited privileges to set up subsequent privilege escalation attempts like DLL hijacking in Burp Suite.

## Description

In the context of exploiting Burp Suite's DLL loading vulnerability, logging in as a low-privileged user is the entry point. This user has default Windows permissions allowing directory creation on the C: drive root, which is crucial for creating hijackable paths. The procedure verifies that the user lacks admin rights, ensuring the escalation potential is real. Expected outcome: A session ready for path manipulation without triggering admin UAC prompts.

## Requirements

1. Valid low-privileged credentials for the target Windows system
2. Local or remote access (e.g., via RDP or console)
3. Burp Suite installed on the system

## Defense

Defensive measures and detection strategies:

- Enforce least privilege: Use non-admin accounts for daily tasks
- Monitor logon events via Windows Event Logs (ID 4624) for unusual low-priv sessions
- Implement AppLocker or WDAC to restrict application launches

## Objectives

1. Secure initial foothold as standard user
2. Verify writable access to C:\ for path creation
3. Prepare for escalation without alerting defenses

## Instructions

### Step 1: Authenticate to System

**Context**: Log in using provided credentials to establish a low-priv session.

No specific command; use Windows login mechanism (e.g., Ctrl+Alt+Del or RDP client).

> Upon success, open Command Prompt and run `whoami /groups` to confirm non-admin status. Expected output: No 'Administrators' group membership.

### Step 2: Verify Permissions

**Context**: Test ability to create test directory on C:\ to confirm exploit feasibility.

Execute a simple mkdir test:

```cmd
mkdir C:\test_dir
```

> If successful, directory is created; delete it afterward with `rmdir C:\test_dir`. This confirms default permissions for authenticated users.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- initial-access
- windows

