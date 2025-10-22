---
id: 24a9f3b8-d8dc-4244-8461-3dc76260f8d9
name: Command Injection - Time Based Data Exfiltration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.455319+00:00'
updated_at: '2023-04-06T03:55:57.479517+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tags:
- '[[Command Injection]]'
- '[[Time based data exfiltration]]'
commands:
- '[[Check First Letter of Username]]'
- '[[Check First Letter of Username]]'
---

# Command Injection - Time Based Data Exfiltration

## Summary

Time-based data exfiltration is a technique used by attackers to extract data from a target system using command injection. This technique involves injecting commands that cause a delay in the response time of the system, allowing the attacker to extract data bit by bit. In this scenario, the comma

## Description

# Description

Time-based data exfiltration is a technique used by attackers to extract data from a target system using command injection. This technique involves injecting commands that cause a delay in the response time of the system, allowing the attacker to extract data bit by bit. In this scenario, the command is injected to check the first character of the username and sleep for 5 seconds if the first character is 's'. This allows the attacker to extract data character by character, eventually exfiltrating sensitive data from the target system.

From a technical perspective, this technique involves injecting malicious commands into a system to execute unauthorized actions. This can be done by exploiting vulnerabilities in web applications or other software that accept user input. By injecting commands, attackers can gain access to sensitive data, execute unauthorized actions, and even take control of the system. The business value of this technique is that it can be used to steal sensitive data, such as login credentials or financial information, which can be sold on the dark web or used for other malicious purposes.

## Requirements

## Defense

1. Ensure that all user input is properly validated and sanitized to prevent command injection attacks

1. Implement proper access control mechanisms to prevent unauthorized access to sensitive data

1. Monitor system logs and network traffic for any suspicious activity that may indicate a command injection attack

## Objectives

1. Extract data from a target system using command injection

1. Steal sensitive data from the target system

# Instructions

1. To extract data character by character, inject the following command and observe the response time:

if [ $(whoami|cut -c 1) == s ]; then sleep 5; fi

This command checks the first character of the username and sleeps for 5 seconds if the first character is 's'. Repeat this command for each character in the string to extract the entire data.

**Code**: [[swissky@crashlab:~$ time if [ $(whoami|cut -c 1) =]]

> The injected command checks the first character of the username and sleeps for 5 seconds if the first character is 's'. This delay in response time allows the attacker to extract data character by character. By repeating this command for each character in the string, the attacker can extract the entire data.

**Command** ([[Check First Letter of Username]]):

```bash
if [ $(whoami|cut -c 1) == s ]; then sleep 5; fi
```

**Command** ([[Check First Letter of Username]]):

```bash
if [ $(whoami|cut -c 1) == a ]; then sleep 5; fi
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

## Commands Used

- [[Check First Letter of Username]]
- [[Check First Letter of Username]]

## Tags

- [[Command Injection]]
- [[Time based data exfiltration]]
