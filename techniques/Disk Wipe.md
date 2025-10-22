---
id: 5fda851d-009f-4b23-8e3c-8068a5c13cd5
name: Disk Wipe
type: technique
mitre_id: T1561
mitre_url: null
created_at: '2023-04-06T00:31:25.633906+00:00'
updated_at: '2023-04-06T00:31:27.791871+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
---

# Disk Wipe

**MITRE ID**: T1561

## Description

Adversaries may wipe or corrupt raw disk data on specific systems or in large numbers in a network to interrupt availability to system and network resources. With direct write access to a disk, adversaries may attempt to overwrite portions of disk data. Adversaries may opt to wipe arbitrary portions of disk data and/or wipe disk structures like the master boot record (MBR). A complete wipe of all disk sectors may be attempted.

To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware used for wiping disks may have worm-like features to propagate across a network by leveraging additional techniques like [Valid Accounts](https://attack.mitre.org/techniques/T1078), [OS Credential Dumping](https://attack.mitre.org/techniques/T1003), and [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002).(Citation: Novetta Blockbuster Destructive Malware)

## Tactics

- [[Impact|TA0040 - Impact]]
