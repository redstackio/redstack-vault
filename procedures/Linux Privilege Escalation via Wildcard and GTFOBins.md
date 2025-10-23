---
id: 781c347b-9b9a-4252-8408-ff782ee1ab9e
name: Linux Privilege Escalation via Wildcard and GTFOBins
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.128928+00:00'
updated_at: '2023-04-10T20:34:29.969326+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[Linux - Privilege Escalation]]'
- '[[Wildcard]]'
---

# Linux Privilege Escalation via Wildcard and GTFOBins

## Summary

This procedure involves exploiting a wildcard vulnerability and using GTFOBins to escalate privileges on a Linux system. Attackers can use this technique to gain access to sensitive data or systems that they would not normally have access to. By exploiting a vulnerability in the wildcard functional

## Description

# Description

This procedure involves exploiting a wildcard vulnerability and using GTFOBins to escalate privileges on a Linux system. Attackers can use this technique to gain access to sensitive data or systems that they would not normally have access to. By exploiting a vulnerability in the wildcard functionality, attackers can execute commands as a higher privileged user. Once escalated, attackers can perform malicious activities such as stealing sensitive data, installing malware or pivoting to other systems. This technique is commonly used by attackers to gain full control of a targeted system.

 

## Requirements

1. Access to a vulnerable Linux system

1. Knowledge of wildcard vulnerability exploitation

1. GTFOBins tool

 

## Defense

1. Regularly update and patch Linux systems to mitigate known vulnerabilities

1. Implement least privilege access controls to limit the impact of privilege escalation attacks

1. Monitor system logs for suspicious activity and implement intrusion detection and prevention measures

 

## Objectives

1. Escalate privileges on a Linux system

1. Gain access to sensitive data or systems

 

# Instructions

1. To exploit a Unix binary using GTFOBins, follow these steps:
1. Identify the binary that can be exploited.
2. Search for the binary on [GTFOBins](https://gtfobins.github.io).
3. Copy the exploit code for the binary.
4. Paste the code in a file and save it.
5. Make the file executable.
6. Run the file to exploit the binary.

 



**Code**: [[# create file for exploitation
touch -- "--checkpo]]



> This command provides a set of instructions to exploit Unix binaries using GTFOBins, which is a curated list of Unix binaries that can be exploited by an attacker to bypass local security restrictions. The `data` field provides a sample exploit code to create a file for exploitation and run a vulnerable script. The `lang` field specifies the language used in the exploit code. The `text` field provides a brief introduction to GTFOBins. The `instruction` field provides step-by-step instructions to exploit a Unix binary using GTFOBins. The `name` field provides a name for the command, which is 'Exploit Unix Binaries using GTFOBins'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Tags

- [[Linux - Privilege Escalation]]
- [[Wildcard]]


