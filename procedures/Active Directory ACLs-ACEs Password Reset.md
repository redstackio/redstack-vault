---
id: 890c2d7b-4ad9-4494-8d12-1f41a56ab490
name: Active Directory ACLs/ACEs Password Reset
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.016564+00:00'
updated_at: '2023-04-10T20:26:38.026479+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
- '[[Group Policy Modification|T1484 - Group Policy Modification]]'
- '[[Password Filter DLL|T1174 - Password Filter DLL]]'
- '[[Password Policy Discovery|T1201 - Password Policy Discovery]]'
tags:
- '[[Abusing Active Directory ACLs/ACEs]]'
- '[[Active Directory Attacks]]'
- '[[ForceChangePassword]]'
commands:
- '[[Using bloodyAD with pass-the-hash]]'
- '[[Using rpcclient from the Samba software suite]]'
---

# Active Directory ACLs/ACEs Password Reset

## Summary

An attacker can abuse Active Directory ACLs/ACEs to force a password reset for a user account. This technique involves modifying the ACLs/ACEs of an object in Active Directory to grant the attacker the necessary permissions to reset the password of a target user. This can be accomplished by modifyi

## Description

# Description

An attacker can abuse Active Directory ACLs/ACEs to force a password reset for a user account. This technique involves modifying the ACLs/ACEs of an object in Active Directory to grant the attacker the necessary permissions to reset the password of a target user. This can be accomplished by modifying the ACLs/ACEs of the target user's account or the ACLs/ACEs of a higher privileged account that can then be used to reset the target user's password. Once the password is reset, the attacker can use the new password to authenticate as the target user and gain access to resources within the organization.

This technique can be used to escalate privileges and gain access to sensitive information within an organization. It requires a good understanding of Active Directory and the permissions required to modify ACLs/ACEs.

## Requirements

1. Access to an account with permissions to modify ACLs/ACEs in Active Directory

## Defense

1. Implement least privilege access for all accounts in Active Directory

1. Monitor for changes to ACLs/ACEs in Active Directory

1. Implement multi-factor authentication to prevent unauthorized password resets

## Objectives

1. Escalate privileges within an organization

1. Gain access to sensitive information within an organization

# Instructions

1. Use either rpcclient or bloodyAD to change the password of a target user. In rpcclient, use the setuserinfo2 command with the target user and new password. In bloodyAD, use the changePassword command with the target user and new password. Make sure to provide the correct domain, attacker user credentials, and DC IP address if using bloodyAD with pass-the-hash.

**Code**: [[# Using rpcclient from the  Samba software suite
r]]

> The commands in this JSON object are used to change the password of a target user in a Windows domain. This is useful for lateral movement and privilege escalation. The rpcclient command is part of the Samba software suite and can be used to interact with Windows systems that have SMB enabled. The bloodyAD tool is a Python script that can be used to interact with Active Directory environments. Both commands require the attacker to have valid credentials for an account with permission to change the password of the target user. The target user's password will be changed to the value provided in the target_newpwd argument.

**Command** ([[Using rpcclient from the Samba software suite]]):

```bash
rpcclient -U 'attacker_user%my_password' -W DOMAIN -c "setuserinfo2 target_user 23 target_newpwd"
```

**Command** ([[Using bloodyAD with pass-the-hash]]):

```bash
bloodyAD.py --host [DC IP] -d DOMAIN -u attacker_user -p :B4B9B02E6F09A9BD760F388B67351E2B changePassword target_user target_newpwd
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]
- [[Group Policy Modification|T1484 - Group Policy Modification]]
- [[Password Filter DLL|T1174 - Password Filter DLL]]
- [[Password Policy Discovery|T1201 - Password Policy Discovery]]

## Commands Used

- [[Using bloodyAD with pass-the-hash]]
- [[Using rpcclient from the Samba software suite]]

## Tags

- [[Abusing Active Directory ACLs/ACEs]]
- [[Active Directory Attacks]]
- [[ForceChangePassword]]
