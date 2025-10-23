---
id: 3f9cf19c-6735-45fb-9b6d-e24d96089fd3
name: Active Directory Object Owner Hijacking
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.897952+00:00'
updated_at: '2023-04-10T20:26:31.142681+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[Modify Existing Service|T1031 - Modify Existing Service]]'
- '[[Valid Accounts|T1078 - Valid Accounts]]'
tags:
- '[[Abusing Active Directory ACLs/ACEs]]'
- '[[Active Directory Attacks]]'
- '[[WriteOwner]]'
commands:
- '[[Set Domain Object Owner]]'
- '[[Set Owner of target_object to devil_user1]]'
---

# Active Directory Object Owner Hijacking

## Summary

Active Directory Object Owner Hijacking is a technique used to gain persistence and evade detection in an Active Directory environment. This attack involves modifying the ownership of a target object in Active Directory, giving the attacker full control over the object and any associated permission

## Description

# Description

Active Directory Object Owner Hijacking is a technique used to gain persistence and evade detection in an Active Directory environment. This attack involves modifying the ownership of a target object in Active Directory, giving the attacker full control over the object and any associated permissions. This can be used to escalate privileges, maintain persistence, and evade detection by security tools.

To execute this attack, the attacker needs to have the necessary permissions to modify the object's owner. This can be achieved through various means such as exploiting vulnerabilities, using stolen credentials, or abusing misconfigured ACLs/ACEs.

From a business perspective, this attack can lead to significant data breaches, loss of sensitive information, and reputational damage. It is important for organizations to implement proper security measures to prevent and detect such attacks.

 

## Requirements

1. Access to the target Active Directory environment

1. Sufficient permissions to modify object ownership

 

## Defense

1. Implement proper access controls and permissions to prevent unauthorized modification of object ownership

1. Monitor and analyze Active Directory logs for any suspicious activity related to object ownership changes

1. Regularly review and update ACLs/ACEs to ensure they are properly configured and do not contain any vulnerabilities

 

## Objectives

1. Gain persistence in an Active Directory environment

1. Escalate privileges

1. Evade detection by security tools

 

# Instructions

1. Use the Set-DomainObjectOwner command to change the owner of the target object to a principal controlled by the attacker.

 



**Code**: [[Set-DomainObjectOwner -Identity 'target_object' -O]]



> The Set-DomainObjectOwner command is used to update the owner of a given object in the domain. In this scenario, the attacker uses this command to change the owner of the target object to a principal that they control. By doing so, the attacker gains complete control over the object and can manipulate it in any way they see fit. This can be particularly dangerous if the object in question contains sensitive data or is used for critical functions within the domain.



**Command** ([[Set Domain Object Owner]]):

```bash
Set-DomainObjectOwner -Identity 'target_object' -OwnerIdentity 'controlled_principal'
```



2. This command sets the owner of the target object to the specified user.

 



**Code**: [[bloodyAD.py --host my.dc.corp -d corp -u devil_use]]



> Arguments:
--host: The hostname of the domain controller.
-d: The name of the domain.
-u: The username of the user with permissions to set the owner.
-p: The password of the user.
setOwner: The command to set the owner of the target object.
devil_user1: The username of the user to set as the owner.
target_object: The name of the target object to set the owner for.



**Command** ([[Set Owner of target_object to devil_user1]]):

```bash
bloodyAD.py --host my.dc.corp -d corp -u devil_user1 -p P@ssword123 setOwner devil_user1 target_object
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[Modify Existing Service|T1031 - Modify Existing Service]]
- [[Valid Accounts|T1078 - Valid Accounts]]

## Commands Used

- [[Set Domain Object Owner]]
- [[Set Owner of target_object to devil_user1]]

## Tags

- [[Abusing Active Directory ACLs/ACEs]]
- [[Active Directory Attacks]]
- [[WriteOwner]]


