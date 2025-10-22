---
id: beedb704-55e5-490c-a76c-8c1f7758fd69
name: Bootkit
type: sub-technique
mitre_id: T1542.003
mitre_url: null
created_at: '2023-04-06T00:31:25.652264+00:00'
updated_at: '2023-04-06T00:31:25.652264+00:00'
parent_technique: '[[Pre-OS Boot|T1542 - Pre-OS Boot]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
---

# Bootkit

**MITRE ID**: T1542.003

**Parent Technique**: [[Pre-OS Boot|T1542 - Pre-OS Boot]]

This is a sub-technique of T1542 - Pre-OS Boot.

## Summary

Adversaries may use bootkits to persist on systems. Bootkits reside at a layer below the operating system and may make it difficult to perform full remediation unless an organization suspects one was used and can act accordingly.

A bootkit is a malware variant that modifies the boot sectors of a ha

## Description

Adversaries may use bootkits to persist on systems. Bootkits reside at a layer below the operating system and may make it difficult to perform full remediation unless an organization suspects one was used and can act accordingly.

A bootkit is a malware variant that modifies the boot sectors of a hard drive, including the Master Boot Record (MBR) and Volume Boot Record (VBR). (Citation: Mandiant M Trends 2016) The MBR is the section of disk that is first loaded after completing hardware initialization by the BIOS. It is the location of the boot loader. An adversary who has raw access to the boot drive may overwrite this area, diverting execution during startup from the normal boot loader to adversary code. (Citation: Lau 2011)

The MBR passes control of the boot process to the VBR. Similar to the case of MBR, an adversary who has raw access to the boot drive may overwrite the VBR to divert execution during startup to adversary code.

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
