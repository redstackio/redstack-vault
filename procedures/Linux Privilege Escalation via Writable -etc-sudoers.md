---
id: d54bfdf2-dc76-4c32-aac2-81942077d102
name: Linux Privilege Escalation via Writable /etc/sudoers
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.297121+00:00'
updated_at: '2023-04-10T20:34:29.628566+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
tags:
- '[[Linux - Privilege Escalation]]'
- '[[Writable /etc/sudoers]]'
- '[[Writable files]]'
commands:
- '[[Add sudo permissions for user ''username'']]'
- '[[Allow user ''username'' to run /bin/bash without password]]'
- '[[Allow user ''username'' to use sudo without password]]'
---

# Linux Privilege Escalation via Writable /etc/sudoers

## Summary

Privilege escalation is a common technique used by attackers to gain higher levels of access in a system. In this case, the attacker has identified a writable /etc/sudoers file, which can be leveraged to grant elevated privileges to an existing user. By adding the user to the sudoers file, the atta

## Description

# Description

Privilege escalation is a common technique used by attackers to gain higher levels of access in a system. In this case, the attacker has identified a writable /etc/sudoers file, which can be leveraged to grant elevated privileges to an existing user. By adding the user to the sudoers file, the attacker can execute commands with root privileges. This technique is commonly used by attackers to maintain persistence in a system and to move laterally within a network.

To execute this technique, the attacker must first identify a writable /etc/sudoers file. Once identified, the attacker can add the desired user to the file using the 'Grant SUDO Access to User' command. This will allow the user to execute commands with elevated privileges. 

This technique can be especially dangerous if the attacker is able to gain access to a highly privileged account, such as an administrator account. With this level of access, the attacker can compromise sensitive data, install malware, or take control of the entire system.

## Requirements

1. Access to a writable /etc/sudoers file

1. Access to a user account on the system

## Defense

1. Limit access to the /etc/sudoers file to only trusted users

1. Regularly monitor the /etc/sudoers file for unauthorized changes

1. Implement least privilege access controls to limit the impact of a successful privilege escalation attack

## Objectives

1. Grant elevated privileges to a user account

1. Maintain persistence in a system

1. Move laterally within a network

# Instructions

1. To grant SUDO access to a user, run the following commands:
1. Replace 'username' with the actual username of the user you want to grant SUDO access to.
2. Run the command 'sudo visudo' to open the sudoers file.
3. Add the following line to the file: 'username ALL=(ALL:ALL) ALL'.
4. Save and close the file.
5. Run the following commands to allow the user to use SUDO without a password:
'echo "username ALL=(ALL) NOPASSWD: ALL" >>/etc/sudoers'
'echo "username ALL=NOPASSWD: /bin/bash" >>/etc/sudoers'

**Code**: [[echo "username ALL=(ALL:ALL) ALL">>/etc/sudoers

#]]

> This command grants SUDO access to a user on a Linux system. The 'username' parameter should be replaced with the actual username of the user you want to grant access to. The first line adds the user to the sudoers file, giving them full access to all commands. The next two lines allow the user to use SUDO without entering a password. This can be useful in certain situations, but should be used with caution.

**Command** ([[Add sudo permissions for user 'username']]):

```bash
echo "username ALL=(ALL:ALL) ALL">>/etc/sudoers
```

**Command** ([[Allow user 'username' to use sudo without password]]):

```bash
echo "username ALL=(ALL) NOPASSWD: ALL" >>/etc/sudoers
```

**Command** ([[Allow user 'username' to run /bin/bash without password]]):

```bash
echo "username ALL=NOPASSWD: /bin/bash" >>/etc/sudoers
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]

## Commands Used

- [[Add sudo permissions for user 'username']]
- [[Allow user 'username' to run /bin/bash without password]]
- [[Allow user 'username' to use sudo without password]]

## Tags

- [[Linux - Privilege Escalation]]
- [[Writable /etc/sudoers]]
- [[Writable files]]
