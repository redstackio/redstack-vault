---
id: ddc5baeb-b72b-4577-a70c-5f893f3b8605
name: Command Injection - Reading /etc/passwd
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.103744+00:00'
updated_at: '2023-04-06T03:55:57.118711+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tags:
- '[[Command Injection]]'
- '[[Exploits]]'
- '[[Inside a command]]'
commands:
- '[[Display /etc/passwd file content]]'
- '[[Display /etc/passwd file content]]'
---

# Command Injection - Reading /etc/passwd

## Summary

Command injection is a technique used by attackers to inject malicious commands into a vulnerable application. This can lead to the execution of arbitrary code on the host system, which can result in a complete compromise of the system. In this scenario, the attacker is able to read the contents of

## Description

# Description

Command injection is a technique used by attackers to inject malicious commands into a vulnerable application. This can lead to the execution of arbitrary code on the host system, which can result in a complete compromise of the system. In this scenario, the attacker is able to read the contents of the /etc/passwd file, which contains user account information. This information can be used to further escalate the attack.

From a technical perspective, command injection occurs when an attacker is able to inject their own command into a system command that is being executed by the application. This can occur when the application does not properly validate input that is being passed to a system command. In this case, the attacker is able to inject the `cat /etc/passwd` command into the original command that is being executed by the server.

The business value of this attack is that it can lead to a complete compromise of the system, which can result in the theft of sensitive data, disruption of business operations, and damage to the organization's reputation.

 

## Requirements

1. Access to a vulnerable application that does not properly validate input

 

## Defense

1. Proper input validation should be performed on any user input that is passed to a system command.

1. Use of parameterized queries can help prevent command injection attacks.

1. Implementing a web application firewall (WAF) can help detect and prevent command injection attacks.

 

## Objectives

1. Read the contents of the /etc/passwd file

 

# Instructions

1. Inject the command into the vulnerable application and observe the output.

 



**Code**: [[original_cmd_by_server `cat /etc/passwd`
original_]]



> The injected command will execute the `cat /etc/passwd` command on the host system. The output of this command will be returned to the attacker, allowing them to read the contents of the /etc/passwd file.



**Command** ([[Display /etc/passwd file content]]):

```bash
cat /etc/passwd
```





**Command** ([[Display /etc/passwd file content]]):

```bash
$(cat /etc/passwd)
```



## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

## Commands Used

- [[Display /etc/passwd file content]]
- [[Display /etc/passwd file content]]

## Tags

- [[Command Injection]]
- [[Exploits]]
- [[Inside a command]]


