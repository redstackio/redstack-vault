---
id: 4df4c2f0-289a-45ca-9c60-9fde8cda7b93
name: Dart Reverse PowerShell Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.780985+00:00'
updated_at: '2023-04-10T20:25:22.428556+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Event Triggered Execution|T1546 - Event Triggered Execution]]'
sub_techniques:
- '[[PowerShell|T1059.001 - PowerShell]]'
- '[[Screensaver|T1546.002 - Screensaver]]'
tags:
- '[[Dart]]'
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
---

# Dart Reverse PowerShell Shell

## Summary

The Dart Reverse PowerShell Shell technique is used to execute PowerShell commands on a remote server. This technique is commonly used by attackers to gain remote access to a system and execute arbitrary commands. To use this technique, the attacker must have access to a system with PowerShell inst

## Description

# Description

The Dart Reverse PowerShell Shell technique is used to execute PowerShell commands on a remote server. This technique is commonly used by attackers to gain remote access to a system and execute arbitrary commands. To use this technique, the attacker must have access to a system with PowerShell installed and the ability to execute PowerShell commands on the target system. Once the attacker has gained access to the target system, they can use this technique to execute commands and perform various actions on the system.

 

## Requirements

1. Access to a system with PowerShell installed

1. Ability to execute PowerShell commands on the target system

 

## Defense

1. Ensure that PowerShell is only used for legitimate purposes and that access to PowerShell is restricted to authorized users

1. Monitor for suspicious activity related to PowerShell usage, such as unusual command execution or network traffic

1. Implement network segmentation and access controls to limit the impact of a successful attack

 

## Objectives

1. Gain remote access to a target system

1. Execute arbitrary commands on the target system

 

# Instructions

1. To execute Powershell commands on a remote server, follow these steps:
1. Replace the IP address and port number in the code with the IP address and port number of the remote server.
2. Run the code on your local machine.
3. Enter the Powershell commands you want to execute on the remote server in the console.
4. The output of the commands will be displayed in the console.

 



**Code**: [[import 'dart:io';
import 'dart:convert';

main() {]]



> This code connects to a remote server using the Socket.connect() method and listens for data. When data is received, it starts a new process using the Process.start() method to execute the Powershell commands on the remote server. The output of the commands is then sent back to the local machine using the socket.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Event Triggered Execution|T1546 - Event Triggered Execution]]

### Sub-Techniques

- [[PowerShell|T1059.001 - PowerShell]]
- [[Screensaver|T1546.002 - Screensaver]]

## Tags

- [[Dart]]
- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]


