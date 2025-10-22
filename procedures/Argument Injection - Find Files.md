---
id: 909f7791-d5b2-41de-af17-6702ce083f2d
name: Argument Injection - Find Files
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:54.131228+00:00'
updated_at: '2023-04-06T03:55:54.143234+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tags:
- '[[Argument Injection]]'
- '[[FIND]]'
- '[[List of exposed commands]]'
---

# Argument Injection - Find Files

## Summary

The Argument Injection - Find Files procedure allows an attacker to execute arbitrary commands on a target system. This specific procedure targets the 'find' command, which is used to search for files and directories in a specified location. By injecting malicious arguments, an attacker can execute

## Description

# Description

The Argument Injection - Find Files procedure allows an attacker to execute arbitrary commands on a target system. This specific procedure targets the 'find' command, which is used to search for files and directories in a specified location. By injecting malicious arguments, an attacker can execute arbitrary code on the target system. The technical explanation is that the attacker is able to manipulate the command-line arguments passed to the system, allowing them to execute arbitrary commands. The business value of this procedure is that it allows an attacker to gain unauthorized access to sensitive data and potentially take control of the target system.

## Requirements

1. Access to the target system's command-line interface

## Defense

1. Always sanitize user input to prevent injection attacks.

1. Restrict access to the command-line interface to authorized personnel only.

1. Monitor the system for any suspicious activity, such as unauthorized command execution.

## Objectives

1. Execute arbitrary code on the target system

1. Gain unauthorized access to sensitive data

1. Take control of the target system

# Instructions

1. To execute this command, simply run the script containing this code on the target system's command-line interface.

**Code**: [[$file = "some_file";
system("find /tmp -iname ".es]]

> This command searches for a file named 'some_file' in the '/tmp' directory. The 'escapeshellcmd' function is used to escape any special characters in the file name to prevent injection attacks.

2. To execute this command, simply run the script containing this code on the target system's command-line interface.

**Code**: [[$file = "sth -or -exec cat /etc/passwd ; -quit";
s]]

> This command searches for a file with the name 'sth -or -exec cat /etc/passwd ; -quit' in the '/tmp' directory. The injected argument '-exec cat /etc/passwd ;' causes the 'cat' command to be executed on the '/etc/passwd' file, which is then printed to the command-line interface. This allows the attacker to view the contents of the '/etc/passwd' file, which may contain sensitive information such as usernames and hashed passwords.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

## Tags

- [[Argument Injection]]
- [[FIND]]
- [[List of exposed commands]]
