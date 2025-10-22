---
id: 82b17d6c-00f8-47e7-a8cf-82448c825a31
name: Abusing Active Directory ACLs/ACEs to Retrieve LAPS Passwords
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.934873+00:00'
updated_at: '2023-04-10T20:26:20.299198+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
- '[[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]'
tags:
- '[[Abusing Active Directory ACLs/ACEs]]'
- '[[Active Directory Attacks]]'
- '[[ReadLAPSPassword]]'
commands:
- '[[Get LAPS Password Attribute for LAPS_PC$ Object]]'
---

# Abusing Active Directory ACLs/ACEs to Retrieve LAPS Passwords

## Summary

Abusing Active Directory ACLs/ACEs to retrieve LAPS passwords is a technique used by attackers to gain access to local administrator passwords for domain-joined computers. This technique involves manipulating the permissions of the LAPS password attribute in Active Directory to grant unauthorized u

## Description

# Description

Abusing Active Directory ACLs/ACEs to retrieve LAPS passwords is a technique used by attackers to gain access to local administrator passwords for domain-joined computers. This technique involves manipulating the permissions of the LAPS password attribute in Active Directory to grant unauthorized users access to the password. This can be accomplished by modifying the Access Control List (ACL) on the LAPS password attribute or by exploiting a misconfigured delegation of control in Active Directory. Once the attacker has access to the LAPS password, they can use it to gain access to the local administrator account on the target computer.

The technical details of this attack involve identifying the LAPS password attribute in Active Directory, modifying the ACLs/ACEs to grant access, and retrieving the password. The business value of this technique is that it allows attackers to gain access to sensitive data and systems, which can lead to data theft, system compromise, and financial loss.

## Requirements

1. Domain credentials with permissions to modify Active Directory ACLs/ACEs

1. Access to Active Directory

1. Knowledge of LAPS password attribute

## Defense

1. Regularly review and audit Active Directory permissions and delegations

1. Implement least privilege access controls for Active Directory

1. Monitor for and investigate suspicious changes to Active Directory ACLs/ACEs

## Objectives

1. Retrieve LAPS passwords for domain-joined computers

1. Gain access to local administrator accounts on target computers

# Instructions

1. To find computers with expired admin passwords, run the following command in PowerShell:

**Code**: [[Get-ADComputer -filter {ms-mcs-admpwdexpirationtim]]

> This command uses the Get-ADComputer cmdlet to search for computers where the ms-mcs-admpwdexpirationtime attribute is not empty, indicating that the admin password has expired. The cmdlet returns the ms-mcs-admpwd and ms-mcs-admpwdexpirationtime properties for each computer that matches the filter. This information can be used to identify computers that need to have their admin passwords reset.

2. To retrieve the Local Administrator Password Solution (LAPS) password and expiration time for a specific computer, use the getObjectAttributes command with the following syntax:

**Code**: [[bloodyAD.py -u john.doe -d bloody -p Password512 -]]

> - Replace 'LAPS_PC$' with the name of the computer you want to retrieve the password and expiration time for.
- The 'ms-mcs-admpwd' argument retrieves the LAPS password.
- The 'ms-mcs-admpwdexpirationtime' argument retrieves the expiration time of the LAPS password.

**Command** ([[Get LAPS Password Attribute for LAPS_PC$ Object]]):

```bash
bloodyAD.py -u john.doe -d bloody -p Password512 --host 192.168.10.2 getObjectAttributes LAPS_PC$ ms-mcs-admpwd,ms-mcs-admpwdexpirationtime
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]
- [[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]

## Commands Used

- [[Get LAPS Password Attribute for LAPS_PC$ Object]]

## Tags

- [[Abusing Active Directory ACLs/ACEs]]
- [[Active Directory Attacks]]
- [[ReadLAPSPassword]]
