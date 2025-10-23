---
id: d59f6973-770a-4078-8499-6df4438b2f4b
name: Linux - Predictable PRNG SSH Key Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.629320+00:00'
updated_at: '2023-04-10T20:34:29.306798+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Linux - Privilege Escalation]]'
- '[[SSH Key]]'
- '[[SSH Key Predictable PRNG (Authorized_Keys) Process]]'
commands:
- '[[Add ssh-dss to PubkeyAcceptedKeyTypes in ssh_config and sshd_config and restart
  ssh service]]'
---

# Linux - Predictable PRNG SSH Key Privilege Escalation

## Summary

This procedure involves exploiting a predictable pseudo-random number generator (PRNG) used in the creation of SSH keys. The attacker can add a malicious key to the authorized_keys file of the target user, which can then be used to gain privileged access to the system. This technique is commonly us

## Description

# Description

This procedure involves exploiting a predictable pseudo-random number generator (PRNG) used in the creation of SSH keys. The attacker can add a malicious key to the authorized_keys file of the target user, which can then be used to gain privileged access to the system. This technique is commonly used by attackers to gain access to sensitive information or to move laterally within a network. From a technical perspective, the attacker would need to have access to the target system and the ability to modify the authorized_keys file. The business value of this attack lies in the ability to gain access to sensitive information or to gain control of critical systems.

 

## Requirements

1. Access to the target system

1. Ability to modify the authorized_keys file

 

## Defense

1. Use a strong PRNG to generate SSH keys

1. Regularly monitor and review the authorized_keys file for unauthorized keys

1. Implement multi-factor authentication to prevent unauthorized access

 

## Objectives

1. Add a malicious SSH key to the authorized_keys file of the target user

1. Gain privileged access to the target system

 

# Instructions

1. To add support for SSH-dss keys, run the following commands:

 



**Code**: [[echo "PubkeyAcceptedKeyTypes=+ssh-dss" >> /etc/ssh]]



> This command adds SSH-dss to the list of accepted key types in the SSH configuration files. This is useful if you need to connect to an older server that doesn't support newer key types. The first two commands append a line to the ssh_config and sshd_config files, respectively, and the third command restarts the SSH service to apply the changes.



**Command** ([[Add ssh-dss to PubkeyAcceptedKeyTypes in ssh_config and sshd_config and restart ssh service]]):

```bash
echo "PubkeyAcceptedKeyTypes=+ssh-dss" >> /etc/ssh/ssh_config
echo "PubkeyAcceptedKeyTypes=+ssh-dss" >> /etc/ssh/sshd_config
/etc/init.d/ssh restart
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Add ssh-dss to PubkeyAcceptedKeyTypes in ssh_config and sshd_config and restart ssh service]]

## Tags

- [[Linux - Privilege Escalation]]
- [[SSH Key]]
- [[SSH Key Predictable PRNG (Authorized_Keys) Process]]


