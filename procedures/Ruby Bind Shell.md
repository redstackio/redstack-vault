---
id: f57a809c-2d51-4cdd-8971-a5474a4bc56e
name: Ruby Bind Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:08.827361+00:00'
updated_at: '2023-04-10T20:21:14.486481+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote Services|T1021 - Remote Services]]'
sub_techniques:
- '[[Remote Desktop Protocol|T1021.001 - Remote Desktop Protocol]]'
- '[[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]'
- '[[Windows Remote Management|T1021.006 - Windows Remote Management]]'
tags:
- '[[Bind Shell]]'
- '[[Ruby]]'
---

# Ruby Bind Shell

## Summary

A Ruby bind shell is a type of shell that listens on a specific port and waits for an incoming connection. When a connection is made, the shell is spawned and the attacker gains access to the victim's system. This technique can be used by an attacker to maintain persistence and access to a system. 

## Description

# Description

A Ruby bind shell is a type of shell that listens on a specific port and waits for an incoming connection. When a connection is made, the shell is spawned and the attacker gains access to the victim's system. This technique can be used by an attacker to maintain persistence and access to a system. From a technical standpoint, the attacker would use a Ruby script to create the bind shell, which would listen on a specified port. The attacker would then connect to the bind shell using a separate tool, such as netcat, to gain access to the victim's system. From a business value perspective, this technique can be used to gain access to sensitive information, disrupt business operations, or steal intellectual property.

 

## Requirements

1. Ruby installed on the attacker's system

1. Victim's system reachable via network

1. Ability to open a listening port on the victim's system

 

## Defense

1. Implement network segmentation to limit the attacker's ability to move laterally

1. Monitor network traffic for suspicious activity, such as connections to unusual ports

1. Use firewalls to restrict inbound and outbound traffic to known good sources

 

## Objectives

1. Gain persistent access to a victim's system

1. Maintain access to sensitive information

1. Disrupt business operations

 

# Instructions

1. To establish a reverse shell, run the following command on the target machine:

 



**Code**: [[ruby -rsocket -e 'f=TCPServer.new(51337);s=f.accep]]



> This command creates a server socket that listens on port 51337. When a connection is made to this port, the server accepts the connection and executes a shell with input/output redirected to the socket. This results in a reverse shell, where the target machine is connected to the attacker's machine and the attacker can execute commands on the target machine.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote Services|T1021 - Remote Services]]

### Sub-Techniques

- [[Remote Desktop Protocol|T1021.001 - Remote Desktop Protocol]]
- [[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]
- [[Windows Remote Management|T1021.006 - Windows Remote Management]]

## Tags

- [[Bind Shell]]
- [[Ruby]]


