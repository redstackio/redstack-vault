---
id: fa4e3fe9-3e32-4d20-8909-4e9c7cf57260
name: Golang Reverse Shell Cheat Sheet
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.348054+00:00'
updated_at: '2023-04-10T20:25:23.851540+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
- '[[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]'
sub_techniques:
- '[[Web Protocols|T1071.001 - Web Protocols]]'
tags:
- '[[Golang]]'
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
---

# Golang Reverse Shell Cheat Sheet

## Summary

A reverse shell is a type of shell in which the target machine communicates back to the attacking machine. This Golang Reverse Shell Cheat Sheet provides a quick reference for creating a reverse shell using Golang. 

From an offensive perspective, a reverse shell is a powerful tool for maintaining 

## Description

# Description

A reverse shell is a type of shell in which the target machine communicates back to the attacking machine. This Golang Reverse Shell Cheat Sheet provides a quick reference for creating a reverse shell using Golang. 

From an offensive perspective, a reverse shell is a powerful tool for maintaining access to a target machine. By establishing a connection back to an attacker-controlled machine, the attacker can execute commands, exfiltrate data, and move laterally within a target network. 

From a technical perspective, this cheat sheet provides a basic implementation of a reverse shell using Golang. The code establishes a connection to the attacker-controlled machine and executes commands via a shell. 

From a business perspective, understanding how a reverse shell works can help organizations better defend against attacks that use this technique.

## Requirements

1. An attacker-controlled machine to receive the reverse shell connection

1. Golang installed on the attacker machine and target machine

## Defense

1. Monitor network traffic for suspicious connections to external IP addresses

1. Implement network segmentation to limit lateral movement within the network

1. Use strong authentication mechanisms to prevent unauthorized access to systems

## Objectives

1. Establish a reverse shell connection to an attacker-controlled machine

1. Execute commands on the target machine via the reverse shell

1. Maintain persistent access to the target machine

# Instructions

1. This command creates a reverse shell to connect to a remote host. It creates a temporary Go file, which establishes a TCP connection to the remote host and executes a shell command. Once the connection is established, the attacker can execute any command on the remote host as if they were physically present on the machine.

**Code**: [[echo 'package main;import"os/exec";import"net";fun]]

> The command consists of three parts: 
1. Creating a temporary Go file with the reverse shell code. 
2. Running the Go file to establish a connection to the remote host. 
3. Removing the temporary Go file. The IP address and port number in the code should be replaced with the attacker's IP address and port number. The attacker should also be listening on the specified port to receive the connection.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Remote Access Tools|T1219 - Remote Access Tools]]
- [[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]

### Sub-Techniques

- [[Web Protocols|T1071.001 - Web Protocols]]

## Tags

- [[Golang]]
- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]
