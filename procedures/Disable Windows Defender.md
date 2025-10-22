---
id: d1dfaf4f-51f5-4106-9db2-d33de91d75b9
name: Disable Windows Defender
type: procedure
verified: true
submitted: true
created_at: '2020-01-28T21:19:38.446334+00:00'
updated_at: '2023-05-25T19:54:42.620009+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Disabling Security Tools|T1089 - Disabling Security Tools]]'
platforms:
- Windows
tags:
- '[[administrator]]'
- '[[defender]]'
commands:
- '[[Set-MpPreference -DisableRealtimeMonitoring $true]]'
- '[[powershell disable av]]'
- '[[Stop and Disable Windows Defender]]'
---

# Disable Windows Defender

**Status**: ✓ Verified

## Summary

Windows Defender will often block tools used for information gathering after escalating to Administrator privileges, such as Mimikatz. While it is simple to disable Windows Defender with Administrator privileges, please be aware that this action may alert security teams to an intrusion. 

## Description

# Description

Windows Defender will often block tools used for information gathering after escalating to Administrator privileges, such as Mimikatz. While it is simple to disable Windows Defender with Administrator privileges, please be aware that this action may alert security teams to an intrusion.

# Instructions

## Windows 8+

**Command** ([[Set-MpPreference -DisableRealtimeMonitoring $true]]):

```bash
Set-MpPreference -DisableRealtimeMonitoring $true
```

## Windows 7 and earlier

**Command** ([[Stop and Disable Windows Defender]]):

```bash
sc config WinDefend start= disabled
sc stop WinDefend
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Disabling Security Tools|T1089 - Disabling Security Tools]]

## Commands Used

- [[Set-MpPreference -DisableRealtimeMonitoring $true]]
- [[powershell disable av]]
- [[Stop and Disable Windows Defender]]

## Tags

- [[administrator]]
- [[defender]]
