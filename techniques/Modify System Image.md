---
id: e321d5e7-3d21-4c08-9fd7-c6c86f3533c2
name: Modify System Image
type: technique
mitre_id: T1601
mitre_url: null
created_at: '2023-04-06T00:31:26.721682+00:00'
updated_at: '2023-04-06T00:31:27.855700+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Modify System Image

**MITRE ID**: T1601

## Description

Adversaries may make changes to the operating system of embedded network devices to weaken defenses and provide new capabilities for themselves.  On such devices, the operating systems are typically monolithic and most of the device functionality and capabilities are contained within a single file.

To change the operating system, the adversary typically only needs to affect this one file, replacing or modifying it.  This can either be done live in memory during system runtime for immediate effect, or in storage to implement the change on the next boot of the network device.

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
