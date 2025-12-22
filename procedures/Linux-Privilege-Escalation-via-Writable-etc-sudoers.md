---
id: d54bfdf2-dc76-4c32-aac2-81942077d102
name: Linux-Privilege-Escalation-via-Writable-etc-sudoers
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:19.297121+00:00'
updated_at: '2023-04-10T20:34:29.628566+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Abuse Elevation Control Mechanism|T1548 - Abuse Elevation
    Control Mechanism]]
sub_techniques: []
tags:
  - '[[tags/Linux - Privilege Escalation]]'
  - '[[tags/Writable /etc/sudoers]]'
  - '[[tags/Writable files]]'
commands:
  - '[[commands/add-sudo-permissions-for-user]]'
  - '[[commands/allow-user-sudo-without-password]]'
  - '[[commands/allow-user-run-bash-without-password]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Privilege-Escalation-via-Writable-etc-sudoers

## Summary

This procedure exploits a writable /etc/sudoers file on a Linux system to grant elevated sudo privileges to a specified user account. By appending specific entries to the sudoers file, an attacker can enable the user to execute commands as root, including without requiring a password, facilitating persistence and further lateral movement in a compromised environment.

## Description

Privilege escalation via a writable /etc/sudoers file targets a misconfiguration where the sudoers configuration file lacks proper permissions, allowing non-root users to modify it. The /etc/sudoers file controls sudo access, defining which users can run what commands with elevated privileges. An attacker with write access can append lines to grant full sudo capabilities or passwordless execution to a target user. This technique is particularly effective in environments with poor file permission controls and can lead to full root access. Note that directly appending via echo bypasses syntax checking (use 'visudo' for safer editing to avoid locking out sudo), but for rapid exploitation, echo is often used. This maps to MITRE ATT&CK technique T1548 for abusing elevation mechanisms and is common in Linux post-exploitation scenarios.

## Requirements

1. Local access to a low-privileged user account on the target Linux system.
2. Write permissions on /etc/sudoers (verifiable via 'ls -l /etc/sudoers' showing writable by the current user).
3. Basic knowledge of the target username to escalate.
4. No additional tools required beyond standard bash shell access.

## Defense

- Enforce strict permissions on /etc/sudoers (mode 0440, owned by root:root) to prevent writes by non-root users.
- Enable file integrity monitoring (e.g., via auditd or Tripwire) to detect unauthorized modifications to /etc/sudoers.
- Regularly audit sudoers file contents and use 'visudo' for all edits to validate syntax.
- Implement principle of least privilege and monitor for anomalous sudo usage via logs (/var/log/auth.log).

## Objectives

1. Grant a user full sudo access to execute arbitrary commands as root.
2. Enable passwordless sudo for seamless escalation without prompting.
3. Establish persistence through elevated account control for further network compromise.

## Instructions

### Step 1: Verify Writable /etc/sudoers

**Context**: Before modification, confirm the file is writable to ensure the technique is viable. This prevents failed attempts and verifies the misconfiguration.

Run a permission check:

```bash
ls -l /etc/sudoers
```

> This command lists file permissions. Look for 'w' in the group or other permissions indicating writability.

### Step 2: Add Basic Sudo Permissions for the User

**Context**: Append an entry granting the user full sudo access to all commands. Replace 'username' with the target user. This step provides standard elevated access but may still require the user's password.

**Command** ([[commands/add-sudo-permissions-for-user]]):

```bash
echo "$_USERNAME ALL=(ALL:ALL) ALL" >> /etc/sudoers
```

> This appends the sudoers line directly. Expected output is silent (no stdout), but verify by running 'tail /etc/sudoers' to see the new line. Warning: This bypasses syntax checks; use 'sudo visudo' in production to avoid errors.

### Step 3: Allow Passwordless Sudo for All Commands

**Context**: Extend privileges to allow the user to run any sudo command without entering a password, reducing friction for escalation and automation.

**Command** ([[commands/allow-user-sudo-without-password]]):

```bash
echo "$_USERNAME ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
```

> Appends the NOPASSWD directive. Silent execution; verify with 'tail /etc/sudoers'. The user can now run 'sudo command' without password prompts.

### Step 4: Allow Passwordless Execution of /bin/bash

**Context**: Specifically enable passwordless root shell access via bash, allowing direct root shell spawning for full control.

**Command** ([[commands/allow-user-run-bash-without-password]]):

```bash
echo "$_USERNAME ALL=NOPASSWD: /bin/bash" >> /etc/sudoers
```

> Targets bash specifically for shell access. Silent; verify addition in file. Success allows 'sudo /bin/bash' to drop into root shell without password.

### Step 5: Validate Escalation

**Context**: Test the modifications by attempting sudo access as the target user to confirm privileges were granted successfully.

Switch to the user if needed (or test inline):

```bash
su - $_USERNAME
sudo whoami
```

> Should output 'root' without password prompt. If errors occur, check sudoers syntax with 'visudo -c'.
