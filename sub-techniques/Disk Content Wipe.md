---
id: a48849a3-67b7-4444-9bc3-e7bf54ec1e56
name: Disk Content Wipe
type: sub-technique
mitre_id: T1561.001
mitre_url: null
created_at: '2023-04-06T00:31:27.230801+00:00'
updated_at: '2023-04-06T00:31:27.230801+00:00'
parent_technique: '[[Disk Wipe|T1561 - Disk Wipe]]'
tactics:
- '[[Impact|TA0040 - Impact]]'
---

# Disk Content Wipe

**MITRE ID**: T1561.001

**Parent Technique**: [[Disk Wipe|T1561 - Disk Wipe]]

This is a sub-technique of T1561 - Disk Wipe.

## Summary

Adversaries may erase the contents of storage devices on specific systems or in large numbers in a network to interrupt availability to system and network resources.

Adversaries may partially or completely overwrite the contents of a storage device rendering the data irrecoverable through the stora

## Description

Adversaries may erase the contents of storage devices on specific systems or in large numbers in a network to interrupt availability to system and network resources.

Adversaries may partially or completely overwrite the contents of a storage device rendering the data irrecoverable through the storage interface.(Citation: Novetta Blockbuster)(Citation: Novetta Blockbuster Destructive Malware)(Citation: DOJ Lazarus Sony 2018) Instead of wiping specific disk structures or files, adversaries with destructive intent may wipe arbitrary portions of disk content. To wipe disk content, adversaries may acquire direct access to the hard drive in order to overwrite arbitrarily sized portions of disk with random data.(Citation: Novetta Blockbuster Destructive Malware) Adversaries have been observed leveraging third-party drivers like [RawDisk](https://attack.mitre.org/software/S0364) to directly access disk content.(Citation: Novetta Blockbuster)(Citation: Novetta Blockbuster Destructive Malware) This behavior is distinct from [Data Destruction](https://attack.mitre.org/techniques/T1485) because sections of the disk are erased instead of individual files.

To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware used for wiping disk content may have worm-like features to propagate across a network by leveraging additional techniques like [Valid Accounts](https://attack.mitre.org/techniques/T1078), [OS Credential Dumping](https://attack.mitre.org/techniques/T1003), and [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002).(Citation: Novetta Blockbuster Destructive Malware)

## Tactics

This sub-technique is used in the following tactics:

- [[Impact|TA0040 - Impact]]
