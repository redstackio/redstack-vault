---
id: b84bfb59-e714-40b3-95be-94fc3be1eb3f
name: Reflection Method with WMF5 Autologging Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.021896+00:00'
updated_at: '2023-04-10T20:36:16.560067+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Bypass User Account Control|T1088 - Bypass User Account Control]]'
- '[[Security Software Discovery|T1063 - Security Software Discovery]]'
tags:
- '[[Using Matt Graebers Reflection method with WMF5 autologging bypass]]'
---

# Reflection Method with WMF5 Autologging Bypass

## Summary

The Reflection method with WMF5 autologging bypass is a technique used to bypass security software and evade detection. This technique involves disabling AMSI, which is a Windows feature that is used by antivirus and other security software to scan PowerShell scripts for malicious code. By disablin

## Description

# Description

The Reflection method with WMF5 autologging bypass is a technique used to bypass security software and evade detection. This technique involves disabling AMSI, which is a Windows feature that is used by antivirus and other security software to scan PowerShell scripts for malicious code. By disabling AMSI, attackers can execute malicious PowerShell scripts without detection. The technique also leverages the WMF5 autologging bypass, which allows attackers to bypass User Account Control (UAC) and execute PowerShell scripts with elevated privileges. This technique is commonly used by attackers to gain access to sensitive information or to install malware on a target system.

 

## Requirements

1. Access to a system with Windows Management Framework 5 (WMF5) installed

1. Authentication credentials with administrative privileges

1. PowerShell or other scripting tools

 

## Defense

1. Implement strict access controls to limit administrative privileges

1. Monitor for suspicious activity, such as the disabling of AMSI

1. Use endpoint detection and response (EDR) tools to detect and respond to malicious activity

 

## Objectives

1. Gain access to sensitive information

1. Install malware on a target system

 

# Instructions

1. Disable AMSI

 



**Code**: [[[Delegate]::CreateDelegate(("Func``3[String, $(([S]]



> This command disables the Antimalware Scan Interface (AMSI) which is a feature of Windows Defender that helps in detecting and preventing malicious scripts from running on the system. By disabling the AMSI, it is possible to bypass the detection mechanism and execute malicious scripts without being detected.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Bypass User Account Control|T1088 - Bypass User Account Control]]
- [[Security Software Discovery|T1063 - Security Software Discovery]]

## Tags

- [[Using Matt Graebers Reflection method with WMF5 autologging bypass]]


