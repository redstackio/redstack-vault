---
id: 302b309e-099c-49f9-ac62-2edcb52dd411
name: VBA-AMSI Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.873981+00:00'
updated_at: '2023-04-10T20:36:59.460524+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
- '[[Scripting|T1064 - Scripting]]'
- '[[Software Packing|T1045 - Software Packing]]'
tags:
- '[[Office - Attacks]]'
- '[[VBA - AMSI]]'
---

# VBA-AMSI Bypass

## Summary

The VBA-AMSI Bypass procedure is an offensive technique used to bypass the Antimalware Scan Interface (AMSI) in Microsoft Office VBA macros. This technique is commonly used by attackers to evade detection by security software and execute malicious code. The technique involves obfuscating the VBA co

## Description

# Description

The VBA-AMSI Bypass procedure is an offensive technique used to bypass the Antimalware Scan Interface (AMSI) in Microsoft Office VBA macros. This technique is commonly used by attackers to evade detection by security software and execute malicious code. The technique involves obfuscating the VBA code to make it difficult for the AMSI to detect malicious behavior. This procedure is highly effective as AMSI is a built-in defense mechanism in Office applications that scans VBA macros for malicious code before execution. By bypassing AMSI, attackers can execute malicious code without detection.

## Requirements

1. Access to Microsoft Office VBA macros

1. Knowledge of obfuscation techniques

1. Access to AMSI-enabled Office applications

## Defense

1. Regularly update and patch Microsoft Office applications

1. Use endpoint protection software that can detect and prevent VBA-AMSI bypass techniques

1. Implement strict email and web filtering policies to prevent phishing attacks that deliver malicious VBA macros

## Objectives

1. Bypass AMSI scan and execute malicious code in VBA macros

1. Evade detection by security software

# Instructions

1. This VB script bypasses the AMSI (Antimalware Scan Interface) scan by patching the memory of the AmsiScanBuffer function. It loads the amsi.dll library, gets the address of the AmsiScanBuffer function, changes the memory protection of the AmsiScanBuffer function to allow writing, and then copies the shellcode to the AmsiScanBuffer function.

**Code**: [[Private Declare PtrSafe Function GetProcAddress Li]]

> The AMSI is a Windows feature that allows antivirus solutions to integrate with other applications and scan for malicious code. By bypassing the AMSI scan, attackers can execute malicious code without being detected by antivirus solutions. This VB script uses a technique called DLL injection to load the amsi.dll library and patch the memory of the AmsiScanBuffer function. The AmsiScanBuffer function is responsible for scanning a buffer for malicious code. By patching the memory of this function, the script is able to bypass the AMSI scan and execute malicious code without being detected.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[Scripting|T1064 - Scripting]]
- [[Software Packing|T1045 - Software Packing]]

## Tags

- [[Office - Attacks]]
- [[VBA - AMSI]]
