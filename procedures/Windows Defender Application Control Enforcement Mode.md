---
id: cb11029e-6f92-467f-a9dc-f6ec0873aa05
name: Windows Defender Application Control Enforcement Mode
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.692335+00:00'
updated_at: '2023-04-10T20:37:06.317434+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[User Execution|T1204 - User Execution]]'
sub_techniques:
- '[[Malicious File|T1204.002 - Malicious File]]'
tags:
- '[[Windows Defender Application Control]]'
- '[[Windows - Defenses]]'
commands:
- '[[Get-ComputerInfo]]'
---

# Windows Defender Application Control Enforcement Mode

## Summary

Windows Defender Application Control (WDAC) is a security feature in Windows that helps prevent unauthorized applications from running. The enforcement mode determines how strict the application control policies are enforced. This procedure provides instructions on how to check the current WDAC enf

## Description

# Description

Windows Defender Application Control (WDAC) is a security feature in Windows that helps prevent unauthorized applications from running. The enforcement mode determines how strict the application control policies are enforced. This procedure provides instructions on how to check the current WDAC enforcement mode. 

From an offensive perspective, an attacker may attempt to bypass WDAC by finding ways to execute unauthorized applications. Understanding the current enforcement mode can help an attacker determine the level of effort required to bypass WDAC. From a defensive perspective, understanding the current enforcement mode can help an organization determine if they need to adjust their policies to better protect against unauthorized applications.

Technical Explanation: The enforcement mode determines how strictly the application control policies are enforced. There are three possible enforcement modes: Audit Mode, Enforce Mode, and Disabled. In Audit Mode, events are logged but no enforcement takes place. In Enforce Mode, only applications that are explicitly allowed by the policy are allowed to run. In Disabled mode, no application control policies are enforced.

 

## Requirements

1. Access to a Windows machine with WDAC enabled

 

## Defense

1. Ensure that WDAC is configured with appropriate policies to prevent unauthorized applications from running

1. Implement additional security measures such as application whitelisting or endpoint detection and response solutions to provide additional layers of protection

1. Regularly review and update WDAC policies to ensure they are up-to-date and effective

 

## Objectives

1. Determine the current WDAC enforcement mode

1. Assess the level of protection provided by WDAC

 

# Instructions

1. To get the current enforcement mode of Windows Defender Application Control (WDAC), run the following command in PowerShell:

Get-ComputerInfo

 



**Code**: [[$ Get-ComputerInfo
DeviceGuardCodeIntegrityPolicyE]]



> This command retrieves the current enforcement mode of WDAC. The DeviceGuardCodeIntegrityPolicyEnforcementStatus and DeviceGuardUserModeCodeIntegrityPolicyEnforcementStatus values indicate whether WDAC is currently enforcing code integrity policies in kernel mode and user mode, respectively. The value 'EnforcementMode' indicates that WDAC is currently enforcing code integrity policies, while 'AuditMode' indicates that it is only logging violations. This information can be useful for troubleshooting issues related to WDAC enforcement.



**Command** ([[Get-ComputerInfo]]):

```bash
$ Get-ComputerInfo
DeviceGuardCodeIntegrityPolicyEnforcementStatus         : EnforcementMode
DeviceGuardUserModeCodeIntegrityPolicyEnforcementStatus : EnforcementMode
```



## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[User Execution|T1204 - User Execution]]

### Sub-Techniques

- [[Malicious File|T1204.002 - Malicious File]]

## Commands Used

- [[Get-ComputerInfo]]

## Tags

- [[Windows Defender Application Control]]
- [[Windows - Defenses]]


