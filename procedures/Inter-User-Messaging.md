---
id: 6ce5e24e-661a-4026-9847-37940f4a0a03
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:21.861809+00:00'
updated_at: '2023-04-06T03:56:21.885506+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques: []
tags:
  - '[[tags/Miscellaneous & Tricks]]'
  - '[[tags/Send a message to another user]]'
  - inter-user-messaging
  - communication
  - social-engineering
commands:
  - '[[commands/who-show-logged-in-users-linux]]'
  - '[[commands/msg-send-message-to-specific-user-windows]]'
  - '[[commands/msg-send-message-to-all-users-windows]]'
  - '[[commands/wall-send-message-to-all-users-linux]]'
  - '[[commands/wall-send-message-non-broadcast-linux]]'
  - '[[commands/write-send-message-to-specific-user-linux]]'
platforms:
  - Windows
  - Linux
tools: []
validated: true
---

# Inter-User-Messaging

## Summary

Inter-User Messaging allows sending notifications or messages to logged-in users on Windows or Linux systems via command-line tools. In offensive security contexts, this technique facilitates communication between compromised accounts, alerts other attackers, or supports social engineering by displaying deceptive messages to users on the target system.

## Description

This procedure covers sending messages to specific users or all users on both Windows and Linux environments. On Windows, the 'msg' command targets local or remote sessions via the Messenger service or Terminal Services, requiring administrative privileges for remote sends. On Linux, 'wall' broadcasts to all terminals (local only), while 'write' enables direct messaging to a specific user's terminal. First, identify logged-in users to target messages effectively. This is useful post-compromise for coordinating actions or mimicking legitimate system alerts to avoid detection. The technique assumes shell access and may require elevated privileges for certain operations like remote messaging or non-broadcast walls.

## Requirements

1. Shell access (local or remote) to the target system
2. Knowledge of target usernames or terminals (obtain via user enumeration)
3. Administrative privileges on Windows for remote 'msg' sends; root on Linux for 'wall -n'
4. Network access if targeting remote Windows systems

## Defense

- Disable legacy messaging services like Windows Messenger or restrict 'msg' to local use via Group Policy
- Monitor command-line executions for 'msg', 'wall', and 'write' using endpoint detection tools (e.g., Sysmon, auditd)
- Implement least privilege: Limit shell access and log all inter-user communications
- Use session isolation to prevent unauthorized terminal writes

## Objectives

1. Communicate discreetly with other users or attackers on a compromised system
2. Deliver social engineering messages to influence user behavior or extract information
3. Verify active sessions before targeted actions in lateral movement

## Instructions

### Step 1: Enumerate Logged-In Users on Linux

**Context**: Before sending messages, identify active users and their terminals to target specific individuals or broadcast broadly. This step uses the 'who' command, which lists current sessions without requiring elevated privileges.

**Command** ([[commands/who-show-logged-in-users-linux]]):
```bash
who
```

> The 'who' command displays usernames, terminal IDs (e.g., pts/2), login time, and originating host. Use this output to select targets for 'write' or confirm users for 'wall'. If no users are listed, the system may have no active sessions.

### Step 2: Send Message to Specific User on Windows

**Context**: Target a single user session locally or remotely to deliver a private message. Replace placeholders with actual username and server (optional for local). This requires the 'msg' tool, available on Windows Server editions.

**Command** ([[commands/msg-send-message-to-specific-user-windows]]):
```cmd
msg $_USERNAME /SERVER:$_SERVER "$_MESSAGE"
```

> Success is indicated by a confirmation like "Message sent to Swissky". The message appears as a popup on the recipient's screen. For local sends, omit /SERVER. Messages are limited to 128 characters.

### Step 3: Send Message to All Users on Windows

**Context**: Broadcast to all active sessions on the target server, useful for system-wide alerts or deception. Use wildcards and options for visibility and acknowledgment.

**Command** ([[commands/msg-send-message-to-all-users-windows]]):
```cmd
msg * /V /W /SERVER:$_SERVER "$_MESSAGE"
```

> The /V flag shows the message in the title bar, /W waits for response. Expected: "Message sent successfully to all sessions". If no response, check privileges or session activity.

### Step 4: Send Message to All Users on Linux

**Context**: Broadcast a message to every logged-in terminal, simulating system announcements. 'wall' requires write permissions on /dev/tty devices; non-root users may be restricted.

**Command** ([[commands/wall-send-message-to-all-users-linux]]):
```bash
wall "$_MESSAGE"
```

> Output: "Broadcast message from [user] (pts/X) at [time]..." echoed to sender. Recipients see the message prefixed with sender info. If permission denied, elevate to root.

### Step 5: Send Non-Broadcast Message on Linux (Root-Only)

**Context**: Send a message without broadcasting to all terminals, useful for targeted alerts without full visibility. The -n flag prevents delivery to terminals, but in practice, it's for selective use; requires root.

**Command** ([[commands/wall-send-message-non-broadcast-linux]]):
```bash
wall -n "$_MESSAGE"
```

> Similar to standard wall but suppresses terminal broadcasts. Expected: No echo if successful, or error if not root. Use for maintenance notices without alerting all.

### Step 6: Send Message to Specific User on Linux

**Context**: Write directly to a user's terminal for private communication. Specify username and tty from 'who' output; ends with Ctrl+D.

**Command** ([[commands/write-send-message-to-specific-user-linux]]):
```bash
write $_USERNAME $_TTY
```

> After execution, type the message and press Ctrl+D to send. Expected: Message appears on recipient's screen with "Message from [user]". If user has 'mesg n', it fails.
