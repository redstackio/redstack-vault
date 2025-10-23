---
id: 5ef1ec9e-6fc9-452e-ac97-ea3976f46ace
name: Windows - Restore Service Account Privileges via Impersonation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.093571+00:00'
updated_at: '2023-04-10T20:37:51.273035+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Replication Through Removable Media|T1091 - Replication Through Removable Media]]'
- '[[Service Execution|T1035 - Service Execution]]'
tags:
- '[[EoP - Impersonation Privileges]]'
- '[[Restore A Service Account''s Privileges]]'
- '[[Windows - Privilege Escalation]]'
---

# Windows - Restore Service Account Privileges via Impersonation

## Summary

This procedure aims to restore a service account's privileges via impersonation. Service accounts often have elevated privileges to perform specific tasks, and attackers may attempt to compromise these accounts to gain elevated access. By impersonating the service account, the attacker can restore 

## Description

# Description

This procedure aims to restore a service account's privileges via impersonation. Service accounts often have elevated privileges to perform specific tasks, and attackers may attempt to compromise these accounts to gain elevated access. By impersonating the service account, the attacker can restore any lost privileges and gain further access to the system. This technique can be used to escalate privileges on a compromised system, and can also be used to move laterally within a network.

 

## Requirements

1. User must have administrative access to the compromised system

1. FullPowers Command must be available on the system

 

## Defense

1. Limit the use of service accounts to only necessary tasks

1. Monitor for suspicious activity, such as unusual logins or changes to service account privileges

1. Implement multi-factor authentication for service accounts to prevent unauthorized access

 

## Objectives

1. Restore privileges to a compromised service account

1. Escalate privileges on a compromised system

1. Move laterally within a network

 

# Instructions

1. FullPowers is a tool that allows you to execute commands with system privileges on Windows. Use the -c flag to specify the command to execute with system privileges. Use the -z flag to execute the command in a new process with a new token. 

 



**Code**: [[# https://github.com/itm4n/FullPowers

c:\TOOLS>Fu]]



> The FullPowers tool is used to execute commands with system privileges on Windows. The -c flag is used to specify the command to execute with system privileges. The -z flag is used to execute the command in a new process with a new token. This tool can be used to obtain admin privileges or read sensitive files. For more information on how to leverage FullPowers to obtain admin privileges, please refer to the Full Privileges Cheat Sheet available at https://github.com/gtworek/Priv2Admin.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Replication Through Removable Media|T1091 - Replication Through Removable Media]]
- [[Service Execution|T1035 - Service Execution]]

## Tags

- [[EoP - Impersonation Privileges]]
- [[Restore A Service Account's Privileges]]
- [[Windows - Privilege Escalation]]


