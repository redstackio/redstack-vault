---
id: a6311525-15fc-4836-aa89-80bfb805ffd2
name: Linux - Add Root User Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:17.910876+00:00'
updated_at: '2023-04-10T20:34:13.310629+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Account Manipulation|T1098 - Account Manipulation]]'
- '[[Create Account|T1136 - Create Account]]'
tags:
- '[[Add a root user]]'
- '[[Linux - Persistence]]'
commands:
- '[[Create new user and set password]]'
---

# Linux - Add Root User Persistence

## Summary

The Linux - Add Root User Persistence procedure involves creating a new root user account and setting its password. This allows an attacker to maintain access to the compromised system even if the original credentials are changed or removed. To execute this procedure, an attacker needs to have admi

## Description

# Description

The Linux - Add Root User Persistence procedure involves creating a new root user account and setting its password. This allows an attacker to maintain access to the compromised system even if the original credentials are changed or removed. To execute this procedure, an attacker needs to have administrative privileges on the target system. 

From a technical perspective, the attacker can use the 'Create and Set Password for a New User' command to create a new root user account and set its password. This can be done using standard Linux command-line tools such as 'useradd' and 'passwd'. Once the new user is created, the attacker can use it to access the system even if the original root account is disabled or removed.

The business value of this procedure is that it allows an attacker to maintain access to a compromised Linux system, enabling them to continue to steal data or use the system for malicious purposes.

## Requirements

1. Administrative privileges on the target Linux system

## Defense

1. Limit the use of administrative privileges on the target system to only necessary users

1. Monitor for new user accounts and changes to existing accounts on the target system

1. Implement multi-factor authentication for all user accounts on the target system

## Objectives

1. Create a new root user account on the target Linux system

1. Set the password for the new root user account

1. Maintain access to the compromised system even if the original credentials are changed or removed

# Instructions

1. To create a new user with username 'john', run the following commands in the terminal:

sudo useradd -ou 0 -g 0 john
sudo passwd john

The first command creates a new user with the specified username, and the second command sets a password for the user.

To set the password to 'linuxpassword', run the following command:

echo "linuxpassword" | passwd --stdin john

**Code**: [[sudo useradd -ou 0 -g 0 john
sudo passwd john
echo]]

> The 'useradd' command is used to create a new user in Linux. The '-ou' option specifies the ID of the user's primary group, and the '-g' option specifies the ID of the user's initial login group.

The 'passwd' command is used to set or change a user's password. In this case, the password for the user 'john' is being set.

The 'echo' command is used to print the string 'linuxpassword', which is then piped to the 'passwd' command using the '|' symbol. The '--stdin' option tells the 'passwd' command to read the new password from standard input, which is the output of the 'echo' command.

**Command** ([[Create new user and set password]]):

```bash
sudo useradd -ou 0 -g 0 john
sudo passwd john
echo "linuxpassword" | passwd --stdin john
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Account Manipulation|T1098 - Account Manipulation]]
- [[Create Account|T1136 - Create Account]]

## Commands Used

- [[Create new user and set password]]

## Tags

- [[Add a root user]]
- [[Linux - Persistence]]
