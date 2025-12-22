---
type: procedure
verified: true
submitted: true
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/SSH Hijacking|T1184 - SSH Hijacking]]'
sub_techniques: []
tags:
  - '[[tags/Network]]'
  - '[[tags/Service Attacks]]'
commands:
  - '[[commands/find-ssh-agent-sockets]]'
  - '[[commands/list-ssh-agent-files]]'
  - '[[commands/ssh-using-hijacked-agent]]'
platforms:
  - Linux
tools: []
validated: true
---

# SSH-Agent-Forwarding-Hijack

## Summary

This procedure demonstrates how to hijack an active SSH agent forwarding session on an intermediary Linux system where the attacker has root access. By identifying the forwarded SSH agent's socket and reusing it, the attacker can impersonate the legitimate user to establish an SSH connection to the target destination without needing the private key, enabling lateral movement across the network.

## Description

SSH agent forwarding allows users to authenticate to remote hosts using keys stored on their local machine without copying the keys to intermediate systems. When enabled (via -A flag in ssh), the SSH agent socket is forwarded through the SSH tunnel to the destination. On the intermediary server, this appears as a socket file in /tmp (e.g., /tmp/ssh-XXXXXXXXXXX/agent.XXX). If the attacker has root privileges on this intermediary, they can access the socket directory, read the agent file, and set the SSH_AUTH_SOCK environment variable to hijack the forwarding. This technique is effective in scenarios where the attacker has compromised a jump host or bastion used for SSH access to internal networks. It maps to MITRE ATT&CK technique T1184 (SSH Hijacking) under the Lateral Movement tactic, as it allows unauthorized access to restricted systems using valid credentials.

## Requirements

1. Root access on the intermediary Linux system where SSH agent forwarding is active.
2. Knowledge of the target user's approximate login time to correlate SSH directories.
3. Network connectivity to the destination target IP from the intermediary.
4. SSH client installed on the intermediary (standard on most Linux distributions).
5. Active SSH session with agent forwarding from the victim user (-A flag used in their ssh command).

## Defense

Defensive measures and detection strategies:

- Disable SSH agent forwarding in sshd_config by setting AllowAgentForwarding no and restart the SSH service.
- Use non-root accounts for intermediary access and implement strict file permissions on /tmp to prevent unauthorized access to sockets (though root bypasses this).
- Monitor for unusual SSH_AUTH_SOCK environment variable changes or multiple SSH connections from the same socket using auditd or SSH logging (e.g., LogLevel VERBOSE in sshd_config).
- Employ host-based intrusion detection to alert on root access to /tmp/ssh-* directories.
- Use key-based authentication with certificate authorities (e.g., SSH CA) to limit forwarding scope.

## Objectives

1. Identify an active SSH agent forwarding session belonging to a target user.
2. Extract the agent socket details to hijack the forwarding.
3. Establish an authenticated SSH connection to the destination using the hijacked agent.
4. Achieve lateral movement to the target system with the victim's privileges.

## Instructions

### Step 1: Identify Active SSH Agent Forwarding Sessions

**Context**: SSH agent forwarding sessions create temporary directories in /tmp starting with 'ssh-'. As root, scan for these to find potential hijackable sessions. Correlate with user login times (e.g., via /var/log/auth.log) to identify the target user's session.

**Command** ([[commands/find-ssh-agent-sockets]]):
```bash
find /tmp -type d -name 'ssh-*' 2>/dev/null
```

> This command lists all SSH-related directories in /tmp. Expected output includes paths like /tmp/ssh-abc123DEF. If multiple exist, check timestamps with ls -ld /tmp/ssh-* to match the user's recent login.

### Step 2: Locate the Agent Socket File

**Context**: Within the identified SSH directory, look for the 'agent.XXX' file, which holds the forwarded agent's socket path. This file allows reuse of the agent's authentication capabilities.

**Command** ([[commands/list-ssh-agent-files]]):
```bash
ls /tmp/ssh-XXXXXXXXXXX/
```

> Replace XXXXXXXXXXX with the actual directory from Step 1. Expected output: agent.XXX (e.g., agent.jDhFSu7EeAnz) and possibly other files like keyring. Note the agent file name for the next step.

### Step 3: Establish Hijacked SSH Connection

**Context**: Set the SSH_AUTH_SOCK environment variable to point to the hijacked agent socket, then initiate an SSH connection to the target. This uses the victim's forwarded keys for authentication without exposing them.

**Command** ([[commands/ssh-using-hijacked-agent]]):
```bash
SSH_AUTH_SOCK=/tmp/ssh-XXXXXXXXXXX/agent.XXX ssh $_TARGET_USER@$_TARGET_IP
```

> Replace paths with values from previous steps, $_TARGET_USER with the victim's username, and $_TARGET_IP with the destination. Expected output: Successful SSH login prompt or shell on the target, e.g., root@target:~#.
