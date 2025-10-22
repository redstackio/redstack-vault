---
id: b41695a3-a0f8-45cd-b021-32e5b1ca63f6
name: Abusing Active Directory ACLs/ACEs with WriteDACL Command and ACL Discovery
  and Pwnage Tool
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.830760+00:00'
updated_at: '2023-04-10T20:26:00.471615+00:00'
tags:
- '[[Abusing Active Directory ACLs/ACEs]]'
- '[[Active Directory Attacks]]'
- '[[WriteDACL]]'
commands:
- '[[Writing DACL]]'
---

# Abusing Active Directory ACLs/ACEs with WriteDACL Command and ACL Discovery and Pwnage Tool

## Summary

Abusing Active Directory ACLs/ACEs with WriteDACL Command and ACL Discovery and Pwnage Tool is a technique used to escalate privileges and gain unauthorized access to critical data and systems. This technique involves modifying the Access Control Lists (ACLs) and Access Control Entries (ACEs) of Ac

## Description

# Description

Abusing Active Directory ACLs/ACEs with WriteDACL Command and ACL Discovery and Pwnage Tool is a technique used to escalate privileges and gain unauthorized access to critical data and systems. This technique involves modifying the Access Control Lists (ACLs) and Access Control Entries (ACEs) of Active Directory objects. The WriteDACL command and ACL Discovery and Pwnage Tool are used to identify and modify the ACLs and ACEs of Active Directory objects. This technique can be used to gain access to sensitive data, escalate privileges, and move laterally within the network. 

Technical Explanation: WriteDACL command is used to modify the DACL of an Active Directory object. The ACL Discovery and Pwnage Tool is used to identify the objects with weak ACLs and ACEs. The attackers can use this information to modify the ACLs and ACEs of the objects to gain unauthorized access. 

Business Value: This technique can be used to gain access to sensitive data and critical systems. Attackers can use this technique to steal sensitive data, disrupt business operations, and cause financial losses.

## Requirements

1. Access to an Active Directory environment

1. Authenticated access to modify the ACLs and ACEs

1. WriteDACL command and ACL Discovery and Pwnage Tool

## Defense

1. Regularly review and update the ACLs and ACEs of Active Directory objects

1. Implement the principle of least privilege to limit the access of users and systems

1. Monitor and analyze the network traffic and behavior to detect any suspicious activity

## Objectives

1. Gain unauthorized access to critical systems and data

1. Escalate privileges

1. Move laterally within the network

# Instructions

1. The WriteDacl command is used to modify the discretionary access control list (DACL) of a specified file or directory. This command allows you to grant or revoke permissions to specific users or groups.

**Code**: [[WriteDacl]]

> The WriteDacl command takes several arguments, including the path to the file or directory you want to modify and the specific permissions you want to grant or revoke. For example, to grant read and write access to a user named 'JohnDoe' for a file located at C:\example\file.txt, you would use the following command: WriteDacl C:\example\file.txt /grant JohnDoe:(R,W). The '/grant' argument specifies that you want to grant permissions, and the '(R,W)' argument specifies that you want to grant both read and write access. You can also use the '/revoke' argument to revoke permissions, and the '/deny' argument to explicitly deny permissions.

**Command** ([[Writing DACL]]):

```bash
WRITE DACL HERE
```

2. To use this tool, run the Invoke-ACL.ps1 script with the appropriate arguments. The SharpHoundLocation and mimikatzLocation arguments should point to the locations of the respective tools on your system. The Username and Password arguments should be set to the credentials of a user with sufficient privileges to perform the necessary actions. The Domain argument should be set to the name of the Active Directory domain being targeted.

**Code**: [[./Invoke-ACL.ps1 -SharpHoundLocation .\sharphound.]]

> This tool is designed to automate the process of discovering and exploiting unsafe ACL configurations in Active Directory. It does this by using the SharpHound tool to collect information about the AD environment, and then using mimikatz to extract credentials that can be used to escalate privileges and take control of the affected systems. The tool is intended for use by penetration testers and other security professionals, and should only be used with appropriate authorization and legal permission.

## Commands Used

- [[Writing DACL]]

## Tags

- [[Abusing Active Directory ACLs/ACEs]]
- [[Active Directory Attacks]]
- [[WriteDACL]]
