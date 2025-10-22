---
id: 997a88fa-6787-4f37-9185-6e2c6047683c
name: Timestomp
type: sub-technique
mitre_id: T1070.006
mitre_url: null
created_at: '2023-04-06T00:31:26.042357+00:00'
updated_at: '2023-04-06T00:31:26.042357+00:00'
parent_technique: '[[Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Timestomp

**MITRE ID**: T1070.006

**Parent Technique**: [[Indicator Removal on Host|T1070 - Indicator Removal on Host]]

This is a sub-technique of T1070 - Indicator Removal on Host.

## Summary

Adversaries may modify file time attributes to hide new or changes to existing files. Timestomping is a technique that modifies the timestamps of a file (the modify, access, create, and change times), often to mimic files that are in the same folder. This is done, for example, on files that have bee

## Description

Adversaries may modify file time attributes to hide new or changes to existing files. Timestomping is a technique that modifies the timestamps of a file (the modify, access, create, and change times), often to mimic files that are in the same folder. This is done, for example, on files that have been modified or created by the adversary so that they do not appear conspicuous to forensic investigators or file analysis tools.

Timestomping may be used along with file name [Masquerading](https://attack.mitre.org/techniques/T1036) to hide malware and tools.(Citation: WindowsIR Anti-Forensic Techniques)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
