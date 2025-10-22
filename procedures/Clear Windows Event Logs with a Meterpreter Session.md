---
id: eca72344-c803-4a09-98e8-31ef20343991
name: Clear Windows Event Logs with a Meterpreter Session
type: procedure
verified: true
submitted: true
created_at: '2019-12-18T18:42:07.362540+00:00'
updated_at: '2023-05-25T19:59:14.495209+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
platforms:
- Windows
tags:
- '[[audit]]'
commands:
- '[[Metasploit Clear Event Logs]]'
---

# Clear Windows Event Logs with a Meterpreter Session

**Status**: ✓ Verified

## Summary

After owning a system, it may be necessary to clear log files to hide the presence and actions of the attack. While clearing common log files can help conceal the attack, it should be noted that many systems are monitored specifically for instances where log files are cleared, and may stand out in 

## Description

# Description

After owning a system, it may be necessary to clear log files to hide the presence and actions of the attack. While clearing common log files can help conceal the attack, it should be noted that many systems are monitored specifically for instances where log files are cleared, and may stand out in SIEM/IPS logs.

# Instructions

From a Meterpreter session, execute the clearev command

**Command** ([[Metasploit Clear Event Logs]]):

```bash
clearev
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Indicator Removal on Host|T1070 - Indicator Removal on Host]]

## Commands Used

- [[Metasploit Clear Event Logs]]

## Tags

- [[audit]]
