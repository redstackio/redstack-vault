---
id: ba124c79-4184-456f-b86e-a9c23323e8e5
name: Patching AmsiScanBuffer to Bypass AMSI Scanning
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.896222+00:00'
updated_at: '2023-04-10T20:36:15.092480+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Hooking|T1179 - Hooking]]'
- '[[Modify Registry|T1112 - Modify Registry]]'
tags:
- '[[Patching amsi.dll AmsiScanBuffer by rasta-mouse]]'
---

# Patching AmsiScanBuffer to Bypass AMSI Scanning

## Summary

Patching AmsiScanBuffer is a technique used to bypass the Antimalware Scan Interface (AMSI) scanning. This technique involves modifying the amsi.dll file to prevent the scanning of specific code. This technique can be used by attackers to bypass antivirus and other security solutions that rely on A

## Description

# Description

Patching AmsiScanBuffer is a technique used to bypass the Antimalware Scan Interface (AMSI) scanning. This technique involves modifying the amsi.dll file to prevent the scanning of specific code. This technique can be used by attackers to bypass antivirus and other security solutions that rely on AMSI to detect malicious code. Technical details on how to patch the AmsiScanBuffer can be found in the original article by rasta-mouse.

From a business standpoint, bypassing AMSI scanning can allow attackers to execute malicious code on a target system without being detected by traditional security solutions. This can lead to data theft, system compromise, and other negative impacts on the targeted organization.

The objectives of this procedure are to modify the amsi.dll file to bypass AMSI scanning and execute malicious code on the target system.

## Requirements

1. Access to the target system

1. Privileges to modify system files

## Defense

1. Ensure that the amsi.dll file is up-to-date and not vulnerable to known exploits.

1. Implement application whitelisting to prevent unauthorized modifications to system files.

1. Monitor system logs for any suspicious modifications to system files.

## Objectives

1. Bypass AMSI scanning on the target system

1. Execute malicious code on the target system

# Instructions

1. This script patches the AMSI Scan Buffer to bypass AMSI scanning. It uses the Win32 API to load the amsi.dll library and retrieve the address of the AmsiScanBuffer function. Then, it overwrites the first 6 bytes of the function with a jump instruction that skips over the AMSI scan.

**Code**: [[$Win32 = @"

using System;
using System.Runtime.In]]

> The script first loads the 'am' + 'si.dll' library using the Win32 API's LoadLibrary function. Then, it retrieves the address of the AmsiScanBuffer function using the GetProcAddress function. The function's memory protection is then changed to allow writing using the VirtualProtect function. The first 6 bytes of the function are then overwritten with a jump instruction that skips over the AMSI scan. This allows malicious code to bypass AMSI scanning and execute without detection.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Hooking|T1179 - Hooking]]
- [[Modify Registry|T1112 - Modify Registry]]

## Tags

- [[Patching amsi.dll AmsiScanBuffer by rasta-mouse]]
