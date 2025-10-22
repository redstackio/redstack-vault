---
id: d7e654a9-e7c4-468b-a1c3-61079b594ae6
name: Social Media Accounts
type: sub-technique
mitre_id: T1586.001
mitre_url: null
created_at: '2023-04-06T00:31:25.758023+00:00'
updated_at: '2023-04-06T00:31:25.758023+00:00'
parent_technique: '[[Compromise Accounts|T1586 - Compromise Accounts]]'
tactics:
- '[[Resource Development|TA0042 - Resource Development]]'
---

# Social Media Accounts

**MITRE ID**: T1586.001

**Parent Technique**: [[Compromise Accounts|T1586 - Compromise Accounts]]

This is a sub-technique of T1586 - Compromise Accounts.

## Summary

Adversaries may compromise social media accounts that can be used during targeting. For operations incorporating social engineering, the utilization of an online persona may be important. Rather than creating and cultivating social media profiles (i.e. [Social Media Accounts](https://attack.mitre.or

## Description

Adversaries may compromise social media accounts that can be used during targeting. For operations incorporating social engineering, the utilization of an online persona may be important. Rather than creating and cultivating social media profiles (i.e. [Social Media Accounts](https://attack.mitre.org/techniques/T1585/001)), adversaries may compromise existing social media accounts. Utilizing an existing persona may engender a level of trust in a potential victim if they have a relationship, or knowledge of, the compromised persona. 

A variety of methods exist for compromising social media accounts, such as gathering credentials via [Phishing for Information](https://attack.mitre.org/techniques/T1598), purchasing credentials from third-party sites, or by brute forcing credentials (ex: password reuse from breach credential dumps).(Citation: AnonHBGary) Prior to compromising social media accounts, adversaries may conduct Reconnaissance to inform decisions about which accounts to compromise to further their operation.

Personas may exist on a single site or across multiple sites (ex: Facebook, LinkedIn, Twitter, etc.). Compromised social media accounts may require additional development, this could include filling out or modifying profile information, further developing social networks, or incorporating photos.

Adversaries can use a compromised social media profile to create new, or hijack existing, connections to targets of interest. These connections may be direct or may include trying to connect through others.(Citation: NEWSCASTER2014)(Citation: BlackHatRobinSage) Compromised profiles may be leveraged during other phases of the adversary lifecycle, such as during Initial Access (ex: [Spearphishing via Service](https://attack.mitre.org/techniques/T1566/003)).

## Tactics

This sub-technique is used in the following tactics:

- [[Resource Development|TA0042 - Resource Development]]
