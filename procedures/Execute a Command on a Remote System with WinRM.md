---
id: 7eb51561-76d8-4ef5-9874-b3f9548be45e
name: Execute a Command on a Remote System with WinRM
type: procedure
verified: false
submitted: false
created_at: '2020-03-21T02:22:47.189795+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Windows Remote Management|T1028 - Windows Remote Management]]'
platforms:
- Windows
tags:
- '[[Network]]'
- '[[powershell]]'
- '[[shell]]'
commands:
- '[[$Pass = ConvertTo-SecureString -String "$_PASSWORD]]'
- '[[Clean up After a PSSession]]'
- '[[Create a PSSession and Execute a Command]]'
- '[[Create a Windows PSCredential Object]]'
---

# Execute a Command on a Remote System with WinRM

## Summary

Create a PSSession on a remote system using WinRM, and execute a command. 

## Description

# Description

Create a PSSession on a remote system using WinRM, and execute a command.

# Instructions

1. Create a PSCredential object

**Command** ([[$Pass = ConvertTo-SecureString -String "$_PASSWORD]]):

```bash
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "$_USER", $Pass
```

2. Create a session and execute a command

**Command** ([[Create a PSSession and Execute a Command]]):

```bash
$Session = New-PSSession -ComputerName $_TARGET_IP -Credential $Cred
Invoke-Command -Session $Session -ScriptBlock {Start-Process $_CMD}
```

Note: Since "Start-Process" runs the command in the background, it won't show the result of the command. Omit "Start-Process" to see the output.

3. (Optional) Clean up after the session

**Command** ([[Clean up After a PSSession]]):

```bash
Remove-PSSession $Session
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Windows Remote Management|T1028 - Windows Remote Management]]

## Commands Used

- [[$Pass = ConvertTo-SecureString -String "$_PASSWORD]]
- [[Clean up After a PSSession]]
- [[Create a PSSession and Execute a Command]]
- [[Create a Windows PSCredential Object]]

## Tags

- [[Network]]
- [[powershell]]
- [[shell]]
