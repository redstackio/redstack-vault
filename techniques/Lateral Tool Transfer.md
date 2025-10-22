---
id: 26c091af-a0af-4ec7-afd4-5731cd9ee14b
name: Lateral Tool Transfer
type: technique
mitre_id: T1570
mitre_url: null
created_at: '2023-04-06T00:31:26.848842+00:00'
updated_at: '2023-04-06T00:31:27.867136+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
---

# Lateral Tool Transfer

**MITRE ID**: T1570

## Description

Adversaries may transfer tools or other files between systems in a compromised environment. Once brought into the victim environment (i.e. [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105)) files may then be copied from one system to another to stage adversary tools or other files over the course of an operation. Adversaries may copy files between internal victim systems to support lateral movement using inherent file sharing protocols such as file sharing over [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) to connected network shares or with authenticated connections via [Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001).(Citation: Unit42 LockerGoga 2019)

Files can also be transferred using native or otherwise present tools on the victim system, such as scp, rsync, curl, sftp, and [ftp](https://attack.mitre.org/software/S0095).

## Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]
