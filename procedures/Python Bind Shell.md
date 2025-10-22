---
id: 7c2d31ad-dd87-4289-9cf1-ae289b9c6f77
name: Python Bind Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:08.779583+00:00'
updated_at: '2023-04-10T20:21:16.273209+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Non-Standard Port|T1571 - Non-Standard Port]]'
- '[[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]'
sub_techniques:
- '[[Web Protocols|T1071.001 - Web Protocols]]'
tags:
- '[[Bind Shell]]'
- '[[Python]]'
---

# Python Bind Shell

## Summary

A Python bind shell is a type of shell that allows an attacker to establish a connection with a victim machine and gain access to the system. The attacker sets up a listener on a specific port and waits for the victim to connect to it. Once the connection is established, the attacker gains access t

## Description

# Description

A Python bind shell is a type of shell that allows an attacker to establish a connection with a victim machine and gain access to the system. The attacker sets up a listener on a specific port and waits for the victim to connect to it. Once the connection is established, the attacker gains access to the victim's command prompt and can execute commands on the victim's machine. This technique is commonly used by attackers to gain remote access to a system.

From a technical perspective, the attacker creates a Python script that sets up a socket listener on a specific port. When the victim connects to the listener, the attacker gains access to the victim's command prompt. This type of attack can be difficult to detect as it uses a common protocol and port that may not be blocked by firewalls.

The business value of this attack is that it allows an attacker to gain remote access to a system, which can be used to steal sensitive data, install malware, or use the compromised system to launch further attacks.

## Requirements

1. Network access to the victim's machine

1. Python installed on the victim's machine

## Defense

1. Limit network access to critical systems

1. Block non-standard ports

1. Monitor network traffic for suspicious activity

## Objectives

1. Gain remote access to a victim's system

1. Execute commands on the victim's machine

1. Maintain persistence on the victim's system

# Instructions

1. This command is used to create a reverse shell on the target machine. It listens on port 51337 and waits for incoming connections. Once a connection is established, it executes the commands sent by the attacker and sends back the output.

**Code**: [[python -c 'exec("""import socket as s,subprocess a]]

> The command uses the Python programming language and creates a socket object. The socket object is then bound to the IP address '0.0.0.0' and port number 51337. The socket object listens for incoming connections and waits for a client to connect. Once a client connects, it enters a loop where it receives commands from the client and executes them using the subprocess module. The output of the command is then sent back to the client using the same socket connection.

2. To use this command, you need to run the script on the target machine and connect to it using a netcat listener. Once the connection is established, you can execute shell commands on the target machine through the netcat listener.

**Code**: [[import socket as s,subprocess as sp;

s1 = s.socke]]

> This command is a Python script that creates a reverse shell. It listens on port 51337 for incoming connections. Once a connection is established, it waits for commands to be received. When a command is received, it executes it on the target machine and returns the output to the client. This command can be used for remote administration or exploitation purposes.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Non-Standard Port|T1571 - Non-Standard Port]]
- [[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]

### Sub-Techniques

- [[Web Protocols|T1071.001 - Web Protocols]]

## Tags

- [[Bind Shell]]
- [[Python]]
