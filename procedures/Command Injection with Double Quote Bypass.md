---
id: b3abc8d9-bf53-49ac-8e8d-9d3f1ae8f5d5
name: Command Injection with Double Quote Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.281551+00:00'
updated_at: '2023-04-06T03:55:57.299651+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Bypass Blacklisted words]]'
- '[[Bypass with double quote]]'
- '[[Command Injection]]'
- '[[Filter Bypasses]]'
---

# Command Injection with Double Quote Bypass

## Summary

Command injection is a technique used by attackers to execute arbitrary commands on a targeted system. In this specific case, the attacker is bypassing a filter that blocks blacklisted words by using double quotes. This technique can be used to bypass filters that are designed to prevent command in

## Description

# Description

Command injection is a technique used by attackers to execute arbitrary commands on a targeted system. In this specific case, the attacker is bypassing a filter that blocks blacklisted words by using double quotes. This technique can be used to bypass filters that are designed to prevent command injection attacks. The attacker can use this technique to execute any command on the targeted system, potentially leading to data theft, system compromise, or other malicious activity.

Technical Explanation: The attacker is using a double quote to bypass the filter that blocks blacklisted words. The double quote is used to encapsulate the blacklisted word, allowing it to pass through the filter. Once the command reaches the target system, the double quote is removed and the command is executed.

Business Value: This attack can allow an attacker to gain unauthorized access to sensitive data, compromise the integrity of the system, and cause significant financial and reputational damage to the targeted organization.

 

## Requirements

 

## Defense

1. Implement input validation to prevent injection attacks

1. Use parameterized queries to prevent injection attacks

1. Implement a WAF to block malicious requests

 

## Objectives

1. Execute arbitrary commands on the targeted system

1. Bypass blacklisted words filter

 

# Instructions

1. To execute the command, copy and paste the following code into a PowerShell console:

 



**Code**: [[w"h"o"am"i]]



> The 'Invoke-Expression' cmdlet is used to execute the command. The command is encapsulated in single quotes, and the double quotes are escaped with a backslash to allow them to pass through the filter.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[Bypass Blacklisted words]]
- [[Bypass with double quote]]
- [[Command Injection]]
- [[Filter Bypasses]]


