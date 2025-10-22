---
id: 184da798-8082-4f0d-9405-4e5702e01830
name: Linux Privilege Escalation via Scheduled Tasks
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.742660+00:00'
updated_at: '2023-04-10T20:34:25.054026+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Scheduled Task|T1053 - Scheduled Task]]'
tags:
- '[[Cron jobs]]'
- '[[Linux - Privilege Escalation]]'
- '[[Scheduled tasks]]'
commands:
- '[[Cron Configuration Files]]'
- '[[Cron User Access Files]]'
- '[[List of Cron Jobs]]'
---

# Linux Privilege Escalation via Scheduled Tasks

## Summary

Linux systems often have scheduled tasks, such as Cron jobs, which can be exploited to escalate privileges. By identifying and exploiting a vulnerable Cron job, an attacker can execute code with elevated privileges. This can allow the attacker to gain access to sensitive information or perform mali

## Description

# Description

Linux systems often have scheduled tasks, such as Cron jobs, which can be exploited to escalate privileges. By identifying and exploiting a vulnerable Cron job, an attacker can execute code with elevated privileges. This can allow the attacker to gain access to sensitive information or perform malicious actions on the system.

To detect Cron jobs, tools like pspy can be used to monitor system calls and identify any new processes being started by the Cron daemon. By analyzing the output of pspy, an attacker can identify Cron jobs that are running and potentially identify vulnerabilities that can be exploited for privilege escalation.

This technique can be valuable for an attacker seeking to gain persistent access to a Linux system and maintain control over it.

## Requirements

1. Access to the Linux system

1. Knowledge of Linux command line tools

1. Access to pspy or similar system call monitoring tool

## Defense

1. Regularly monitor system logs and system call activity to detect any suspicious activity

1. Implement least privilege principles to limit the impact of any successful privilege escalation attacks

1. Regularly audit and review scheduled tasks, such as Cron jobs, to identify and remove any unnecessary or potentially vulnerable tasks

## Objectives

1. Identify vulnerable Cron jobs that can be exploited for privilege escalation

1. Execute code with elevated privileges to gain access to sensitive information or perform malicious actions on the system

# Instructions

1. Run the following commands to check the system configuration files and their permissions:
- crontab -l
- ls -alh /var/spool/cron;
- ls -al /etc/ | grep cron
- ls -al /etc/cron*
- cat /etc/cron*
- cat /etc/at.allow
- cat /etc/at.deny
- cat /etc/cron.allow
- cat /etc/cron.deny*

**Code**: [[/etc/init.d
/etc/cron*
/etc/crontab
/etc/cron.allo]]

> This command provides a list of system configuration files that can be checked for write permissions. It also provides a set of commands that can be run to check the permissions of these files. The output of these commands can be used to identify any files that have write permissions and may be vulnerable to exploitation. It is important to ensure that only authorized users have write permissions to these files to prevent unauthorized access and modification of the system configuration.

**Command** ([[List of Cron Jobs]]):

```bash
ls -alh /var/spool/cron;
ls -al /etc/ | grep cron
ls -al /etc/cron*
```

**Command** ([[Cron Configuration Files]]):

```bash
cat /etc/init.d
/etc/cron*
/etc/crontab
/etc/cron.allow
/etc/cron.d 
/etc/cron.deny
/etc/cron.daily
/etc/cron.hourly
/etc/cron.monthly
/etc/cron.weekly
/etc/sudoers
/etc/exports
/etc/anacrontab
/var/spool/cron
/var/spool/cron/crontabs/root
```

**Command** ([[Cron User Access Files]]):

```bash
cat /etc/at.allow
cat /etc/at.deny
cat /etc/cron.allow
cat /etc/cron.deny*
```

2. To detect a CRON job using pspy, run the following command:

**Code**: [[# print both commands and file system events and s]]

> This command will print both commands and file system events and scan procfs every 1000 ms (=1sec), allowing you to detect any CRON jobs that are running on the system.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Scheduled Task|T1053 - Scheduled Task]]

## Commands Used

- [[Cron Configuration Files]]
- [[Cron User Access Files]]
- [[List of Cron Jobs]]

## Tags

- [[Cron jobs]]
- [[Linux - Privilege Escalation]]
- [[Scheduled tasks]]
