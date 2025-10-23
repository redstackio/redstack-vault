---
id: b6c4a146-0b20-43f4-a79d-a6759a96ef4a
name: 'Windows - Privilege Escalation: EoP Looting for Passwords (SessionGopher)'
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.230393+00:00'
updated_at: '2023-04-10T20:37:49.215200+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[EoP - Looting for passwords]]'
- '[[Passwords stored in services]]'
- '[[Windows - Privilege Escalation]]'
---

# Windows - Privilege Escalation: EoP Looting for Passwords (SessionGopher)

## Summary

SessionGopher is a PowerShell script that gathers data about user sessions and passwords stored in memory on Windows systems. This script can be used by attackers to escalate privileges by stealing credentials of logged-in users. By using this script, attackers can gain access to sensitive informat

## Description

# Description

SessionGopher is a PowerShell script that gathers data about user sessions and passwords stored in memory on Windows systems. This script can be used by attackers to escalate privileges by stealing credentials of logged-in users. By using this script, attackers can gain access to sensitive information and elevate their privileges on the compromised system. 

From a technical perspective, SessionGopher works by using Windows API calls to extract password data from memory. It can extract passwords from various sources, including Windows Credential Manager, LSASS, and the SAM database. The script then saves the extracted data to a file for later use. 

The business value of this procedure lies in its ability to provide attackers with access to sensitive information and elevated privileges. This can lead to further compromise of the network and theft of valuable data.

 

## Requirements

1. Access to a Windows system

1. PowerShell installed on the system

1. User context with administrative privileges

 

## Defense

1. Regularly monitor and review logs for suspicious activity, including PowerShell execution

1. Implement the principle of least privilege to limit the access of user accounts

1. Use multi-factor authentication to protect against stolen credentials

 

## Objectives

1. Gather data about user sessions and passwords stored in memory on Windows systems

1. Escalate privileges by stealing credentials of logged-in users

1. Gain access to sensitive information and elevate privileges on the compromised system

 

# Instructions

1. To use SessionGopher, first download the script from the provided link. Import the module by specifying the path to the downloaded script. Then, run the Invoke-SessionGopher command with the desired arguments. The '-AllDomain' argument will search for saved sessions across all domains. The '-o' argument will output the results to a file. The '-u' and '-p' arguments can be used to specify a username and password for authentication if necessary.

 



**Code**: [[https://raw.githubusercontent.com/Arvanaghi/Sessio]]



> SessionGopher is a PowerShell script that searches for and saves session information for various remote access tools, including PuTTY, WinSCP, FileZilla, SuperPuTTY, and RDP. This can be useful for post-exploitation activities, as it allows an attacker to easily access previously saved credentials and session information.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Tags

- [[EoP - Looting for passwords]]
- [[Passwords stored in services]]
- [[Windows - Privilege Escalation]]


