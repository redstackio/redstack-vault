---
id: 0486e193-04ec-4969-9235-70959a2b96f0
name: Linux-Privilege-Escalation-via-Doas-Misconfiguration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:19.048387+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Abuse Elevation Control Mechanism|T1548 - Abuse Elevation
    Control Mechanism]]
sub_techniques:
  - >-
    [[sub-techniques/Bypass User Account Control|T1548.002 - Bypass User Account
    Control]]
tags:
  - '[[tags/Doas]]'
  - '[[tags/Linux - Privilege Escalation]]'
  - '[[tags/SUDO]]'
commands:
  - '[[commands/check-doas-presence]]'
  - '[[commands/view-doas-configuration]]'
  - '[[commands/exploit-doas-vim-misconfig]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-Privilege-Escalation-via-Doas-Misconfiguration

## Summary

This procedure outlines how to escalate privileges on a Linux system by exploiting misconfigurations in the doas utility, a lightweight alternative to sudo for executing commands as another user, typically root. Attackers with low-privileged user access can inspect the doas configuration file for rules that allow passwordless execution of powerful commands like vim, then leverage those to gain a root shell or modify sensitive files.

## Description

Doas is a simple elevation tool similar to sudo but with a minimal configuration file (/etc/doas.conf) that defines rules for permitting users to run specific commands as root or other users. Misconfigurations, such as rules allowing passwordless access to editors like vim without restrictions, can be abused for privilege escalation. This technique is effective in environments where doas is deployed instead of or alongside sudo, particularly on systems derived from OpenBSD or customized Linux distributions. The procedure assumes the attacker has shell access as a non-root user and focuses on enumeration, identification of weak rules, and exploitation to achieve root privileges. Success enables full system control, including persistence mechanisms like adding backdoors or exfiltrating data.

## Requirements

1. Shell access to a Linux system as a low-privileged user (e.g., via initial access like SSH with valid credentials).
2. Doas must be installed and configured on the target system.
3. Read access to /etc/doas.conf (typically requires no elevated privileges).
4. Basic knowledge of Linux commands and text editors like vim for exploitation.

## Defense

- Regularly audit /etc/doas.conf for overly permissive rules, avoiding 'nopass' for sensitive commands and using specific user/command restrictions.
- Implement least privilege: Only grant doas access to necessary users and commands; prefer sudo with logging for better auditing.
- Monitor for anomalous doas usage via system logs (e.g., auth.log) and process monitoring tools like auditd.
- Use AppArmor or SELinux to restrict what elevated processes can do, even if spawned via doas.

## Objectives

1. Enumerate and verify the presence of doas on the target system.
2. Identify misconfigured rules in /etc/doas.conf that allow passwordless elevation.
3. Exploit vulnerable rules to execute commands as root and obtain a root shell.
4. Verify escalation by performing root-only actions, such as reading /etc/shadow.

## Instructions

### Step 1: Verify Doas Presence

**Context**: Confirm if doas is installed and available, as this is a prerequisite for the escalation technique. If not present, fallback to sudo enumeration may be needed, but doas-specific exploits won't apply.

**Command** ([[commands/check-doas-presence]]):
```bash
which doas || echo "doas not found"
```

> This command checks the PATH for the doas executable. If found, it returns the path (e.g., /usr/bin/doas), indicating availability. If not, the technique cannot proceed without installation, which requires prior privileges.

### Step 2: Inspect Doas Configuration

**Context**: Review the configuration file to identify permissive rules. Look for lines starting with 'permit' that include 'nopass' (no password required) and target commands like 'vim', 'sh', or wildcards that could allow escalation.

**Command** ([[commands/view-doas-configuration]]):
```bash
cat /etc/doas.conf
```

> Expected output is the contents of /etc/doas.conf, such as "permit nopass demo as root cmd vim". Analyze for rules matching the current user (e.g., if username is 'demo') that allow root execution without authentication. If no such rules exist, the misconfiguration is not exploitable.

### Step 3: Test for Exploitable Rules

**Context**: Attempt to invoke doas with a potentially allowed command to confirm passwordless access. This step validates if the config permits elevation without prompting.

**Command** ([[commands/exploit-doas-vim-misconfig]]):
```bash
doas vim
```

> If successful, vim opens as root without a password prompt. Inside vim, you can now perform root actions. Expected output: Vim editor launches in elevated context (verify with :!whoami showing 'root'). If prompted for password or denied, the rule is not exploitable.

### Step 4: Achieve Root Shell via Editor Escape

**Context**: Once in an elevated editor like vim, escape to a shell to gain interactive root access. This bypasses direct shell restrictions by leveraging the editor's capabilities.

**Instructions**: With vim open as root (from Step 3), execute the following within vim:

```vim
:set shell=/bin/sh
:shell
```

> This sets the shell to /bin/sh and spawns an interactive shell. Expected output: A root prompt (e.g., # instead of $). Verify success by running `id` (should show uid=0(root)). Exit the shell with 'exit' to return to vim, then :q to quit.

If the rule allows other commands (e.g., 'sh'), directly use `doas /bin/sh` instead.
