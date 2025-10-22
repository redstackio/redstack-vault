---
id: 5cf956a4-a4fc-4076-bd22-9519f9e0f1dc
name: Component Firmware
type: sub-technique
mitre_id: T1542.002
mitre_url: null
created_at: '2023-04-06T00:31:26.388760+00:00'
updated_at: '2023-04-06T00:31:26.388760+00:00'
parent_technique: '[[Pre-OS Boot|T1542 - Pre-OS Boot]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
---

# Component Firmware

**MITRE ID**: T1542.002

**Parent Technique**: [[Pre-OS Boot|T1542 - Pre-OS Boot]]

This is a sub-technique of T1542 - Pre-OS Boot.

## Summary

Adversaries may modify component firmware to persist on systems. Some adversaries may employ sophisticated means to compromise computer components and install malicious firmware that will execute adversary code outside of the operating system and main system firmware or BIOS. This technique may be s

## Description

Adversaries may modify component firmware to persist on systems. Some adversaries may employ sophisticated means to compromise computer components and install malicious firmware that will execute adversary code outside of the operating system and main system firmware or BIOS. This technique may be similar to [System Firmware](https://attack.mitre.org/techniques/T1542/001) but conducted upon other system components/devices that may not have the same capability or level of integrity checking.

Malicious component firmware could provide both a persistent level of access to systems despite potential typical failures to maintain access and hard disk re-images, as well as a way to evade host software-based defenses and integrity checks.

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
