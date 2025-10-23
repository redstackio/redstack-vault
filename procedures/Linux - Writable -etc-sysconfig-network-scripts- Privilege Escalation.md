---
id: bde66c0e-b1d4-4c22-b296-de55267f37f0
name: Linux - Writable /etc/sysconfig/network-scripts/ Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.195678+00:00'
updated_at: '2023-04-10T20:34:24.698689+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
- '[[Setuid and Setgid|T1166 - Setuid and Setgid]]'
tags:
- '[[Linux - Privilege Escalation]]'
- '[[Writable /etc/sysconfig/network-scripts/ (Centos/Redhat)]]'
- '[[Writable files]]'
---

# Linux - Writable /etc/sysconfig/network-scripts/ Privilege Escalation

## Summary

This procedure involves exploiting a vulnerability in the /etc/sysconfig/network-scripts/ directory on a Centos or Redhat system where the directory is writable. Attackers can modify network configuration files in this directory to execute arbitrary commands as root. This can be used to escalate pr

## Description

# Description

This procedure involves exploiting a vulnerability in the /etc/sysconfig/network-scripts/ directory on a Centos or Redhat system where the directory is writable. Attackers can modify network configuration files in this directory to execute arbitrary commands as root. This can be used to escalate privileges and gain full control of the system. This technique is commonly used in post-exploitation scenarios where the attacker has already gained access to a low-privileged account on the system.

Technical Explanation: Attackers can modify the network interface configuration files in the /etc/sysconfig/network-scripts/ directory to include arbitrary commands that will be executed as the root user. This is possible because the scripts in this directory are executed with root privileges during system startup. To exploit this vulnerability, attackers need to have write access to the directory.

Business Value: This procedure can be used by attackers to gain full control of a system, allowing them to steal sensitive data, install malware, or use the system as a pivot point to launch further attacks.

 

## Requirements

1. Write access to /etc/sysconfig/network-scripts/ directory

 

## Defense

1. Restrict write access to the /etc/sysconfig/network-scripts/ directory

1. Monitor the directory for any unauthorized changes

1. Implement the principle of least privilege to limit the impact of a successful attack

 

## Objectives

1. Gain root privileges on the target system

1. Execute arbitrary commands as the root user

 

# Instructions

1. To configure a network interface, use the following commands:
1. NAME: Enter the name of the network interface.
2. ONBOOT: Set to 'yes' to enable the interface on boot.
3. DEVICE: Specify the device name of the interface.
4. EXEC: Enter the command to execute.

For example:
NAME=eth0
ONBOOT=yes
DEVICE=eth0
EXEC:/etc/sysconfig/network-scripts/ifcfg-1337

 



**Code**: [[NAME=Network /bin/id <= Note the blank space
ONBOO]]



> This command is used to configure a network interface on a Linux system. The 'NAME' field specifies the name of the network interface, 'ONBOOT' field is used to enable the interface on boot, 'DEVICE' field specifies the device name of the interface and 'EXEC' is the command to execute. This command is useful when you need to configure a new network interface or modify an existing one.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]
- [[Setuid and Setgid|T1166 - Setuid and Setgid]]

## Tags

- [[Linux - Privilege Escalation]]
- [[Writable /etc/sysconfig/network-scripts/ (Centos/Redhat)]]
- [[Writable files]]


