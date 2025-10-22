---
id: 774103be-9b39-41f8-8949-5277b5e130ef
name: Botnet
type: sub-technique
mitre_id: T1584.005
mitre_url: null
created_at: '2023-04-06T00:31:26.482649+00:00'
updated_at: '2023-04-06T00:31:26.482649+00:00'
parent_technique: '[[Compromise Infrastructure|T1584 - Compromise Infrastructure]]'
tactics:
- '[[Resource Development|TA0042 - Resource Development]]'
---

# Botnet

**MITRE ID**: T1584.005

**Parent Technique**: [[Compromise Infrastructure|T1584 - Compromise Infrastructure]]

This is a sub-technique of T1584 - Compromise Infrastructure.

## Summary

Adversaries may compromise numerous third-party systems to form a botnet that can be used during targeting. A botnet is a network of compromised systems that can be instructed to perform coordinated tasks.(Citation: Norton Botnet) Instead of purchasing/renting a botnet from a booter/stresser service

## Description

Adversaries may compromise numerous third-party systems to form a botnet that can be used during targeting. A botnet is a network of compromised systems that can be instructed to perform coordinated tasks.(Citation: Norton Botnet) Instead of purchasing/renting a botnet from a booter/stresser service, adversaries may build their own botnet by compromising numerous third-party systems.(Citation: Imperva DDoS for Hire) Adversaries may also conduct a takeover of an existing botnet, such as redirecting bots to adversary-controlled C2 servers.(Citation: Dell Dridex Oct 2015) With a botnet at their disposal, adversaries may perform follow-on activity such as large-scale [Phishing](https://attack.mitre.org/techniques/T1566) or Distributed Denial of Service (DDoS).

## Tactics

This sub-technique is used in the following tactics:

- [[Resource Development|TA0042 - Resource Development]]
