---
id: 924f8d76-db72-4b6e-8b11-65c701d32b9c
name: Spawn an Interactive Shell with WinRM (Windows)
type: procedure
verified: true
submitted: true
created_at: '2020-03-21T01:59:57.868009+00:00'
updated_at: '2023-05-25T19:53:46.374157+00:00'
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
- '[[Create a PSSession and Enter It]]'
- '[[Create a Windows PSCredential Object]]'
---

# Spawn an Interactive Shell with WinRM (Windows)

**Status**: ✓ Verified

## Summary

Spawn a PowerShell interactive session on a remote system using the WinRM service. 

## Description

# Description

Spawn a PowerShell interactive session on a remote system using the WinRM service.

# Instructions

1. Create a PSCredential object

**Command** ([[$Pass = ConvertTo-SecureString -String "$_PASSWORD]]):

```bash
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "$_USER", $Pass
```

Note: if creating domain credentials, specify the user as: "$_DOMAIN\$_USER"

2. Create and enter a session using the PSCrednetial object

**Command** ([[Create a PSSession and Enter It]]):

```bash
$Session = New-PSSession -Credential $Cred -ComputerName $_TARGET_IP
Enter-PSSession $Session
```

3. (Optional) Clean up after exiting the session

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
- [[Create a PSSession and Enter It]]
- [[Create a Windows PSCredential Object]]

## Tags

- [[Network]]
- [[powershell]]
- [[shell]]
