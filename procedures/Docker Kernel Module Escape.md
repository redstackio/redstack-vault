---
id: 6f6fc630-a1b9-4124-b4b1-081fb0e106e2
name: Docker Kernel Module Escape
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:17.245600+00:00'
updated_at: '2023-04-10T20:33:51.396977+00:00'
tags:
- '[[Breaking out of Docker via kernel modules loading]]'
- '[[Container - Docker Pentest]]'
commands:
- '[[View /proc/escape file]]'
---

# Docker Kernel Module Escape

## Summary

The Docker Kernel Module Escape procedure is a technique used to break out of a Docker container by exploiting a vulnerability in the kernel module loading process. This technique is commonly used by attackers to gain access to the host machine and potentially other containers running on the same h

## Description

# Description

The Docker Kernel Module Escape procedure is a technique used to break out of a Docker container by exploiting a vulnerability in the kernel module loading process. This technique is commonly used by attackers to gain access to the host machine and potentially other containers running on the same host. The attack involves loading a malicious kernel module that allows the attacker to execute arbitrary code on the host machine.

From a technical perspective, this attack is achieved by exploiting the way Docker loads kernel modules. By loading a malicious kernel module, the attacker can gain access to the host machine's kernel and execute arbitrary code. This attack can be particularly devastating in multi-tenant environments where multiple containers are running on the same host.

From a business perspective, this attack can result in significant data breaches, intellectual property theft, and financial loss. It is essential for organizations to take proactive measures to prevent this type of attack.

## Requirements

1. Access to the Docker container

1. Knowledge of the kernel module loading process

1. Ability to write and load a malicious kernel module

## Defense

1. Ensure that Docker is configured to use secure kernel settings

1. Monitor for suspicious kernel module loading activity

1. Implement network segmentation to prevent lateral movement

## Objectives

1. Gain access to the host machine

1. Execute arbitrary code on the host machine

1. Potentially gain access to other containers running on the same host

# Instructions

1. To escape proc files, use the following commands:
1. cd /proc/escape
2. echo '1' > hide
3. echo '1' > protect

The 'hide' file hides the module from the list of loaded kernel modules and the 'protect' file prevents the module from being unloaded.

**Code**: [[/proc/escape]]

> The 'cd' command changes the current directory to '/proc/escape'. The 'echo' command writes the value '1' to the 'hide' and 'protect' files respectively. This hides the module from the list of loaded kernel modules and prevents the module from being unloaded.

**Command** ([[View /proc/escape file]]):

```bash
/proc/escape
```

2. grep -E '<text>' <data>

**Code**: [[/proc/output]]

> This command filters the output of the given data file by searching for lines that contain the specified text. The '-E' option enables extended regular expressions. Replace '<text>' with the text to search for and '<data>' with the path to the data file.

## Commands Used

- [[View /proc/escape file]]

## Tags

- [[Breaking out of Docker via kernel modules loading]]
- [[Container - Docker Pentest]]
