---
id: 78f4c085-c861-4409-aa46-fb19784625f9
name: Wrapper Expect LFI/RFI
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.400086+00:00'
updated_at: '2023-04-10T20:22:15.920122+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[File Inclusion]]'
- '[[LFI / RFI using wrappers]]'
- '[[Wrapper expect://]]'
commands:
- '[[Expect id command on http://example.com]]'
- '[[Expect ls command on http://example.com]]'
---

# Wrapper Expect LFI/RFI

## Summary

Wrapper Expect LFI/RFI is a technique that leverages the expect:// wrapper to perform Local File Inclusion (LFI) or Remote File Inclusion (RFI) attacks. This technique works by passing the path of the file to be included as an argument to the expect:// wrapper, which then executes the specified com

## Description

# Description

Wrapper Expect LFI/RFI is a technique that leverages the expect:// wrapper to perform Local File Inclusion (LFI) or Remote File Inclusion (RFI) attacks. This technique works by passing the path of the file to be included as an argument to the expect:// wrapper, which then executes the specified command and returns its output. By using this technique, an attacker can execute arbitrary commands on the target system, which can lead to sensitive data disclosure, system compromise, or further attacks. This technique can be used to bypass access controls and execute code on a target system.

 

## Requirements

1. Access to a vulnerable web application that uses the expect:// wrapper

1. Knowledge of the path of the file to be included

 

## Defense

1. Input validation should be implemented to prevent the use of the expect:// wrapper.

1. Access controls should be implemented to prevent unauthorized access to sensitive files.

1. File permissions should be configured to prevent the execution of arbitrary commands.

 

## Objectives

1. To obtain sensitive data from the target system

1. To execute arbitrary code on the target system

1. To bypass access controls on the target system

 

# Instructions

1. 1. Replace 'id' or 'ls' with the path of the file to be included.
2. Pass the path of the file to be included as an argument to the expect:// wrapper.
3. Execute the command by passing the URL to the vulnerable web application.
4. The output of the command will be returned by the expect:// wrapper.

 



**Code**: [[http://example.com/index.php?page=expect://id
http]]



> The 'http://example.com/index.php?page=' parameter is vulnerable to LFI/RFI attacks. By using the expect:// wrapper, an attacker can execute arbitrary commands on the target system. In the provided example, the attacker is executing the 'id' and 'ls' commands to obtain information about the target system.



**Command** ([[Expect id command on http://example.com]]):

```bash
http://example.com/index.php?page=expect://id

```





**Command** ([[Expect ls command on http://example.com]]):

```bash
http://example.com/index.php?page=expect://ls
```



## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Expect id command on http://example.com]]
- [[Expect ls command on http://example.com]]

## Tags

- [[File Inclusion]]
- [[LFI / RFI using wrappers]]
- [[Wrapper expect://]]


