---
id: 55f94a72-7c86-49b3-afb7-e1a667062a6b
name: VBA Spawning via svchost.exe using Scheduled Task - Kaspersky AV Update Task
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.524383+00:00'
updated_at: '2023-04-10T20:36:51.537211+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Scheduled Task|T1053 - Scheduled Task]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[DOCM - VBA Spawning via svchost.exe using Scheduled Task]]'
- '[[Office - Attacks]]'
---

# VBA Spawning via svchost.exe using Scheduled Task - Kaspersky AV Update Task

## Summary

This procedure involves using a malicious macro-enabled Microsoft Word document (DOCM) to spawn a Visual Basic for Applications (VBA) script via svchost.exe using a scheduled task. This technique can be used to evade detection and execute arbitrary code on the target system. The VBA script can be u

## Description

# Description

This procedure involves using a malicious macro-enabled Microsoft Word document (DOCM) to spawn a Visual Basic for Applications (VBA) script via svchost.exe using a scheduled task. This technique can be used to evade detection and execute arbitrary code on the target system. The VBA script can be used to download and execute additional payloads, steal sensitive information, or establish persistence on the system.

Technical Explanation: The malicious macro in the DOCM file creates a scheduled task that spawns a VBA script via svchost.exe. The VBA script can then execute commands on the target system, such as downloading and executing additional payloads or stealing sensitive information. By using svchost.exe, the attacker can blend in with legitimate system processes and evade detection.

Business Value: This procedure can be used by attackers to gain access to sensitive information, establish persistence on the target system, or execute additional attacks on the target organization.

 

## Requirements

1. Access to a malicious macro-enabled Microsoft Word document (DOCM)

 

## Defense

1. Regularly update and patch Microsoft Office and other software to prevent exploitation of known vulnerabilities

1. Use anti-malware software to detect and remove malicious macros and other malware

1. Monitor for suspicious scheduled tasks and anomalous network traffic

 

## Objectives

1. Gain access to sensitive information

1. Establish persistence on the target system

1. Execute additional attacks on the target organization

 

# Instructions

1. Create a scheduled task to update Kaspersky Anti-Virus definitions

 



**Code**: [[Sub AutoOpen()
    Set service = CreateObject("Sch]]



> This command creates a scheduled task that will update Kaspersky Anti-Virus definitions. The task is set to start when available, and is not hidden. It uses a time trigger to start 30 seconds from the current time, and runs the specified PowerShell command to download and execute a script to update the definitions. The task is registered with the name 'AVUpdateTask'.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Scheduled Task|T1053 - Scheduled Task]]
- [[Scripting|T1064 - Scripting]]

## Tags

- [[DOCM - VBA Spawning via svchost.exe using Scheduled Task]]
- [[Office - Attacks]]


