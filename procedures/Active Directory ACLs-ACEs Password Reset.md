---
id: "890c2d7b-4ad9-4494-8d12-1f41a56ab490"
name: "Active Directory ACLs/ACEs Password Reset"
type: procedure
verified: false
submitted: false
created_at: "2023-04-06T03:56:07.016564+00:00"
updated_at: "2023-04-10T20:26:38.026479+00:00"
tactics: ["[[Credential Access|TA0006 - Credential Access]]","[[Defense Evasion|TA0005 - Defense Evasion]]","[[Discovery|TA0007 - Discovery]]","[[Privilege Escalation|TA0004 - Privilege Escalation]]"]
techniques: ["[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]","[[Group Policy Modification|T1484 - Group Policy Modification]]","[[Password Filter DLL|T1174 - Password Filter DLL]]","[[Password Policy Discovery|T1201 - Password Policy Discovery]]"]
sub_techniques: []
tags: ["[[Abusing Active Directory ACLs/ACEs]]","[[Active Directory Attacks]]","[[ForceChangePassword]]"]
commands: ["[[Using bloodyAD with pass-the-hash]]","[[Using rpcclient from the Samba software suite]]"]
platforms: ["[[Windows]]"]
tools: ["[[rpcclient]]","[[bloodyAD]]"]
---

# Active Directory ACLs/ACEs Password Reset

## Summary

This procedure allows an attacker to abuse Active Directory Access Control Lists (ACLs) and Access Control Entries (ACEs) to force a password reset for a target user account, enabling privilege escalation or lateral movement by granting the attacker permissions like ForceChangePassword to modify user credentials without direct administrative access.

## Description

An attacker can abuse Active Directory ACLs/ACEs to force a password reset for a user account. This technique involves modifying the ACLs/ACEs of an object in Active Directory to grant the attacker the necessary permissions to reset the password of a target user. This can be accomplished by modifying the ACLs/ACEs of the target user's account or the ACLs/ACEs of a higher privileged account that can then be used to reset the target user's password. Once the password is reset, the attacker can use the new password to authenticate as the target user and gain access to resources within the organization.

This technique can be used to escalate privileges and gain access to sensitive information within an organization. It requires a good understanding of Active Directory and the permissions required to modify ACLs/ACEs. The attack scenario typically targets Windows domain environments where the attacker has initial access and seeks to exploit misconfigured permissions for lateral movement or privilege escalation. Expected outcomes include successful password change and impersonation of the target user.

## Requirements

1. Access to an account with permissions to modify ACLs/ACEs in Active Directory
2. Valid credentials for an account with ForceChangePassword rights on the target user
3. Access to tools like rpcclient or bloodyAD

## Defense

Defensive measures and detection strategies:

- Implement least privilege access for all accounts in Active Directory
- Monitor for changes to ACLs/ACEs in Active Directory
- Implement multi-factor authentication to prevent unauthorized password resets

## Objectives

1. Primary objective of the attack: Escalate privileges within an organization
2. Secondary objective: Gain access to sensitive information within an organization
3. Expected outcome: Successful password reset and authentication as the target user

## Instructions

### Step 1: Prepare and Execute Password Change Using rpcclient

**Context**: This step uses rpcclient from the Samba suite to interact with the Windows domain and force a password change for the target user, assuming the attacker has the necessary permissions.

**Command** ([[Using rpcclient from the Samba software suite]]):
```bash
rpcclient -U 'attacker_user%my_password' -W DOMAIN -c "setuserinfo2 target_user 23 target_newpwd"
```

> The rpcclient command is part of the Samba software suite and can be used to interact with Windows systems that have SMB enabled. This command changes the password of the target user to the specified new password. It requires valid credentials for an account with permission to change the password of the target user.

### Step 2: Alternative Password Change Using bloodyAD with Pass-the-Hash

**Context**: This alternative step uses bloodyAD to change the target user's password via pass-the-hash authentication, providing another method to achieve the same outcome in Active Directory environments.

**Command** ([[Using bloodyAD with pass-the-hash]]):
```bash
bloodyAD.py --host [DC IP] -d DOMAIN -u attacker_user -p :B4B9B02E6F09A9BD760F388B67351E2B changePassword target_user target_newpwd
```

> The bloodyAD tool is a Python script that can be used to interact with Active Directory environments. This command changes the target user's password using pass-the-hash. Both commands require the attacker to have valid credentials for an account with permission to change the password of the target user. The target user's password will be changed to the value provided in the target_newpwd argument.

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

### Sub-Techniques

- [[Sub-Technique Name]]

## Commands Used

- [[Using bloodyAD with pass-the-hash]]
- [[Using rpcclient from the Samba software suite]]

## Tools Used

- [[rpcclient]]
- [[bloodyAD]]

## Tags

- [[Abusing Active Directory ACLs/ACEs]]
- [[Active Directory Attacks]]
- [[ForceChangePassword]]