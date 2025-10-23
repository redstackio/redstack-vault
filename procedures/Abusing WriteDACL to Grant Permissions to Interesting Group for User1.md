---
id: 496410c0-15dc-4442-b904-fbd41c1e8ad7
name: Abusing WriteDACL to Grant Permissions to Interesting Group for User1
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.859369+00:00'
updated_at: '2023-04-10T20:36:10.606929+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Account Manipulation|T1098 - Account Manipulation]]'
- '[[Permission Groups Discovery|T1069 - Permission Groups Discovery]]'
tags:
- '[[Abusing Active Directory ACLs/ACEs]]'
- '[[Active Directory Attacks]]'
- '[[WriteDACL]]'
commands:
- '[[Add User1 to INTERESTING_GROUP]]'
- '[[Add WriteMembers permission to INTERESTING_GROUP for User1]]'
- '[[Remove right for devil_user1 to INTERESTING_GROUP]]'
- '[[Set Generic All for devil_user1 to INTERESTING_GROUP]]'
---

# Abusing WriteDACL to Grant Permissions to Interesting Group for User1

## Summary

This procedure abuses the WriteDACL command to grant permissions to an interesting group for User1. This can be used to gain access to sensitive information or systems within the organization. WriteDACL is a powerful command that allows the attacker to modify the permissions of an object in Active 

## Description

# Description

This procedure abuses the WriteDACL command to grant permissions to an interesting group for User1. This can be used to gain access to sensitive information or systems within the organization. WriteDACL is a powerful command that allows the attacker to modify the permissions of an object in Active Directory. In this case, the attacker is granting write access to an interesting group for User1.

From a technical perspective, the attacker can use this technique to gain access to sensitive information or systems within the organization. From a business value perspective, this attack can result in the theft of sensitive data, intellectual property, or financial information. It can also result in the disruption of business operations and damage to the organization's reputation.

 

## Requirements

1. Valid credentials with sufficient permissions to modify Active Directory objects

1. Access to the Active Directory environment

 

## Defense

1. Implement the principle of least privilege to limit the permissions of user accounts

1. Monitor and review Active Directory permissions regularly to ensure they are appropriate

1. Implement multi-factor authentication to prevent unauthorized access to user accounts

 

## Objectives

1. Grant write access to an interesting group for User1

1. Gain access to sensitive information or systems within the organization

 

# Instructions

1. Use the WriteDACL command to set a new Discretionary Access Control List (DACL) on a specified domain.

 

The WriteDACL command is used to set a new DACL on a specified domain. This command requires administrative privileges and can only be run on a domain controller. The command takes several arguments, including the name of the domain, the security identifier (SID) of the new DACL, and the permissions that should be granted or denied to users or groups. The DACL determines which users or groups have access to specific resources on the domain, and which actions they are allowed to perform. It is important to carefully consider the permissions granted in the DACL to ensure that only authorized users or groups have access to sensitive resources on the domain.

2. This command will grant Write Members access to the Interesting Group for User1.

 



**Code**: [[Add-DomainObjectAcl -TargetIdentity "INTERESTING_G]]



> The 'Add-DomainObjectAcl' cmdlet is used to add access control entries (ACEs) to a security descriptor for a specified Active Directory Domain Services (AD DS) object. In this case, we are adding an ACE for User1 with the 'WriteMembers' right to the security descriptor of the Interesting Group. The 'net group' command is then used to add User1 to the Interesting Group. The '/add' switch adds the specified user to the group, while the '/domain' switch specifies that the group is in the domain context.



**Command** ([[Add WriteMembers permission to INTERESTING_GROUP for User1]]):

```bash
Add-DomainObjectAcl -TargetIdentity "INTERESTING_GROUP" -Rights WriteMembers -PrincipalIdentity User1
```





**Command** ([[Add User1 to INTERESTING_GROUP]]):

```bash
net group "INTERESTING_GROUP" User1 /add /domain
```



3. To set user rights on a group in Active Directory, run the following command: 

bloodyAD.py --host <domain_controller> -d <domain_name> -u <username> -p <password> setGenericAll <username> cn=<group_name>,dc=<domain_name>

To remove user rights on a group in Active Directory, run the same command with the 'False' argument at the end:

bloodyAD.py --host <domain_controller> -d <domain_name> -u <username> -p <password> setGenericAll <username> cn=<group_name>,dc=<domain_name> False

 



**Code**: [[bloodyAD.py --host my.dc.corp -d corp -u devil_use]]



> This command allows you to set or remove user rights on a group in Active Directory. The 'bloodyAD.py' script is used for this purpose and requires you to provide the domain controller, domain name, username, and password. The 'setGenericAll' command is used to set or remove the user rights, and you need to provide the username and group name as arguments. By default, the command sets the user rights to 'True', but you can remove the rights by adding the 'False' argument at the end of the command.



**Command** ([[Set Generic All for devil_user1 to INTERESTING_GROUP]]):

```bash
bloodyAD.py --host my.dc.corp -d corp -u devil_user1 -p P@ssword123 setGenericAll devil_user1 cn=INTERESTING_GROUP,dc=corp
```





**Command** ([[Remove right for devil_user1 to INTERESTING_GROUP]]):

```bash
bloodyAD.py --host my.dc.corp -d corp -u devil_user1 -p P@ssword123 setGenericAll devil_user1 cn=INTERESTING_GROUP,dc=corp False
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Account Manipulation|T1098 - Account Manipulation]]
- [[Permission Groups Discovery|T1069 - Permission Groups Discovery]]

## Commands Used

- [[Add User1 to INTERESTING_GROUP]]
- [[Add WriteMembers permission to INTERESTING_GROUP for User1]]
- [[Remove right for devil_user1 to INTERESTING_GROUP]]
- [[Set Generic All for devil_user1 to INTERESTING_GROUP]]

## Tags

- [[Abusing Active Directory ACLs/ACEs]]
- [[Active Directory Attacks]]
- [[WriteDACL]]


