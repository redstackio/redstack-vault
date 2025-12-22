---
id: bbab094d-f104-4e0f-a442-a570cd056c48
name: Linux-SUDO-NOPASSWD-Privilege-Escalation-via-Vim
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:18.970740+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Abuse Elevation Control Mechanism|T1548 - Abuse Elevation
    Control Mechanism]]
sub_techniques:
  - '[[sub-techniques/Sudo and Sudo Caching|T1548.003 - Sudo and Sudo Caching]]'
tags:
  - '[[tags/Linux - Privilege Escalation]]'
  - '[[tags/NOPASSWD]]'
  - '[[tags/SUDO]]'
commands:
  - '[[commands/sudo-list-privileges]]'
  - '[[commands/vim-spawn-root-shell]]'
platforms:
  - Linux
tools: []
validated: true
---

# Linux-SUDO-NOPASSWD-Privilege-Escalation-via-Vim

## Summary

This procedure exploits a misconfigured sudoers file allowing a user to run the Vim text editor as root without a password (NOPASSWD). By invoking Vim with specific command-line arguments, an attacker can execute a shell command as root, achieving privilege escalation from a standard user to root access on a Linux system.

## Description

In Linux environments, the sudoers configuration can grant specific users permission to execute certain binaries as root without requiring a password. If the configuration includes an entry like '(root) NOPASSWD: /usr/bin/vim' for the current user, this represents a privilege escalation vulnerability. The technique leverages Vim's ability to execute external shell commands via its command-line interface or internal ex commands. This is particularly effective in scenarios where an attacker has obtained initial foothold access via a low-privilege account, such as through phishing or weak credentials. The procedure assumes a standard Linux distribution like Ubuntu or CentOS with sudo and Vim installed. Success grants full root shell access, enabling further post-exploitation activities like data exfiltration or persistence installation. Note that this abuse falls under MITRE ATT&CK's Abuse Elevation Control Mechanism, specifically targeting sudo caching and configuration flaws.

## Requirements

1. Local access to a low-privilege user account on the target Linux system.
2. The user must have sudo privileges configured for /usr/bin/vim with NOPASSWD option (verifiable via sudoers file or sudo -l output).
3. Vim must be installed and available in the PATH (typically /usr/bin/vim).
4. No additional tools required beyond standard bash shell access.

## Defense

- Regularly audit and monitor sudoers file (/etc/sudoers and /etc/sudoers.d/) for unauthorized modifications using tools like auditd or file integrity monitoring (e.g., Tripwire, AIDE).
- Restrict sudo privileges to the minimum necessary commands and users; avoid NOPASSWD for interactive editors like Vim.
- Enable sudo logging (Defaults logfile="/var/log/sudo.log") and review logs for anomalous executions of vim or shell spawns.
- Implement principle of least privilege: Use sudo -l to verify configurations periodically and remove broad editor permissions.
- Consider AppArmor or SELinux policies to confine sudo executions and prevent shell escapes from editors.

## Objectives

1. Identify if the target user has NOPASSWD sudo access to Vim.
2. Exploit the configuration to spawn a root shell without password prompts.
3. Achieve full root access for further system compromise.

## Instructions

### Step 1: Verify Sudo Privileges for Vim

**Context**: First, enumerate the current user's sudo privileges to confirm the presence of the NOPASSWD Vim allowance. This step identifies if the vulnerability exists without alerting defenses unnecessarily.

**Command** ([[commands/sudo-list-privileges]]):
```bash
sudo -l
```

> This command queries the sudo policy and lists allowed commands. Look for an entry like '(root) NOPASSWD: /usr/bin/vim'. If present, proceed to exploitation. If not, this procedure does not apply.

### Step 2: Spawn Root Shell via Vim

**Context**: With confirmed privileges, invoke Vim as root and use its external command execution feature to launch a shell. This bypasses the need to edit files and directly escalates privileges.

**Command** ([[commands/vim-spawn-root-shell]]):
```bash
sudo vim -c '!/bin/sh'
```

> The -c flag executes the ex command '!/bin/sh', which runs /bin/sh as root. Alternatively, use 'sudo -u root vim -c "!/bin/sh"' for explicit user specification. Upon success, you will drop into a root shell prompt (e.g., # instead of $). Verify with 'id' or 'whoami' showing uid=0(root). Exit the shell with 'exit' to return to the original session.
