---
id: f909a0ec-3e25-49df-825d-08e93ab55726
name: Software Packing
type: sub-technique
mitre_id: T1027.002
mitre_url: null
created_at: '2023-04-06T00:31:27.049833+00:00'
updated_at: '2023-04-06T00:31:27.049833+00:00'
parent_technique: '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[Windows 10+ Binary Replacement via HID.dll]]'
- '[[XLSM - Hot Manchego VBA Macro Generation]]'
---

# Software Packing

**MITRE ID**: T1027.002

**Parent Technique**: [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

This is a sub-technique of T1027 - Obfuscated Files or Information.

## Summary

Adversaries may perform software packing or virtual machine software protection to conceal their code. Software packing is a method of compressing or encrypting an executable. Packing an executable changes the file signature in an attempt to avoid signature-based detection. Most decompression techni

## Description

Adversaries may perform software packing or virtual machine software protection to conceal their code. Software packing is a method of compressing or encrypting an executable. Packing an executable changes the file signature in an attempt to avoid signature-based detection. Most decompression techniques decompress the executable code in memory. Virtual machine software protection translates an executable's original code into a special format that only a special virtual machine can run. A virtual machine is then called to run this code.(Citation: ESET FinFisher Jan 2018) 

Utilities used to perform software packing are called packers. Example packers are MPRESS and UPX. A more comprehensive list of known packers is available, but adversaries may create their own packing techniques that do not leave the same artifacts as well-known packers to evade defenses.(Citation: Awesome Executable Packing)  

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures

There are 2 procedures using this sub-technique:

- [[Windows 10+ Binary Replacement via HID.dll]]
- [[XLSM - Hot Manchego VBA Macro Generation]]
