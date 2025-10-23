---
id: 0486e193-04ec-4969-9235-70959a2b96f0
name: Linux - Privilege Escalation via Doas
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.048387+00:00'
updated_at: '2023-04-10T20:34:35.504301+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
sub_techniques:
- '[[Bypass User Account Control|T1548.002 - Bypass User Account Control]]'
tags:
- '[[Doas]]'
- '[[Linux - Privilege Escalation]]'
- '[[SUDO]]'
commands:
- '[[Install doas]]'
- '[[Install Sudo]]'
- '[[View doas.conf file]]'
---

# Linux - Privilege Escalation via Doas

## Summary

Privilege escalation via Doas is a technique used to gain higher privileges on a Linux system. Doas is similar to SUDO, allowing users to run commands as other users, including the root user. By exploiting a misconfiguration or vulnerability in Doas, an attacker can gain root privileges, allowing t

## Description

# Description

Privilege escalation via Doas is a technique used to gain higher privileges on a Linux system. Doas is similar to SUDO, allowing users to run commands as other users, including the root user. By exploiting a misconfiguration or vulnerability in Doas, an attacker can gain root privileges, allowing them to perform any action on the system. This technique is commonly used by attackers to gain persistence on a compromised system.

 

## Requirements

1. Access to a Linux system with Doas installed

1. Knowledge of the system and user privileges

 

## Defense

1. Regularly review and update the Doas configuration file to ensure it is secure

1. Limit the use of Doas to only necessary users and commands

1. Implement multi-factor authentication to prevent unauthorized access to the system

 

## Objectives

1. Gain root privileges on a Linux system

1. Maintain persistence on a compromised system

 

# Instructions

1. sudo allows a user to run programs with the security privileges of another user (by default, as the superuser). It prompts for the password of the current user unless the user is root or has been granted sudo access by the system administrator. Sudo is often used to execute commands with elevated privileges, such as installing software or modifying system files.

 



**Code**: [[sudo]]



> The sudo command stands for 'superuser do' and is used to execute commands with elevated privileges. It allows a user to run programs with the security privileges of another user (by default, as the superuser). This command is often used to execute commands that require root privileges, such as installing software or modifying system files. The sudo command can be used in combination with other commands to perform various tasks on a Linux system. For example, 'sudo apt-get update' can be used to update the system's package list, while 'sudo apt-get install' can be used to install new software packages. The sudo command is a powerful tool that should be used with caution to avoid accidentally damaging the system.



**Command** ([[Install Sudo]]):

```bash
sudo apt-get install sudo -y
```



2. The doas command is used to run commands with superuser privileges. It is similar to the sudo command.

 



**Code**: [[doas]]



> The doas command can be used to execute commands with elevated privileges, such as installing software or modifying system files. It requires the user to have the necessary permissions to execute the command with superuser privileges. The syntax for the doas command is as follows: doas [options] command [arguments]. The options and arguments are similar to those used with the sudo command. Some common options include -u to specify a different user, -s to run the shell specified in the SHELL environment variable, and -i to simulate an initial login. It is important to use the doas command with caution, as executing commands with superuser privileges can have unintended consequences.



**Command** ([[Install doas]]):

```bash
sudo apt-get install doas
```



3. To configure doas on OpenBSD, edit the /etc/doas.conf file with the desired permissions and rules. Refer to the doas.conf man page for more information.

 



**Code**: [[/etc/doas.conf]]



> The /etc/doas.conf file is used to configure the doas utility on OpenBSD. This file contains rules that specify which users are allowed to execute certain commands with elevated privileges, as well as the commands themselves. It is important to review and configure this file properly to ensure the security of the system.



**Command** ([[View doas.conf file]]):

```bash
cat /etc/doas.conf
```



4. To grant root access for the 'vim' command, run the following command:

permit nopass demo as root cmd vim

This command will allow the user 'demo' to run 'vim' command with root privileges without entering a password.

 



**Code**: [[permit nopass demo as root cmd vim]]



> The 'permit' command is used to grant specific permissions to users. In this case, we are granting the user 'demo' the permission to run the 'vim' command as the root user without having to enter a password. The 'nopass' keyword specifies that no password is required to run the command. The 'as root' keyword specifies that the command should be run as the root user. Finally, 'cmd vim' specifies the command that the user is allowed to run with root privileges.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]

### Sub-Techniques

- [[Bypass User Account Control|T1548.002 - Bypass User Account Control]]

## Commands Used

- [[Install doas]]
- [[Install Sudo]]
- [[View doas.conf file]]

## Tags

- [[Doas]]
- [[Linux - Privilege Escalation]]
- [[SUDO]]


