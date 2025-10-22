---
id: e732288e-4146-473e-a29c-f135908e637e
name: Downgrade System Image
type: sub-technique
mitre_id: T1601.002
mitre_url: null
created_at: '2023-04-06T00:31:27.237264+00:00'
updated_at: '2023-04-06T00:31:27.237264+00:00'
parent_technique: '[[Modify System Image|T1601 - Modify System Image]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Downgrade System Image

**MITRE ID**: T1601.002

**Parent Technique**: [[Modify System Image|T1601 - Modify System Image]]

This is a sub-technique of T1601 - Modify System Image.

## Summary

Adversaries may install an older version of the operating system of a network device to weaken security.  Older operating system versions on network devices often have weaker encryption ciphers and, in general, fewer/less updated defensive features. (Citation: Cisco Synful Knock Evolution)

On embed

## Description

Adversaries may install an older version of the operating system of a network device to weaken security.  Older operating system versions on network devices often have weaker encryption ciphers and, in general, fewer/less updated defensive features. (Citation: Cisco Synful Knock Evolution)

On embedded devices, downgrading the version typically only requires replacing the operating system file in storage.  With most embedded devices, this can be achieved by downloading a copy of the desired version of the operating system file and reconfiguring the device to boot from that file on next system restart.  The adversary could then restart the device to implement the change immediately or they could wait until the next time the system restarts.

Downgrading the system image to an older versions may allow an adversary to evade defenses by enabling behaviors such as [Weaken Encryption](https://attack.mitre.org/techniques/T1600).  Downgrading of a system image can be done on its own, or it can be used in conjunction with [Patch System Image](https://attack.mitre.org/techniques/T1601/001).  

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
