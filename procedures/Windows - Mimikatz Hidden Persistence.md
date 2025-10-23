---
id: c11f68b5-4104-4f63-9b5e-80455c17103b
name: Windows - Mimikatz Hidden Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.609420+00:00'
updated_at: '2023-04-10T20:37:30.062948+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Hide Artifacts|T1564 - Hide Artifacts]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
sub_techniques:
- '[[Hidden Files and Directories|T1564.001 - Hidden Files and Directories]]'
tags:
- '[[Hide Your Binary]]'
- '[[Windows - Persistence]]'
commands:
- '[[Set Hidden Attribute on Mimikatz]]'
---

# Windows - Mimikatz Hidden Persistence

## Summary

The Mimikatz Hidden Persistence technique allows an attacker to maintain access to a compromised Windows system by hiding the Mimikatz binary from detection. Mimikatz is a powerful tool that can be used to extract credentials from memory, and is often used by attackers to escalate privileges or mov

## Description

# Description

The Mimikatz Hidden Persistence technique allows an attacker to maintain access to a compromised Windows system by hiding the Mimikatz binary from detection. Mimikatz is a powerful tool that can be used to extract credentials from memory, and is often used by attackers to escalate privileges or move laterally within a network. By hiding the Mimikatz binary, an attacker can evade detection and continue to extract credentials without being detected.

To achieve this technique, the attacker must first obtain administrative privileges on the target system. Once this is done, the attacker can use the 'Hide Mimikatz Executable' command to create a hidden copy of the Mimikatz binary on the system. The attacker can then use this hidden binary to extract credentials without being detected.

This technique can be used by attackers to maintain persistence on a compromised system, and to continue to extract credentials and move laterally within a network.

 

## Requirements

1. Administrative privileges on the target system

1. Mimikatz binary

 

## Defense

1. Implement strong access controls to limit the ability of attackers to obtain administrative privileges

1. Use endpoint detection and response (EDR) solutions to detect and respond to attempts to hide binaries or extract credentials from memory

1. Regularly review system logs to detect suspicious activity

 

## Objectives

1. Maintain access to a compromised Windows system

1. Extract credentials from memory

1. Evade detection by hiding the Mimikatz binary

 

# Instructions

1. Use the 'attrib' command to set the hidden attribute on the 'mimikatz.exe' file.

 



**Code**: [[PS> attrib +h mimikatz.exe]]



> This command will hide the 'mimikatz.exe' file from being visible in the file explorer or command prompt, making it harder for an attacker to detect or remove the file.



**Command** ([[Set Hidden Attribute on Mimikatz]]):

```bash
attrib +h mimikatz.exe
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Hide Artifacts|T1564 - Hide Artifacts]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

### Sub-Techniques

- [[Hidden Files and Directories|T1564.001 - Hidden Files and Directories]]

## Commands Used

- [[Set Hidden Attribute on Mimikatz]]

## Tags

- [[Hide Your Binary]]
- [[Windows - Persistence]]


