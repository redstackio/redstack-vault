---
id: 35a01dc5-6dd7-4196-a2f8-f2dfe2f6b2ea
name: Windows - Password Looting via System and Application Logs
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.151925+00:00'
updated_at: '2023-04-10T20:37:32.977104+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
tags:
- '[[EoP - Looting for passwords]]'
- '[[Other files]]'
- '[[Windows - Privilege Escalation]]'
---

# Windows - Password Looting via System and Application Logs

## Summary

This procedure involves looting for passwords via Windows system and application logs. Attackers can gain access to these logs through various means of privilege escalation, and then use them to find stored passwords. By analyzing logs, attackers can identify weak passwords, reused passwords, and o

## Description

# Description

This procedure involves looting for passwords via Windows system and application logs. Attackers can gain access to these logs through various means of privilege escalation, and then use them to find stored passwords. By analyzing logs, attackers can identify weak passwords, reused passwords, and other valuable credentials. This technique can be used to gain access to other systems, applications, or networks.

 

## Requirements

1. Access to Windows system and application logs

1. Privilege escalation to access logs

1. Ability to analyze logs for valuable credentials

 

## Defense

1. Ensure logs are properly secured and access is restricted

1. Implement strong password policies to prevent weak or reused passwords

1. Monitor logs for suspicious activity and unauthorized access

 

## Objectives

1. Find and collect passwords stored in system and application logs

1. Use collected passwords to gain access to other systems, applications, or networks

 

# Instructions

1. This command will retrieve system and application logs from various locations on the system. The logs include pagefile.sys, NetSetup.log, sam, system, software, security, iis6.log, AppEvent.Evt, SecEvent.Evt, default.sav, security.sav, software.sav, system.sav, *.log files in CCM\logs, ntuser.dat, index.dat, hosts file, Configs folder in ProgramData, PowerShell folder in Program Files, vnc.ini, and ultravnc.ini files in the C drive.

 



**Code**: [[%SYSTEMDRIVE%\pagefile.sys
%WINDIR%\debug\NetSetup]]



> The command will search for logs and configuration files in various locations on the system. The retrieved logs may contain important system events and troubleshooting information. The command can be used to investigate system issues and security incidents. The retrieved logs can be analyzed using log analysis tools to identify system issues and security breaches.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

## Tags

- [[EoP - Looting for passwords]]
- [[Other files]]
- [[Windows - Privilege Escalation]]


