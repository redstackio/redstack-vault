---
id: bef04dd5-50dc-4b20-b39b-b325e1ca9341
name: Create a Windows SMB Share with PowerShell
type: procedure
verified: false
submitted: false
created_at: '2020-03-27T22:21:14.939690+00:00'
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
- '[[Create a Windows SMB Share (PowerShell)]]'
---

# Create a Windows SMB Share with PowerShell

## Summary

This text briefly explains the purpose of the procedure and key take-aways. It will typically range from one sentence to multiple paragraphs, and may include H2 subheadings. 

## Description

# Description

This text briefly explains the purpose of the procedure and key take-aways. It will typically range from one sentence to multiple paragraphs, and may include H2 subheadings.

# Instructions

1. Identify (or create) a folder to share
2. Configure the shared folder, specifying a user who will have full access

**Command** ([[Create a Windows SMB Share (PowerShell)]]):

```bash
New-SmbShare -Name "$_NAME" -Path "$_FULL/PATH/TO/SHARE" -FullAccess "$_USERNAME"
```

Note: the "Name" field defines the share name used when mounting it.

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]

## Commands Used

- [[Create a Windows SMB Share (PowerShell)]]

## Tags

- [[file transfer]]
- [[Network]]
