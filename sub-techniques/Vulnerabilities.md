---
id: 8c5ad4db-aa50-4206-91f3-f501284fbb6e
name: Vulnerabilities
type: sub-technique
mitre_id: T1588.006
mitre_url: null
created_at: '2023-04-06T00:31:25.790829+00:00'
updated_at: '2023-04-06T00:31:25.790829+00:00'
parent_technique: '[[Obtain Capabilities|T1588 - Obtain Capabilities]]'
tactics:
- '[[Resource Development|TA0042 - Resource Development]]'
---

# Vulnerabilities

**MITRE ID**: T1588.006

**Parent Technique**: [[Obtain Capabilities|T1588 - Obtain Capabilities]]

This is a sub-technique of T1588 - Obtain Capabilities.

## Summary

Adversaries may acquire information about vulnerabilities that can be used during targeting. A vulnerability is a weakness in computer hardware or software that can, potentially, be exploited by an adversary to cause unintended or unanticipated behavior to occur. Adversaries may find vulnerability i

## Description

Adversaries may acquire information about vulnerabilities that can be used during targeting. A vulnerability is a weakness in computer hardware or software that can, potentially, be exploited by an adversary to cause unintended or unanticipated behavior to occur. Adversaries may find vulnerability information by searching open databases or gaining access to closed vulnerability databases.(Citation: National Vulnerability Database)

An adversary may monitor vulnerability disclosures/databases to understand the state of existing, as well as newly discovered, vulnerabilities. There is usually a delay between when a vulnerability is discovered and when it is made public. An adversary may target the systems of those known to conduct vulnerability research (including commercial vendors). Knowledge of a vulnerability may cause an adversary to search for an existing exploit (i.e. [Exploits](https://attack.mitre.org/techniques/T1588/005)) or to attempt to develop one themselves (i.e. [Exploits](https://attack.mitre.org/techniques/T1587/004)).

## Tactics

This sub-technique is used in the following tactics:

- [[Resource Development|TA0042 - Resource Development]]
