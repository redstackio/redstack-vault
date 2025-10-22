---
id: 0efb1e98-1ba8-4e00-aebe-4e6f6130986d
name: Mimikatz RDP Password Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.429767+00:00'
updated_at: '2023-04-10T20:37:15.514270+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[RDP Passwords]]'
- '[[Windows - Mimikatz]]'
---

# Mimikatz RDP Password Extraction

## Summary

Mimikatz RDP Password Extraction is a technique used to extract passwords from Remote Desktop Services (RDP) on Windows systems. This technique is often used by attackers to gain access to a network by compromising a user's RDP credentials. Mimikatz is a powerful tool that can extract passwords fro

## Description

# Description

Mimikatz RDP Password Extraction is a technique used to extract passwords from Remote Desktop Services (RDP) on Windows systems. This technique is often used by attackers to gain access to a network by compromising a user's RDP credentials. Mimikatz is a powerful tool that can extract passwords from memory, including RDP passwords. This technique can be used to gain access to a network or to escalate privileges within a network.

Technical Explanation: Mimikatz uses a technique called "pass-the-hash" to extract RDP passwords from memory. When a user logs into RDP, their password is stored in memory. Mimikatz can extract this password from memory and use it to gain access to the network.

Business Value: This technique can be used by attackers to gain access to a network, steal sensitive data, or disrupt business operations. By compromising RDP credentials, an attacker can gain access to a network and move laterally to other systems, potentially causing significant damage.

## Requirements

1. Local or remote access to a Windows system with RDP enabled

1. Mimikatz tool

## Defense

1. Disable RDP if it is not required

1. Implement strong password policies and multi-factor authentication

1. Monitor for suspicious activity, including failed login attempts

## Objectives

1. Extract RDP passwords from memory

1. Gain access to a network

1. Escalate privileges within a network

# Instructions

1. Run the following commands in PowerShell to check the status of the Remote Desktop Services: 
 - 'sc queryex termservice' to check if the service is running 
 - 'tasklist /M:rdpcorets.dll' to verify if the Remote Desktop Services DLL is loaded 
 - 'netstat -nob | Select-String TermService -Context 1' to check if the service is listening on any ports.

**Code**: [[sc queryex termservice
tasklist /M:rdpcorets.dll
n]]

> The 'sc queryex termservice' command provides information about the Remote Desktop Services, including the status of the service.

The 'tasklist /M:rdpcorets.dll' command lists all the running processes that have loaded the rdpcorets.dll module, which is required for Remote Desktop Services.

The 'netstat -nob | Select-String TermService -Context 1' command shows all the active network connections on the system and filters the output to show only the connections related to the Remote Desktop Services. This can help identify any network-related issues with the service.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Tags

- [[RDP Passwords]]
- [[Windows - Mimikatz]]
