---
id: bdddb937-ee03-4c54-b874-baa6592fb19c
name: Mount a Windows SMB Share with PowerShell (Authenticated)
type: procedure
verified: false
submitted: false
created_at: '2020-03-27T22:02:36.049583+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
platforms:
- Windows
tags:
- '[[file transfer]]'
- '[[Network]]'
commands:
- '[[$Pass = ConvertTo-SecureString -String "$_PASSWORD]]'
- '[[Create a Windows PSCredential Object]]'
- '[[Mount a Windows SMB Share (PowerShell)]]'
---

# Mount a Windows SMB Share with PowerShell (Authenticated)

## Summary

Use PowerShell to mount a remote share with credentials on a local Windows machine. 

## Description

# Description

Use PowerShell to mount a remote share with credentials on a local Windows machine.

# Instructions

1. Create a credentials object using the username and password assigned to the share

**Command** ([[$Pass = ConvertTo-SecureString -String "$_PASSWORD]]):

```bash
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "$_USER", $Pass
```

2. Mount the shared folder

**Command** ([[Mount a Windows SMB Share (PowerShell)]]):

```bash
New-PSDrive -Name "$_NAME" -PSProvider FileSystem -Credential $Cred -Root \\$_TARGET_IP\$_SHARE
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]

## Commands Used

- [[$Pass = ConvertTo-SecureString -String "$_PASSWORD]]
- [[Create a Windows PSCredential Object]]
- [[Mount a Windows SMB Share (PowerShell)]]

## Tags

- [[file transfer]]
- [[Network]]
