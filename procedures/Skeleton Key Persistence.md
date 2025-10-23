---
id: bfd1cf6b-1077-4ec8-885e-b158580ad63c
name: Skeleton Key Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.274014+00:00'
updated_at: '2023-04-10T20:37:25.386010+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Account Manipulation|T1098 - Account Manipulation]]'
tags:
- '[[Elevated]]'
- '[[Skeleton Key]]'
- '[[Windows - Persistence]]'
commands:
- '[[Access machine using password]]'
- '[[Execute skeleton key attack using Mimikatz]]'
---

# Skeleton Key Persistence

## Summary

Skeleton Key Persistence is a technique used by attackers to obtain access to a Windows domain controller by bypassing authentication mechanisms. This technique involves replacing the domain controller's password validation process with a backdoor authentication mechanism. By doing so, attackers ca

## Description

# Description

Skeleton Key Persistence is a technique used by attackers to obtain access to a Windows domain controller by bypassing authentication mechanisms. This technique involves replacing the domain controller's password validation process with a backdoor authentication mechanism. By doing so, attackers can authenticate as any user in the domain without their password, effectively obtaining persistent access to the domain.

To execute a Skeleton Key Persistence attack, an attacker must first gain administrative access to the domain controller. They can then use a tool such as Mimikatz to replace the password validation process with a backdoor authentication mechanism. This technique can be particularly effective against organizations that use weak or easily guessable passwords, as it allows attackers to bypass password-based authentication altogether.

The business value of this attack is that it allows attackers to maintain persistent access to the domain, making it easier for them to exfiltrate sensitive data or carry out further attacks.

 

## Requirements

1. Administrative access to the domain controller

1. Mimikatz or similar tool

 

## Defense

1. Implement strong password policies to prevent easy-to-guess passwords

1. Monitor for suspicious activity on the domain controller

1. Regularly review and update access controls to limit administrative access to the domain controller

 

## Objectives

1. Gain persistent access to the domain controller

1. Bypass password-based authentication mechanisms

 

# Instructions

1. Execute the Skeleton Key Attack by running the commands provided.

 



**Code**: [[# Execute the skeleton key attack
mimikatz "privil]]



> The Skeleton Key Attack is a technique used to bypass Active Directory authentication. It works by injecting a fake password into the authentication process, allowing an attacker to gain access to any account in the domain. This can be done by using the Mimikatz tool, which is a post-exploitation tool that allows attackers to extract credentials from memory. The first two commands in the provided script execute the Skeleton Key Attack using Mimikatz. The last command demonstrates how to access a machine using the password 'mimikatz'. Note that this attack requires administrative privileges on the domain controller.



**Command** ([[Execute skeleton key attack using Mimikatz]]):

```bash
mimikatz "privilege::debug" "misc::skeleton"
```





**Command** ([[Access machine using password]]):

```bash
Enter-PSSession -ComputerName <AnyMachineYouLike> -Credential <Domain>\Administrator
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Account Manipulation|T1098 - Account Manipulation]]

## Commands Used

- [[Access machine using password]]
- [[Execute skeleton key attack using Mimikatz]]

## Tags

- [[Elevated]]
- [[Skeleton Key]]
- [[Windows - Persistence]]


