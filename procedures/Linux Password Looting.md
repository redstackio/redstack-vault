---
id: 444aeb81-620c-453d-9861-f07f112e0862
name: Linux Password Looting
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.562810+00:00'
updated_at: '2023-04-10T20:34:20.575885+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credentials from Password Stores|T1555 - Credentials from Password Stores]]'
sub_techniques:
- '[[Credentials from Web Browsers|T1555.003 - Credentials from Web Browsers]]'
tags:
- '[[Find sensitive files]]'
- '[[Linux - Privilege Escalation]]'
- '[[Looting for passwords]]'
commands:
- '[[Locate password files]]'
---

# Linux Password Looting

## Summary

Linux Password Looting is a technique used by attackers to obtain sensitive information, such as passwords, from a compromised Linux system. This technique involves searching for files containing passwords and other sensitive information that are stored on the system. Attackers can then use this in

## Description

# Description

Linux Password Looting is a technique used by attackers to obtain sensitive information, such as passwords, from a compromised Linux system. This technique involves searching for files containing passwords and other sensitive information that are stored on the system. Attackers can then use this information to escalate privileges and gain access to additional resources on the system.

To locate password files, attackers typically search for files that contain specific keywords, such as 'password' or 'shadow'. These files may be stored in various locations on the system, including /etc/passwd and /etc/shadow. Once the files are located, attackers can use a variety of tools and techniques to extract the passwords and other sensitive information.

The business value of this technique is that it allows attackers to gain access to sensitive information that can be used to further compromise the system and steal valuable data.

## Requirements

1. Access to a compromised Linux system

1. Tools for searching and extracting information from files, such as grep and awk

## Defense

1. Implement strong password policies and regularly update passwords

1. Limit access to sensitive files containing passwords and other sensitive information

1. Monitor system logs and network traffic for suspicious activity

## Objectives

1. Locate files containing passwords and other sensitive information on a compromised Linux system

1. Extract passwords and other sensitive information from the located files

# Instructions

1. To locate password files, use the locate command followed by the keyword 'password'. To view the output in a more readable format, pipe it to the 'more' command.

**Code**: [[$ locate password | more           
/boot/grub/i38]]

> The 'locate' command is used to search for files and directories that match a specified pattern. In this case, we are searching for any files that have the word 'password' in their name. The 'more' command is used to display the output in a paginated format. This command is useful for finding files that may contain sensitive information such as passwords.

**Command** ([[Locate password files]]):

```bash
locate password
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credentials from Password Stores|T1555 - Credentials from Password Stores]]

### Sub-Techniques

- [[Credentials from Web Browsers|T1555.003 - Credentials from Web Browsers]]

## Commands Used

- [[Locate password files]]

## Tags

- [[Find sensitive files]]
- [[Linux - Privilege Escalation]]
- [[Looting for passwords]]
