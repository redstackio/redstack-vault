---
id: b648dec8-802c-4ef0-86f1-962d46ec6844
name: John Hash Cracking Procedure
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:17.596214+00:00'
updated_at: '2023-04-06T03:56:17.617642+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
tags:
- '[[Hash Cracking]]'
- '[[John]]'
- '[[John Usage]]'
commands:
- '[[Restoring interrupted sessions]]'
- '[[Running John the Ripper on password file]]'
- '[[Running John the Ripper with a specific wordlist]]'
- '[[Running John the Ripper with a specific wordlist and rules]]'
- '[[Showing cracked passwords]]'
---

# John Hash Cracking Procedure

## Summary

The John Hash Cracking Procedure is a method for cracking password hashes using the John the Ripper tool. This procedure is commonly used by attackers to gain unauthorized access to systems, networks, and applications. John the Ripper is a powerful password cracking tool that uses a variety of tech

## Description

# Description

The John Hash Cracking Procedure is a method for cracking password hashes using the John the Ripper tool. This procedure is commonly used by attackers to gain unauthorized access to systems, networks, and applications. John the Ripper is a powerful password cracking tool that uses a variety of techniques to crack password hashes, including dictionary attacks, brute force attacks, and hybrid attacks. The tool is highly configurable and can be customized to target specific types of password hashes and attack scenarios. The business value of this procedure is that it can help organizations identify weak passwords and improve their overall security posture.

 

## Requirements

1. Access to the target system or network

1. John the Ripper tool installed on the attacker's machine

 

## Defense

1. Use strong and complex passwords that are difficult to crack

1. Implement multi-factor authentication to prevent unauthorized access

1. Regularly monitor and analyze system logs for suspicious activity

 

## Objectives

1. Crack password hashes to gain unauthorized access to systems, networks, and applications

1. Identify weak passwords and improve overall security posture

 

# Instructions

1. The above commands are used to crack passwords using John the Ripper tool.

 



**Code**: [[# Run on password file containing hashes to be cra]]



> The `john` command is used for password cracking. The `passwd` argument is used to specify the password file containing hashes to be cracked. The `--wordlist` argument is used to specify a specific wordlist to be used for cracking. The `--rules` argument is used to specify a specific rule to be applied to the cracking process. The `--show` argument is used to display the cracked passwords. The `--restore` argument is used to restore an interrupted session.



**Command** ([[Running John the Ripper on password file]]):

```bash
john passwd
```





**Command** ([[Running John the Ripper with a specific wordlist]]):

```bash
john --wordlist=<wordlist> passwd
```





**Command** ([[Running John the Ripper with a specific wordlist and rules]]):

```bash
john --wordlist=<wordlist> passwd --rules=Jumbo
```





**Command** ([[Showing cracked passwords]]):

```bash
john --show passwd
```





**Command** ([[Restoring interrupted sessions]]):

```bash
john --restore
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[Restoring interrupted sessions]]
- [[Running John the Ripper on password file]]
- [[Running John the Ripper with a specific wordlist]]
- [[Running John the Ripper with a specific wordlist and rules]]
- [[Showing cracked passwords]]

## Tags

- [[Hash Cracking]]
- [[John]]
- [[John Usage]]


