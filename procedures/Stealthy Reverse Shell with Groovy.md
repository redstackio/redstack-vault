---
id: 171fd728-7b29-4bac-82ef-3d6ff8cdbe97
name: Stealthy Reverse Shell with Groovy
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.721058+00:00'
updated_at: '2023-04-10T20:25:29.140848+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Custom Cryptographic Protocol|T1024 - Custom Cryptographic Protocol]]'
tags:
- '[[Groovy]]'
- '[[Groovy Alternative 1]]'
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
---

# Stealthy Reverse Shell with Groovy

## Summary

This procedure allows an attacker to establish a stealthy reverse shell connection to a compromised system using Groovy. Groovy is a powerful scripting language that runs on the Java Virtual Machine and is commonly used for automation tasks. By using a custom cryptographic protocol, the attacker ca

## Description

# Description

This procedure allows an attacker to establish a stealthy reverse shell connection to a compromised system using Groovy. Groovy is a powerful scripting language that runs on the Java Virtual Machine and is commonly used for automation tasks. By using a custom cryptographic protocol, the attacker can encrypt the communication between the compromised system and their command and control server, making it difficult for defenders to detect the connection.

To establish the connection, the attacker first needs to execute the Groovy script on the compromised system. This can be done using various methods, such as exploiting a vulnerability, tricking a user into running a malicious file, or using a previously established foothold. Once the script is executed, it will initiate a connection to the attacker's command and control server and wait for commands.

This procedure is valuable for attackers who want to maintain persistent access to a compromised system while avoiding detection by defenders. The stealthy nature of the connection makes it difficult to detect and block by traditional security measures.

## Requirements

1. Access to a compromised system with the ability to execute a Groovy script

1. A command and control server to receive the connection

## Defense

1. Monitor network traffic for suspicious connections and communication protocols

1. Implement strong authentication and access controls to prevent unauthorized access to systems

1. Regularly update and patch software to prevent exploitation of vulnerabilities

## Objectives

1. Establish a stealthy reverse shell connection to a compromised system using Groovy

# Instructions

1. To use this command, simply add the code snippet to your Java program. This will start a new thread and run the reverse shell code in the background, making it harder to detect.

**Code**: [[Thread.start {
    // Reverse shell here
}]]

> This command starts a new thread in your Java program and runs a reverse shell in the background. This allows you to access a remote system without being detected, as the reverse shell is hidden in the background thread. The code snippet provided can be customized to fit your specific needs, such as changing the IP address and port number for the reverse shell connection.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Custom Cryptographic Protocol|T1024 - Custom Cryptographic Protocol]]

## Tags

- [[Groovy]]
- [[Groovy Alternative 1]]
- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]
