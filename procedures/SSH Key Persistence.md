---
id: 9c204191-31d4-4de5-9beb-f5e002c381ea
name: SSH Key Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.150019+00:00'
updated_at: '2023-04-10T20:34:16.190799+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[AppInit DLLs|T1103 - AppInit DLLs]]'
tags:
- '[[Backdooring the SSH]]'
- '[[Linux - Persistence]]'
commands:
- '[[Create SSH Directory]]'
---

# SSH Key Persistence

## Summary

SSH Key Persistence is a technique used by attackers to maintain access to a compromised Linux machine. By adding a malicious SSH key to the authorized_keys file, attackers can ensure that they can access the system even if the original credentials are changed. This technique is often used in conju

## Description

# Description

SSH Key Persistence is a technique used by attackers to maintain access to a compromised Linux machine. By adding a malicious SSH key to the authorized_keys file, attackers can ensure that they can access the system even if the original credentials are changed. This technique is often used in conjunction with other persistence techniques to ensure that the attacker can maintain access to the system even after a reboot. From a technical perspective, this technique involves adding a public key to the authorized_keys file in the ~/.ssh directory of the target user. The private key is then used by the attacker to gain access to the system. The business value of this technique is that it allows attackers to maintain access to a system and continue to exfiltrate data or use the system for other malicious purposes.

 

## Requirements

1. Access to the target Linux machine

1. Knowledge of the target user's credentials

 

## Defense

1. Regularly monitor the authorized_keys file for any unauthorized changes

1. Implement two-factor authentication for SSH access

1. Restrict access to the authorized_keys file to prevent unauthorized modifications

 

## Objectives

1. Maintain access to a compromised Linux machine

1. Ensure continued access to the system even after a reboot

 

# Instructions

1. To add an ssh key into the specified directory, follow the below steps:
1. Generate a new ssh key using the command 'ssh-keygen'.
2. Copy the public key generated to the remote server using the command 'ssh-copy-id -i ~/.ssh/id_rsa.pub user@host'.
3. Enter the password for the user when prompted.
4. The ssh key has now been added to the authorized keys list on the remote server.

Alternatively, you can manually add the public key to the authorized_keys file on the remote server.
1. Copy the public key generated to your clipboard using the command 'pbcopy < ~/.ssh/id_rsa.pub'.
2. SSH into the remote server using the command 'ssh user@host'.
3. Create the .ssh directory if it doesn't already exist using the command 'mkdir -p ~/.ssh'.
4. Create the authorized_keys file using the command 'touch ~/.ssh/authorized_keys'.
5. Open the file using a text editor and paste the public key into the file.
6. Save and exit the file.
7. The ssh key has now been added to the authorized keys list on the remote server.

 



**Code**: [[~/.ssh]]



> This command is used to add an ssh key to the specified directory. The ssh key can be used to authenticate the user when logging into a remote server. The command provides detailed instructions on how to generate a new ssh key and add it to the authorized keys list on the remote server. The user can choose to either use the ssh-copy-id command or manually add the public key to the authorized_keys file on the remote server.



**Command** ([[Create SSH Directory]]):

```bash
~/.ssh
```



## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[AppInit DLLs|T1103 - AppInit DLLs]]

## Commands Used

- [[Create SSH Directory]]

## Tags

- [[Backdooring the SSH]]
- [[Linux - Persistence]]


