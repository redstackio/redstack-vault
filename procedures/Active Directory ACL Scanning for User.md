---
id: 016ec01a-829e-4b74-96a5-67d13a250649
name: Active Directory ACL Scanning for User
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.678186+00:00'
updated_at: '2023-04-10T20:25:59.701265+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Permission Groups Discovery|T1069 - Permission Groups Discovery]]'
sub_techniques:
- '[[Domain Groups|T1069.002 - Domain Groups]]'
tags:
- '[[Abusing Active Directory ACLs/ACEs]]'
- '[[Active Directory Attacks]]'
commands:
- '[[ADACLScan]]'
---

# Active Directory ACL Scanning for User

## Summary

Active Directory Access Control Lists (ACLs) are used to define permissions on various objects within the domain. By scanning the ACLs for a specific user, an attacker can identify which objects the user has access to and what permissions they have. This information can then be used to further esca

## Description

# Description

Active Directory Access Control Lists (ACLs) are used to define permissions on various objects within the domain. By scanning the ACLs for a specific user, an attacker can identify which objects the user has access to and what permissions they have. This information can then be used to further escalate privileges or perform lateral movement within the network. 

To perform this attack, the attacker would use a tool to scan the ACLs for a specific user and then analyze the results to identify potential targets for further exploitation. This attack can be particularly effective when combined with other Active Directory attacks, such as Kerberoasting or Golden Ticket attacks.

The business value of this attack is that it can allow an attacker to gain access to sensitive information or systems within the network, potentially leading to data theft or system compromise.

 

## Requirements

1. Access to the Active Directory domain

1. A tool to scan the ACLs, such as BloodHound or PowerView

 

## Defense

1. Limit the number of users with administrative privileges within the domain

1. Regularly review and update the ACLs to ensure that users only have access to the objects they need

1. Monitor the network for suspicious activity, such as frequent scans of the Active Directory ACLs

 

## Objectives

1. Identify which objects within the domain a specific user has access to

1. Identify potential targets for further exploitation or lateral movement

 

# Instructions

1. To scan the Active Directory ACL for a specific user, use the ADACLScanner tool. Use the following command:

 



**Code**: [[ADACLScan.ps1 -Base "DC=contoso;DC=com" -Filter "(]]



> -Base: The base distinguished name (DN) of the search.
-Filter: The LDAP query filter to use.
-Scope: The scope of the search.
-EffectiveRightsPrincipal: The user account to check the effective permissions for.
-Output: The format to output the results in.
-Show: Whether to display the results in a console window or not.



**Command** ([[ADACLScan]]):

```bash
ADACLScan.ps1 -Base "DC=contoso;DC=com" -Filter "(&(AdminCount=1))" -Scope subtree -EffectiveRightsPrincipal User1 -Output HTML -Show
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Permission Groups Discovery|T1069 - Permission Groups Discovery]]

### Sub-Techniques

- [[Domain Groups|T1069.002 - Domain Groups]]

## Commands Used

- [[ADACLScan]]

## Tags

- [[Abusing Active Directory ACLs/ACEs]]
- [[Active Directory Attacks]]


