---
id: 78783c41-2347-4e8f-bef2-0249d8820f97
name: ROMMONkit
type: sub-technique
mitre_id: T1542.004
mitre_url: null
created_at: '2023-04-06T00:31:26.687637+00:00'
updated_at: '2023-04-06T00:31:26.687637+00:00'
parent_technique: '[[Pre-OS Boot|T1542 - Pre-OS Boot]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
---

# ROMMONkit

**MITRE ID**: T1542.004

**Parent Technique**: [[Pre-OS Boot|T1542 - Pre-OS Boot]]

This is a sub-technique of T1542 - Pre-OS Boot.

## Summary

Adversaries may abuse the ROM Monitor (ROMMON) by loading an unauthorized firmware with adversary code to provide persistent access and manipulate device behavior that is difficult to detect. (Citation: Cisco Synful Knock Evolution)(Citation: Cisco Blog Legacy Device Attacks)

ROMMON is a Cisco net

## Description

Adversaries may abuse the ROM Monitor (ROMMON) by loading an unauthorized firmware with adversary code to provide persistent access and manipulate device behavior that is difficult to detect. (Citation: Cisco Synful Knock Evolution)(Citation: Cisco Blog Legacy Device Attacks)

ROMMON is a Cisco network device firmware that functions as a boot loader, boot image, or boot helper to initialize hardware and software when the platform is powered on or reset. Similar to [TFTP Boot](https://attack.mitre.org/techniques/T1542/005), an adversary may upgrade the ROMMON image locally or remotely (for example, through TFTP) with adversary code and restart the device in order to overwrite the existing ROMMON image. This provides adversaries with the means to update the ROMMON to gain persistence on a system in a way that may be difficult to detect.

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
