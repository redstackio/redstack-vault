---
id: 240890c1-bffe-4dee-9c04-feebaad2f7d4
name: Virtual Private Server
type: sub-technique
mitre_id: T1584.003
mitre_url: null
created_at: '2023-04-06T00:31:25.940078+00:00'
updated_at: '2023-04-06T00:31:25.940078+00:00'
parent_technique: '[[Compromise Infrastructure|T1584 - Compromise Infrastructure]]'
tactics:
- '[[Resource Development|TA0042 - Resource Development]]'
---

# Virtual Private Server

**MITRE ID**: T1584.003

**Parent Technique**: [[Compromise Infrastructure|T1584 - Compromise Infrastructure]]

This is a sub-technique of T1584 - Compromise Infrastructure.

## Summary

Adversaries may compromise third-party Virtual Private Servers (VPSs) that can be used during targeting. There exist a variety of cloud service providers that will sell virtual machines/containers as a service. Adversaries may compromise VPSs purchased by third-party entities. By compromising a VPS 

## Description

Adversaries may compromise third-party Virtual Private Servers (VPSs) that can be used during targeting. There exist a variety of cloud service providers that will sell virtual machines/containers as a service. Adversaries may compromise VPSs purchased by third-party entities. By compromising a VPS to use as infrastructure, adversaries can make it difficult to physically tie back operations to themselves.(Citation: NSA NCSC Turla OilRig)

Compromising a VPS for use in later stages of the adversary lifecycle, such as Command and Control, can allow adversaries to benefit from the ubiquity and trust associated with higher reputation cloud service providers as well as that added by the compromised third-party.

## Tactics

This sub-technique is used in the following tactics:

- [[Resource Development|TA0042 - Resource Development]]
