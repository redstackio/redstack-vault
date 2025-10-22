---
id: f8139b73-8428-4719-b7df-1ebf4e97ace2
name: TFTP Boot
type: sub-technique
mitre_id: T1542.005
mitre_url: null
created_at: '2023-04-06T00:31:25.774598+00:00'
updated_at: '2023-04-06T00:31:25.774598+00:00'
parent_technique: '[[Pre-OS Boot|T1542 - Pre-OS Boot]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
---

# TFTP Boot

**MITRE ID**: T1542.005

**Parent Technique**: [[Pre-OS Boot|T1542 - Pre-OS Boot]]

This is a sub-technique of T1542 - Pre-OS Boot.

## Summary

Adversaries may abuse netbooting to load an unauthorized network device operating system from a Trivial File Transfer Protocol (TFTP) server. TFTP boot (netbooting) is commonly used by network administrators to load configuration-controlled network device images from a centralized management server.

## Description

Adversaries may abuse netbooting to load an unauthorized network device operating system from a Trivial File Transfer Protocol (TFTP) server. TFTP boot (netbooting) is commonly used by network administrators to load configuration-controlled network device images from a centralized management server. Netbooting is one option in the boot sequence and can be used to centralize, manage, and control device images.

Adversaries may manipulate the configuration on the network device specifying use of a malicious TFTP server, which may be used in conjunction with [Modify System Image](https://attack.mitre.org/techniques/T1601) to load a modified image on device startup or reset. The unauthorized image allows adversaries to modify device configuration, add malicious capabilities to the device, and introduce backdoors to maintain control of the network device while minimizing detection through use of a standard functionality. This technique is similar to [ROMMONkit](https://attack.mitre.org/techniques/T1542/004) and may result in the network device running a modified image. (Citation: Cisco Blog Legacy Device Attacks)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
