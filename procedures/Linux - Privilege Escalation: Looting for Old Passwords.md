---
id: 97882abd-dc3b-4ded-b48e-be1a13f2328a
name: 'Linux - Privilege Escalation: Looting for Old Passwords'
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.484892+00:00'
updated_at: '2023-04-10T20:34:25.734695+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credentials in Files|T1081 - Credentials in Files]]'
- '[[Screen Capture|T1113 - Screen Capture]]'
tags:
- '[[Linux - Privilege Escalation]]'
- '[[Looting for passwords]]'
- '[[Old passwords in /etc/security/opasswd]]'
commands:
- '[[View /etc/security/opasswd file]]'
---

# Linux - Privilege Escalation: Looting for Old Passwords

## Summary

Linux systems store user passwords in a hashed format in the /etc/shadow file. However, older versions of Linux may also store user passwords in the /etc/security/opasswd file. Attackers can loot for these old passwords and use them to escalate their privileges on the system. This technique can be 

## Description

# Description

Linux systems store user passwords in a hashed format in the /etc/shadow file. However, older versions of Linux may also store user passwords in the /etc/security/opasswd file. Attackers can loot for these old passwords and use them to escalate their privileges on the system. This technique can be used as a post-exploitation step, after an attacker has already gained access to a system.

To loot for old passwords in the /etc/security/opasswd file, an attacker can use the 'Security Password File Location' command. This command will reveal the location of the password file and allow the attacker to access it.

From a technical perspective, this attack is relatively simple. However, it can be very effective if an attacker is able to obtain valid credentials. The business value of this attack lies in its ability to allow attackers to gain higher levels of access on a compromised system, potentially leading to further compromise of the organization's assets.

 

## Requirements

1. Access to a Linux system

1. Ability to execute commands on the system

1. Knowledge of the 'Security Password File Location' command

 

## Defense

1. Regularly update Linux systems to ensure that old password files are not present

1. Monitor for unauthorized access to the /etc/security/opasswd file

1. Implement multi-factor authentication to prevent attackers from gaining access to valid credentials

 

## Objectives

1. Obtain old passwords stored in the /etc/security/opasswd file

1. Use these passwords to escalate privileges on the system

 

# Instructions

1. This file contains the hashed passwords for all users on the system. It is used by the system to authenticate users when they log in.

 



**Code**: [[/etc/security/opasswd]]



> The file is located at /etc/security/opasswd and should only be accessible by the root user. It is recommended to use a strong password policy and to regularly update passwords to ensure the security of the system.



**Command** ([[View /etc/security/opasswd file]]):

```bash
cat /etc/security/opasswd
```



## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credentials in Files|T1081 - Credentials in Files]]
- [[Screen Capture|T1113 - Screen Capture]]

## Commands Used

- [[View /etc/security/opasswd file]]

## Tags

- [[Linux - Privilege Escalation]]
- [[Looting for passwords]]
- [[Old passwords in /etc/security/opasswd]]


