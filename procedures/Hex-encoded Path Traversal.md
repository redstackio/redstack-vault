---
id: 6a553be7-438f-4416-87b9-8b1a7adeaa6b
name: Hex-encoded Path Traversal
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.189319+00:00'
updated_at: '2023-04-06T03:55:57.202409+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tags:
- '[[Bypass characters filter via hex encoding]]'
- '[[Command Injection]]'
- '[[Filter Bypasses]]'
---

# Hex-encoded Path Traversal

## Summary

The hex-encoded path traversal technique is used to bypass filters that block certain characters. The attacker encodes the path to the file they want to access in hex format and passes it as an argument to the command. The command then decodes the path and accesses the file. This technique can be u

## Description

# Description

The hex-encoded path traversal technique is used to bypass filters that block certain characters. The attacker encodes the path to the file they want to access in hex format and passes it as an argument to the command. The command then decodes the path and accesses the file. This technique can be used to bypass filters that block special characters, such as single quotes or backslashes. It can also be used to access files that are not in the current directory.

## Requirements

1. Access to a vulnerable application or service

## Defense

1. Use input validation to sanitize user input and prevent injection attacks.

1. Use a web application firewall (WAF) to block known attack patterns.

1. Limit the permissions of the user running the vulnerable application or service to prevent access to sensitive files.

## Objectives

1. Execute arbitrary commands on the target system

1. Access sensitive files on the target system

# Instructions

1. To use this technique, encode the path to the file you want to access in hex format and pass it as an argument to the command. Use one of the following commands:

**Code**: [[swissky@crashlab:~$ echo -e "\x2f\x65\x74\x63\x2f\]]

> The attacker can use any of the provided commands to access the file they want. The first command uses the 'echo' command to print the hex-encoded path to the console. The second command uses command substitution to execute the 'cat' command with the decoded path as its argument. The third command stores the hex-encoded path in a variable and then uses command substitution to execute the 'cat' command with the decoded path as its argument. The fourth command uses command substitution to execute the 'cat' command with the hex-encoded path as its argument, but encodes the space character as well. The fifth command uses the 'xxd' command to convert the hex-encoded path to binary and then passes the binary output as an argument to the 'cat' command. The sixth command uses process substitution to achieve the same result as the fifth command.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

## Tags

- [[Bypass characters filter via hex encoding]]
- [[Command Injection]]
- [[Filter Bypasses]]
