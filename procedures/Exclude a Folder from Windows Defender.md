---
id: b338f5ff-f18a-4747-99a8-c29a02309b77
name: Exclude a Folder from Windows Defender
type: procedure
verified: true
submitted: true
created_at: '2020-03-04T18:38:21.982510+00:00'
updated_at: '2023-05-25T19:54:56.410181+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Disabling Security Tools|T1089 - Disabling Security Tools]]'
platforms:
- Windows
tags:
- '[[administrator]]'
- '[[defender]]'
- '[[Defense Bypass]]'
commands:
- '[[Exclude a Folder from Windows Defender (PowerShell 4+)]]'
---

# Exclude a Folder from Windows Defender

**Status**: ✓ Verified

## Summary

Exclude a folder from Windows Defender's scans using PowerShell 4+. This command requires Administrator privileges and will only exclude the path from Defender's static analysis. 

## Description

# Description

Exclude a folder from Windows Defender's scans using PowerShell 4+. This command requires Administrator privileges and will only exclude the path from Defender's static analysis.

# Instructions

**Command** ([[Exclude a Folder from Windows Defender (PowerShell 4+)]]):

```bash
Add-MpPreference -ExclusionPath "$_PATH"
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Disabling Security Tools|T1089 - Disabling Security Tools]]

## Commands Used

- [[Exclude a Folder from Windows Defender (PowerShell 4+)]]

## Tags

- [[administrator]]
- [[defender]]
- [[Defense Bypass]]
