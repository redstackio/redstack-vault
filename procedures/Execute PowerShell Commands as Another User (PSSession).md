---
id: c77c1279-0a41-4626-8e58-ff8b94405f0b
name: Execute PowerShell Commands as Another User (PSSession)
type: procedure
verified: true
submitted: true
created_at: '2020-04-01T05:10:21.541159+00:00'
updated_at: '2023-05-25T19:42:07.523409+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
platforms:
- Windows
tags:
- '[[Active Directory]]'
- '[[authentication]]'
- '[[powershell]]'
- '[[shell]]'
commands:
- '[[Create a PSSession and Execute a Command]]'
- '[[Create a Windows PSCredential Object]]'
---

# Execute PowerShell Commands as Another User (PSSession)

**Status**: ✓ Verified

## Summary

PowerShell can create a "runas" command using simple built-in cmdlets, allowing a user to execute commands as another user without the need to spawn a new shell. This is useful in situations when an attacker has credentials for another account, but PSEXEC and WinRM sessions cannot be established. T

## Description

# Description

PowerShell can create a "runas" command using simple built-in cmdlets, allowing a user to execute commands as another user without the need to spawn a new shell. This is useful in situations when an attacker has credentials for another account, but PSEXEC and WinRM sessions cannot be established. These same concepts can be applied to remote systems  using the WinRM protocol.



# Instructions

Instructions on how to complete the procedure. Typically multiple numbered lists with commands included, and may contain H2 subheadings.



1. Create a PSCredential object





**Command** ([[Create a Windows PSCredential Object]]):

```bash
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "$_DOMAIN\$_USER", $Pass
```



Note: It may be necessary to specify the computer name along with the username, in the format: "$_COMPUTER\$_USER"



2. Create a session and execute a command. Use the local computer's name for the "ComputerName" value, or it's  FQDN if authenticating with a domain. (eg: desktop.megabank.local)





**Command** ([[Create a PSSession and Execute a Command]]):

```bash
$Session = New-PSSession -ComputerName $_TARGET_IP -Credential $Cred
Invoke-Command -Session $Session -ScriptBlock {Start-Process $_CMD}
```







## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]

## Commands Used

- [[Create a PSSession and Execute a Command]]
- [[Create a Windows PSCredential Object]]

## Tags

- [[Active Directory]]
- [[authentication]]
- [[powershell]]
- [[shell]]


