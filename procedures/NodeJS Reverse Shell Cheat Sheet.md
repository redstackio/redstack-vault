---
id: 29ac2fde-d323-484f-aefd-5e685e60d35e
name: NodeJS Reverse Shell Cheat Sheet
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.677843+00:00'
updated_at: '2023-04-10T20:25:30.537873+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tags:
- '[[NodeJS]]'
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
---

# NodeJS Reverse Shell Cheat Sheet

## Summary

A NodeJS Reverse Shell is a method of establishing a remote command line session with a target system. This is achieved by running a script on the target system that connects back to the attacker's machine. The attacker can then execute commands on the target system as if they were sitting in front

## Description

# Description

A NodeJS Reverse Shell is a method of establishing a remote command line session with a target system. This is achieved by running a script on the target system that connects back to the attacker's machine. The attacker can then execute commands on the target system as if they were sitting in front of it. This technique is commonly used by attackers to gain a foothold on a target network and move laterally through the environment.

From a technical standpoint, a NodeJS Reverse Shell works by establishing a connection between the target system and the attacker's machine using a TCP socket. Once the connection is established, the attacker can send commands to the target system, which are executed in a command shell. The output of these commands is then sent back to the attacker's machine for analysis.

From a business perspective, a NodeJS Reverse Shell can be used by attackers to gain access to sensitive information, disrupt business operations, or deploy additional malware on the target network.

## Requirements

1. Access to the target system

1. NodeJS installed on the target system

## Defense

1. Limit network access to critical systems

1. Monitor network traffic for suspicious activity

1. Implement strong authentication measures to prevent unauthorized access

## Objectives

1. Establish a remote command line session with a target system

1. Execute commands on the target system

1. Move laterally through the target network

# Instructions

1. This command allows the attacker to establish a remote shell on the target machine by connecting to a specified IP address and port. The command can be executed in multiple ways as shown in the data field. 

Instructions:
1. Replace the IP address and port number in the command with the IP address and port number of the target machine.
2. Execute the command in the target machine's terminal.
3. The attacker can now use the remote shell to execute commands on the target machine.

**Code**: [[(function(){
    var net = require("net"),
       ]]

> The command uses the 'net' and 'child_process' modules in Node.js to establish a connection to the attacker's machine. Once the connection is established, the 'spawn' function is used to create a new shell process on the target machine. The 'pipe' function is then used to redirect the input and output of the shell process to the network socket. This allows the attacker to send commands to the shell process and receive the output on their own machine. The command can also be executed using the 'exec' function of the 'child_process' module along with the 'nc' command to establish the connection and open a shell.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

## Tags

- [[NodeJS]]
- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]
