---
id: 4ed8e0ca-08a7-4688-b3d0-dfde9cab0667
name: Command Injection - Filter Bypass with Backslash Newline
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.164064+00:00'
updated_at: '2023-04-06T03:55:57.179155+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Bypass with backslash newline]]'
- '[[Command Injection]]'
- '[[Filter Bypasses]]'
commands:
- '[[Display contents of /etc/passwd file]]'
---

# Command Injection - Filter Bypass with Backslash Newline

## Summary

Command Injection is a technique used by attackers to execute arbitrary commands on a targeted system. Filter Bypasses are a way to bypass security measures put in place to prevent Command Injection attacks. One such way of bypassing filters is by using the backslash newline technique. This techniq

## Description

# Description

Command Injection is a technique used by attackers to execute arbitrary commands on a targeted system. Filter Bypasses are a way to bypass security measures put in place to prevent Command Injection attacks. One such way of bypassing filters is by using the backslash newline technique. This technique involves breaking up the command into multiple parts using the backslash followed by a newline character. This can help bypass filters that look for specific keywords or characters. A successful Command Injection attack can result in the attacker gaining unauthorized access to sensitive data, modifying or deleting data, or even taking control of the entire system. It is important to implement measures to prevent Command Injection attacks, including filter validation, input sanitization, and command whitelisting.

## Requirements

1. Access to a system with a vulnerable application

1. Knowledge of the application and its vulnerabilities

## Defense

1. Implement filter validation to prevent the use of backslash newline characters

1. Implement input sanitization to prevent the injection of malicious commands

1. Implement command whitelisting to restrict the use of certain commands

## Objectives

1. Execute arbitrary commands on a targeted system

1. Bypass security measures put in place to prevent Command Injection attacks

# Instructions

1. To view the /etc/passwd file using the backslash newline technique, enter the following command:

**Code**: [[❯ cat /et\
c/pa\
sswd
root:x:0:0:root:/root:/usr/b]]

> The backslash followed by a newline character breaks up the command into multiple parts, which can help bypass filters that look for specific keywords or characters. In this example, the command 'cat /etc/passwd' has been broken up into 'cat /et\n' and 'c/pa\nsswd'. When executed, the command will display the contents of the /etc/passwd file.

**Command** ([[Display contents of /etc/passwd file]]):

```bash
cat /etc/passwd
```

2. To view the /etc/passwd file using the backslash newline technique in URL encoded form, enter the following command:

**Code**: [[cat%20/et%5C%0Ac/pa%5C%0Asswd]]

> URL encoding is a way to represent special characters using only ASCII characters. In this example, the command 'cat /etc/passwd' has been URL encoded as 'cat%20/et%5C%0Ac/pa%5C%0Asswd'. The '%5C%0A' represents the backslash newline character. When executed, the command will display the contents of the /etc/passwd file.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Commands Used

- [[Display contents of /etc/passwd file]]

## Tags

- [[Bypass with backslash newline]]
- [[Command Injection]]
- [[Filter Bypasses]]
