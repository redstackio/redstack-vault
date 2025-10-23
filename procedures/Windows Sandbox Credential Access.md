---
id: 669d46ed-abc4-4d9d-8a45-bcee0656d804
name: Windows Sandbox Credential Access
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.700517+00:00'
updated_at: '2023-04-10T20:37:57.104592+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques:
- '[[LSASS Memory|T1003.001 - LSASS Memory]]'
tags:
- '[[Get credentials]]'
- '[[Sandbox Credential]]'
- '[[Windows - Using credentials]]'
---

# Windows Sandbox Credential Access

## Summary

The Windows Sandbox Credential Access procedure involves accessing the Windows Sandbox using the WDAGUtilityAccount credentials. This procedure can be used to obtain sensitive information such as credentials and other data stored within the Windows Sandbox. This technique can be used by an attacker

## Description

# Description

The Windows Sandbox Credential Access procedure involves accessing the Windows Sandbox using the WDAGUtilityAccount credentials. This procedure can be used to obtain sensitive information such as credentials and other data stored within the Windows Sandbox. This technique can be used by an attacker to gain a foothold within the target network, escalate privileges or move laterally within the network.

To execute this procedure, the attacker must have access to the target system and have knowledge of the WDAGUtilityAccount credentials. Once the attacker has obtained access to the Windows Sandbox, they can extract sensitive information and use it to further their attack.

The business value of this procedure is that it can help identify weaknesses in the target network's security posture and allow for remediation of those weaknesses before an attacker can exploit them.

 

## Requirements

1. Access to the target system

1. Knowledge of the WDAGUtilityAccount credentials

 

## Defense

1. Limit access to the target system to authorized personnel only

1. Implement multi-factor authentication to prevent unauthorized access to credentials

1. Monitor for suspicious activity such as unauthorized access to the Windows Sandbox or unusual data extraction

 

## Objectives

1. Gain access to the Windows Sandbox using WDAGUtilityAccount credentials

1. Extract sensitive information such as credentials and other data stored within the Windows Sandbox

 

# Instructions

1. To access Windows Sandbox, use the WDAGUtilityAccount credentials provided above.

 



**Code**: [[\\windowssandbox
Username: wdagutilityaccount
Pass]]



> The WDAGUtilityAccount is a built-in account in Windows 10 that is used to launch Windows Sandbox. It has limited permissions and is isolated from the host system, making it a secure way to test potentially harmful software. To use Windows Sandbox, simply enter the provided credentials when prompted.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

### Sub-Techniques

- [[LSASS Memory|T1003.001 - LSASS Memory]]

## Tags

- [[Get credentials]]
- [[Sandbox Credential]]
- [[Windows - Using credentials]]


