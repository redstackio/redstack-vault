---
id: 5648de7c-2fbd-42d5-b5d9-dcba667dbfc8
name: ForceChangePassword Active Directory Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.988968+00:00'
updated_at: '2023-04-10T20:26:31.515668+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Account Manipulation|T1098 - Account Manipulation]]'
- '[[Brute Force|T1110 - Brute Force]]'
tags:
- '[[Abusing Active Directory ACLs/ACEs]]'
- '[[Active Directory Attacks]]'
- '[[ForceChangePassword]]'
commands:
- '[[Change Domain User Password]]'
---

# ForceChangePassword Active Directory Attack

## Summary

The ForceChangePassword Active Directory Attack is a technique used by attackers to change the password of a user account in Active Directory. This can be done by abusing the ACLs/ACEs (Access Control Lists/Access Control Entries) that control access to the user account. By changing the password, t

## Description

# Description

The ForceChangePassword Active Directory Attack is a technique used by attackers to change the password of a user account in Active Directory. This can be done by abusing the ACLs/ACEs (Access Control Lists/Access Control Entries) that control access to the user account. By changing the password, the attacker can gain access to the user's account and any resources that the user has access to.

From a technical perspective, the attacker needs to have sufficient permissions in Active Directory to modify the ACLs/ACEs of the user account. Once the permissions are obtained, the attacker can use a tool like 'Change User Password' to change the password of the user account.

The business value of this attack is that it allows the attacker to gain access to sensitive information or resources that are only accessible to the compromised user account. This can lead to data theft, data destruction, or unauthorized access to critical systems.

## Requirements

1. Sufficient permissions in Active Directory to modify the ACLs/ACEs of the user account.

1. Access to a tool like 'Change User Password'.

## Defense

1. Limit permissions in Active Directory to only those that are necessary for users to perform their job functions.

1. Monitor for changes to ACLs/ACEs in Active Directory and investigate any unauthorized changes.

1. Enforce strong password policies and require regular password changes.

## Objectives

1. Change the password of a user account in Active Directory.

1. Gain access to resources that the compromised user account has access to.

# Instructions

1. Use this command to change the password of the target user. Replace 'Password123!' with the desired password and 'TargetUser' with the username of the target user.

**Code**: [[$NewPassword = ConvertTo-SecureString 'Password123]]

> This command uses the ConvertTo-SecureString cmdlet to create a secure string object from the password provided. The Set-DomainUserPassword cmdlet is then used to set the password for the target user. The -Identity parameter is used to specify the username of the target user and the -AccountPassword parameter is used to specify the new password.

**Command** ([[Change Domain User Password]]):

```bash
$NewPassword = ConvertTo-SecureString 'Password123!' -AsPlainText -Force
Set-DomainUserPassword -Identity 'TargetUser' -AccountPassword $NewPassword
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Account Manipulation|T1098 - Account Manipulation]]
- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[Change Domain User Password]]

## Tags

- [[Abusing Active Directory ACLs/ACEs]]
- [[Active Directory Attacks]]
- [[ForceChangePassword]]
