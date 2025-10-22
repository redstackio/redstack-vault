---
id: c31b1e54-dca3-44c4-8a58-9b7c312a6e1f
name: Disable or Modify Cloud Firewall
type: sub-technique
mitre_id: T1562.007
mitre_url: null
created_at: '2023-04-06T00:31:26.379452+00:00'
updated_at: '2023-04-06T00:31:26.379452+00:00'
parent_technique: '[[Impair Defenses|T1562 - Impair Defenses]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Disable or Modify Cloud Firewall

**MITRE ID**: T1562.007

**Parent Technique**: [[Impair Defenses|T1562 - Impair Defenses]]

This is a sub-technique of T1562 - Impair Defenses.

## Summary

Adversaries may disable or modify a firewall within a cloud environment to bypass controls that limit access to cloud resources. Cloud firewalls are separate from system firewalls that are described in [Disable or Modify System Firewall](https://attack.mitre.org/techniques/T1562/004). 

Cloud enviro

## Description

Adversaries may disable or modify a firewall within a cloud environment to bypass controls that limit access to cloud resources. Cloud firewalls are separate from system firewalls that are described in [Disable or Modify System Firewall](https://attack.mitre.org/techniques/T1562/004). 

Cloud environments typically utilize restrictive security groups and firewall rules that only allow network activity from trusted IP addresses via expected ports and protocols. An adversary may introduce new firewall rules or policies to allow access into a victim cloud environment. For example, an adversary may use a script or utility that creates new ingress rules in existing security groups to allow any TCP/IP connectivity.(Citation: Expel IO Evil in AWS)

Modifying or disabling a cloud firewall may enable adversary C2 communications, lateral movement, and/or data exfiltration that would otherwise not be allowed.

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
