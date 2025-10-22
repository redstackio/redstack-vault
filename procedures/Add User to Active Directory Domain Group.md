---
id: bccbfd67-4fd2-4536-9418-ad65959bf3c4
name: Add User to Active Directory Domain Group
type: procedure
verified: false
submitted: false
created_at: '2020-03-16T01:01:25.873472+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Account Manipulation|T1098 - Account Manipulation]]'
platforms:
- Windows
tags:
- '[[Active Directory]]'
- '[[privileges]]'
commands:
- '[[Create a Windows PSCredential Object]]'
- '[[PowerView Add Active Directory Group Privileges]]'
---

# Add User to Active Directory Domain Group

## Summary

Use PowerView's "Add-DomainGroupMember" cmdlet to add a user  to a domain group, assuming the current user has sufficient domain privileges (eg: GenericAll). 

## Description

# Description

Use PowerView's "Add-DomainGroupMember" cmdlet to add a user  to a domain group, assuming the current user has sufficient domain privileges (eg: GenericAll). 

## Objectives

Account manipulation is a critical step in the lateral movement process, as it allows the attacker to move from one system to another by compromising the credentials of legitimate users. This technique can be used to escalate privileges, gain access to sensitive data, and further compromise the target network.

1. Use PowerView to add AD group privileges to a user

# Instructions

1. Download PowerView (dev branch), and import it on the target machine: [Download from GitHub](https://github.com/PowerShellMafia/PowerSploit/blob/dev/Recon/PowerView.ps1)

2. (Optional) It may be necessary to create a PS Credentials object of the user who is authorized to modify group membership.

**Command** ([[Create a Windows PSCredential Object]]):

```bash
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "$_DOMAIN\$_USER", $Pass
```

3. Execute the cmdlet

**Command** ([[PowerView Add Active Directory Group Privileges]]):

```bash
Add-DomainGroupMember -Identity '$_GROUP' -Members '$_USER'
```

Note: The "Credential" argument may not be necessary if the current session is already running as that user.

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Account Manipulation|T1098 - Account Manipulation]]

## Commands Used

- [[Create a Windows PSCredential Object]]
- [[PowerView Add Active Directory Group Privileges]]

## Tags

- [[Active Directory]]
- [[privileges]]
