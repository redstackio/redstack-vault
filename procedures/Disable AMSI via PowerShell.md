---
id: 4e03d037-00e4-464b-9177-af711139ae28
name: Disable AMSI via PowerShell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.410983+00:00'
updated_at: '2023-04-10T20:37:02.880458+00:00'
tags:
- '[[Anti Malware Scan Interface]]'
- '[[Powershell]]'
- '[[Windows - Defenses]]'
---

# Disable AMSI via PowerShell

## Summary

Disabling Anti Malware Scan Interface (AMSI) via PowerShell is a technique used to bypass security controls and evade detection. AMSI is a Windows feature that allows applications and services to integrate with installed anti-virus software, and disabling it can allow malicious scripts to run undet

## Description

# Description

Disabling Anti Malware Scan Interface (AMSI) via PowerShell is a technique used to bypass security controls and evade detection. AMSI is a Windows feature that allows applications and services to integrate with installed anti-virus software, and disabling it can allow malicious scripts to run undetected. This technique is commonly used by attackers to deliver and execute malware payloads. From a technical standpoint, disabling AMSI involves modifying the Windows Registry to disable the AMSI provider. From a business perspective, this technique can be used to bypass security controls and deliver malware payloads, which can result in data theft, financial loss, and reputational damage.

 

## Requirements

1. Access to a Windows system with PowerShell

1. Sufficient privileges to modify the Windows Registry

 

## Defense

1. Enable and properly configure anti-virus software to detect and prevent malicious scripts

1. Implement application whitelisting to prevent unauthorized scripts from running

1. Regularly monitor and analyze system logs for suspicious activity

 

## Objectives

1. Disable AMSI to bypass security controls and evade detection

1. Deliver and execute malware payloads undetected

 

# Instructions

1. This command disables AMSI (Antimalware Scan Interface) which is a feature in PowerShell that helps in detecting malicious scripts. The command uses reflection to access a non-public static field in the System.Management.Automation.AmsiUtils class and sets its value to true, thereby disabling AMSI.

 



**Code**: [[PS C:\> [Ref].Assembly.GetType('System.Management.]]



> This command takes no arguments.

## Tags

- [[Anti Malware Scan Interface]]
- [[Powershell]]
- [[Windows - Defenses]]


