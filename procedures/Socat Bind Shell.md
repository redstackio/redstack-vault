---
id: cbeb730e-a621-4ce4-b9e2-d4c8df35c46b
name: Socat Bind Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:08.901490+00:00'
updated_at: '2023-04-10T20:21:16.968205+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
- '[[External Remote Services|T1133 - External Remote Services]]'
tags:
- '[[Bind Shell]]'
- '[[Socat]]'
---

# Socat Bind Shell

## Summary

A bind shell is a type of shell in which the target machine opens up a communication port or a listener on the victim machine and waits for an incoming connection. This procedure uses Socat to create a bind shell. Socat is a command-line utility that establishes two bidirectional byte streams and t

## Description

# Description

A bind shell is a type of shell in which the target machine opens up a communication port or a listener on the victim machine and waits for an incoming connection. This procedure uses Socat to create a bind shell. Socat is a command-line utility that establishes two bidirectional byte streams and transfers data between them. It can be used as a general-purpose network tool or as a tunneling tool. The Socat Bind Shell can be used by attackers to gain remote access to a target machine, bypassing any firewall or network restrictions. The attacker can then use this access to steal sensitive information, install malware, or launch further attacks.

Technical Explanation: The attacker first needs to upload and execute the Socat binary on the target machine. Once executed, the attacker can create a listener on a specific port or IP address using the following command: `socat TCP-L:<port> -`. This will create a listener on the specified port and wait for an incoming connection. The attacker can then connect to the listener using the `nc` command or any other tool of their choice. This will establish a shell on the attacker's machine, which can be used to execute commands on the target machine.

Business Value: The Socat Bind Shell can be used by attackers to gain remote access to a target machine, bypassing any firewall or network restrictions. This can lead to the theft of sensitive information, installation of malware, or further attacks. By understanding and implementing measures to secure against this type of attack, organizations can protect their assets and reputation.

## Requirements

1. Ability to upload and execute Socat binary on the target machine

1. Network access to the target machine

## Defense

1. Monitor network traffic for any suspicious activity, such as incoming connections on unusual ports

1. Use firewalls and other network security measures to restrict access to critical assets

1. Regularly update and patch software to prevent known vulnerabilities from being exploited

## Objectives

1. Gain remote access to a target machine

1. Execute commands on the target machine

# Instructions

1. This command is used to establish a reverse shell connection using the socat utility. The attacker machine initiates the connection to the victim machine and sends a shell command to be executed on the victim machine. This allows the attacker to gain remote access to the victim machine.

**Code**: [[user@attacker$ socat FILE:`tty`,raw,echo=0 TCP:tar]]

> The command consists of two parts, one for the attacker machine and one for the victim machine. 

On the attacker machine, the command starts with the socat utility followed by the FILE command which opens a connection to the terminal device. The `tty` option specifies the terminal device to use. The `raw` option sets the terminal to raw mode and the `echo=0` option disables the echoing of input characters. This is followed by the TCP command which connects to the victim machine on port 12345.

On the victim machine, the command starts with the socat utility followed by the TCP-LISTEN command which listens for incoming connections on port 12345. The `reuseaddr` option allows the port to be reused immediately after the connection is closed. The `fork` option forks a new process for each incoming connection. This is followed by the EXEC command which executes the /bin/sh shell command with various options. The `pty` option requests a pseudo-terminal for the shell. The `stderr` option redirects standard error to the same channel as standard output. The `setsid` option starts the shell in a new session. The `sigint` option forwards SIGINT signals to the shell. The `sane` option sets the terminal to a sane state before executing the shell command.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[External Remote Services|T1133 - External Remote Services]]

## Tags

- [[Bind Shell]]
- [[Socat]]
