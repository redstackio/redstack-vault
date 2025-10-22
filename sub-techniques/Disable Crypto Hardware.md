---
id: 1f55d91d-a44c-491b-a3dc-145f9a422f0c
name: Disable Crypto Hardware
type: sub-technique
mitre_id: T1600.002
mitre_url: null
created_at: '2023-04-06T00:31:26.454679+00:00'
updated_at: '2023-04-06T00:31:26.454679+00:00'
parent_technique: '[[Weaken Encryption|T1600 - Weaken Encryption]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Disable Crypto Hardware

**MITRE ID**: T1600.002

**Parent Technique**: [[Weaken Encryption|T1600 - Weaken Encryption]]

This is a sub-technique of T1600 - Weaken Encryption.

## Summary

Adversaries disable a network device’s dedicated hardware encryption, which may enable them to leverage weaknesses in software encryption in order to reduce the effort involved in collecting, manipulating, and exfiltrating transmitted data.

Many network devices such as routers, switches, and firewa

## Description

Adversaries disable a network device’s dedicated hardware encryption, which may enable them to leverage weaknesses in software encryption in order to reduce the effort involved in collecting, manipulating, and exfiltrating transmitted data.

Many network devices such as routers, switches, and firewalls, perform encryption on network traffic to secure transmission across networks. Often, these devices are equipped with special, dedicated encryption hardware to greatly increase the speed of the encryption process as well as to prevent malicious tampering. When an adversary takes control of such a device, they may disable the dedicated hardware, for example, through use of [Modify System Image](https://attack.mitre.org/techniques/T1601), forcing the use of software to perform encryption on general processors. This is typically used in conjunction with attacks to weaken the strength of the cipher in software (e.g., [Reduce Key Space](https://attack.mitre.org/techniques/T1600/001)). (Citation: Cisco Blog Legacy Device Attacks)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
