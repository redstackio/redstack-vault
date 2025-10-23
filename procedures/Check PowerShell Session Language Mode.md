---
id: 6acfefb7-490d-48e6-99ed-fd746459410b
name: Check PowerShell Session Language Mode
type: procedure
verified: true
submitted: true
created_at: '2020-03-30T18:49:29.648478+00:00'
updated_at: '2023-05-25T19:53:23.044009+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Security Software Discovery|T1063 - Security Software Discovery]]'
platforms:
- Windows
tags:
- '[[Enumeration]]'
commands:
- '[[PowerShell Show Current Language Mode]]'
---

# Check PowerShell Session Language Mode

**Status**: ✓ Verified

## Summary

Constrained Language Mode (CLM) restricts many PowerShell elements in order to minimize the potential attack surface, while still supporting common day-to-day administration tasks. While it's not a foolproof solution to stop attacks (multiple bypasses exist), CLM can hinder attackers enough that th

## Description

# Description

Constrained Language Mode (CLM) restricts many PowerShell elements in order to minimize the potential attack surface, while still supporting common day-to-day administration tasks. While it's not a foolproof solution to stop attacks (multiple bypasses exist), CLM can hinder attackers enough that they opt to find different approaches to attacking a system.



# Instructions





**Command** ([[PowerShell Show Current Language Mode]]):

```bash
$ExecutionContext.SessionState.LanguageMode
```







## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Security Software Discovery|T1063 - Security Software Discovery]]

## Commands Used

- [[PowerShell Show Current Language Mode]]

## Tags

- [[Enumeration]]


