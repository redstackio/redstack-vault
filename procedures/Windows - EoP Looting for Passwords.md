---
id: f6793a11-c4b0-4cac-9cb9-bb924d9086d1
name: Windows - EoP Looting for Passwords
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.988087+00:00'
updated_at: '2023-04-10T20:37:53.834552+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[Credentials in Files|T1081 - Credentials in Files]]'
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
tags:
- '[[EoP - Looting for passwords]]'
- '[[Search for a file with a certain filename]]'
- '[[Windows - Privilege Escalation]]'
---

# Windows - EoP Looting for Passwords

## Summary

Elevation of Privileges (EoP) is a common technique used by attackers to escalate their privileges on a compromised system. One way attackers can achieve EoP is by looting for passwords. This technique involves searching for files on the target system that contain passwords or credentials. Attacker

## Description

# Description

Elevation of Privileges (EoP) is a common technique used by attackers to escalate their privileges on a compromised system. One way attackers can achieve EoP is by looting for passwords. This technique involves searching for files on the target system that contain passwords or credentials. Attackers can then use these credentials to escalate their privileges and gain access to additional resources on the network.

Technical Explanation: The attacker uses the 'Find Password and Credential Files' command to search for files containing passwords or credentials. These files may be stored in various locations on the target system, such as the Windows registry, configuration files, or log files. Once the attacker has obtained these credentials, they can use them to escalate their privileges and gain access to additional resources on the network.

Business Value: Attackers who successfully escalate their privileges can gain access to sensitive data, intellectual property, and other valuable resources. This can result in significant financial and reputational damage for the victim organization.

## Requirements

1. Access to a compromised Windows system

1. Ability to run commands on the target system

## Defense

1. Implement strong password policies and regularly change passwords

1. Monitor for file and directory changes, especially those containing sensitive information

1. Implement least privilege access controls to limit the impact of privilege escalation attacks

## Objectives

1. Obtain passwords or credentials from the target system

1. Escalate privileges on the target system

1. Gain access to additional resources on the network

# Instructions

1. This command will search for password and credential files in the system. It will search for files with the following extensions: txt, xml, ini, config, and files with the keywords 'pass', 'cred', and 'vnc' in their names. It will also search for a file named 'user.txt' and all files with the extension '.ini' recursively in the C:\ directory.

**Code**: [[dir /S /B *pass*.txt == *pass*.xml == *pass*.ini =]]

> The 'dir' command will search for files with the specified extensions and keywords in the current directory and all subdirectories. The 'where' command will search for files with the specified name or extension recursively in the specified directory. This command can be useful for finding sensitive information stored in plain text files or configuration files on a system.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[Credentials in Files|T1081 - Credentials in Files]]
- [[File and Directory Discovery|T1083 - File and Directory Discovery]]

## Tags

- [[EoP - Looting for passwords]]
- [[Search for a file with a certain filename]]
- [[Windows - Privilege Escalation]]
