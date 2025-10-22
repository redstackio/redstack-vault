---
id: e26a9998-ab7c-4ee7-95d8-d33a5089ca58
name: Windows 10+ Binary Replacement via HID.dll
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.157377+00:00'
updated_at: '2023-04-10T20:37:23.226956+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
- '[[Windows Management Instrumentation Event Subscription|T1084 - Windows Management
  Instrumentation Event Subscription]]'
sub_techniques:
- '[[Software Packing|T1027.002 - Software Packing]]'
tags:
- '[[Binary Replacement]]'
- '[[Binary Replacement on Windows 10+]]'
- '[[Elevated]]'
- '[[Windows - Persistence]]'
---

# Windows 10+ Binary Replacement via HID.dll

## Summary

Windows 10+ Binary Replacement via HID.dll is a technique used by attackers to replace legitimate system binaries with malicious ones. This technique involves the use of the HID.dll file to bypass security measures and elevate privileges. The HID.dll file is a legitimate Microsoft library that is u

## Description

# Description

Windows 10+ Binary Replacement via HID.dll is a technique used by attackers to replace legitimate system binaries with malicious ones. This technique involves the use of the HID.dll file to bypass security measures and elevate privileges. The HID.dll file is a legitimate Microsoft library that is used to interact with Human Interface Devices (HIDs). By using this file, attackers can replace system binaries without triggering security alerts or setting off antivirus software.

To execute this attack, the attacker needs to have access to the target system and know the location of the binary they want to replace. Once they have this information, they can use the HID.dll file to replace the binary with a malicious one. This technique is effective because it allows attackers to bypass security measures and elevate privileges without being detected.

The business value of this technique is that it allows attackers to gain persistent access to the target system, which can be used for further attacks or data exfiltration.

## Requirements

1. Access to the target system

1. Knowledge of the location of the binary to be replaced

1. HID.dll file

## Defense

1. Monitor for changes to system binaries and verify their integrity

1. Implement application whitelisting to prevent unauthorized binaries from executing

1. Use antivirus software to detect and remove malicious binaries

## Objectives

1. Replace legitimate system binaries with malicious ones

1. Elevate privileges

1. Gain persistent access to the target system

# Instructions

1. To locate the HID.dll file, follow these steps:

**Code**: [[C:\Program Files\Common Files\microsoft shared\ink]]

> 1. Open File Explorer
2. Navigate to the 'C:\Program Files\Common Files\microsoft shared\ink' directory
3. Look for the HID.dll file in this directory

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[Windows Management Instrumentation Event Subscription|T1084 - Windows Management Instrumentation Event Subscription]]

### Sub-Techniques

- [[Software Packing|T1027.002 - Software Packing]]

## Tags

- [[Binary Replacement]]
- [[Binary Replacement on Windows 10+]]
- [[Elevated]]
- [[Windows - Persistence]]
