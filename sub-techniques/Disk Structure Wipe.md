---
id: 2434d9ab-e199-45c6-aca3-7b6e9946d0d7
name: Disk Structure Wipe
type: sub-technique
mitre_id: T1561.002
mitre_url: null
created_at: '2023-04-06T00:31:25.496260+00:00'
updated_at: '2023-04-06T00:31:25.496260+00:00'
parent_technique: '[[Disk Wipe|T1561 - Disk Wipe]]'
tactics:
- '[[Impact|TA0040 - Impact]]'
---

# Disk Structure Wipe

**MITRE ID**: T1561.002

**Parent Technique**: [[Disk Wipe|T1561 - Disk Wipe]]

This is a sub-technique of T1561 - Disk Wipe.

## Summary

Adversaries may corrupt or wipe the disk data structures on a hard drive necessary to boot a system; targeting specific critical systems or in large numbers in a network to interrupt availability to system and network resources. 

Adversaries may attempt to render the system unable to boot by overwr

## Description

Adversaries may corrupt or wipe the disk data structures on a hard drive necessary to boot a system; targeting specific critical systems or in large numbers in a network to interrupt availability to system and network resources. 

Adversaries may attempt to render the system unable to boot by overwriting critical data located in structures such as the master boot record (MBR) or partition table.(Citation: Symantec Shamoon 2012)(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)(Citation: Unit 42 Shamoon3 2018) The data contained in disk structures may include the initial executable code for loading an operating system or the location of the file system partitions on disk. If this information is not present, the computer will not be able to load an operating system during the boot process, leaving the computer unavailable. [Disk Structure Wipe](https://attack.mitre.org/techniques/T1561/002) may be performed in isolation, or along with [Disk Content Wipe](https://attack.mitre.org/techniques/T1561/001) if all sectors of a disk are wiped.

To maximize impact on the target organization, malware designed for destroying disk structures may have worm-like features to propagate across a network by leveraging other techniques like [Valid Accounts](https://attack.mitre.org/techniques/T1078), [OS Credential Dumping](https://attack.mitre.org/techniques/T1003), and [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002).(Citation: Symantec Shamoon 2012)(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)

## Tactics

This sub-technique is used in the following tactics:

- [[Impact|TA0040 - Impact]]
