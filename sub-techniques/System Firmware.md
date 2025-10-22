---
id: bf45fcf6-2f9d-42dc-b88a-5da3ef500f01
name: System Firmware
type: sub-technique
mitre_id: T1542.001
mitre_url: null
created_at: '2023-04-06T00:31:25.605097+00:00'
updated_at: '2023-04-06T00:31:25.605097+00:00'
parent_technique: '[[Pre-OS Boot|T1542 - Pre-OS Boot]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
---

# System Firmware

**MITRE ID**: T1542.001

**Parent Technique**: [[Pre-OS Boot|T1542 - Pre-OS Boot]]

This is a sub-technique of T1542 - Pre-OS Boot.

## Summary

Adversaries may modify system firmware to persist on systems.The BIOS (Basic Input/Output System) and The Unified Extensible Firmware Interface (UEFI) or Extensible Firmware Interface (EFI) are examples of system firmware that operate as the software interface between the operating system and hardwa

## Description

Adversaries may modify system firmware to persist on systems.The BIOS (Basic Input/Output System) and The Unified Extensible Firmware Interface (UEFI) or Extensible Firmware Interface (EFI) are examples of system firmware that operate as the software interface between the operating system and hardware of a computer. (Citation: Wikipedia BIOS) (Citation: Wikipedia UEFI) (Citation: About UEFI)

System firmware like BIOS and (U)EFI underly the functionality of a computer and may be modified by an adversary to perform or assist in malicious activity. Capabilities exist to overwrite the system firmware, which may give sophisticated adversaries a means to install malicious firmware updates as a means of persistence on a system that may be difficult to detect.

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
