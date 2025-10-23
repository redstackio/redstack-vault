---
id: 6b3e4332-c5d9-4799-b713-875a3d46a940
name: Linux Password Looting via Recently Modified Files
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.517331+00:00'
updated_at: '2023-04-10T20:34:33.381095+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Event Triggered Execution|T1546 - Event Triggered Execution]]'
sub_techniques:
- '[[Accessibility Features|T1546.008 - Accessibility Features]]'
tags:
- '[[Last edited files]]'
- '[[Linux - Privilege Escalation]]'
- '[[Looting for passwords]]'
---

# Linux Password Looting via Recently Modified Files

## Summary

Linux Password Looting via Recently Modified Files is a technique used to escalate privileges on a Linux system. Attackers can use this technique to loot the password hashes from recently modified files on the target system. This method can be used to gain access to user accounts and escalate privi

## Description

# Description

Linux Password Looting via Recently Modified Files is a technique used to escalate privileges on a Linux system. Attackers can use this technique to loot the password hashes from recently modified files on the target system. This method can be used to gain access to user accounts and escalate privileges. The attacker can then use the stolen credentials to move laterally across the network and gain access to other systems.

To execute this technique, an attacker needs to identify recently modified files on the target system. The attacker can then loot the password hashes from these files and use them to escalate privileges. This technique can be executed using a variety of tools and methods, including command-line utilities and custom scripts.

This technique can be valuable to an attacker as it provides a way to gain access to user accounts and escalate privileges, which can help them to achieve their objectives.

 

## Requirements

1. Access to the target system.

1. Permission to execute commands on the system.

1. Knowledge of recently modified files on the target system.

 

## Defense

1. Ensure that file permissions are set correctly to prevent unauthorized access to sensitive files.

1. Use strong passwords and implement multi-factor authentication to make it more difficult for attackers to steal credentials.

1. Monitor the system for suspicious activity, such as unauthorized access to sensitive files or unusual network traffic.

 

## Objectives

1. To loot password hashes from recently modified files on the target system.

1. To use the stolen credentials to escalate privileges and gain access to other systems on the network.

 

# Instructions

1. To find recently modified files, use the 'find' command with the '-mmin' option followed by the number of minutes. In this example, we're searching for files modified within the last 10 minutes. The '2>/dev/null' part of the command redirects any errors to /dev/null so they aren't displayed on the screen. Finally, we use 'grep' to exclude any results from the /proc directory.

 



**Code**: [[find / -mmin -10 2>/dev/null | grep -Ev "^/proc"]]



> - 'find': command used to search for files and directories
- '/': starting directory for the search
- '-mmin': option to search for files modified within a certain number of minutes
- '-10': number of minutes to search for
- '2>/dev/null': redirects any errors to /dev/null so they aren't displayed on the screen
- 'grep': command used to search for patterns in files
- '-Ev': options to exclude any results that match the pattern
- '"^/proc"': pattern to exclude any results from the /proc directory

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]
- [[Event Triggered Execution|T1546 - Event Triggered Execution]]

### Sub-Techniques

- [[Accessibility Features|T1546.008 - Accessibility Features]]

## Tags

- [[Last edited files]]
- [[Linux - Privilege Escalation]]
- [[Looting for passwords]]


