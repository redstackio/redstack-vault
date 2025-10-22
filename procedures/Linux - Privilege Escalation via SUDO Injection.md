---
id: b1798713-c622-46ac-96c1-cc033f0341e5
name: Linux - Privilege Escalation via SUDO Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.083524+00:00'
updated_at: '2023-04-10T20:34:21.316412+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
sub_techniques:
- '[[Setuid and Setgid|T1548.001 - Setuid and Setgid]]'
tags:
- '[[Linux - Privilege Escalation]]'
- '[[SUDO]]'
- '[[sudo_inject]]'
commands:
- '[[Create Invalid Sudo Tokens]]'
- '[[Get Root Privileges]]'
- '[[Run Exploit Script]]'
---

# Linux - Privilege Escalation via SUDO Injection

## Summary

Linux systems often use SUDO to give users elevated privileges. However, if the SUDO configuration is not properly secured, an attacker may be able to inject malicious commands into the SUDO configuration file and execute them with elevated privileges. This technique is called SUDO Injection. 

To 

## Description

# Description

Linux systems often use SUDO to give users elevated privileges. However, if the SUDO configuration is not properly secured, an attacker may be able to inject malicious commands into the SUDO configuration file and execute them with elevated privileges. This technique is called SUDO Injection. 

To perform SUDO Injection, the attacker needs to have access to the target machine and knowledge of the SUDO configuration file. Once the attacker has identified a vulnerable configuration file, they can inject malicious commands into it. When a user executes a command with SUDO privileges, the injected command will also be executed with elevated privileges, allowing the attacker to escalate their privileges and gain persistent access to the system. 

SUDO Injection can be a powerful technique for attackers to gain persistent access to a system and move laterally within a network. It is important for system administrators to properly secure their SUDO configurations to prevent this type of attack.

## Requirements

1. Access to the target machine

1. Knowledge of the SUDO configuration file

1. Ability to modify the SUDO configuration file

## Defense

1. Properly secure the SUDO configuration file by limiting access to it

1. Monitor the SUDO configuration file for unauthorized changes

1. Implement least privilege policies to limit the impact of a successful attack

## Objectives

1. Escalate privileges on a Linux system

1. Gain persistent access to the system

1. Move laterally within a network

# Instructions

1. To bypass the sudo password, follow these steps:
1. Run the command `sudo whatever`.
2. When prompted for a password, press <ctrl>+c to create an invalid sudo token.
3. Run the command `sh exploit.sh`.
4. Wait for 1 second.
5. Run the command `sudo -i`.
6. You should now have root access without needing a password.

Note: This exploit uses the [sudo_inject](https://github.com/nongiach/sudo_inject) tool.

**Code**: [[$ sudo whatever
[sudo] password for user:    
# Pr]]

> This command explains how to bypass the sudo password on a system. It provides detailed steps to follow and also mentions the tool used to perform the exploit.

**Command** ([[Create Invalid Sudo Tokens]]):

```bash
# Press <ctrl>+c since you don't have the password. 
# This creates an invalid sudo tokens.
```

**Command** ([[Run Exploit Script]]):

```bash
$ sh exploit.sh
```

**Command** ([[Get Root Privileges]]):

```bash
$ sudo -i # no password required :)
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]

### Sub-Techniques

- [[Setuid and Setgid|T1548.001 - Setuid and Setgid]]

## Commands Used

- [[Create Invalid Sudo Tokens]]
- [[Get Root Privileges]]
- [[Run Exploit Script]]

## Tags

- [[Linux - Privilege Escalation]]
- [[SUDO]]
- [[sudo_inject]]
