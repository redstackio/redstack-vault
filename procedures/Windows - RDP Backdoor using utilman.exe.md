---
id: bd1889e4-e167-406e-81f5-aceaa5b98a82
name: Windows - RDP Backdoor using utilman.exe
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.182556+00:00'
updated_at: '2023-04-10T20:37:23.607203+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Accessibility Features|T1015 - Accessibility Features]]'
- '[[Remote Desktop Protocol|T1076 - Remote Desktop Protocol]]'
- '[[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]'
tags:
- '[[Elevated]]'
- '[[RDP Backdoor]]'
- '[[utilman.exe]]'
- '[[Windows - Persistence]]'
---

# Windows - RDP Backdoor using utilman.exe

## Summary

This procedure involves adding a debugger for utilman.exe which allows an attacker to open a command prompt as SYSTEM. This can be used to create a backdoor for RDP access, bypassing authentication requirements. By replacing the utilman.exe binary with a malicious one, the attacker can maintain per

## Description

# Description

This procedure involves adding a debugger for utilman.exe which allows an attacker to open a command prompt as SYSTEM. This can be used to create a backdoor for RDP access, bypassing authentication requirements. By replacing the utilman.exe binary with a malicious one, the attacker can maintain persistence and access to the system even after a reboot. This technique can be used for lateral movement and privilege escalation, allowing the attacker to move laterally within the network and escalate privileges to gain access to sensitive data.

 

## Requirements

1. Access to the target system

1. Ability to replace the utilman.exe binary

1. Knowledge of the system's authentication requirements

 

## Defense

1. Disable accessibility features if not needed

1. Monitor for changes to the utilman.exe binary

1. Implement network segmentation to limit lateral movement

 

## Objectives

1. Create a backdoor for RDP access

1. Maintain persistence on the compromised system

1. Move laterally within the network

1. Escalate privileges to gain access to sensitive data

 

# Instructions

1. To open a cmd.exe window as SYSTEM, press Windows Key+U at the login screen.

 



**Code**: [[REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\Curren]]



> This command adds a Debugger value for utilman.exe in the registry. This causes utilman.exe to launch cmd.exe instead of its original functionality. By pressing Windows Key+U at the login screen, you can launch utilman.exe which will now open cmd.exe as SYSTEM. This can be useful for various administrative tasks.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Accessibility Features|T1015 - Accessibility Features]]
- [[Remote Desktop Protocol|T1076 - Remote Desktop Protocol]]
- [[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]

## Tags

- [[Elevated]]
- [[RDP Backdoor]]
- [[utilman.exe]]
- [[Windows - Persistence]]


