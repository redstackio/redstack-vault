---
id: 57f1636e-c3b1-4b6a-b794-16f90d05fea6
name: Linux - Privilege Escalation via Systemd Timers
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.771506+00:00'
updated_at: '2023-04-10T20:34:34.059146+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
sub_techniques:
- '[[Sudo and Sudo Caching|T1548.003 - Sudo and Sudo Caching]]'
tags:
- '[[Linux - Privilege Escalation]]'
- '[[Systemd timers]]'
commands:
- '[[List Timers]]'
---

# Linux - Privilege Escalation via Systemd Timers

## Summary

Linux systems often use Systemd timers to schedule recurring tasks or jobs. Attackers can abuse these timers to escalate their privileges on a system. By creating a malicious timer or modifying an existing one, an attacker can execute arbitrary code with elevated privileges. This technique is often

## Description

# Description

Linux systems often use Systemd timers to schedule recurring tasks or jobs. Attackers can abuse these timers to escalate their privileges on a system. By creating a malicious timer or modifying an existing one, an attacker can execute arbitrary code with elevated privileges. This technique is often used in post-exploitation scenarios to maintain persistence on a compromised system. To mitigate this attack, it is important to regularly review and audit the existing timers on a system.

## Requirements

1. Access to a Linux system with Systemd timers

1. Knowledge of Linux command line

## Defense

1. Regularly review and audit the existing timers on a system

1. Restrict access to the Systemd timers configuration files

1. Monitor for suspicious or unauthorized changes to the timers configuration files

## Objectives

1. Escalate privileges on a Linux system

1. Maintain persistence on a compromised system

# Instructions

1. To list all the system timers, use the command 'systemctl list-timers --all'.

**Code**: [[systemctl list-timers --all
NEXT                  ]]

> This command lists all the active timers on the system along with their next activation time, time left until next activation, last activation time, and the service they activate. The output also includes the number of timers listed. This command is particularly useful in managing system services and scheduling tasks.

**Command** ([[List Timers]]):

```bash
systemctl list-timers --all
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]

### Sub-Techniques

- [[Sudo and Sudo Caching|T1548.003 - Sudo and Sudo Caching]]

## Commands Used

- [[List Timers]]

## Tags

- [[Linux - Privilege Escalation]]
- [[Systemd timers]]
